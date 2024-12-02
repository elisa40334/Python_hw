import os
from os.path import getsize,join

def list_file_by_size(directory, n):
    for root, dirs, files in os.walk(directory, topdown=True):
        for file in files:
            if getsize(join(root,file)) >= n:
                yield (os.path.join(root,file),getsize(join(root,file)))

    

    # for entry in os.scandir(directory):
    #     if  os.path.getsize(entry) >= n:
    #         yield (os.path.join(directory,entry), os.path.getsize(entry))
            
            
# for f in list_file_by_size("/Users",1000000):
#     print(f)
    
cmd ='' 
while True:
    try:
        s = input()
        cmd += s+'\n'
    except EOFError:
        break
p = compile(cmd,'default','exec')
exec(p)     