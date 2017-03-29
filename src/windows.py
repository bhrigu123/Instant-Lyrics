import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import dbus
import threading

from src.utils import get_icon_path
from src.lyrics import get_lyrics

class LyricsWindow(Gtk.Window):

    def __init__(self, type):
        Gtk.Window.__init__(self, title="Lyrics")
        self.set_icon_from_file(get_icon_path('../icons/instant-lyrics.svg'))
        self.set_border_width(20)
        self.set_default_size(350, 650)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_box.set_size_request(350, 700)

        if(type == "get"):
            entry_hbox = self.create_input_box()
            self.main_box.pack_start(entry_hbox, False, False, 10)

        lyrics_vbox = self.create_lyrics_box()
        self.main_box.pack_start(lyrics_vbox, True, True, 0)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.main_box)

        self.add(scrolled)
        self.show_all()

    def on_key_release(self, widget, ev, data=None):
        if ev.keyval == Gdk.KEY_Return:
            self.fetch_lyrics()

    def create_input_box(self):
        entry_hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        entry_hbox.set_property("margin", 10)

        self.input = Gtk.Entry()
        self.input.set_text("song/artist")
        self.input.connect("key-release-event", self.on_key_release)
        entry_hbox.pack_start(self.input, True, True, 0)

        submit = Gtk.Button.new_with_label("Get Lyrics")
        submit.connect("clicked", self.fetch_lyrics)
        entry_hbox.pack_start(submit, True, True, 0)

        return entry_hbox

    def create_lyrics_box(self):
        lyrics_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.title = Gtk.Label()
        self.title.set_justify(Gtk.Justification.CENTER)

        self.lyrics = Gtk.Label()
        self.lyrics.set_justify(Gtk.Justification.CENTER)
        self.lyrics.set_property("margin_left", 40)
        self.lyrics.set_property("margin_right", 40)
        self.lyrics.set_line_wrap(True)

        self.spinner = Gtk.Spinner()

        lyrics_vbox.pack_start(self.title, False, False, 5)
        lyrics_vbox.pack_start(self.spinner, False, False, 5)
        lyrics_vbox.pack_start(self.lyrics, False, False, 5)
        lyrics_vbox.set_size_request(350, 700)

        return lyrics_vbox

    def put_lyrics(self, song):
        self.spinner.start()

        self.lyrics.set_text("")
        lyrics = get_lyrics(song)
        self.lyrics.set_text(lyrics)

        self.spinner.stop()

    def fetch_lyrics(self, source=None):
        input = self.input.get_text()
        text = "<b><big>" + input + "</big></b>"
        self.title.set_markup(text)

        thread = threading.Thread(
            target=self.put_lyrics, kwargs={'song': input})
        thread.daemon = True
        thread.start()

    def get_spotify_song_data(self):
        session_bus = dbus.SessionBus()

        spotify_bus = session_bus.get_object(
            "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(
            spotify_bus, "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get(
            "org.mpris.MediaPlayer2.Player", "Metadata")

        title = metadata['xesam:title'].encode(
            'utf-8').decode('utf-8').replace("&", "&amp;")
        artist = metadata['xesam:artist'][0].encode(
            'utf-8').decode('utf-8').replace("&", "&amp;")
        return {'title': title, 'artist': artist}

    def get_spotify(self):

        try:
            song_data = self.get_spotify_song_data()
            song = song_data['title']
            artist = song_data['artist']
        except:
            self.title.set_markup("<big><b>Error</b></big>")
            message = ("Could not get current spotify song\n"
                       "Either spotify is not running or\n"
                       "no song is playing on spotify.\n\n"
                       "Else, report an issue <a href=\"https://"
                       "github.com/bhrigu123/Instant-Lyrics\" "
                       "title=\"Repo url\">here</a>")

            self.lyrics.set_markup(message)
            return

        title = "<b><big>" + song + "</big>\n" + artist + "</b>"
        self.title.set_markup(title)

        self.put_lyrics(song + " " + artist)

class PreferenceWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Instant-Lyrics Prefenreces")
        self.set_icon_from_file(get_icon_path('../icons/instant-lyrics.svg'))
        self.set_border_width(20)
        self.set_default_size(350, 550)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_box.set_size_request(350, 550)

        pref_box = self.create_pref_box()
        self.main_box.pack_start(lyrics_vbox, True, True, 0)

        self.add(main_box)
        self.show_all()