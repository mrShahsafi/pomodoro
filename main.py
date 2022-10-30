from time import sleep
import sys

suffixes = ["th", "st", "nd", "rd", ] + ["th"] * 16

cycle = int(input("Input your pomodoros cycles, leave it for (4): "))

if cycle is None:
    cycle = 4

for i in range(1,cycle+1):
    suffixed_num = str(i) + suffixes[i % 100]
    print('\r\a')
    input(f"wainting to start the {suffixed_num} pomodoro..\nPlease press any key...[Enter]")
    print(f"Starting the {suffixed_num} pomodoro")
    sleep(1200)
    print(f'\r\a{suffixed_num} pomodoro ended.')

print('Your pomodoro cycle fulfied,Please rest for 15 mins')
