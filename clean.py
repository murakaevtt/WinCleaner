import os, shutil, getpass

def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Error while removing {file_path}. {e}')

def clean_files():
    username = str(getpass.getuser())

    delete_files_in_folder(f"C:/Users/{username}/AppData/Local/Temp")
    delete_files_in_folder("C:/Windows/Temp")
    delete_files_in_folder("C:/Windows/SoftwareDistribution")
    delete_files_in_folder("C:/Windows/Prefetch")

    os.system('WSReset.exe')
    os.system('ipconfig /flushdns')
    os.system('Dism.exe /online /cleanup-image /AnalyzeComponentStore')
    os.system('Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase')