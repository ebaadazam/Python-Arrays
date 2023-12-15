#DATA STRUCTURE AND ALGORITHM IN PYTHON
#DSA Basics

#Arrays
class Arrays:
    def __init__(self, len):
        self.array_size = len
        self.array_filled = 0
        self.data = []

    def get_array_filled(self):
        return self.array_filled

    def get_array_size(self):
        return self.array_size

    def insert_at_end(self, element):
        if self.array_size > self.array_filled:
            self.data.append(element)
            self.array_filled += 1
        else:
            print('Array is Full')

    def insert_at_begin(self, item):
        self.data.append(None)
        if self.array_size > self.array_filled:
            for i in range(self.array_filled-1, -1, -1):
                self.data[i+1] = self.data[i]
            self.data[i] = item
            self.array_filled += 1
        else:
            print('Array is full')


    def insert_at_position(self, index, item):
        self.data.append(None)
        if self.array_size > self.array_filled:
            for i in range(self.array_filled-1, index-1, -1):
                self.data[i+1] = self.data[i]
            self.data[index] = item
            self.array_filled += 1
        else:
            print('Array size is Full!')

    
    def delete_at_end(self):
        if self.arr_filled > 0:
            del self.arr[self.arr_filled-1]
            self.arr_filled -= 1
        print('element deleted')
        return ''

    
    def delete_at_begin(self):
        if self.arr_filled > 0:
            for i in range(1, self.arr_filled-1):
                self.arr[i-1] = self.arr[i]
            del self.arr[i]
            self.arr_filled -= 1
        return ''


    def delete_at_position(self, index):
        for i in range(index, self.array_filled-1):
            self.data[i] = self.data[i+1]
        del self.data[self.array_filled-1]
        self.array_filled -= 1


    def search_element(self, elem):
        flag = 0
        count = 0 # for finding the index position
        for i in self.data:
            if i == elem:
                flag = 1
                break
            count += 1
        if flag:
            print(elem, 'is present in the Array at the index position', count)
        else:
            print('Oops!', elem, 'is not present in the Array')
        return ''

    def display(self):
        for i in range(self.array_filled):
            print(self.data[i])
        return ''

    def reverse(self):
        for i in range(self.arr_filled-1, -1, -1):
            print(self.arr[i], end=' ')
        return ''


obj = Array(10)
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.insert_at_end(4)
obj.insert_at_end(5)
print(obj.display())

obj.insert_at_begin(10)
print(obj.display())

obj.insert_at_position(1, 20)
print(obj.display())

obj.delete_at_begin()
print(obj.display())

obj.delete_at_end()
print(obj.display())

obj.delete_at_position(3)
print(obj.display())

print(obj.reverse())
