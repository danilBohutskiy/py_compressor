from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

class ColoramaHelper:
    def __init__(self) -> None:
        colorama_init()
        pass

    def print_current_dir(self, directory):
        print(f"{Fore.YELLOW}Current directory:{Style.RESET_ALL} " + directory)
    
    def print_current_file(self, filename):
        print('Current file: ' + filename)

    def print_comparison_directories_size(self, directory, size_original, size_compressed):
        print(f"{Fore.GREEN}Directory{Style.RESET_ALL} " + directory + f"{Fore.GREEN} compressed!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Original size:{Style.RESET_ALL} " + size_original)
        print(f"{Fore.YELLOW}Compressed size:{Style.RESET_ALL} " + size_compressed)