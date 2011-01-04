# -*- coding: UTF-8 -*-

##############################################################################
#                                                                            #
# Copyright (c) 2007-2010 Bernd Kreuss <prof7bit@gmail.com>                  #
#                                                                            #
# Translation file for TorChat                                               #
#                                                                            #
##############################################################################

LANGUAGE_CODE = u"fr"
LANGUAGE_NAME = u"Français"
LANGUAGE_NAME_ENGLISH = u"French"
TRANSLATOR_NAMES = [u"vitisch"]

#buttons
BTN_CANCEL = u"Annuler"
BTN_OK = u"Ok"
BTN_SAVE_AS = u"Save as..."
BTN_CLOSE = u"Fermer"

#status
ST_AVAILABLE = u"Disponible"
ST_AWAY = u"Absent"
ST_EXTENDED_AWAY = u"Absent pour longtemps"
ST_OFFLINE = u"Déconnecté"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = u"Montrer/Cacher TorChat"
MTB_QUIT = u"Arrêtez"

#popup menu
MPOP_CHAT = u"Chat..."
MPOP_SEND_FILE = u"Envoyer un fichier..."
MPOP_EDIT_CONTACT = u"Rediger contact..."
MPOP_DELETE_CONTACT = u"Supprimer contact..."
MPOP_SHOW_OFFLINE_MESSAGES = u"Montrer les messages hors-ligne"
MPOP_CLEAR_OFFLINE_MESSAGES = u"Effacer les messages hors-ligne"
# MPOP_ACTIVATE_LOG = u"Activate logging to file"
# MPOP_STOP_LOG = u"Stop logging"
# MPOP_DELETE_EXISTING_LOG = u"Delete existing log file"
# MPOP_DELETE_AND_STOP_LOG = u"Delete log and stop logging"
MPOP_ADD_CONTACT = u"Ajouter un contact..."
MPOP_ABOUT = u"À propos..."
MPOP_ASK_AUTHOR = u"Demandez %s..."
MPOP_SETTINGS = u"Paramètres..."
# MPOP_EDIT_MY_PROFILE = u"Edit my profile..."

# #chat window popup menu
# CPOP_COPY = u"Copy"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = u"Confirmez la supression"
D_CONFIRM_DELETE_MESSAGE = u"Êtes-vous sûr de vouloir supprimer le contact?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = u"TorChat: Archivage est actif"
D_LOG_WARNING_MESSAGE = u"L'archivage au fichier est activé!!\n\nFicher d'archivage: %s\n\nRappelez-vous de supprimer le ficher d'archivage si vous avez fini la correction parce que le ficher d'archivage peut contenir l'information sensible."

# #warning about used port
# D_WARN_USED_PORT_TITLE = u"TorChat: Port already in use"
# D_WARN_USED_PORT_MESSAGE = u"Something, probably another TorChat instance, is already listening at %s:%s. You must create another profile using different ports to be able to start TorChat a second time."

#warnig about unread messages
D_WARN_UNREAD_TITLE = u"TorChat: Messages non lus"
D_WARN_UNREAD_MESSAGE = u"Il y a des messages non lus.\nIls seront perdus pour toujours!\n\nVoulez-vous vraiment sortir maintenant?"

#warning about offline buddy
# D_WARN_BUDDY_OFFLINE_TITLE = u"TorChat: Buddy is offline"
# D_WARN_BUDDY_OFFLINE_MESSAGE = u"This operation is not possible with offline buddies"

#warning about multiple files
# D_WARN_FILE_ONLY_ONE_TITLE = u"TorChat: Multiple files"
# D_WARN_FILE_ONLY_ONE_MESSAGE = u"You may not start multiple file transfers with one operation. Start the transfers individually or send a zip-file instead"

# #warning about file save error
# D_WARN_FILE_SAVE_ERROR_TITLE = u"TorChat: Error saving file"
# D_WARN_FILE_SAVE_ERROR_MESSAGE = u"The file '%s' could not be created.\n\n%s"

# #warning about file already exists
# D_WARN_FILE_ALREADY_EXISTS_TITLE = u"TorChat: File exists"
# D_WARN_FILE_ALREADY_EXISTS_MESSAGE = u"The file '%s' already exists.\nOverwrite it?"

#dialog: add/edit contact
DEC_TITLE_ADD = u"Ajouter un nouveau contact"
DEC_TITLE_EDIT = u"Modifier le contact"
DEC_TORCHAT_ID = u"TorChat ID"
DEC_DISPLAY_NAME = u"Nom d'utilisateur"
DEC_INTRODUCTION = u"Introduction"
DEC_MSG_16_CHARACTERS = u"L'adresse doit avoir 16 caractères, pas %i."
DEC_MSG_ONLY_ALPANUM = u"L'adresse doit seulement contenir des nombres et des lettres minuscule."
DEC_MSG_ALREADY_ON_LIST = u"%s est déjà sur votre liste."

