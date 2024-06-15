import unittest

from linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    def test_create_node(self):
        node = Node(1)
        self.assertEqual(node.data, 1)
        self.assertIsNone(node.next)

    def test_append_node(self):
        linked_list = LinkedList()
        linked_list.append(Node(1))
        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.tail.data, 1)
        linked_list.append(Node(2))
        self.assertEqual(linked_list.tail.next.data, 2)

    def test_delete_head(self):
        linked_list = LinkedList()
        linked_list.append(Node(1))
        linked_list.delete_head()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_length_of_list(self):
        linked_list = LinkedList()
        self.assertEqual(len(linked_list), 0)
        linked_list.append(Node(1))
        self.assertEqual(len(linked_list), 1)
        linked_list.append(Node(2))
        self.assertEqual(len(linked_list), 2)   

    def test_iterate_list(self):
        linked_list = LinkedList()
        linked_list.append(Node(1))
        linked_list.append(Node(2))
        
    

if __name__ == "__main__":
    unittest.main()