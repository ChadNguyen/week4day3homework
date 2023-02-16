class LinkedNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    @staticmethod
    def convert_list(linked):
        if not linked:
            return None
        
        head = LinkedNode(linked[0])
        current_node = head
        
        for i in range(1, len(linked)):
            current_node.next_node = LinkedNode(linked[i])
            current_node = current_node.next_node

        return head
    
    @staticmethod
    def sort_input_list(func):
        def wrapper(linked_list):
            node_list = []
            current_node = linked_list
            while current_node:
                node_list.append(current_node)
                current_node = current_node.next_node

            sorted_node_list = LinkedNode.merge_sort(node_list)
            if sorted_node_list:
                head = sorted_node_list[0] 
            else:
                return None

            for i in range(len(sorted_node_list)-1):
                sorted_node_list[i].next_node = sorted_node_list[i+1]
            sorted_node_list[-1].next_node = None

            return func(head)
        return wrapper

    @staticmethod
    def merge_sort(node_list):
        if len(node_list) <= 1:
            return node_list

        mid = len(node_list) // 2
        left_half = node_list[:mid]
        right_half = node_list[mid:]

        left_half = LinkedNode.merge_sort(left_half)
        right_half = LinkedNode.merge_sort(right_half)  

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].value <= right_half[j].value:
                node_list[k] = left_half[i]
                i += 1
            else:
                node_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            node_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            node_list[k] = right_half[j]
            j += 1
            k += 1

        return node_list

    def print_nodes(self):
        current_node = self
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next_node
        print('None')
linked_list = LinkedNode.convert_list([1,3,5,6,2,7,9,8,10])
sorted_linked_list = LinkedNode.sort_input_list(sorted)(linked_list)
sorted_linked_list.print_nodes()





            

    
    

