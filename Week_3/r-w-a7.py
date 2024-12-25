with open("suman.txt","r") as f:
    f.read()

with open("suman.txt","w") as f:
    f.write("Hello World!!!")

with open("suman.txt","a") as f:
    f.write("new text")