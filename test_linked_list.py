from node_removal import Node, LinkedList

if __name__ == "__main__":
    ll = LinkedList()

    ll.head = Node("assemble")
    ll.head.next = Node("prepare")
    ll.head.next.next = Node("roll")
    ll.tail = ll.head.next.next

    print("Removed from beginning:", ll.remove_beginning())
    print("Removed at end:", ll.remove_at_end())
    print("Removed specific:", ll.remove_at("prepare"))
    print("Remove not found:", ll.remove_at("roll"))
