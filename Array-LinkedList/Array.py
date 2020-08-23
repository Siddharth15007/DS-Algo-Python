def InsertElementInBetween(N, Arr, Pos, Ele):
    NewArr = []
    for i in range(0, N-1):
        if i < Pos-1:
            NewArr[i] = Arr[i]
        elif i == Pos-1:
            NewArr[i]=Ele
        else:
            NewArr[i]=Arr[i - 1]
    return NewArr

if __name__ == "__main__":
    # Array - Read
    Arr = ['x','y','z']
    print("Before Perform any operation:")
    print(Arr) #o/p: [x,y,z]
    Arr = InsertElementInBetween(len(Arr), Arr, 2, "YZ")
    print("After Perform any operation:")
    print(Arr) #o/p: 
