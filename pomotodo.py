import time
import math
import csv


def gen_basic_report():
    report = {}

    f = open('data.csv')
    r = csv.reader(f)
    header = next(r)

    if header is not None:
        for row in r:
            report[row[2]] = report.get(row[2], 0) + int(row[1])
    else:
        print("No data")

    spacing = 8
    print("\n")
    for category in report:
        bar = '■' * math.floor(report[category]/25)
        spaces_l = spacing - len(category)
        spaces_r = spacing - len(bar)
        print(f"{spaces_l * ' '}{category}: {bar} {spaces_r * ' '}{len(bar) * 25} mins")
    print("\n")


def save_pomo(duration_min):
    now = time.localtime()
    fieldnames = ["date", "duration", "task"]
    task = input("In a few words, what did you work on? ")
    with open('data.csv', 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)

        if f.tell() == 0:  # write header only if blank file
            w.writeheader()

        w.writerow({"date": f"{now.tm_mon}/{now.tm_mday}/{now.tm_year}",
                    "duration": duration_min,
                    "task": f"{task}"})


def run_pomo(duration_min):
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
        time.sleep(.01)
    print("DONE!")
    save_pomo(duration_min)


def main_menu():
    print('''
                             ___     _       
                            |__ \   | |      
  _ __   ___  _ __ ___   ___   ) |__| | ___  
 | '_ \ / _ \| '_ ` _ \ / _ \ / // _` |/ _ \ 
 | |_) | (_) | | | | | | (_) / /| (_| | (_) |
 | .__/ \___/|_| |_| |_|\___/____\__,_|\___/ 
 | |                                         
 |_|                                         
    ''')
    while True:
        menu = {
            "1": "25-min pomo",
            "2": "15-min pomo",
            "3": "basic report"
        }

        print("---------------")
        for item in menu:
            print(f"{item}. {menu[item]}")
        print("---------------")

        answer = input("What would you like to do? ")

        if answer == "1":
            run_pomo(25)

        if answer == "3":
            gen_basic_report()


main_menu()
