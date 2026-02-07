import os

summary ={}

for file in os.listdir():
    if "." in file :
        ext=file.split(".")[-1]
        summary[ext]=summary.get(ext,0)+1


with open("summary.txt","w") as f:
    for k ,v in summary.items():
        f.write(f" {k}:{v}\n")


print(" sumary save summary.txt file\n")
print(" detail of summary txt is :\n")


with open("summary.txt","r") as f:
    print(f.read())