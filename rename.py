import os
import shutil


for el in os.listdir("."):
    if ".py" not in el:
        for files in os.listdir(el):
            if ".JPG" in files:
                os.rename(el + "/" + files, el + "/" + files.replace("JPG", "jpg"))