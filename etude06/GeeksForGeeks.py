# Python program to implement
# Brent's cycle detection
# algorithm to detect cycle
# in a linked list.

# Node class
class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new Node
    #  at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit
    # the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next


    def detectCycle(self):
         # if head is null
         # then no loop
         temp=self.head

         if not (temp):
             return False
         first_p=temp
         second_p=temp.next
         power = 1
         length = 1

         # This loop runs till we
         # find the loop. If there
         # is no loop then second
         # pointer ends at NULL
         while (second_p and second_p!= first_p):

             # condition after which
             # we will update the power
             # and length as smallest
             # power of two gives
             # the start of cycle.
           if (length == power):

            # updating the power.
                power *= 2

            # updating the length
                length = 0

                first_p = second_p

           second_p = second_p.next
           length=length+1
         # if it is null then no loop
         if not (second_p) :
             return

    # Otherwise length stores
    # actual length of loop.
    # If needed, we can also
    # print length of loop.
    # print("Length of loop is ")
    # print (length)

    # Now set first_pointer
    # to the beginning and
    # second_pointer to
    # beginning plus cycle
    # length which is length.
         first_p = second_p = self.head
         while (length > 0):
             second_p = second_p.next
             length=length-1

            # Now move both pointers
            # at same speed so that
            # they meet at the
            # beginning of loop.
         while (second_p!= first_p) :
               second_p = second_p.next
               first_p = first_p.next

         return first_p

# Driver program for testing
llist = LinkedList()
# llist.push(50)
# llist.push(20)
# llist.push(15)
# llist.push(4)
# llist.push(10)
llist.push(1264460)
llist.push(1547860)
llist.push(1727636)
llist.push(1305184)
llist.push(1264460)



# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next
res=llist.detectCycle()
if( res.data):
    print ("loop found at ",end=' ')
    print (res.data)
else :
    print ("No Loop ")