import os
import re

target = '.assetbundle$'

string_to_keep = b'\x55\x6e\x69\x74\x79\x46\x53'    #Find 'UnityFS' in Hex
num = 0; success = 0                    #Record how many files read and how many of them are modified sucessfully
#To get files in current directory
current = os.path.dirname(__file__)
os.chdir(current)
files = os.listdir(current)

#Where outputs are
if 'output' not in files:
    os.mkdir('output')          

for file in files:
    result = re.search(target, file)

    if os.path.isfile(file) and re.search(target, file):
        num += 1
        with open(file, 'rb') as f:
            data = f.read()
        index = data.find(string_to_keep)   #Find 1st 'UnityFS'
        if index != -1:
            os.chdir('output')
            with open('new' + file,'wb') as new_f:
                new_f.write(data[index:])
            success += 1
            os.chdir('..')

print('Number of files: ', num)
print('Success: ', success)