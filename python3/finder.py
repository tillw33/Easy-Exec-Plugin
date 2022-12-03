import vim
import os
from os import listdir
from os.path import isfile, join

max_depth = 3

class Finder:
    def find(self, new_window):
        mypath = os.getcwd()
        
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
                    main_file = os.path.join(mypath,file.replace("main",""))
                    break
            if not found:
                mypath = os.path.dirname(mypath)
            depth += 1
        if not found:
            print('Run main file: executing current file')
            main_file = vim.eval("@%")
        else:
            print('Run main file: executing '+main_file)

        if new_window:
            self.run_vert_right(main_file)
        else:
            self.run_in_ter(main_file)
                    
    def run_vert_right(self,file):
        ext = file.split('.')[-1]
        if ext == 'py':
            vim.command(":w")
            vim.command(":vert belowright sb")# 
            vim.command(":ter python3 "+file)
        else:
            print('unknown extension:', ext)
            print('nothing will be executed')

    def run_in_ter(self, file):
        ext = file.split('.')[-1]
        if ext == 'py':
            vim.command(":w")
            vim.command(":exec '!python' shellescape('"+file+"', 1)")
        else:
            print('unknown extension:', ext)
            print('nothing will be executed')
