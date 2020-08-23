class MyHashSet:
    def HashFunction(self, key):
        return key % 1000000

    def __init__(self):
        self.arr = [None for _ in range(1000000)]
        

    def add(self, key: int) -> None:
        result = self.HashFunction(key)
        self.arr[result] = key
        print(self.arr[result])
        

    def remove(self, key: int) -> None:
        result = self.HashFunction(key)
        self.arr[result] = None
        print(self.arr[result])
        
    def contains(self, key: int) -> bool:
        result = self.HashFunction(key)
        print(self.arr[result] != None)

 
print("Intialize Hash Function")
hashSet = MyHashSet()
print("Insert 1 and 2 in Hash Table")
hashSet.add(1);         
hashSet.add(2);   
print("Search 1 and 3")      
hashSet.contains(1);    
hashSet.contains(3);  
print("Insert 2")   
hashSet.add(2);     
print("Search 2")      
hashSet.contains(2);  
print("Remove 2 into Hash Table") 
hashSet.remove(2);    
print("Search 2 after Remove 2")      
hashSet.contains(2);