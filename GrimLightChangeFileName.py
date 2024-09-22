import os

currentfld = os.path.dirname(__file__)
os.chdir(currentfld)
files = os.listdir(currentfld)
for file in files:
    if file.count('.') != 2:
        continue
    a,ext=os.path.splitext(file)
    name,extension = os.path.splitext(a)
    if extension == '.json':
        extension = '.skel'
    os.rename(file,name + extension)