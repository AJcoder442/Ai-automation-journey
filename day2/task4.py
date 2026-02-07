import os

with open("autiomation_log.txt","w") as f:
    for file in os.listdir():
        f.write(" found file : {file} \n")


print(" log genearted")
print(os.listdir())