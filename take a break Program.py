import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on" + time.ctime())
while(break_count < total_breaks):
    time.sleep(60*60*1.5)
    webbrowser.open("https://www.youtube.com/watch?v=0p3tWJbMTeQ")
    break_count = break_count + 1
