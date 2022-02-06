import pypresence
import psutil
import time
import logging
import os
try:
    import pywinauto
except ImportError:
    print("Pywinauto not found!\nSome Features will not be available!")
    pywinauto = False

KEEP_EXTENTIONS = False

# Only works perfectly when title is set to file name - Change title text to "$u" in settings.
# Menu Tools -> Preferences (Show settings = ALL) -> Input/Codecs.
# Then at the very bottom of the right panel set the option.
# "Change title according to current media" to "$u".
# Save, exit and restart VLC.


def get_vlc_title(keep_ext=True):
    app = pywinauto.Desktop(backend='uia').windows()
    for w in app:
        if w.window_text().endswith('VLC media player'):
            title = w.window_text().rstrip(' - VLC media player')
            if not keep_ext:
                title = '.'.join(title.split('.')[:-1])
            return title


def set_to_vlc():
    global VLC_RUNNING, VLC_START_TIME, VLC_TITLE, VLC_CLIENT
    if not VLC_RUNNING:
        print('Setting to VLC!')
        if VLC_START_TIME == 0:
            VLC_START_TIME = int(time.time())
        VLC_CLIENT.connect()
        VLC_RUNNING = True
        if not pywinauto:
            VLC_START_TIME = int(time.time())
            VLC_CLIENT.update(details='Playing Media', start=VLC_START_TIME, large_image='vlc_large',
                              large_text='VideoLAN')
    if pywinauto:
        if VLC_TITLE != get_vlc_title(KEEP_EXTENTIONS):
            print("Title Changed!")
            VLC_START_TIME = int(time.time())
            VLC_TITLE = get_vlc_title(KEEP_EXTENTIONS)
            VLC_CLIENT.update(state=VLC_TITLE, details='Playing Media', start=VLC_START_TIME, large_image='vlc_large',
                              large_text='VideoLAN')


def close_vlc():
    global VLC_RUNNING, VLC_START_TIME, VLC_TITLE, VLC_CLIENT
    if VLC_RUNNING:
        print('Closing VLC!')
        VLC_CLIENT.close()
        VLC_RUNNING = False
        VLC_START_TIME = 0
        VLC_TITLE = ''


VLC_CLIENT = pypresence.Presence(client_id='890945084940492881')
VLC_RUNNING = False
VLC_START_TIME = 0
VLC_TITLE = ''

if not os.path.isdir('Logs'):
    print('Creating Logs Folder')
    os.mkdir('Logs')
if not os.path.isfile('Logs/run.log'):
    print('Creating Log File')
    open('Logs/run.log', 'a').close()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fmt = logging.Formatter("%(module)s:%(levelname)s:%(asctime)s:%(message)s")

log_file = logging.FileHandler('Logs/run.log', 'a')
log_file.setFormatter(fmt)
logger.addHandler(log_file)

while 1:
    try:
        if any('vlc' in i.name() for i in psutil.process_iter()):
            set_to_vlc()
        else:
            close_vlc()
        time.sleep(15)
    except KeyboardInterrupt:
        if VLC_RUNNING:
            VLC_CLIENT.close()
        exit(0)
    except pypresence.exceptions.InvalidID:
        print("Client ID is invalid or you are not connected to the internet!")
        logger.error("Invalid Client ID or no internet connection!")
    except Exception as e:
        print("Unhandeled exception as occured!")
        logger.critical('An unhandeled exception as occured!', exc_info=e)
