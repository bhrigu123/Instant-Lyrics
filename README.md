# Instant-Lyrics

Instantly fetches the lyrics of the currently playing spotify song, or any song, and displays it on a window.

A linux application with a very convinient GUI. Build with Python Gtk+3 (gi).

# Screenshot
![Screenshot](https://cloud.githubusercontent.com/assets/6123105/23824316/3fe58044-069a-11e7-804e-180ea4041002.jpeg)

# Working
### GIF
![working](https://cloud.githubusercontent.com/assets/6123105/23824730/e0e0829e-06a1-11e7-8d57-3235c4266f2c.gif)


# Compatibility

* Python 2/3

* Linux


# Installation

## From Source

### Requirements

* python-gi (PyGObject)

* AppIndicator3

* python-dbus

* requests

* beautifulsoup4

* lxml


First, install the requirements:

### For Ubuntu/Debian based systems:

``` sh
sudo apt install python-gi python-dbus gir1.2-appindicator3-0.1 python-requests python-bs4 python-lxml
```

(requests, lxml and bs4 can be install from `pip` also: `pip install requests lxml beautifiulsoup4`)

### For Arch users

``` sh
sudo pacman -S python2-dbus python2-requests python2-lxml python2-beautifulsoup4 python2-gobject libappindicator-gtk3
```

### Fedora

``` sh
sudo dnf install dbus-python python-gobject libappindicator-gtk3 python2-requests python-beautifulsoup4 python2-lxml
```

## Install from source

After you've installed the dependencies, open terminal and go to the directory where you want to install. Enter the commands:

``` sh
git clone https://github.com/bhrigu123/Instant-Lyrics.git

cd Instant-Lyrics/

python InstantLyrics.py
```

The icon will appear in the system tray (indicator panel). You can start using the application from there.

<br>

# Creating a launcher shortcut

If you have installed from source, you can go to **Preferences** from the menu options, and click on the button `Create Desktop Entry`.

You should be able to see the `Instant Lyrics` application shortcut in your launcher menu.

You can also find several manual ways of doing so from the web.

![Launcher](https://cloud.githubusercontent.com/assets/6123105/23824317/4735e83e-069a-11e7-8b1e-2814632bb3aa.jpeg)


# Contribution
Create an issue to discuss the changes/modifications before sending a PR.

======
## Icon Credits
Icon made by [Freepik](http://www.freepik.com/) from www.flaticon.com

======

## The MIT License
> Copyright (c) 2017 Bhrigu Srivastava http://bhrigu.me

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

