class AlgoHashTable:

    def __init__(self, size): # constructor used to create the hash table object
        self.size = size
        self.hash_table = [[] for _ in range(self.size)] # creating many mini lists within one big lists

    def create_buckets(self):
        pass

    def set_val(self, key, value): # insert method
        pass

    def get_val(self,key): # search method
        pass

    
    def __str__(self): # method called when we try to print the hash table 
        return "".join(str(item) for item in self.hash_table) # return a string representation of each minilist 
    
hash_table = AlgoHashTable(256) # creating a new hash table object and passing in the size
print(hash_table)