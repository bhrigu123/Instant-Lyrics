import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator

import os
import signal
import dbus
from Lyrics import get_lyrics

APPINDICATOR_ID = 'myappindicator'


class LyricsWindow(Gtk.Window):

	def __init__(self, type):
		Gtk.Window.__init__(self, title="Lyrics")
		self.set_border_width(20)
		self.set_default_size(350, 700)
		self.set_position(Gtk.WindowPosition.CENTER)

		self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.main_box.set_size_request(350, 700)
		
		if(type == "get"):

			entry_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
			entry_hbox.set_property("margin", 10)

			self.input = Gtk.Entry()
			self.input.set_text("Enter song/artist")
			entry_hbox.pack_start(self.input, True, True, 0)

			submit = Gtk.Button.new_with_label("Get Lyrics")
			submit.connect("clicked", self.fetch_lyrics)
			entry_hbox.pack_start(submit, True, True, 0)

			self.main_box.pack_start(entry_hbox, False, False, 10)


		self.lyrics_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

		self.title = Gtk.Label()
		self.title.set_justify(Gtk.Justification.CENTER)

		self.lyrics = Gtk.Label()
		self.lyrics.set_justify(Gtk.Justification.CENTER)
		self.lyrics.set_property("margin_left", 40)
		self.lyrics.set_property("margin_right", 40)
		self.lyrics.set_line_wrap(True)


		self.lyrics_vbox.pack_start(self.title, False, False, 5)
		self.lyrics_vbox.pack_start(self.lyrics, False, False, 5)
		self.lyrics_vbox.set_size_request(350, 700)

		self.main_box.pack_start(self.lyrics_vbox, True, True, 0)

		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled.add(self.main_box)

		self.add(scrolled)
		self.show_all()

		if(type == "spotify"):
			self.get_spotify()

	def fetch_lyrics(self, source):

		text = self.input.get_text()
		lyrics = get_lyrics(text)

		text = "<b><big>"+text+"</big></b>"
		self.title.set_markup(text)
		self.lyrics.set_text(lyrics)

	def get_spotify_song_data(self):
		session_bus = dbus.SessionBus()
		
		spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify","/org/mpris/MediaPlayer2")
		spotify_properties = dbus.Interface(spotify_bus,"org.freedesktop.DBus.Properties")
		metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
	
		title = metadata['xesam:title'].encode('utf-8')
		artist = metadata['xesam:artist'][0].encode('utf-8')
		return {'title':title, 'artist':artist,'artUrl':str(metadata['mpris:artUrl']) }

	def get_spotify(self):

		try:
			song_data = self.get_spotify_song_data()
			song = song_data['title']
			artist = song_data['artist']
			artUrl = song_data['artUrl']
		except:
			self.title.set_markup("<big><b>Error</b></big>")
			self.lyrics.set_text("Could not get current spotify song details")
			return

		title = "<b><big>" + song + "</big>\n" + artist + "</b>"
		self.title.set_markup(title)

		lyrics = get_lyrics(song + " " + artist)
		self.lyrics.set_text(lyrics)

class AppIndicator():
	
	def __init__(self):
		signal.signal(signal.SIGINT, signal.SIG_DFL)

		indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('lyrics.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
		indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
		indicator.set_menu(self.build_menu())
		Gtk.main()
	
	def build_menu(self):
		menu = Gtk.Menu()

		get_lyrics = Gtk.MenuItem('Get Lyrics')
		get_lyrics.connect('activate', self.fetch_lyrics)

		spotify_lyrics = Gtk.MenuItem('Spotify Lyrics')
		spotify_lyrics.connect('activate', self.spotify_lyrics)

		item_quit = Gtk.MenuItem('Quit')
		item_quit.connect('activate', self.quit)

		
		menu.append(get_lyrics)
		menu.append(spotify_lyrics)
		menu.append(item_quit)
		menu.show_all()
		return menu
	 
	def fetch_lyrics(self, source):
		win = LyricsWindow("get")

	def spotify_lyrics(self, source):
		win = LyricsWindow("spotify")

	def quit(self, source):
		Gtk.main_quit()

if __name__ == "__main__":
	app = AppIndicator()