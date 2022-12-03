# Easy Execute Plugin

## Description
This is a simple plugin and just my first project writing a neovim plugin.  
Its purpose is to allow easy execution of python files. It searches for a *file_to_run*.mainpy file up to the directories up and executes the corresponding *file_to_run*.py, either with :EEshort or :EEextensive. "Small" opens a little terminal at the bottom, "Large" splits vertically and executes the file in a new buffer on the right. If no file is found, the commands will execute the current file.

Its easily extendable to different programming languages.

## Install

The plugin can be installed using for example packer:

```
use {"tillw33/Easy-Exec-Plugin" }
```
