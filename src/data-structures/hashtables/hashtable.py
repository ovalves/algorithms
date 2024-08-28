class Hashtable:
    def __init__(self, bucket_size=32):
        self.bucket_size = bucket_size
        self.hashmap =  [[]] * self.bucket_size

    def __hash(self, key: str) -> int:
        index = 0
        for index, key_at in enumerate(key):
            index = (index + ord(key_at) * index) % self.bucket_size
        return index

    def set(self, key: str, value: any) -> None:
        index = self.__hash(key)
        if not self.hashmap[index]:
            self.hashmap[index] = [[key, value]]
            return None

        self.hashmap[index].append([key, value])
        return None

    def get(self, key: str) -> any:
        index = self.__hash(key)

        if not self.hashmap[index]:
            return None

        for i in self.hashmap[index]:
            if i[0] == key:
                return i[1]

    def keys(self) -> list:
        return self.__get_hash_table_key_or_value(key_or_value=0) # 0 => key

    def values(self) -> list:
        return self.__get_hash_table_key_or_value(key_or_value=1) # 1 => value

    def __get_hash_table_key_or_value(self, key_or_value):
        keys = []
        for index in range(self.bucket_size):
            if not self.hashmap[index]:
                continue
            if len(self.hashmap[index]) > 1:
                keys.extend(
                    self.hashmap[index][j][key_or_value]
                    for j in range(len(self.hashmap[index]))
                )
                continue
            keys.append(self.hashmap[index][0][key_or_value])
        return keys

    def __str__(self) -> str:
        return str(self.hashmap)


ht = Hashtable(16)
print(ht)
# [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

ht.set('item 1', 100)
ht.set('item 2', 99)
ht.set('item 3', 55)
print(ht)
# [[], [], [], [], [['item 3', 55]], [], [], [], [], [], [['item 1', 100]], [], [], [], [], [['item 2', 99]]]

print(ht.get('item 1'))
# 100

print(ht.keys())
# ['item 3', 'item 1', 'item 2']

print(ht.values())
# [55, 100, 99]