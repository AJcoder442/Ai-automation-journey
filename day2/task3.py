with open("log.txt","w") as f:
    f.write(" hi i am learning ai automation")


with open ("log.txt","r") as f:
    print(" read file :",f.read()) 
 # "w"-> overwrite 
 # "r"-> only read

with open("task12.txt","a") as file:

    file.write(" hello what about today what are doing you\n")

with open ("task12.txt","r") as f:
    print(f.read())