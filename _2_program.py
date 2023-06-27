# Reverse a linked list in groups of given size

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
def reverse(head, k):
	if not head or k == 1:
		return head
	dummy = Node(-1) 
	dummy.next = head
	prev = dummy
	curr = dummy
	next = dummy
	count = 0
	toLoop = 0
	i = 0
	while curr:
		curr = curr.next
		count += 1
	while next:
		curr = prev.next 
		next = curr.next 
		toLoop = count > k and k or count - 1
		for i in range(1, toLoop):
			curr.next = next.next
			next.next = prev.next
			prev.next = next
			next = curr.next
			prev = curr
			count -= k
	return dummy.next
def printList(node):
	while node is not None:
		print(node.data, end=" ")
		node = node.next
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

print("Given linked list")
printList(head)
head = reverse(head, 3)
print("\nReversed Linked list")
printList(head)


