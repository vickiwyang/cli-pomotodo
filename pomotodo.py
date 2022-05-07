import time
import math


def run_pomo(duration_min):
    now = time.localtime()
    duration_s = duration_min * 60
    while duration_s > 0:
        duration_s -= 1
        m = math.floor(duration_s / 60)
        s = duration_s - (m * 60)
        if s < 10:
            lead_s = "0"
        else:
            lead_s = ""
        print(f'\r{m}:{lead_s}{s} ', end="")
        time.sleep(1)
    print("\ndone!")


def main_menu():
    menu = {
        "1": "25-min pomo",
        "2": "15-min pomo"
    }

    print("----------")
    for item in menu:
        print(f"{item}. {menu[item]}")
    print("----------")

    answer = input("What would you like to do? ")

    if answer == "1":
        run_pomo(2)


main_menu()
