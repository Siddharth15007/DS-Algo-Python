# simple search
list1 = [20,21,22,23,24,25,33,34,35,44,45,55,56,57,58,59,60,66,67,68,69,70,77,88,99,100,101,102]
Key = 100
# list1 = []
# for i in range(0,10000):
#    list1.append(i)
# in this list simple search algorithm take 9998 steps and Binary Search takes only 13 steps for searching 9999
# #Key = 9999

class SimpleSearch():
    print("<--Simple Serch Algorithm-->")
    count = 0
    for i in range(0, len(list1)):
        if( list1[i] == Key ):
            print("Key found: ", list1[i])
            break
        else:
            print("step ", i)
    # it takes around 24 steps to find "Key"

class BinarySearch():
    print("<--Binary Serch Algorithm-->")

    def BinarySearch(list,item):
        low = 0
        high = len(list1) - 1
        count = 0
        while low <= high:
            mid = (low + high) // 2
            guess = list[mid]
            if guess == item:
                return guess
            elif guess > item:
                high = mid - 1
                count += 1
                print("step ", count)
            else:
                low = mid + 1
                count += 1
                print("step ", count)
        return None
    
    print(BinarySearch(list1,Key))
    # it takes only 4 steps on given list: "list1"