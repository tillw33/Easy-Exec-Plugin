if !has('python3')
    echomsg ':python3 is not available, plugin will not be loaded.'
    finish
endif

python3 import finder
python3 finder = finder.Finder()

command! EEshort python3 finder.find(False)
command! EEextensive python3 finder.find(True)
