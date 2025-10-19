from node_removal import Node, LinkedList

if __name__ == "__main__":
    ll = LinkedList()

    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.tail = ll.head.next.next

    print("Removed from beginning:", ll.remove_beginning())
    print("Removed at end:", ll.remove_at_end())
    print("Removed specific (20):", ll.remove_at(20))
    print("Remove not found (99):", ll.remove_at(99))
