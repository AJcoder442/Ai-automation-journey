import os

for root, dirs, files in os.walk("."): #E:\AI_Automation 
    print(" root :",root)
    print(" dirs:",dirs)
    print("files :",files)
    # for file in files:
    #     print(os.path.join(root, file))
