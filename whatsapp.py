import pandas as pd
import pyautogui as pt
import webbrowser as web
from datetime import datetime
import time


def main():
    print(
        "To use this script properly, you must login to whatsapp web in your default web browser\n"
        + "And you shouldn´t do anythings, once the script started sending messages.\n"
        + "Bot will start sending once the current hour and current minute are equal to starting hour and starting minute.\n"
        + "So if the hour/min input is already passed, bot will send the messages next day.\n"
        + "Also the estimated time for whatsapp web to open cannot be lesser than the actual time it takes to open it.\n"
        + "If it is lesser, bot will not be able to send the messages, but will print that it sended.\n"
        + "Faster your internet connection and computer is, smaller this value must be.",
        end="\n\n",
    )

    SECS_TAKES_TO_OPEN_WHATSAPP_WEB = int(
        input("Estimated time (in seconds) for whatsapp web to open in the computer: ")
    )

    START_HOUR = int(input("Starting hour (in 24 hours format): "))
    START_MIN = int(input("Starting minute: "))

    MESSAGE_INPUT = str(input("What is the message: "))

    df = pd.read_csv("phone_book.csv", dtype=str)
    # print(df)

    while True:
        current_time = datetime.now().strftime("%H:%M").split(":")
        current_hour, current_min = int(current_time[0]), int(current_time[1])
        if current_hour == START_HOUR and current_min == START_MIN:
            print("Starting to send messages")
            for index, row in df.iterrows():
                number = "+" + row[0]
                name = row[1]
                message = f"Hello the person called {name}, {MESSAGE_INPUT}"
                web.open(
                    "https://web.whatsapp.com/send?phone=" + number + "&text=" + message
                )
                time.sleep(SECS_TAKES_TO_OPEN_WHATSAPP_WEB)
                # sending the message
                pt.press("enter")
                print(f"Phone Number: {number}\nMessage: {message}")
                # closing the tab
                pt.hotkey("ctrl", "w")
                pt.press("enter")
                time.sleep(1)
            print("Finished")
            break
        else:
            left_hour, left_min = calculate_hours_mins_left(
                START_HOUR, START_MIN, current_hour, current_min
            )
            print(f"Hours: {left_hour} Mins: {left_min} left")
            time.sleep(60)


def calculate_hours_mins_left(start_hour, start_min, current_hour, current_min):
    day = (
        "02"
        if (start_hour == current_hour and start_min < current_min)
        or start_hour < current_hour
        else "01"
    )
    fmt = "%Y-%m-%d %H:%M:%S"
    d1 = datetime.strptime(f"2042-01-01 {current_hour}:{current_min}:42", fmt)
    d2 = datetime.strptime(f"2042-01-{day} {start_hour}:{start_min}:50", fmt)

    diff = d2 - d1
    diff_minutes = round((diff.days * 24 * 60) + (diff.seconds / 60))
    left_hour, left_min = divmod(diff_minutes, 60)

    return left_hour, left_min


if __name__ == "__main__":
    main()
