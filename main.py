from pyautogui import *
import pyautogui as pg
import time

PICKAXE_TYPES = {
    "WOODEN": 191,
    "STONE": 198,
    "IRON": 376,
    "GOLDEN": 49
}

# intro
def print_intro():
    print("*" * 60)
    print("[💡] ESC -> Options -> Controls -> Key Binds")

# key
def get_key_bind():
    while True:
        key_bind = input("[🙋] Please enter your preferred keybind for Attack/Destroy : ")
        if len(key_bind) == 1: 
            return key_bind
        else:
            print("[❌] Invalid keybind. Please try again.")
            time.sleep(3)

# type
def get_pickaxe_type():
    print("*" * 60)
    print("[🙋] What type of pickaxes are you going to use this time?")
    while True:
        pickaxe_type = input("[💡] (Wooden, Stone, Iron, Golden, Diamond, Netherite): ").upper()
        if pickaxe_type in PICKAXE_TYPES:
            return pickaxe_type, PICKAXE_TYPES[pickaxe_type]
        else:
            print("[❌] Invalid pickaxe type. Please try again.")
            time.sleep(3)

# slots
def get_slots():
    print("*" * 60)
    print("[💡] How many slots do you have for pickaxes?")
    while True:
        slots = int(input("[🙋] Enter a number between 0 and 9: "))
        if slots == 0:
            print("[❌] I think you should go craft pickaxe.")
            break
        elif 0 < slots <= 9:
            return slots
        else:
            print("[❌] Invalid number of slots. Please try again.")
            time.sleep(3)

# auto func
def mine_for_seconds(secs, keybind):
    pg.keyDown(keybind)
    sleep(secs)
    pg.keyUp(keybind)

def mine_prompt(secs, keybind, pickaxe_slots):
    for i in range(1, pickaxe_slots+1):
        pg.press(str(i))
        print(f"[🔄] {i} has been picked up.")
        mine_for_seconds(secs, keybind)
        print(f"[✅] {i} pickaxe has been used.")

# summarize
def summarize_and_start(key_bind, pickaxe_type, pickaxe_slots, seconds):
    print("*" * 60)
    print(f"[🔑] Keybind : {key_bind}\n[⛏️]Pickaxe Type : {pickaxe_type}\n[🎒]Slots : {pickaxe_slots}")
    print("[⚠️] After confirming the bot, Please enter the game immediately")
    while True:
        ready_response = input("Ready?...? (Y/N): ").upper()
        if ready_response == "Y":
            print("[⏱️] The bot starting in 3...")
            time.sleep(1)
            print("[⏱️] The bot starting in 2...")
            time.sleep(1)
            print("[⏱️] The bot starting in 1...")
            time.sleep(1)
            print("[🎉] The bot starting now!")
            mine_prompt(seconds, key_bind, pickaxe_slots)
            break
        elif ready_response == "N":
            print("[o] Don't worry! Take your time.")
            time.sleep(3)
        else:
            print("[-] Invalid response prompt. Please try again.")
            time.sleep(3)

# main
def main():
    print_intro()
    key_bind = get_key_bind()
    pickaxe_type, seconds = get_pickaxe_type()
    pickaxe_slots = get_slots()
    summarize_and_start(key_bind, pickaxe_type, pickaxe_slots, seconds)

if __name__ == "__main__":
    main()