# #dialog: edit my profile
# DEP_TITLE = u"Edit my profile"
# DEP_NAME = u"Name"
# DEP_TEXT = u"Text"
# DEP_AVATAR_SELECT_PNG = u"Select .PNG file to use as your avatar (will be scaled to 64*64, may contain transparency)"
# DEP_PNG_FILES = u"PNG files"
# DEP_ALL_FILES = u"All files"
# DEP_WARN_TITLE = u"Avatar selection not possible"
# DEP_WARN_IS_ALREADY = u"This is already the current avatar"
# DEP_WARN_MUST_BE_PNG = u"The avatar must be a .png file"

#file transfer window
# DFT_FILE_OPEN_TITLE = u"Send file to %s"
# DFT_FILE_SAVE_TITLE = u"Save file from %s"
DFT_SEND = u"Envoyer %s\nà %s\n%04.1f%% (%i de %i bytes)"
DFT_RECEIVE = u"Recevoir %s\nde %s\n%04.1f%% (%i de %i bytes)"
# DFT_WAITING = u"waiting for connection"
# DFT_STARTING = u"starting transfer"
# DFT_ABORTED = u"transfer aborted"
# DFT_COMPLETE = u"transfer complete"
# DFT_ERROR = u"error"

#settings dialaog
DSET_TITLE = u"Configuration de TorChat"
DSET_NET_TITLE = u"Réseau"
DSET_NET_ACTIVE = u"actif"
DSET_NET_INACTIVE = u"inactif"
DSET_NET_TOR_ADDRESS = u"Adresse de procuration pour Tor"
DSET_NET_TOR_SOCKS = u"Port de SOCKS"
DSET_NET_TOR_CONTROL = u"Port de commande"
DSET_NET_OWN_HOSTNAME = u"Mon TorChat ID"
DSET_NET_LISTEN_INTERFACE = u"Interface d'écouter"
DSET_NET_LISTEN_PORT = u"Port d'écouter"
DSET_GUI_TITLE = u"Interface d'utilisateur"
# DSET_GUI_LANGUAGE = u"Language"
# DSET_GUI_OPEN_MAIN_HIDDEN = u"Start with minimized main window"
# DSET_GUI_OPEN_CHAT_HIDDEN = u"Don't automatically open new windows"
# DSET_GUI_NOTIFICATION_POPUP = u"Notification pop-up"
# DSET_GUI_FLASH_WINDOW = u"Flash window title on new message"
# DSET_MISC_TITLE = u"Misc"
# DSET_MISC_TEMP_IN_DATA = u"Store temporary files inside data directory"
# DSET_MISC_TEMP_CUSTOM_DIR = u"Temporary directory (leave empty for OS-default)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = u"messages retardés attendant pour être envoyé"
NOTICE_DELAYED_MSG_SENT = u"messages retardés ont été envoyés"
NOTICE_DELAYED = u"retardé"

# #messagebox for offline messages
# MSG_OFFLINE_TITLE = u"TorChat: queued messages"
# MSG_OFFLINE_EMPTY = u"there are no (more) queued messages for %s"
# MSG_OFFLINE_QUEUED = u"queued offline messages for %s:\n\n%s"

# #buddy list mouse hover popup
# BPOP_BUDDY_IS_OFFLINE = u"Buddy is offline"
# BPOP_CONNECTED_AWAITING_RETURN_CONN = u"Connected, awaiting return connection..."
# BPOP_CLIENT_SOFTWARE = u"Client: %s %s"

# #logging of conversations to file
# LOG_HEADER = u"This log file is not signed and has no cogency of proof"
# LOG_STARTED = u"Logging started"
# LOG_STOPPED = u"Logging stopped"
# LOG_DELETED = u"Log files have been deleted"
# LOG_IS_ACTIVATED = u"Logging to file is activated:\n%s"
# LOG_IS_STOPPED_OLD_LOG_FOUND = u"Logging is stopped but old log file still exists:\n%s"

#about box
ABOUT_TITLE = u"À propos de TorChat"
ABOUT_TEXT = u"""TorChat %(version)s (svn: r%(svn)s)
  %(copyright)s

Translations:
  %(translators)s

Runtime environment:
  Python: %(python)s
  wx: %(wx)s

TorChat is free software: you can redistribute it and/or \
modify it under the terms of the GNU General Public \
License as published by the Free Software Foundation, \
either version 3 of the License, or (at your option) \
any later version.

TorChat is distributed in the hope that it will be useful, \
but WITHOUT ANY WARRANTY; without even the implied \
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. \
See the GNU General Public License for more details.

*

And now for something completely different:

If you happen to run a software company near Hannover, Germany and \
are in need of a new coder, feel free to regard this little program \
as my application documents and drop me a mail with your answer.
"""