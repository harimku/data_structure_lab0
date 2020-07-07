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



# Implement Queue
class Queue:
        def __init__(self):
                self.head = None
                self.tail = None

    # Queue Operations

        # inserts x at end of the queue
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

        # returns and removes item at front of queue
        def pop(self): 
                if (self.head == None):
                        raise ValueError('There is no element to delete')
                        return None   
                value = self.head.node   
                self.head = self.head.next
                self.head.prev = None
                return value

        # returns but does not remove item at the front
        def peek(self):
            if self.head is None:
                print('There is no element in the list')
                return None
            else:
                return self.head.node

        # Returns true if queue has no items
        def isEmpty(self):
                while (self.tail):
                        return False
                return True

        # returns the number of items in the queue
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
        list = Queue()
        for x in range( count ):
                rnumber = random.randint(1,100)
                list.push( rnumber )
        print()
        list.Output()
        
    # our test code
        '''
        que = Queue()
        que.push(0)
        que.push(1)
        que.push(2)
        que.push(3)
        que.push(4)
        que.pop()
        que.peek()
        x = que.isEmpty()
        y = que.getLength()
        
        ## que test
        runner = que.tail
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

        print('Is this Queue empty? {} '.format(x))
        print('Queue length is: {} '.format(str(y)))

        exit()
        
        runner = que.head
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