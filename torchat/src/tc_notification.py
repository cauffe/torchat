import wx
import config
import os
import subprocess

def notificationWindow_gtknotify(mw, text, buddy):
    import pynotify
    if not pynotify.is_initted():
        if not pynotify.init('torchat'):
            raise Exception('gtknotify not supported')
    pynotify.Notification(buddy.name, text).show()

def notificationWindow_knotify(mw, text, buddy):
    import dbus
    knotify = dbus.SessionBus().get_object("org.kde.knotify", "/Notify")
    knotify.event('warning', 'kde', [], buddy.name, text,
            [], [], 0, 0, dbus_interface='org.kde.KNotify')

def notificationWindow_growlnotify(mw, text, buddy):
    # This seems to fail about half the time
    # iconpath = os.path.join(config.ICON_DIR, "torchat.png")
    #args = ['growlnotify', '-m', text, '--image', iconpath]
    args = ['growlnotify', '-m', text]
    subprocess.Popen(args).communicate()

def notificationWindow_xosd(mw, text, buddy):
    import pyosd
    osd = pyosd.osd()
    osd.display(text)

def notificationWindow_generic(mw, text, buddy):
    NotificationWindowGeneric(mw, text, buddy)

class NotificationWindowGeneric(wx.Frame):
    def __init__(self, mw, text, buddy):
        wx.Frame.__init__(self, mw, style=wx.FRAME_NO_TASKBAR | wx.NO_BORDER)
        self.panel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        self.panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))
        sizer = wx.BoxSizer()
        self.panel.SetSizer(sizer)

        if buddy.profile_avatar_object <> None:
            bitmap = buddy.profile_avatar_object
        else:
            bitmap = wx.Bitmap(os.path.join(config.ICON_DIR, "torchat.png"), wx.BITMAP_TYPE_PNG)
        static_image = wx.StaticBitmap(self.panel, -1, bitmap)
        sizer.Add(static_image, 0, wx.ALL, 5 )

        self.label = wx.StaticText(self.panel)
        self.label.SetLabel(text)
        sizer.Add(self.label, 0, wx.ALL, 5 )

        wsizer = wx.BoxSizer()
        wsizer.Add(self.panel, 0, wx.ALL, 0)
        self.SetSizerAndFit(wsizer)
        self.Layout()

        # initialize animation
        cx, cy, maxx, maxy = wx.ClientDisplayRect()
        self.w, self.h = self.GetSize()
        self.x_end = maxx - self.w - 20
        self.y_end = maxy - self.h - 20

        self.x_pos = -self.w
        self.y_pos = self.y_end
        self.phase = 0

        self.SetPosition((self.x_pos, self.y_pos))
        
        # the following will prevent the focus 
        # stealing on windows
        self.Disable()
        self.Show()
        self.Enable()

        self.timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.onTimer)

        # start animation
        self.timer.Start(10, True)


    def onTimer(self, evt):
        if self.phase == 0:
            if self.x_pos < self.x_end:
                # move right and restart timer
                speed = ((self.x_end - self.x_pos) ^ 2) / 10
                self.x_pos += (1 + speed)
                self.SetPosition((self.x_pos, self.y_pos))
                self.timer.Start(10, True)
                return
            else:
                # we are at the right border.
                # now switch phase and wait a bit
                self.phase = 1
                self.timer.Start(3000, True)
                
                # and from now on we also close on mouse contact
                self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.onMouse)
                return

        if self.phase == 1:
            if self.y_pos > -self.h:
                # move upwards and restart timer
                speed = ((self.y_end - self.y_pos) ^ 2) / 10
                self.y_pos -= (5 + speed)
                self.SetPosition((self.x_pos, self.y_pos))
                self.timer.Start(10, True)
                return
            else:
                # we reached the end of the animation
                self.Hide()
                self.Destroy()
        
    def onMouse(self, evt):
        # restart the timer to immediately end the waiting
        self.timer.Start(10, True)
        
def notificationWindow(mw, text, buddy):
    method = config.get('gui', 'notification_method')
    try:
        function = globals()["notificationWindow_%s" % method]
    except:
        print "(1) notification method '%s' is not implemented, falling back to 'generic'." % method
        notificationWindow_generic(mw, text, buddy)
        return
    
    try:
        function(mw, text, buddy)
    except:
        print "(1) exception while using notification method '%s'" % method
        print "(1) falling back to 'generic'. Traceback follows:"
        config.tb()
        notificationWindow_generic(mw, text, buddy)


# vim: set tw=0 sts=4 sw=4 expandtab:
