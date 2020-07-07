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

        # returns and removes item at the front of queue
        def pop(self): 
                if (self.head == None):
                        print('There is no element to delete')
                        return None   
                # if head exists
                value = self.head.node   
                if(self.head == self.tail):
                        self.head = None
                        self.tail = None
                        return value
                self.head = self.head.next 
                if(self.head is None):
                        return value
                self.head.prev = None
                return value

        # returns but does not remove item at the front of queue
        def peek(self):
            if self.head is None:
                print('There is no element in the queue')
                return None
            else:
                return self.head.node

        # returns true if queue has no items
        def isEmpty(self):
                if(self.head is None and self.tail is None):
                    return True
                else:
                    return False

        # returns the number of items in the queue
        def getLength(self):
                temp = self.tail
                count = 0
                while (temp): 
                        count += 1
                        temp = temp.prev
                return count 
        
        # prints queue from tail(top) of queue
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
        print('=============== Queue Implementation ===============')
        print('Operation: Creating Queue')
        que = Queue()
        print('Current Queue:')
        que.Output()
        print('=================================================================')
        print('Operation: push({})'.format(str(0)))
        print('Operation: push({})'.format(str(1)))
        print('Operation: push({})'.format(str(2)))
        print('Operation: push({})'.format(str(3)))
        que.push(0)
        que.push(1)
        que.push(2)
        que.push(3)
        print('Current Queue:')
        que.Output()
        print('=================================================================')
        print('Operation: getLength()')
        x = que.getLength()
        print('Length of current Queue: {}'.format(str(x)))
        print('=================================================================')
        print('Operation: pop()')
        que.pop()
        print('Current Queue:')
        que.Output()
        print('=================================================================')
        print('Operation: peek()')
        x = que.peek()
        print('Item at the front of Queue: {}'.format(str(x)))
        print('=================================================================')
        print('Operation: isEmpty()')
        val = que.isEmpty()
        if val:
            print('Queue is empty')
        else:
            print('Queue is not empty')
        print('')
        print('Current Queue:')
        que.Output()
        print('=================================================================')
        print('Operation: pop()')
        que.pop()
        print('Current Queue:')
        que.Output()
        print('=================================================================')
        print('Operation: pop()')
        que.pop()
        print('Current Queue:')
        que.Output()
        print('=================================================================')
        print('Operation: pop()')
        que.pop()
        print('Current Queue:')
        que.Output()
        print('=================================================================')
        print('Operation: isEmpty()')
        val = que.isEmpty()
        if val:
            print('Queue is empty')
        else:
            print('Queue is not empty')
        print('')
        print('Current Queue:')
        que.Output()
        print('=================================================================')
        print('Program Finished')


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