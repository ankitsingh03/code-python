class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        temp = self.get_head()
        if temp == None:
            self.__head = Node(data)
            return
        while temp.get_next() != None:
            temp = temp.get_next()
        temp.set_next(Node(data))

        # Remove pass and write the logic to add an element

    def display(self):
        temp = self.get_head()
        # if temp.get_next() == None:
        #     print(temp.get_data())
        while temp != None:
            print(temp.get_data())
            temp = temp.get_next()
        # Remove pass and write the logic to display the elements

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


list1 = LinkedList()
list1.add("Sugar")
list1.add(("cool"))
# list1.add("cool")
print("Element added successfully")
list1.display()
# Similarly add all the specified element(s)