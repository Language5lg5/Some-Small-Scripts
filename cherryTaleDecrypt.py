import os

def changeVersion(fileobj):
    version_fake = b'\x32\x30\x31\x38\x2E\x33\x2E\x35\x66\x31\x00'  #2018.3.5f1.
    version = b'\x32\x30\x32\x30\x2E\x33\x2E\x34\x31\x66\x31'       #2020.3.41f1
    #consider improvement to speed up
    data = fileobj.read()       
    newdata = data.replace(version_fake,version)
    fileobj.seek(0)
    fileobj.write(newdata)
    fileobj.truncate()

def changeIdx(fileobj):
    v7 = [0x3FB, 0xD99, 0x197C]
    v8 = os.fstat(fileobj.fileno()).st_size
    for v12 in v7:
        if v8 > v12:
            #v19 = v8 - v12
            fileobj.seek(v12)
            v21 = fileobj.read(1)
            v19 = v8 - v12
            #data[v12] = data[v8 - v12]
            fileobj.seek(v19)
            tmp = fileobj.read(1)
            fileobj.seek(v12)
            fileobj.write(tmp)
            #data[v19] = v21
            fileobj.seek(v19)
            fileobj.write(v21)
        else:
            return

current = os.path.dirname(__file__)
os.chdir(current)
files = os.listdir(current)
for file in files:
    #check if file is this py file or dir, still can improve to identify if file is target
    if file == os.path.abspath(__file__):
        continue
    if os.path.isdir(file):
        continue
    #prepare 2 files, one to read, one to write into
    with open(file,'rb') as file_r, open('modified'+file,'wb+') as file_w:
        file_w.write(file_r.read())     #copy the original file
        file_w.seek(0)      #make point to head
        changeVersion(file_w)    #change copy version hex
        file_w.seek(0)
        changeIdx(file_w)        #change decrpyted(incorrected) idx

print("Finish")