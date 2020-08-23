class HashFunction:
    def __init__(self):
        self.bucket = []
        
    def update(self, key):
        found = False
        for i, k in enumerate(self.bucket):
            if key == k:
                self.bucket[i] = key
                found = True
                break
        if not found:
            self.bucket.append(key)
            
    def get(self, key):
        for k in enumerate(self.bucket):
            return True
        return False
    
    def remove(self, key):
        for i, k in enumerate(self.bucket):
            if key == k:
                del self.bucket[i]


class MyHashSet:

    def __init__(self):
        self.key_space = 2096
        self.hash_table = [HashFunction() for i in range(self.key_space)]
        
    def add(self, key: int) -> None:
        hash_key = key % self.key_space
        print(self.hash_table[hash_key].update(key))

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        print(self.hash_table[hash_key].remove(key))

    def contains(self, key: int) -> bool:
        hash_key = key % self.key_space
        print(self.hash_table[hash_key].get(key))


# Your MyHashSet object will be instantiated and called as such:
# OBJ = MYHASHSET()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

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