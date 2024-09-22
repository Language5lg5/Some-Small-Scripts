import os
import shutil

current = os.path.dirname(__file__)

os.chdir(current)

files = os.listdir(current)

dirs = set()

numofby = int(input("How many chars to group: "))

for file in files:
    if os.path.abspath(file) == __file__:
        continue

    if os.path.isdir(file):
        dirs.add(file)
        continue
    
    start_name = file[:numofby]
    
    if not start_name in dirs:
        os.mkdir(start_name)
        dirs.add(start_name)
    
    shutil.move(os.path.abspath(file), os.path.abspath(start_name))