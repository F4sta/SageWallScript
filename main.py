import keyboard
import os
import time
import ctypes
os.system("mode 46, 14")

keybind = None

try:
    with open('cfg.cfg', "r", encoding="utf-8") as cfg:
        keybind = cfg.readline()
except:
    os.system("cls")
    print('                                             ')
    print('    _____________________________________    ')
    print('   |                                     |   ')
    print('   |         Valorant Soundboard         |   ')
    print('   |                                     |   ')
    print('   |            After 5 second           |   ')
    print('   |        Press the key that you       |   ')
    print('   |        u want for the keybind       |   ')
    print('   |                                     |   ')
    print('   |                                     |   ')
    print('    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    ')
    print('')
    print('                          Created by Asta    ')
    time.sleep(5)
    while keybind == None:
        try:
            keybind = keyboard.read_key()
        except:
            ctypes.windll.user32.MessageBoxW(0, keybind + " is not bindable!", "BindError", 0)
            time.sleep(5)
            exit()
    with open('cfg.cfg', "w", encoding="utf-8") as cfg:
        cfg.write(keybind)
    os.system('attrib +h cfg.cfg')

os.system("cls")
print('                                            ')
print('    ____________________________________    ')
print('   |          Sage Wall Script          |   ')
print('   |                                    |   ')
print('   |             Important!             |   ')
print('   |  Before using the app you have to  |   ')
print('   | set your fire button 2nd bind to p |   ')
print('   |                                    |   ')
print('   |            Hope u enjoy            |   ')
print('   |                                    |   ')
print('    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    ')
print('    keybind: ' + str(keybind))
print('                         Created by Asta    ')

jump_time = 0.4
script_end = True
def script():
    global script_end
    if script_end:
        script_end = False
        keyboard.press_and_release('space')
        time.sleep(0.2)
        keyboard.press('ctrl')
        time.sleep(0.1)
        keyboard.press_and_release('p')
        time.sleep(0.2)
        keyboard.release('ctrl')
        script_end = True

keyboard.add_hotkey('num_9', lambda: script())

keyboard.add_hotkey('w + num_9', lambda: script())
keyboard.add_hotkey('s + num_9', lambda: script())
keyboard.add_hotkey('a + num_9', lambda: script())
keyboard.add_hotkey('d + num_9', lambda: script())

keyboard.add_hotkey('w + a + num_9', lambda: script())
keyboard.add_hotkey('s + a + num_9', lambda: script())
keyboard.add_hotkey('w + d + num_9', lambda: script())
keyboard.add_hotkey('s + d + num_9', lambda: script())

keyboard.wait()
