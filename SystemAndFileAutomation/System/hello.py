import psutil
import time

print(psutil.cpu_percent())
print(psutil.virtual_memory().percent())