import os
#import time
import getpass
import shutil
#import keyboard

VERSION = "alpha 0.0.1"
username = str(getpass.getuser())

answer = ""

def deleteFilesInFolder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Error while removing {file_path}. {e}')

#def deleteEverythingInFolder(folder_path):
#    shutil.rmtree(folder_path)
#    os.mkdir(folder_path)

while answer != "3":
    os.system("cls")
    print("\t\tWinCleaner by MTT\n")
    print("1. Start the cleaning.")
    print("2. Check the version.")
    print("3. Quit.\n")
    
    answer = str(input("Enter the number of action: "))
    
    if answer == "1":
        os.system("cls")

        print("1. AMD Graphics Card.")
        print("2. NVIDIA Graphics Card.")
        graphics_card = int(input("Which grapgics card do you have?: "))

        os.system("cls")

        print("Cleaning the system...")

        deleteFilesInFolder(f"C:\\Users\\{username}\\AppData\\Local\\Temp")
        deleteFilesInFolder("C:\\Windows\\Temp")
        deleteFilesInFolder("C:\\Windows\\SoftwareDistribution")
        deleteFilesInFolder("C:\\Windows\\Prefetch")

        os.system('cls')

        os.system('WSReset.exe')
        os.system('ipconfig /flushdns')
        if graphics_card == 1:
            deleteFilesInFolder(f"C:\\Users\\{username}\\AppData\\Local\\NVIDIA\\GLCache")
            pass
        elif graphics_card == 2:
            pass
        os.system('Dism.exe /online /cleanup-image /AnalyzeComponentStore')
        os.system('Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase')
        os.system('powercfg -h off')
         
    if answer == "2":
        os.system("cls")
        print(f"Version: {VERSION}.\n")
        input("Press enter to continue.")