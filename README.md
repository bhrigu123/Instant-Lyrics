# Instant-Lyrics

Get lyrics of the currently playing spotify song, or any song, instantly.

A linux application with a very convinient GUI. Build with Python Gtk+3 (gi).

# Screenshot
![Screenshot](https://cloud.githubusercontent.com/assets/6123105/23824316/3fe58044-069a-11e7-804e-180ea4041002.jpeg)

# Working
### GIF
![working](https://cloud.githubusercontent.com/assets/6123105/23824730/e0e0829e-06a1-11e7-8d57-3235c4266f2c.gif)

# Requirements

* python-gi

* python-dbus

* requests

* beautifulsoup4

* lxml

`requests`, `beautifulsoup4` and `lxml` can be installed via pip (shown below).

To install `python-dbus` and `python-gi`, you will need to install using your package manager.

For Ubuntu/Debian based systems, you can install as:

`sudo apt install python-gi`

`sudo apt install python-dbus`


# Installation

## From source

1. Clone the repository. `git clone https://github.com/bhrigu123/Instant-Lyrics.git`

2. `cd Instant-Lyrics/`

3. Run the command `pip install -r requirements.txt` to install the pip packages.

3. Run the command `python InstantLyrics.py`

The icon will appear in the system tray (indicator panel). You can start using the application from there.


# Creating a launcher shortcut

You can either use the application from the terminal, or create a launcher shortcut, which will add the application in your launcher menu:

![Launcher](https://cloud.githubusercontent.com/assets/6123105/23824317/4735e83e-069a-11e7-8b1e-2814632bb3aa.jpeg)

You can find several ways of doing so. You can also follow the below steps:

(You will have to use `sudo` while doing this from terminal)

* Create a new file in the location `/usr/share/applications` and name it `instant-lyrics.desktop`

* Paste the following in the created file:

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

Replace `[path of icon]` with the complete path of the icon. The icon is named `icon.svg` inside the root directory of the repository.

Replace `[path of python file]` with the complete path of the file `InstantLyrics.py` which is also in the root directory of the repo.

These two lines should look something like:

```
Icon=/home/ubuntu/Instant-Lyrics/icon.svg
Exec=python /home/ubuntu/Instant-Lyrics/InstantLyrics.py
```

You should be able to see the `Instant Lyrics` application shortcut in your launcher menu.

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

