import os
from pathlib import Path
import shutil
import sys

home = Path.home()
extension = input("extension type: ")
rawpathh = input("path (default is Downloads): ")
name = input("folder name: ")

if rawpathh == "":
    rawpathh = f"{home}/Downloads"

pathh = Path(rawpathh)

if name == "":
    name = "New-Folder"

if extension == "":
    extension = input("no extension input detected, type a new or retype an extension: ")
    if extension == "":
        print("no extension detected still, exiting")
        sys.exit()

confirm = input(f"confirm these are correct by typing yes:\n\nextension: {extension}\npath: {rawpathh}\nfolder name: {name}\n\nconfirm? ")

if confirm == "yes":

    destination = pathh / name

    destination.mkdir(parents=True, exist_ok=True)

    for x in os.listdir(rawpathh):
        if x.endswith(extension):
            print(x)
            shutil.move(f"{rawpathh}/{x}", destination)
