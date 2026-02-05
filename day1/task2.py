import os

# for file in os.listdir():
#     if file.endswith(".py"):
#         print(" python file :",file)



# for file in os.listdir():
#     if file.endswith(".txt"):
#         print("docs file",file)


for file in os.listdir():
    if file.startswith("task"):
        print("start with task",file)