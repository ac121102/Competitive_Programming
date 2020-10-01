file=open("file.txt")
print(file.read())
with open("file.txt",mode='a') as f:
    print(f.write("\nIt's hard."))
with open("file.txt",mode='r') as g:
    print(g.read())