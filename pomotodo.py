import time
import math


def run_pomo(duration_min):
    now = time.localtime()
    start_duration = duration_min * 60
    duration_s = start_duration
    time_to_add_block = math.ceil(duration_s / 50)
    blocks = ""
    dashes = "-" * 50
    bar = f"|{blocks}{dashes}|"
    while duration_s > 0:
        if duration_s % time_to_add_block == 0:
            blocks += "■"
            dashes = dashes[:-1]
            bar = f"|{blocks}{dashes}|"
        duration_s -= 1
        m = math.floor(duration_s / 60)
        s = duration_s - (m * 60)
        if s < 10:
            lead_s = "0"
        else:
            lead_s = ""
        pct = 100 * ((start_duration - duration_s) / start_duration)
        print(f'\r{m}:{lead_s}{s} {bar} {round(pct, 1)}% ', end="")
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
        run_pomo(25)


main_menu()
