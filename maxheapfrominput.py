import sys

def sequence_from_input():

    for test_case in sys.stdin:
        sequence = test_case.strip().split()   
        for i in range(len(sequence)):
            sequence[i] = int(sequence[i])
            
        heap = heap_build(sequence)
        
        p_string = ""
        for item in heap:
            p_string += str(item) + " "
        p_string.strip()
        print(p_string)

def heap_build(sequence): #input array(list) from 0 to n-1
    root = (len(sequence)//2) - 1

    while root >= 0:
        percolate_down(sequence, root, len(sequence))
        root -= 1

    return sequence

def percolate_down(sequence, root, num_items):
    left_i = (root * 2) + 1
    right_i = left_i + 1
    if left_i < num_items - 1 and sequence[root] < sequence[left_i + 1] and sequence[left_i] < sequence[left_i + 1]:
        sequence[root], sequence[right_i] = sequence[right_i], sequence[root]
        return percolate_down(sequence, right_i, num_items)
    if left_i < num_items and sequence[root] < sequence[left_i]:
        sequence[root], sequence[left_i] = sequence[left_i], sequence[root]
        return percolate_down(sequence, left_i, num_items)
    return
    
    
sequence_from_input()
    
