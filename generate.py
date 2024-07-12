import os

class generatemodfile():
    def __init__(self, datapath):
        self.datapath = datapath
        self.modpath = os.path.normpath(datapath + "\\mod")
    def start(self, modname):
        targetmod = os.path.normpath(self.modpath + f'\\{modname}')
        with open(targetmod + '\\descriptor.mod', "r", encoding='utf-8') as file:
            lines = file.readlines()
            for i in lines:
                if i[0:4] == 'path':
                    lines.remove(i)
                if i[0:4] == 'name':
                    modname = eval(i[5:])
            lines.append(f'\npath="{self.modpath}\\{modname}"'.replace('\\','/'))

        os.rename(targetmod, self.modpath + f'\\{modname}')
        with open(f'{self.modpath}\\{modname}.mod', 'w', encoding='utf-8') as file:
            file.writelines(lines)



