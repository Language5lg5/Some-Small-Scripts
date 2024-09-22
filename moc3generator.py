import json

json_name=input("Input json name: ")
with open(json_name+'.json','r') as load_f:
    load_dict=json.load(load_f)

l2dbytes=load_dict['_bytes']
'''print(type(l2dbytes))'''

import struct
with open(json_name+'.moc3','wb')as fp:
    for x in l2dbytes:
        a=struct.pack('B',x)
        fp.write(a)
print('\nDone.')
input('\nEnter any key to quit...')