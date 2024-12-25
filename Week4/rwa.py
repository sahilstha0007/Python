# Read, write and append
with open("py.txr","r") as f:
    f.read()
with open("py.txt","w") as f:
    f.write("Helloe World!!")
with open("py.txt","a") as f:
    f.write("new text")