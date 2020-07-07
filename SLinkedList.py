import random

# node definition
class Node:
        def __init__(self):
                self.data = None
                self.previous = None

        def get(self):
                return self.data
        def getPrev(self):
                return self.previous
        def setPrev(self,previous):
                self.previous = previous
        def set(self,data):
                self.data = data
        node = property(get,set)
        prev = property(getPrev,setPrev)
     

# Singly Linked List
class SList:
        def __init__(self):
                self.tail = None

        # appends to tail of list
        def Append(self,data):
                pdata = Node()
                pdata.node = data
                if (self.tail == None):
                        self.tail = pdata
                else:
                        # tail exists
                        pdata.prev = self.tail
                        self.tail = pdata

        # prepends to head of list
        def Prepend(self,data):
                pdata = Node()
                pdata.node = data
                if (self.tail == None):
                        self.tail = pdata      
                else:
                        # tail exists
                        runner = self.tail
                        while(runner):
                                if runner.prev is None:
                                        break
                                runner = runner.prev
                        runner.prev = pdata

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

                pdata.prev = runner.prev
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
                runner = self.tail
                while(runner):
                        if runner.prev is not None and runner.node == find:
                                break
                        runner = runner.prev

                if runner is None:
                        return None
                
                pdata.prev = runner.prev
                runner.prev = pdata
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
                        return None

                runner = self.tail
                while(runner):
                        if runner.prev is not None and runner.prev.node is not None and runner.prev.node == data:
                                break 
                        runner = runner.prev
                if runner is None:
                        raise ValueError('The list does not contain the given element')
                else:
                        runner.prev = runner.prev.prev

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
                temp = self.tail
                while (temp):
                        return False
                return True

        # prints list from tail of list
        def Output(self):
                rover = self.tail
                while (rover != None):
                        #print(rover.node,end='\t')
                        rover = rover.prev
                print()



def main():
        '''
        count = 10
        list = SList()
        for x in range( count ):
                rnumber = random.randint(1,100)
                list.Append( rnumber )
                print( rnumber, end='\t' )
        print()
        list.Output()
        '''

        sll = SList()
        sll.Append(1)
        sll.Append(2)
        sll.Append(3)
        sll.Prepend(0)
        x = sll.InsertAfter(1, -666)
        x = sll.InsertBefore(1, -777)
        sll.Delete(-777)
        y = sll.Search(-777)
        z = sll.IsEmpty()
        
        ## sll test
        runner = sll.tail
        count = 0
        while(runner):
                if runner.prev is None:
                        prev_out = 'NULL'
                else:
                        prev_out = str(runner.prev.node)

                print('Node {} : data={}, prev={}'.format(str(count), str(runner.node), prev_out))
                count += 1
                runner = runner.prev

        print('Is this list empty? {} '.format(z))
        print('Searched value is: {} '.format(str(y)))

        exit()
        

if __name__ == '__main__':
        main()