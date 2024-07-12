import os
import shutil
import generate
path = os.path.normpath(r'E:\Crusader Kings 3 v1.12.5\gamedata\mod')
datapath = r'E:\Crusader Kings 3 v1.12.5\gamedata'
mod1 = generate.generatemodfile(datapath)
mods = os.listdir(path)
for a in mods:
    if os.path.isfile(os.path.join(path, a)):
        mods.remove(a)

for i in mods:
    i1 = os.path.join(path, i)
    if not path == os.path.join(datapath, 'mod'):
        shutil.move(i1, os.path.join(datapath, 'mod', os.path.basename(i1)))
    mod1.start(os.path.basename(i1))
