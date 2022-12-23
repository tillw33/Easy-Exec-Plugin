import vim
import os
from os import listdir
from os.path import isfile, join
import platform

max_depth = 3

class Finder:
    def find(self, new_window):
        # get full path to open file
        mypath = os.getcwd()
        myfile = vim.eval("@%")
        myloc  = os.path.join(mypath, myfile)
        mypath = os.path.dirname(myloc)

        # loop through dirs below, looking for main file
        found = False
        depth = 0
        while not found and depth < max_depth:
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            for file in onlyfiles:
                try:
                    name, ext = file.split('.')
                except:
                    continue
                if "main" in ext:
                    found = True
                    name, ext = file.split('.')
                    ext = ext.replace('main','')
                    file = '.'.join([name, ext])
                    main_file = os.path.join(mypath,file)
                    # print(main_file)
                    break
            if not found:
                mypath = os.path.dirname(mypath) # move one dir for next iteration
            depth += 1
        if not found: 
            if platform.system() == 'Linux':
                main_file = r"./" + myfile # execute current file for
            elif platform.system() == 'Windows':
                main_file = r".\" + myfile
            else:
                print("error, os unknown")
                exit()
        if new_window:
            self.run_vert_right(main_file) # :EEextensive
        else:
            self.run_in_ter(main_file) # :EEshort
                    
    def run_vert_right(self,file):
        vim.command(":w")
        vim.command(":vert belowright sb") 
        vim.command(":ter "+file)
        # vim.command("")

    def run_in_ter(self, file):
        vim.command(":w")
        vim.command(":!"+file)
