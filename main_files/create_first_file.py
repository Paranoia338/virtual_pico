import os
from pathlib import Path

from appdirs import AppDirs


class InitializeFile:
    commands_names = ["Ionut", "Andrei", "Irinel", "Gabriela", "Vasile", "Ion", "Gheorghe"]
    appName = "Stimuli_Editor"
    appAuthor = "Lorenzo Varriano"
    dirs = AppDirs(appName, appAuthor, roaming=True)
    directory = Path(dirs.user_data_dir)
    file = Path(dirs.user_data_dir + "/data.h5")

    def __init__(self):
        if self.directory.exists():
            print("Folder-ul exista deja")
            # print("The folder with configuration files exists")
            self.check_file_and_create(self.file)
        else:
            print("Folder-ul nu exista")
            try:
                os.makedirs(self.directory)
                print("Folder-ul a fost creat acum")
                self.check_file_and_create(self.file)
            except Exception as e:
                pass
                # print(e)

    @classmethod
    def check_file_and_create(cls, file):
        if file.exists():
            print("Fisier-ul exista deja")
            pass
        else:
            print("Fisier-ul nu exista")
            try:
                f = open(file, "w+")
                print("Fisier-ul a fost creat acum")
                f.close()
            except Exception as e:
                pass
                # print(e)
