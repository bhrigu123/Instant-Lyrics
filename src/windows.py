import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import dbus
import threading
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from src.lyrics import get_lyrics
from src.settings import CONFIG_PATH
from . import utils

class LyricsWindow(Gtk.Window):

    def __init__(self, type, app):
        Gtk.Window.__init__(self, title="Lyrics")
        self.set_icon_from_file(
                    utils.get_icon_path('../icons/instant-lyrics-32.png'))
        self.set_border_width(20)
        self.set_default_size(
                            int(app.Config.get('Main', 'window width')), 
                            int(app.Config.get('Main', 'window height')))
        self.set_position(Gtk.WindowPosition.CENTER)

        self.main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.main_box.set_size_request(
                            int(app.Config.get('Main', 'window width')), 
                            int(app.Config.get('Main', 'window height')))

        if(type == "get"):
            entry_hbox = self.create_input_box()
            self.main_box.pack_start(entry_hbox, False, False, 10)

        lyrics_vbox = self.create_lyrics_box(app)
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

    def create_lyrics_box(self, app):
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
        lyrics_vbox.set_size_request(
                        int(app.Config.get('Main', 'window width')), 
                        int(app.Config.get('Main', 'window height')))

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

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Instant-Lyrics Prefenreces")
        self.set_icon_from_file(utils.get_icon_path('../icons/instant-lyrics-32.png'))
        self.set_border_width(20)
        #self.set_default_size(350, 550)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.save = Gtk.Button.new_with_label("Save")
        self.save.set_sensitive(False)
        self.save.connect("clicked", self.save_config, app)

        pref_box = self.create_pref_box(app)
        self.main_box.pack_start(pref_box, True, True, 0)

        reset = Gtk.Button.new_with_label("Reset to default")
        reset.connect("clicked", self.reset_config, app)

        button_hbox = Gtk.Box(spacing=10)
        button_hbox.pack_start(reset, True, True, 0)
        button_hbox.pack_start(self.save, True, True, 0)

        desktop_entry = Gtk.Button.new_with_label("Create Desktop Entry")
        desktop_entry.connect("clicked", self.create_desktop_entry)

        self.message = Gtk.Label()

        self.main_box.pack_start(button_hbox, False, False, 0)
        self.main_box.pack_start(desktop_entry, True, True, 0)
        self.main_box.pack_start(self.message, True, True, 0)

        self.add(self.main_box)
        self.show_all()

    def create_pref_box(self, app):
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox) 
        width = Gtk.Label("Lyrics window width", xalign=0)
        self.width_val = Gtk.Entry()
        self.width_val.set_text(app.Config.get('Main', 'window width'))
        self.width_val.connect("changed", self.entry_change)

        hbox.pack_start(width, True, True, 0)
        hbox.pack_start(self.width_val, False, True, 0)
        
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        height = Gtk.Label("Lyrics window height", xalign=0)
        self.height_val = Gtk.Entry()
        self.height_val.set_text(app.Config.get('Main', 'window height'))
        self.height_val.connect("changed", self.entry_change)


        hbox.pack_start(height, True, True, 0)
        hbox.pack_start(self.height_val, False, True, 0)
        
        listbox.add(row)

        """ TODO: autostart
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Auto start", xalign=0)
        self.switch = Gtk.Switch()
        self.switch.connect("state-set", self.entry_change)
        self.switch.props.valign = Gtk.Align.CENTER
        switch_val = app.Config.getboolean('Main', 'auto start')
        if(switch_val):
            self.switch.set_active(True)
        else:
            self.switch.set_active(False)

        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(self.switch, False, True, 0)
        
        listbox.add(row)
        """
        
        return listbox

    def save_config(self, source, *arg):
        self.save.set_sensitive(False)
        self.message.set_markup("")
        app = arg[0]

        new_width = self.width_val.get_text()
        new_height = self.height_val.get_text()

        if(new_width.isdigit() and new_height.isdigit()):
            app.Config.set('Main', "window width", new_width)
            app.Config.set('Main', "window height", new_height)
            
            with open(CONFIG_PATH, 'w') as config_file:
                app.Config.write(config_file)

            return

        msg = ("Invalid values of height and width\n"
                "Please add valid positive integers")

        self.show_message(msg)

    def entry_change(self, source):
        self.save.set_sensitive(True)

    def reset_config(self, source, *arg):
        utils.create_default_config()
        app = arg[0]
        app.Config = utils.get_config()

        self.width_val.set_text(app.Config.get('Main', 'window width'))
        self.height_val.set_text(app.Config.get('Main', 'window height'))
        self.save.set_sensitive(False)

    def create_desktop_entry(self, source):
        utils.create_desktop_entry()
        msg = ("Desktop entry created. You can now start the\n" 
                "application from your Applications Launcher.\n\n"
                "<small>If you ever change the location "
                "of the Instant-Lyrics\nfolder, you will "
                "need to create the Desktop Entry\nfrom "
                "here again.</small>")

        self.show_message(msg)

    def show_message(self, msg):
        self.message.set_markup(msg)
