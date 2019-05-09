Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`? 
Answer:  The runtime complexity of `enqueue` is 0(n).

2. What is the runtime complexity of `dequeue`? 
Answer:  The runtime complexity of `dequeue` is 0(1).

3. What is the runtime complexity of `len`?
Answer:  The runtime complexity of `len` is 0(1).

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
Answer: log(n)

2. What is the runtime complexity of `contains`?
Answer: log(n)

3. What is the runtime complexity of `get_max`? 
Answer: log(n)

## Heap

1. What is the runtime complexity of `_bubble_up`? 
Answer: log(n)

2. What is the runtime complexity of `_sift_down`? 
Answer: log(n)

3. What is the runtime complexity of `insert`? 
Answer: log(n)

4. What is the runtime complexity of `delete`? 
Answer: log(n)

5. What is the runtime complexity of `get_max`?
Answer: 

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
Answer: O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
Answer: O(1)

3. What is the runtime complexity of `ListNode.delete`?
Answer: O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
Answer: O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
Answer: O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
Answer: O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
Answer: O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
Answer: O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
Answer: O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
Answer: O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    Answer: Array.splice in JS would be a worst case of 0(n) which means delete runs faster.