class MyHashMap:

    def __init__(self):
        self.bucket = [None for _ in range(1000000)]

    def _hashFunction(self, key):
        return key % 1000000
        
    def put(self, key: int, value: int) -> None:
        newKey = self._hashFunction(key)
        self.bucket[newKey] = value
        print(self.bucket[newKey])

    def get(self, key: int) -> int:
        newKey = self._hashFunction(key)
        result = self.bucket[newKey]
        if result is None:
            print(-1)
        else:
            print(result)

    def remove(self, key: int) -> None:
        newKey = self._hashFunction(key)
        self.bucket[newKey] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

print("Hash Map Functon Initialization")
hashMap = MyHashMap()
print("put 1 and 2 in bucket")
hashMap.put(1, 1)        
hashMap.put(2, 2)  
print("Get 1 and 3")      
hashMap.get(1)         
hashMap.get(3)                             # if key 3 not found than return -1
print("Put 1 at position 2 in bucket")     
hashMap.put(2, 1)  
print("get 2")       
hashMap.get(2)    
print("Remove 2 into bucket")      
hashMap.remove(2)        
print("Get 2 after deletion")
hashMap.get(2)