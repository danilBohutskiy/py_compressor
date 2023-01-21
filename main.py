import os

from colorama import init as colorama_init
from colorama import Back
from colorama import Fore
from colorama import Style

colorama_init()

from Compressor import Compressor

def run():
    
    print('Start...')

    model = Compressor(os.getcwd())
    os.chdir('./' + model.inputdir)

    for directory in os.listdir():
        os.chdir('./' + directory)
        print(f"{Fore.YELLOW}Current directory:{Style.RESET_ALL} " + directory)
        model.clearOutputDir(directory)

        for index, filename in enumerate(os.listdir()):
            
            print('Current file: ' + filename)
            
            pathToFile = model.getPathToSrcFie(filename)
            pathToOutput = model.getPathToOutputDirectory(directory)

            compressor = model.getCompressor(pathToFile)

            if compressor == None:
                continue

            compressor.compress(pathToFile, pathToOutput, filename)
        
        srcSize = model.getDirSize(model.getPathToSrcFie(''))
        outSize = model.getDirSize(model.getPathToOutputDirectory(directory)) 

        print(f"{Fore.GREEN}Directory{Style.RESET_ALL} " + directory + f"{Fore.GREEN} compressed!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Original size:{Style.RESET_ALL} " + srcSize)
        print(f"{Fore.YELLOW}Compressed size:{Style.RESET_ALL} " + outSize)

        os.chdir('..')
    
    print('Done!')

run()
