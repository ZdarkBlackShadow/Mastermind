import time
from time import strftime

today = strftime("%H:%M:%S",time.localtime())
print(today)
print(today[0]+today[1])

#11:09:46
