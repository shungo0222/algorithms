# Chaining
# O(1)

import hashlib

class Bucket(object):
    def __init__(self, key, value, bucket = None):
        self.key = key
        self.value= value
        self.next = bucket

class HashTable(object):
    def __init__(self, size):
        self.size = 0
        self.hash_size = size
        self.hash_table = [None] * size
        
    def _hash_func(self, key):
        hash_string = hashlib.sha256(str(key).encode(encoding='utf-8')).hexdigest()
        sum_ = 0
        for i in hash_string:
            sum_ += ord(i)
        return sum_ % self.hash_size
    
    def search(self, key):
        index = self._hash_func(key)
        bucket = self.hash_table[index]
        while bucket:
            if bucket.key == key:
                return (True, bucket)
            else:
                bucket = bucket.next
        return (False, index)
        
    def insert(self, key, value):
        exist, x = self.search(key)
        if exist:
            x.value = value
        else:
            bucket = Bucket(key, value, self.hash_table[x])
            self.hash_table[x] = bucket
            self.size += 1
            
    def delete(self, key):
        index = self._hash_func(key)
        bucket = self.hash_table[index]
        value = None
        flag = False
        if bucket:
            if bucket.key == key:
                value = bucket.value
                self.hash_table[index] = bucket.next
                self.size -= 1
                flag = True
            else:
                while bucket.next:
                    if bucket.next.key == key:
                        value = bucket.next.value
                        bucket.next = bucket.next.next
                        self.size -= 1
                        flag = True
                        break
                    else:
                        bucket = bucket.next
            if flag:
                print('The bucket with (key: {}, value: {}) has been deleted'.format(key, value))
            else:
                print('There is no bucket with {} key'.format(key))
        else:
            print('There is no bucket with {} key'.format(key))
            
    def display(self):
        print('-' * 30)
        for index, bucket in enumerate(self.hash_table):
            if bucket:
                print(index, end=' ')
                while bucket:
                    if bucket.next is None:
                        print(bucket.value)
                    else:
                        print(bucket.value, end=' -> ')
                    bucket = bucket.next
            else:
                print(index, bucket)
        print('-' * 30)
    
    
    
if __name__ == '__main__':
    hash_table = HashTable(10)
    
    people = [(50, 'Noah'), (82, 'James'), (53, 'Emma'), (492, 'Sophia'), (435, 'Harper'), \
                (16, 'Ethan'), (98, 'Olivia'), (828, 'Logan'), (384, 'Lucas'), (1, 'Mateo'), \
                (23, 'Liam'), (587, 'Ava'), (18, 'Mia')] 
    
    for i in people:
        hash_table.insert(*i)
        
    print(hash_table.search(98)[1].value)
    print(hash_table.search(100))
    hash_table.delete(82)
    hash_table.delete(3)
    
    hash_table.display()
    print('size: {}'.format(hash_table.size))