import ctypes

class MyList:
    def __init__(self):
        self.size = 1 # capacity of array
        self.n = 0 # no. of items or lenght

        #creating a new array as soon an an instance gets created
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __make_array(self,capacity):
        # creating array of size capacity
        return (capacity*ctypes.py_object)()
    
    def append(self, entry):
        #resize if needed
        if self.n == self.size:
            self.__resize(self.size*2)

        #append
        self.A[self.n] = entry
        self.n+=1

    def __resize(self,capacity):
        new_A = self.__make_array(capacity)

        for i in range(self.n):
            new_A[i] = self.A[i]

        self.size*=2
        self.A = new_A

    # adding print method 
    def __str__(self):
        res = ""
        for i in range(self.n):
            res += str(self.A[i]) + ","
        return "[" + res[:-1] + "]"
    
    # search by index in list
    def __getitem__(self,index):
        if (0 <= index <= self.n):
            return  self.A[index]
        else:
            return "index not found!"
        
    # pop method
    def pop(self):
        if(self.n == 0):
            print("Empty list")
        else:
            print(f"Deleted {self.A[self.n-1]}")
            self.n -= 1

    # clear method
    def clear(self):
        self.n = 0
        self.size = 1

    # find by value
    def index(self, value):
        for i in range(self.n):
            if (self.A[i] == value):
                return i
        return f"{value} not in list"
        
    def insert(self,index,value):
        #resize if needed
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,index,-1):
            self.A[i] = self.A[i-1]

        self.A[index] = value
        self.n+=1
        
    # delete item
    def __delitem__(self,index):
        if (0<=index<self.n):
            for i in range(index,self.n-1):
                self.A[i] = self.A[i+1]

            if(self.n != 0):
                self.n-=1  
        else:
            print("Index not found")
        
    # remove first occurence by value
    def remove(self,val):
        index = self.index(val)
        if type(index) == int:
            self.__delitem__(index)
        else:
            print(index)

    # finding minimum value
    def __min__(self):
        min = self.A[0]
        for i in range(self.n):
            if self.A[i] < min:
                min = self.A[i]
        return min
    
    # finding maximum value
    def __max__(self):
        max = self.A[0]
        for i in range(self.n):
            if self.A[i] > max:
                max = self.A[i]
        return max
    
    # extend method
    def extend(self,listB):
        for i in range(listB.n):
            self.append(listB[i])
        return self
    
        
# ================================================================================

L1 = MyList()
L2 = MyList()

L1.append(10)
L1.append(20)
L1.append(30)
L1.insert(1,40)
print(L1)
print(min(L1))
print(max(L1))
print(sum(L1))

L2.append(100)
L2.append(200)
L2.append(300)
L2.insert(1,400)
print(L2)

L1.extend(L2)
print(L1)
