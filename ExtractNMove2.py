'''
-start_location
    -ExtractNMove.py
    -dir1
        -zipfile1.zip
    ...
    -dirN
        -zipfileN.zip
    -dirloc1
        -dir1
            -file1
            -file2
            ...
            -fileN
        ...
        -dirN
    -dirloc2
    ...
    -dirlocN
'''

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
start_location = os.path.dirname(__file__)
os.chdir(start_location)

# Extract zip files and move them to trash
extraction_path = start_location
dirs = os.listdir(start_location)
for dirx in dirs:
    if os.path.isfile(dirx):
        continue
    zips = os.listdir(dirx)
    for zip in zips:
        if os.path.isfile(zip) and zip.endswith('.zip'):
            with support_gbk(zipfile.ZipFile(zip)) as zip_ref:
                zip_ref.extractall(extraction_path)
            send2trash.send2trash(zip)

for dirloc in os.listdir(start_location):

    # Move files to their parent dir
    if os.path.isdir(dirloc):
        files = os.listdir(dirloc)
        os.chdir(dirloc)
        for dir in files:
            if os.path.isdir(dir):
                subfiles = os.listdir(dir)
                for subfile in subfiles:
                    shutil.move(os.path.join(dir,subfile),dir+subfile)
                os.rmdir(dir)
        
        os.chdir(start_location)

response=input("Another move? ('y' to continue or exit)") 
if 'y' == response.lower() or 'yes' == response.lower():
    for dirloc in os.listdir(start_location):
        if not os.path.isdir(dirloc):
            continue
        files = os.listdir(dirloc)
        os.chdir(dirloc)
        for file in files:
            if os.path.isfile(file):
                shutil.move(file,os.path.join(start_location,dirloc+file))
        
        os.chdir(start_location)
        os.rmdir(dirloc)        #delete dirlocs
        

#os.remove(__file__)    #delete self after complete successfully