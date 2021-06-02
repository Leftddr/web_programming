import time
import webbrowser

new = 2
url = "https://www.youtube.com/watch?v=Z6qnRS36EgE"
total_breaks = 3
break_count = 0

print ("This program started on" + time.ctime())
while (break_count < total_breaks) :
    time.sleep(10)
    webbrowser.open(url, new=new)
    break_count = break_count + 1
