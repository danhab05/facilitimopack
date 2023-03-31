import os
import shutil


for el in os.listdir("."):
    if ".py" not in el:
        for files in os.listdir(el):
            if "DS_Store" not  in files:
                for file in os.listdir(el + "/" + files):
                    if ".JPG" in files or "DS_Store" in files:
                        os.rename(el + "/" + files + "/" + file, el + "/" + files.replace("JPG", "jpg"))