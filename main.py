from pyautogui import *
import pyautogui as pg
import time

# Mining button key bind: M

# intro
print("*" * 20)
print("Please change your keybind of Attack/Destroy to M.")
print("ESC -> Options -> Controls -> Key Binds")
while True:
    continue_response = input("Continue...? (Y/N): ")
    continue_response = continue_response.upper()
    if continue_response == "Y":
        break
    elif continue_response == "N":
        print("Don't worry! Take your time.")
        time.sleep(3)
    else:
        print("Invalid response prompt. Please try again.")
        time.sleep(3)

# type
print("*" * 20)
print("What type of pickaxes are you going to use this time?")
while True:
    pickaxe_type = input("(Wooden, Stone, Iron, Golden, Diamond, Netherite): ")
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
        print("Invalid pickaxe type. Please try again.")
        time.sleep(3)

# slots
print("*" * 20)
print("How many slots do you have for pickaxes?")
while True:
    slots = int(input("Enter a number between 0 and 9: "))
    if slots == 0:
        print("I think you should go craft pickaxe.")
        break
    elif 0 < slots <= 9:
        pickaxe_slots = slots
        break
    else:
        print("Invalid number of slots. Please try again.")


# auto func
def mine_for_seconds(secs):
    pg.keyDown("M")
    sleep(secs)
    pg.keyUp("M")


# summarize
print("*" * 20)
print(f"Pickaxe Type : {pickaxe_type}\nSlots : {pickaxe_slots}")
print("After confirming the bot, Please enter the minecraft immediately")
while True:
    ready_response = input("Ready?...? (Y/N): ")
    if ready_response == "Y":
        print("The bot starting in 3...")
        time.sleep(1)
        print("The bot starting in 2...")
        time.sleep(1)
        print("The bot starting in 1...")
        time.sleep(1)
        print("The bot starting now!")
        mine_for_seconds(seconds)
        break
    elif ready_response == "N":
        print("Don't worry! Take your time.")
        time.sleep(3)
    else:
        print("Invalid response prompt. Please try again.")
        time.sleep(3)


"""sleep(3)
mine_for_seconds(197)  # around 3:17 (1 block)"""
