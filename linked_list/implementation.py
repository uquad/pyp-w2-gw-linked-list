from .interface import AbstractLinkedList
from linked_list import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements is  None:
            self.start=None
            self.end=None
        else:
            self.start=None
            self.end=None
            for elem in elements:
                self.append(elem)

    def __str__(self):
        if self is None:
            return "[]"
        else:
            start_str="["
            aux=self.start
            while aux.next is not None:
                start_str+= str(aux.elem) +", "
                aux=aux.next
            start_str+= str(aux.elem) +"]"
            
            return start_str
            

    def __len__(self):
        
        if self.start is None:
            return 0
            
        count=1
        aux=self.start
        while aux.next is not None:
            aux=aux.next
            count+=1
        
        return count

    def __iter__(self):
        current_node = self.start
        while current_node != None:
            yield current_node
            current_node = current_node.next
    

    def __getitem__(self, index):
        if len(self)<=index:
            raise IndexError
        
        aux=self.start
        for i in range(index):
            aux=aux.next
        
        return aux.elem
            

    def __add__(self, other):
        if self is None:
            return other
        elif other is None:
            return self
            
        newLList=LinkedList()
        self.end.next=other.start
        self.end=other.end   
        
        newLList.start=self.start
        newLList.end=self.end
        
        return newLLlist

    def __iadd__(self, other):
        self.end.next=other.start
        self.end=other.end
        return self


    def __ne__(self, other):
        return not (self==other)

        

    def __eq__(self, other):
        if self.start is None and other.start is not None:
            return False
        elif self.start is not None and other.start is None:
            return False
        elif self.start is  None and other.start is None:
            return True
        elif len(self)!=len(other):
            return False
            
        firstListNode=self.start
        secondListNode=other.start
        
        while firstListNode.next is not None:
            if firstListNode.elem == secondListNode.elem:
                continue
            else:
                return False
        
        return True

    def append(self, elem):
        
        newNode=Node(elem)
        if self.start is None:
            self.start=newNode
            self.end=newNode
        else:
            aux=self.end
            aux.next=newNode
            self.end=aux.next
                

    def count(self):
        
        return len(self)

    def pop(self, index=None):
        
        #if index specified is more than the lenght of the list
        if index >= len(self):
            raise IndexError
        
        #if no index specified,pop last element
        if index is None:
            aux=self.start
            while aux.next!= self.end:
                aux=aux.next
            
            val=self.end.elem
            aux.next=None
            self.end=aux

            
        #pop first element    
        elif index==0:
            val=self.start.elem
            self.start=self.start.next
            
        #pop from index location
        else:
            aux=self.start
            for i in range(index-1):
                aux=aux.next
                
            nodeToPop=aux.next
            val=nodeToPop.elem
            aux.next=nodeToPop.next
            
            
        return val
            
            
            
            
                
