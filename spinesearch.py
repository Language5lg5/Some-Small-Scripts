import os
import re
import shutil

currentdir = os.getcwd()
dirlist1 = os.listdir(currentdir)

for subdir1 in dirlist1:
    if os.path.isdir(subdir1):
        dirlist2 = os.listdir(subdir1)
        for subdir2 in dirlist2:
            if os.path.isdir(subdir2):
                files = os.listdir(subdir2)
                for file in files:
                    if re.search(r'.skel$', file):
                        shutil.move(os.join(os.join(currentdir,subdir1),subdir2),'Spine')