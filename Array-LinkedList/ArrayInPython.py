# Array - Read
Arr = ['x','y','z']
print(Arr) #o/p: [x,y,z]

# Array - Insert
Arr.append('A')
print(Arr) #o/p: [x,y,z,A]

#Array - Delete
Arr.pop(2)
print(Arr) #o/p: [x,y,A]

print(Arr[2:]) # [A]

Arr[1] = "B"
print(Arr) # [x,B,A]