import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Gtk, Gdk

import signal
import threading

from src.windows import LyricsWindow, PreferenceWindow
from . import utils
from src.settings import APPINDICATOR_ID, CONFIG_PATH


class AppIndicator():

    def __init__(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        Gdk.set_allowed_backends("x11,*")
        
        indicator = appindicator.Indicator.new(APPINDICATOR_ID, utils.get_icon_path(
            '../icons/instant-lyrics-24.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        indicator.set_menu(self.build_menu())

        self.Config = utils.get_config()
        Gtk.main()

    def build_menu(self):
        menu = Gtk.Menu()

        get_lyrics = Gtk.MenuItem('Get Lyrics')
        get_lyrics.connect('activate', self.fetch_lyrics)

        spotify_lyrics = Gtk.MenuItem('Spotify Lyrics')
        spotify_lyrics.connect('activate', self.spotify_lyrics)

        preferences = Gtk.MenuItem('Preferences')
        preferences.connect('activate', self.preferences)

        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.quit)

        menu.append(get_lyrics)
        menu.append(spotify_lyrics)
        menu.append(preferences)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def fetch_lyrics(self, source):
        win = LyricsWindow("get", self)

    def spotify_lyrics(self, source):
        win = LyricsWindow("spotify", self)
        thread = threading.Thread(target=win.get_spotify)
        thread.daemon = True
        thread.start()

    def preferences(self, source):
        win = PreferenceWindow(self)

    def quit(self, source):
        Gtk.main_quit()