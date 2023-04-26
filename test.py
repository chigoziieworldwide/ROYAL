import os, sys, platform,time
try:
    import requests
except:
    os.system('pip install requests')
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import test
