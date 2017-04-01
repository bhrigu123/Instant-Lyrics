import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from src.settings import CONFIG_PATH

def create_default_config():
    if not os.path.isdir(os.path.dirname(CONFIG_PATH)):
        os.makedirs(os.path.dirname(CONFIG_PATH))

    Config = configparser.ConfigParser()
        
    Config.add_section('Main')
    Config.set('Main', "window width", "350")
    Config.set('Main', "window height", "650")

    with open(CONFIG_PATH, 'w') as config_file:
        Config.write(config_file)

def get_config():
    if not os.path.isfile(CONFIG_PATH):
        create_default_config()
    
    Config = configparser.ConfigParser()
    Config.read(CONFIG_PATH)
    return Config

def get_icon_path(rel_path):
    dir_of_py_file = os.path.dirname(__file__)
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource

def create_desktop_entry():
    #path of scr folder
    src_path = os.path.dirname(os.path.realpath(__file__))
    # path of base folder
    base_path = os.path.dirname(src_path)

    entry = "[Desktop Entry]\n"
    v = "Version=1.0\n"
    tp = "Type=Application\n"
    nm = "Name=Instant Lyrics\n"
    ic = "Icon="+base_path+"/icons/instant-lyrics-256.png\n"
    ex = "Exec=python2 "+base_path+"/InstantLyrics.py\n"
    cm = "Comment=Shows lyrics of songs instantly\n"
    tm = "Terminal=false\n"

    entry_path = os.getenv("HOME") + "/.local/share/applications/instant-lyrics.desktop"

    with open(entry_path, 'w') as file:
        file.write(entry)
        file.write(v)
        file.write(tp)
        file.write(nm)
        file.write(ic)
        file.write(ex)
        file.write(cm)
        file.write(tm)