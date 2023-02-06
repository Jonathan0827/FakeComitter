import os
print('''
  _____     _         ____                          _ _   _
 |  ___|_ _| | _____ / ___|___  _ __ ___  _ __ ___ (_) |_| |_ ___ _ __
 | |_ / _` | |/ / _ \ |   / _ \| '_ ` _ \| '_ ` _ \| | __| __/ _ \ '__|
 |  _| (_| |   <  __/ |__| (_) | | | | | | | | | | | | |_| ||  __/ |
 |_|  \__,_|_|\_\___|\____\___/|_| |_| |_|_| |_| |_|_|\__|\__\___|_|
                            By Jonathan0827
                                                                       ''')
times = input("Input: ")
num = 0
fakePath = os.path.dirname(os.path.realpath(__file__))
os.chdir(fakePath)

while num < int(times):
    os.system('git commit --allow-empty -m "fake commit"')
    num += 1

os.system('git push')
