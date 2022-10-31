from time import sleep
import sys

suffixes = ["th", "st", "nd", "rd", ] + ["th"] * 16

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}min / {}min".format(prefix, "#"*x, "."*(size-x), round(j/60,2), int(count/60)), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)


cycle = int(input("Input your pomodoros cycles, leave it for (4): "))

if cycle is None:
    cycle = 4

for i in range(1,cycle+1):
    suffixed_num = str(i) + suffixes[i % 100]
    print('\r\a')
    input(f"wainting to start the {suffixed_num} pomodoro..\nPlease press any key...[Enter]")
    print(f"Starting the {suffixed_num} pomodoro")
    for j in progressbar(range(1200), f"{suffixed_num} Pomodoro: ", 60):
        sleep(1)
    print(f'\r\a{suffixed_num} pomodoro ended.')

print('Your pomodoro cycle fulfied,Please rest for 15 mins')
