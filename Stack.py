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


# Implementing Stack class
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
                        print('There is no element to delete')
                        return None   
                # if tail exist
                value = self.tail.node   
                if(self.tail == self.head):
                        self.tail = None
                        self.head = None
                        return value
                self.tail = self.tail.prev 
                if(self.tail is None):
                        return value
                self.tail.next = None
                return value

        # returns but does not remove item at top of stack
        def peek(self):
            if self.tail is None:
                print('There is no element in the Stack')
                return None
            else:
                return self.tail.node

        # returns true if stack has no items
        def isEmpty(self):
                if(self.head is None and self.tail is None):
                    return True
                else:
                    return False

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
                if count == 0:
                    print('<Empty Stack>')

def main():
# our test code
        print('=============== Stack Implementation ===============')
        print('Operation: Creating Stack')
        stk = Stack()
        print('Current Stack:')
        stk.Output()
        print('=================================================================')
        print('Operation: push({})'.format(str(0)))
        print('Operation: push({})'.format(str(1)))
        print('Operation: push({})'.format(str(2)))
        print('Operation: push({})'.format(str(3)))
        stk.push(0)
        stk.push(1)
        stk.push(2)
        stk.push(3)
        print('Current Stack:')
        stk.Output()
        print('=================================================================')
        print('Operation: getLength()')
        x = stk.getLength()
        print('Length of current Stack: {}'.format(str(x)))
        print('=================================================================')
        print('Operation: pop()')
        stk.pop()
        print('Current Stack:')
        stk.Output()
        print('=================================================================')
        print('Operation: peek()')
        x = stk.peek()
        print('Item at the top of stack: {}'.format(str(x)))
        print('=================================================================')
        print('Operation: isEmpty()')
        val = stk.isEmpty()
        if val:
            print('Stack is empty')
        else:
            print('Stack is not empty')
        print('')
        print('Current Stack:')
        stk.Output()
        print('=================================================================')
        print('Operation: pop()')
        stk.pop()
        print('Current Stack:')
        stk.Output()
        print('=================================================================')
        print('Operation: pop()')
        stk.pop()
        print('Current Stack:')
        stk.Output()
        print('=================================================================')
        print('Operation: pop()')
        stk.pop()
        print('Current Stack:')
        stk.Output()
        print('=================================================================')
        print('Operation: isEmpty()')
        val = stk.isEmpty()
        if val:
            print('Stack is empty')
        else:
            print('Stack is not empty')
        print('')
        print('Current Stack:')
        stk.Output()
        print('=================================================================')
        print('Program Finished')
        


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