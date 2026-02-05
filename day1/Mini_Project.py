import os
# Folder file  Analyzer

file_count={}

for file in os.listdir(".."):
    if "." in file :
        ext=file.split(".")[-1]
        file_count[ext]=file_count.get(ext,0)+1


print ("file summary")
for k ,v in file_count.items():

    print(k ,":",v)

