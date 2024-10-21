import random
from winsound import Beep as beep
from time import sleep
from os import system as cmd
import os

note_duration = 250
note_time = note_duration / 1000



def clear():
    cmd("CLS")

def b(f):
    if f == "--":
        sleep(note_time)
    else:
        beep(notes[f], note_duration)

def settings():
    global s
    global note_duration
    global note_time
    clear()
    print("Settings :\n")

    ch = input("[S] Save project\n[L] Load Project\n[C] Change note duration\n[R] Generate random melody\n[Q] Quit Retro Loops Studio\n\n> ")

    if ch.lower() == "s":
        global s
        path = input('Name of the project : ') + ".rlsp"
        f = open(path, "w+")
        input("SJR")
        f.write(s["01"] + "\n")
        f.write(s["02"] + "\n")
        f.write(s["03"] + "\n")
        f.write(s["04"] + "\n")

        f.write(s["05"] + "\n")
        f.write(s["06"] + "\n")
        f.write(s["07"] + "\n")
        f.write(s["08"] + "\n")

        f.write(s["09"] + "\n")
        f.write(s["10"] + "\n")
        f.write(s["11"] + "\n")
        f.write(s["12"] + "\n")

        f.write(s["13"] + "\n")
        f.write(s["14"] + "\n")
        f.write(s["15"] + "\n")
        f.write(s["16"] + "\n")
        input("Project saved !\nPress enter to continue./")

    elif ch.lower() == "l":
        file = input("Drag'N'Drop the project here : ").replace('"', '')
        f = open(file, "r+").read()
        seq = f.splitlines()

        s["01"] = seq[0]
        s["02"] = seq[1]
        s["03"] = seq[2]
        s["04"] = seq[3]

        s["05"] = seq[4]
        s["06"] = seq[5]
        s["07"] = seq[6]
        s["08"] = seq[7]

        s["09"] = seq[8]
        s["10"] = seq[9]
        s["11"] = seq[10]
        s["12"] = seq[11]

        s["13"] = seq[12]
        s["14"] = seq[13]
        s["15"] = seq[14]
        s["16"] = seq[15]
        
        input("Sucessfuly loaded the project !\nPress enter to continue./")

    elif ch.lower() == "r":
        s["01"] = random.choice(pbnotes)
        s["02"] = random.choice(pbnotes)
        s["03"] = random.choice(pbnotes)
        s["04"] = random.choice(pbnotes)

        s["05"] = random.choice(pbnotes)
        s["06"] = random.choice(pbnotes)
        s["07"] = random.choice(pbnotes)
        s["08"] = random.choice(pbnotes)

        s["09"] = random.choice(pbnotes)
        s["10"] = random.choice(pbnotes)
        s["11"] = random.choice(pbnotes)
        s["12"] = random.choice(pbnotes)

        s["13"] = random.choice(pbnotes)
        s["14"] = random.choice(pbnotes)
        s["15"] = random.choice(pbnotes)
        s["16"] = random.choice(pbnotes)

        input("Successfully generated a random melody !\nPress enter to continue./")

    elif ch.lower() == "c":
        if note_duration == 250:
            print("Note duration : 250ms (default).")
        else:
            print("Note duration :", str(note_duration) + "ms.")
        
        note_duration = int(input("\nNew note duration (in milliseconds): "))
        note_time = note_duration / 1000

    elif ch.lower() == "q":
        quit()

    else:
        pass

notes = {
    "C3" : 131,
    "D3" : 147,
    "E3" : 165,
    "G3" : 196,
    "A3" : 220,

    "C4" : 262,
    "D4" : 294,
    "E4" : 330,
    "G4" : 392,
    "A4" : 440,

    "C5" : 524,
    "D5" : 588,
    "E5" : 660,
    "G5" : 784,
    "A5" : 880
}

s = {
    "01" : "--",
    "02" : "--",
    "03" : "--",
    "04" : "--",
    
    "05" : "--",
    "06" : "--",
    "07" : "--",
    "08" : "--",

    "09" : "--",
    "10" : "--",
    "11" : "--",
    "12" : "--",

    "13" : "--",
    "14" : "--",
    "15" : "--",
    "16" : "--"

}

