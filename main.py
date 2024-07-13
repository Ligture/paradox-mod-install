import os
import shutil
import generate

# 0 file 1 dir
method = 1
if method == 0:
    #path mod实际存在的位置
    path = os.path.normpath(r"D:\WorkshopDLv2.0.0\steamcmd\steamapps\workshop\content\1158310\2752613114")
    #modpath mod移动到的位置
    #默认情况应为r'%USER_DOCUMENTS%\Paradox Interactive\Crusader Kings III\mod'
    modpath = "E:\Crusader Kings 3 v1.12.5\gamedata\mod"
    mod1 = generate.Generatemodfile(modpath)
    if not os.path.dirname(path) == modpath:
        shutil.move(path, os.path.join(modpath, os.path.basename(path)))
    mod1.start(os.path.basename(path))


elif method == 1:
    #path 多个mod实际存在的文件夹
    path = os.path.normpath(r'E:\Crusader Kings 3 v1.12.5\gamedata\mod')
    #modpath mod移动到的位置
    # 默认情况应为r'%USER_DOCUMENTS%\Paradox Interactive\Crusader Kings III\mod'
    modpath = r'E:\Crusader Kings 3 v1.12.5\gamedata\mod'
    mod1 = generate.Generatemodfile(modpath)
    mods = os.listdir(path)
    for a in mods:
        if os.path.isfile(os.path.join(path, a)):
            mods.remove(a)

    for i in mods:
        i1 = os.path.join(path, i)
        if not path == os.path.join(modpath, 'mod'):
            shutil.move(i1, os.path.join(modpath, os.path.basename(i1)))
        mod1.start(os.path.basename(i1))

#dasda