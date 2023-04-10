class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def head(self) -> any:
        return self.data[0]

    def tail(self) -> any:
        return self.data[self.length - 1]

    def get(self, index) -> any:
        return self.data[index]

    def push(self, item: int) -> int:
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self) -> any:
        item = self.data[self.length - 1]
        return self.__remove_tail_item(item)

    def remove(self, index) -> any:
        item = self.data[index]

        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        return self.__remove_tail_item(item)

    def __remove_tail_item(self, item):
        del self.data[self.length - 1]
        self.length -= 1
        return item

    def __str__(self) -> str:
        return str(list(self.data.values()))


array = Array()
array.push('olá')
array.push('mundo')
array.push('REMOVE THIS')
array.push('?')
array.pop()
array.push('!!!')

print(f'head: {array.head()}') # head: olá
print(f'tail: {array.tail()}') # tail: !!!
print(f'get: {array.get(1)}') # get: mundo
print(f'remove: {array.remove(2)}') # remove: REMOVE THIS
print(array) # ['olá', 'mundo', '!!!']