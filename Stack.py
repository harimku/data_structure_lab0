import random

# node definition
class Node:
        def __init__(self):
                self.data = None
                self.previous = None
                self.next = None

        def get(self):
                return self.data
        def getPrev(self):
                return self.previous
        def getNext(self):
                return self.next
        def setPrev(self,previous):
                self.previous = previous
        def setNext(self, new_next):
                self.next = new_next
        def set(self,data):
                self.data = data
        node = property(get,set)
        prev = property(getPrev,setPrev)
        next = property(getNext, setNext)


# Implement Stack
class Stack:
        def __init__(self):
                self.head = None
                self.tail = None

    # Stack Operations

        # inserts x on top of stack 
        def push(self, data):
                pdata = Node()
                pdata.node = data
                if (self.tail == None):
                        self.tail = pdata
                        if (self.head is None):
                                self.head = pdata
                        elif(self.head is not None):
                                self.head.next = self.tail
                                self.tail.prev = self.head
                else:
                        # tail exists
                        if (self.head is not None):
                                self.tail.next = pdata
                        pdata.prev = self.tail
                        self.tail = pdata

        # returns and removes item at top of stack
        def pop(self): 
                if (self.tail == None):
                        raise ValueError('There is no element to delete')
                        return None   
                value = self.tail.node   
                self.tail = self.tail.prev 
                self.tail.next = None
                return value

        # returns but does not remove item at top of stack
        def peek(self):
            if self.tail is None:
                print('There is no element in the list')
                return None
            else:
                return self.tail.node

        # returns true if stack has no items
        def isEmpty(self):
                while (self.tail):
                        return False
                return True

        # returns the number of items in the stack
        def getLength(self):
                temp = self.tail
                count = 0
                while (temp): 
                        count += 1
                        temp = temp.prev
                return count 
        
        # prints stack from tail(top) of stack
        def Output(self):
                rover = self.tail
                count = 0

                while (rover != None):
                        if rover.next is None:
                                next_out = 'NULL'
                        else:
                                next_out = str(rover.next.node)
                        if rover.prev is None:
                                prev_out = 'NULL'
                        else:
                                prev_out = str(rover.prev.node)
                        
                        print('Node {} : data={}, prev={}, next={}'.format(str(count), str(rover.node), prev_out, next_out))
                        count += 1
                        rover = rover.prev

def main():
    # provided test code
        count = 10
        list = Stack()
        for x in range( count ):
                rnumber = random.randint(1,100)
                list.push( rnumber )
        print()
        list.Output()
        

    # our test code
        '''
        stk = Stack()
        stk.push(0)
        stk.push(1)
        stk.push(2)
        stk.push(3)
        stk.push(4)
        stk.pop()
        stk.peek()
        x = stk.isEmpty()
        y = stk.getLength()

        ## stk test
        runner = stk.tail
        count = 0
        while(runner):
                if runner.next is None:
                        next_out = "NULL"
                else:
                        next_out = str(runner.next.node)

                if runner.prev is None:
                        prev_out = 'NULL'
                else:
                        prev_out = str(runner.prev.node)

                print('Node {} : data={}, prev={}, next={}'.format(str(count), str(runner.node), prev_out, next_out))
                count += 1
                runner = runner.prev

        print('Is this stack empty? {} '.format(x))
        print('Stack length is: {} '.format(str(y)))

        exit()
        
        runner = stk.head
        count = 0
        while(runner):
                if runner.next is None:
                        next_out = "NULL"
                else:
                        next_out = str(runner.next.node)

                if runner.prev is None:
                        prev_out = 'NULL'
                else:
                        prev_out = str(runner.prev.node)

                print('Node {} : data={}, prev={}, next={}'.format(str(count), str(runner.node), prev_out, next_out))
                count += 1
                runner = runner.next
        '''

if __name__ == '__main__':
        main()