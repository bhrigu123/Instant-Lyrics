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
You can either download an [AppImage](http://appimage.org/) or install from source.

## AppImage

AppImage runs on most of the Linux distros.

1. Download the `.AppImage` file of the latest version from the [releases](https://github.com/bhrigu123/Instant-Lyrics/releases)

2. Make the file executable (two ways):
    
    * Open terminal. Go to the directory of the downloaded AppImage file. Run the command:
        `chmod a+x filename.AppImage`. (where `filename` is your downloaded AppImage)

    * Or you can also use GUI: ([see this](http://discourse.appimage.org/t/how-to-make-an-appimage-executable/80))

3. Run the file by double-clicking it. (or from terminal using the command: `./filename.AppImage`)

4. The first time you run it, it will ask you to integrate the file with system. Click `Yes`. This will create a desktop entry in you Applications list, and you can start the app from your Applications also.


## From Source

To install from source, you will need to install the required dependencies first (shown below):

### Requirements

* python-gi (PyGObject)

* AppIndicator3

* python-dbus

* requests

* beautifulsoup4

* lxml


Shown below is installation and running with Python 2.

### For Ubuntu/Debian based systems:

``` sh
sudo apt install python-gi python-dbus gir1.2-appindicator3-0.1
```

``` sh
sudo apt install python-requests python-bs4 python-lxml
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

If you have installed from source, you can either use the application from the terminal, or create a launcher shortcut (which will add the application in your launcher menu):

![Launcher](https://cloud.githubusercontent.com/assets/6123105/23824317/4735e83e-069a-11e7-8b1e-2814632bb3aa.jpeg)

You can find several ways of doing so. You can also follow the below steps:

(From the terminal)

* `sudo touch /usr/share/applications/instant-lyrics.desktop`. (Creates a new file in /usr/share/applications).

* Open this new file with an editor. Eg. opening with gedit: `gedit /usr/share/applications/instant-lyrics.desktop`. Paste the following in it:

```
[Desktop Entry]
Version=1.0
Type=Application
Name=Instant Lyrics
Comment=Show lyrics of songs instantly
Icon=[path of icon]
Exec=python [path of python file]
Terminal=false
```

Replace `[path of icon]` with the complete path of the icon. The icon is present in `icons/instant-lyrics.svg` inside the root directory of the repository.

Replace `[path of python file]` with the complete path of the file `InstantLyrics.py` which is also in the root directory of the repo.

These two lines should look something like:

```
Icon=/home/ubuntu/Instant-Lyrics/icons/instant-lyrics.svg
Exec=python /home/ubuntu/Instant-Lyrics/InstantLyrics.py
```

* Save the file.

You should be able to see the `Instant Lyrics` application shortcut in your launcher menu.


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

