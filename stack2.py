a = input("Input your charaters:")
b = []
r = ""

for i in a:
    b.append(i)

print(b)

for j in a:
    r += b.pop()
    
print(r)
