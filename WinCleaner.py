import curses, time, os, shutil, getpass
from curses import wrapper

VERSION = "beta 0.1.0"

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

def menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 4, "Win Cleaner by mtt.")
    stdscr.addstr(2, 0, "Pess keys on your keyboard to navigate...")
    stdscr.addstr(4, 0, "1. Start the cleaning.")
    stdscr.addstr(5, 0, "2. Check the version.")
    stdscr.addstr(6, 0, "3. Quit.")
    stdscr.refresh()

def version(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, VERSION)
    stdscr.addstr(2, 0, "Press any key to continue.")
    stdscr.refresh()
    stdscr.getkey()

def start_clean(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Close all the running programs on your pc before the clean starts, because it can intervene the program.", curses.color_pair(3))
    stdscr.addstr(1, 0, "Also close all the windows and apps, that will appear.", curses.color_pair(3))
    stdscr.addstr(3, 0, "Press any key to start the process")
    stdscr.refresh()
    stdscr.getkey()

    stdscr.clear()
    stdscr.refresh()

    clean_files()

    stdscr.clear()
    stdscr.addstr(0, 0, "System was successfully cleaned.", curses.color_pair(1))
    stdscr.addstr(2, 0, "Press any key to go to the menu.")
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while True:
        menu(stdscr)

        key = stdscr.getkey()

        if ord(key) == 51:
            break
        elif ord(key) == 50:
            version(stdscr)
        elif ord(key) == 49:
            start_clean(stdscr)

        time.sleep(0.03)

if __name__ == "__main__":
    wrapper(main)