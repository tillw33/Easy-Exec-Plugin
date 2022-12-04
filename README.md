# Easy Execute Plugin

## Description
This is a simple plugin and just my first project writing a neovim plugin.  
Its purpose is to allow easy execution of a main file. It searches for a *file_to_run*.*main*ext file up to three directories up and executes the corresponding *file_to_run*.ext, either with :EEshort or :EEextensive. "Small" opens a little terminal at the bottom, "Large" splits vertically and executes the file in a new buffer on the right. If no file is found, the commands will execute the current file.

Its easily extendable to different programming languages.

## Install

The plugin can be installed using for example packer:
```
use {"tillw33/Easy-Exec-Plugin"}
```

## Usage
You can bind this commands to any key you want.
```
:EEextensive
```
- writes the current file, opens a new buffer on the right, executes the mainfile there

```
:EEshort
```
- writes the current file, executes the mainfile in a small terminal at the bottom

