import requests
url = "https://jsonplaceholder.typicode.com/users"
respone = requests.get(url)


print(" stuts code\n",respone.status_code)

data= respone.json()
count=0
with open("file.txt","w") as f:
     for n in data:
         f.write(f"{n['name']}| {n['email']}")
 # count=count+1
print(" data saved in file.txt:\n")
       
#print(respone.json())
with open("file.txt","r") as f:
    print(" data\n",f.read())
# with open("file.txt","r") as f:
#      fi=f.read()
#      for i in fi:
#          print(i)
print("total name:",count)