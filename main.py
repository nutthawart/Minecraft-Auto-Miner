from pyautogui import *
import pyautogui as pg
import time

# intro
print("*" * 60)
print("[💡] ESC -> Options -> Controls -> Key Binds")
while True:
    key_bind = input("[🙋] Please enter your preferred keybind for Attack/Destroy : ")
    if len(key_bind) == 1: #accept 1 len key to be hold
        break
    else:
        print("[❌] Invalid keybind. Please try again.")
        time.sleep(3)

# type
print("*" * 60)
print("[🙋] What type of pickaxes are you going to use this time?")
while True:
    pickaxe_type = input("[💡] (Wooden, Stone, Iron, Golden, Diamond, Netherite): ")
    pickaxe_type = pickaxe_type.upper()
    if pickaxe_type == "WOODEN":
        seconds = 200
        break
    elif pickaxe_type == "STONE":
        seconds = 198
        break
    elif pickaxe_type == "IRON":
        seconds = 4
        break
    elif pickaxe_type == "GOLDEN":
        seconds = 3
        break
    elif pickaxe_type == "DIAMOND":
        seconds = 2
        break
    elif pickaxe_type == "NETHERITE":
        seconds = 1
        break
    else:
        print("[❌] Invalid pickaxe type. Please try again.")
        time.sleep(3)

# slots
print("*" * 60)
print("[💡] How many slots do you have for pickaxes?")
while True:
    slots = int(input("[🙋] Enter a number between 0 and 9: "))
    if slots == 0:
        print("[❌] I think you should go craft pickaxe.")
        break
    elif 0 < slots <= 9:
        pickaxe_slots = slots
        break
    else:
        print("[❌] Invalid number of slots. Please try again.")
        time.sleep(3)


# auto func
def mine_for_seconds(secs, keybind):
    pg.keyDown(keybind)
    sleep(secs)
    pg.keyUp(keybind)

def mine_prompt(secs, keybind):
    for i in range(1, pickaxe_slots+1):
        pg.press(str(i)) #press 1-9 buttons
        mine_for_seconds(secs, keybind)
        print(f"[✅] {i} pickaxe has been used.")


# summarize
print("*" * 60)
print(f"[🔑] Keybind : {key_bind}\n[⛏️]Pickaxe Type : {pickaxe_type}\n[🎒]Slots : {pickaxe_slots}")
print("[⚠️] After confirming the bot, Please enter the game immediately")
while True:
    ready_response = input("Ready?...? (Y/N): ")
    if ready_response == "Y":
        print("[⏱️] The bot starting in 3...")
        time.sleep(1)
        print("[⏱️] The bot starting in 2...")
        time.sleep(1)
        print("[⏱️] The bot starting in 1...")
        time.sleep(1)
        print("[🎉] The bot starting now!")
        mine_prompt(seconds, key_bind)
        break
    elif ready_response == "N":
        print("[o] Don't worry! Take your time.")
        time.sleep(3)
    else:
        print("[-] Invalid response prompt. Please try again.")
        time.sleep(3)