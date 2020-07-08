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
            print('Find argument must be int')

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
            print('Find argument must be int')

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
            return None
        if (runner):
            return runner
        else: 
            return None
                
    # deletes a node from the list
    def Delete(self,data):
        if (self.tail == None):
            print('There is no element to delete')
            return None      
        if (self.tail.node == data):
            self.tail = self.tail.prev 
            if(self.tail is None):
                return None
            return None

        runner = self.tail
        while(runner):
            if runner.prev is not None and runner.prev.node is not None and runner.prev.node == data:
                break 
            runner = runner.prev
        if runner is None:
            print('There is no such element in the list.')
            return None
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
        if(self.tail is None):
            return True
        else:
            return False

    # prints list from tail of list
    def Output(self):
        rover = self.tail
        count = 0

        while (rover != None):
            if rover.prev is None:
                prev_out = 'NULL'
            else:
                prev_out = str(rover.prev.node)
                
            print('Node {} : data={}, prev={}'.format(str(count), str(rover.node), prev_out))
            count += 1
            rover = rover.prev

        if count == 0:
            print('<Empty List>')

    # recursive output function for Recursion Exercise
    @staticmethod
    def recurseOutput(runner,count=0):
        if(runner is None):
            return
        else:   
            if(runner.prev is not None):
                prev = runner.prev.node
            else:
                prev = "NULL"
            print('Node {} : data={}, prev={}'.format(str(count), str(runner.node), prev))
            count += 1
            runner = runner.prev
            return SList.recurseOutput(runner,count=count)



def main():
    # Automated Test
    print('=============== Singly Linked List Implementation ===============')
    print('Operation: Creating List')
    sll = SList()
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: Append({})'.format(str(1)))
    print('Operation: Append({})'.format(str(2)))
    print('Operation: Append({})'.format(str(3)))
    sll.Append(1)
    sll.Append(2)
    sll.Append(3)
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: Prepend({})'.format(str(0)))
    sll.Prepend(0)
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: InsertAfter({},{})'.format(str(1),str(-1841)))
    sll.InsertAfter(1,-1841)
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: InsertBefore({},{})'.format(str(1),str(-777)))
    sll.InsertBefore(1,-777)
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: Delete({})'.format(str(-777)))
    sll.Delete(-777)
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: Search({})'.format(str(-777)))
    val = sll.Search(-777)
    if val is not None:
        print('Node found with value {}'.format(str(val.node)))
    else:
        print('Node not Found')
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: Search({})'.format(str(-1841)))
    val = sll.Search(-1841)
    if val is not None:
        print('Node found with value {}'.format(str(val.node)))
    else:
        print('Node not Found')
    print('')
    print('Operation: Search({})'.format(str(99999)))
    val = sll.Search(99999)
    if val is not None:
        print('Node found with value {}'.format(str(val.node)))
    else:
        print('Node not Found')
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: IsEmpty()')
    val = sll.IsEmpty()
    if val:
        print('List is empty')
    else:
        print('List is not empty')
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: Delete(2)')
    print('Operation: Delete(3)')
    print('Operation: Delete(-1841)')
    print('Operation: Delete(1)')
    print('Operation: Delete(0)')
    sll.Delete(2)
    sll.Delete(3)
    sll.Delete(-1841)
    sll.Delete(1)
    sll.Delete(0)
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Operation: IsEmpty()')
    sll.IsEmpty()
    val = sll.IsEmpty()
    if val:
        print('List is empty')
    else:
        print('List is not empty')
    print('')
    print('Current List:')
    sll.Output()
    print('=================================================================')
    print('Program Finished')


if __name__ == '__main__':
    main()