# -- coding: utf-8 --
import os
import zipfile
import send2trash
import shutil
import sys

def support_gbk(zip_file: zipfile.ZipFile):
    name_to_info = zip_file.NameToInfo
    # copy map first
    for name, info in name_to_info.copy().items():
        real_name = name.encode('cp437').decode('gbk')
        if real_name != name:
            info.filename = real_name
            del name_to_info[name]
            name_to_info[real_name] = info
    return zip_file

# Get current path and change working path to this
current = os.path.dirname(__file__)
os.chdir(current)

# Extract zip files and move them to trash
extraction_path = current
files = os.listdir(current)
for file in files:
    if os.path.isfile(file) and file.endswith('.zip'):
        with support_gbk(zipfile.ZipFile(file)) as zip_ref:
            zip_ref.extractall(current)
        send2trash.send2trash(file)

# Move files to their parent dir
files = os.listdir(current)
for dir in files:
    if os.path.isdir(dir):
        subfiles = os.listdir(dir)
        for subfile in subfiles:
            shutil.move(os.path.join(dir,subfile),os.path.join(current,dir+subfile))
        os.rmdir(dir)
        
#os.remove(__file__)