def new():
    global s
    s = {
        "01" : "--",
        "02" : "--",
        "03" : "--",
        "04" : "--",
        
        "05" : "--",
        "06" : "--",
        "07" : "--",
        "08" : "--",

        "09" : "--",
        "10" : "--",
        "11" : "--",
        "12" : "--",

        "13" : "--",
        "14" : "--",
        "15" : "--",
        "16" : "--"

    }

def playSequence():
    b(s["01"])
    b(s["02"])
    b(s["03"])
    b(s["04"])

    b(s["05"])
    b(s["06"])
    b(s["07"])
    b(s["08"])

    b(s["09"])
    b(s["10"])
    b(s["11"])
    b(s["12"])

    b(s["13"])
    b(s["14"])
    b(s["15"])
    b(s["16"])

    input("Played your B A N G E R.\nPress enter to continue./")

ids = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16"]
pbnotes = ["C3", "D3", "E3", "G3", "A3", "C4", "D4", "E4", "G4", "A4", "C5", "D5", "E5", "G5", "A5", "--"]

def addNote():
    n = input("\nWhich note do you want to change ?\n> ")
    if n in ids:
        pass
    else:
        main()
              
    print("\nPossible notes :")
    print("C3, D3, E3, G3, A3")
    print("C4, D4, E4, G4, A4")
    print("C5, D5, E5, G5, A5")

    wn = input(f"\nWhich note do you wanna put in {n} (put '--' to remove the note) ?\n> ")

    if wn in pbnotes:
        pass
    else:
        main()

    s[n] = wn

def printSequence():
    print("Full sequence:\n")
    print("-------------------------------------------------")
    print("|" + "01 02 03 04|05 06 07 08|09 10 11 12|13 14 15 16|")
    print("|" + s["01"], s["02"], s["03"], s["04"]+ "|" + s["05"], s["06"], s["07"], s["08"]+ "|" + s["09"], s["10"], s["11"], s["12"]+ "|" + s["13"], s["14"], s["15"], s["16"]+"|")
    print("-------------------------------------------------\n")

def h():
    clear()
    print("HELP :\n")
    print("Retro Loops Studio is a tiny music software that allows\nyou to create melodies using the pentatonic scale (CDEGA)\n")
    print("To get started, type the letter 'A' and press Enter to add a note somewhere in the sequence.\nWhen you added notes, type the letter 'P' and press enter to play the banger you just made")
    print("If you want to delete on note, type the letter 'A' and select this note,\nbut instead of writing a normal note, just write '--' and the note will be deleted.")
    print("If you want to delete all the notes,\ntype 'N' (for 'New sequence') and press enter : you will have an empty project")
    print("----------------------------------------------------------")
    print("SETTINGS HELP : ")
    print("There are 5 features in the settings :")
    print("\n\nTo save your project, type the letter 'S' and press enter.\nThen type the name of the project and press enter. That's it : you saved a project\n")
    print("To load a saved project, type the letter 'L' and press enter.\nThen type  the name of he project and press enter. That's it : you just loaded a project\n")
    print("To change the note duration, type the letter 'C' and press enter\nThen type the note duration in milliseconds.\n")
    print("To generate a random melody, type the letter 'R' and then press enter.\nThe whole sequence will be modified and you will have a base for starting a new project.\n")
    print("And finally, to quit, type the letter 'Q' and press enter.")
    print("----------------------------------------------------------")
    input("\nPress enter to quit the help menu./")

def main():
    clear()
    print("⌌                  ⌍")
    print(" RETRO LOOPS STUDIO ")
    print("⌎                  ⌏")
    print("By AnGus Studios\n")
    printSequence()
    ch = input("[A] Add a note\n[P] Play your banger\n[N] New sequence\n[H] Help\n[S] Settings\n\n> ")
    if ch.lower() == "a":
        addNote()
    elif ch.lower() == "p":
        playSequence()
    elif ch.lower() == "h":
        h()
    elif ch.lower() == "s":
        settings()
    elif ch.lower() == "n":
        new()
    else:
        pass

while True:
    main()