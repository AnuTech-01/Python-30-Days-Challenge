#CHALLENAGE 17

#Python Iterator

# Creating a simple iterator using a class
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

# Create an instance of MyIterator
my_iter = MyIterator(1, 5)

# Use the iterator
for num in my_iter:
    print(num)
