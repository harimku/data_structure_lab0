import random

# node definition
class Node:
        def __init__(self):
                self.data = None
                self.previous = None
                # introduce a 'next' node for doubly linked list
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

class DList:
        def __init__(self):
                self.tail = None
                # introduce 'head' node for double link
                self.head = None

        # appends to tail of list
        def Append(self,data):
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

        # prepends to head of list
        def Prepend(self,data):
                pdata = Node()
                pdata.node = data
                if (self.head == None):
                        self.head = pdata         
                else:
                        self.head.prev = pdata
                        pdata.next = self.head
                        self.head = pdata

        # inserts data after found data
        def InsertAfter(self, find, data):
                if find is None:
                        return None
                if not isinstance(find, int):
                        raise ValueError('Find argument must be int')

                pdata = Node()
                pdata.node = data

                # look for find
                if(self.tail.node == find):
                        self.tail.next = pdata
                        pdata.prev = self.tail
                        self.tail = pdata
                        return pdata


                runner = self.tail
                while(runner):
                        if runner.prev is not None and runner.prev.node is not None and runner.prev.node == find:
                                break
                        runner = runner.prev
                if runner is None:
                        return None

                runner.prev.next = pdata
                pdata.prev = runner.prev
                pdata.next = runner
                runner.prev = pdata
                return pdata


        # inserts data before found data
        def InsertBefore(self, find, data):
                if find is None:
                        return None
                if not isinstance(find, int):
                        raise ValueError('Find argument must be int')

                pdata = Node()
                pdata.node = data

                # look for find
                if(self.head.node == find):
                        self.head.prev = pdata
                        pdata.next = self.head
                        self.head = pdata
                        return pdata

                runner = self.tail
                while(runner):
                        if runner.prev is not None and runner.node == find:
                                break
                        runner = runner.prev

                if runner is None:
                        return None
                
                pdata.prev = runner.prev
                runner.prev = pdata
                pdata.prev.next = pdata
                pdata.next = runner
                return pdata
                
        # finds data node and returns it
        def Search(self,data):
                runner = self.tail
                while(runner):
                        if runner.node == data:
                                break 
                        runner = runner.prev
                if runner is None:
                        print('There is no such element in the list')

                if (runner):
                        return runner.node
                else: return None
                
        # deletes a node from the list
        def Delete(self,data):
                if (self.tail == None):
                        raise ValueError('There is no element to delete')
                        return None      
                if (self.tail.node == data):
                        self.tail = self.tail.prev 
                        self.tail.next = None
                        return None

                runner = self.tail
                while(runner):
                        if runner.prev is not None and runner.prev.node is not None and runner.prev.node == data:
                                break 
                        runner = runner.prev
                if runner is None:
                        raise ValueError('The list does not contain the given element')
                if (runner.prev == self.head):
                        self.head = runner
                        self.head.prev = None
                else:
                        runner.prev = runner.prev.prev
                        runner.prev.next = runner

        # returns number of nodes in list
        def Count(self):
                temp = self.tail
                count = 0
                while (temp): 
                        count += 1
                        temp = temp.prev
                return count 

        # returns true if list is empty
        def IsEmpty(self):
                temp = self.head
                while (temp):
                        return False
                return True

        # prints list from tail of list
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
        list = DList()
        for x in range( count ):
                rnumber = random.randint(1,100)
                list.Append( rnumber )
        print()
        list.Output()
       
    # our test code
        '''
        dll = DList()
        dll.Append(1)
        dll.Append(2)
        dll.Append(3)
        dll.Prepend(0)
        x = dll.InsertAfter(1, -1841)
        x = dll.InsertBefore(1, -777)
        dll.Delete(-777)
        y = dll.Search(-777)
        z = dll.IsEmpty()
        
        dll.Output()
        

        ## dll test
        runner = dll.tail
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

        print('Is this list empty? {} '.format(z))
        print('Searched value is: {} '.format(str(y)))

        exit()
        
        runner = dll.head
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