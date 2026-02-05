print("AI Automation Day 1 Started 🚀")

import os

print(" current directory/folder",os.getcwd())
print("Files in current folder")
print(os.listdir())

for file in os.listdir():
    print("found:",file)


