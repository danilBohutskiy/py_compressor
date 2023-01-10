import os
from Compressor import *

def run():
    
    print('Start...')

    model = Compressor(os.getcwd())
    os.chdir('./' + model.inputdir)

    for directory in os.listdir():
        os.chdir('./' + directory)
        print('Current directory: ' + directory)

        model.clearOutputDir(directory)

        for index, filename in enumerate(os.listdir()):
            img = model.compressImage(filename)
            model.saveImgToDir(img, directory, filename)
            
        os.chdir('..')
    
    print('Done!')

run()
