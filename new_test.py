class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

def removeZeroSumSublists(head):
    # I was very drunk
    # the consept is clever
    # but the execution ...
    sums = {}
    node = head
    i = 0
    cur_sum = 0
    while node:
        cur_sum += node.val
        sums[i] = cur_sum
        node = node.next
        i += 1
    flipped = {}
    for k,v in sums.items():
        if v not in flipped:
            flipped[v] = [k]
        else:
            flipped[v].append(k)
    max_distance = 0
    max_value = 0
    max_distance_key = None
    for k, v in flipped.items():
        if k == 0 and v[-1] >= max_value:
            max_distance_key = k
            distance = v[-1] - 0
            max_value = v[-1]
            # special logic
        elif len(v) > 1:
            distance = v[-1] - v[0]
            if distance > max_distance:
                max_value = v[-1]
                max_distance = distance
                max_distance_key = k
    if max_distance_key is not None:
        if max_distance_key == 0:
            start = 0
            end = flipped[max_distance_key][-1] + 1
        else:
            start = flipped[max_distance_key][0] + 1
            end = flipped[max_distance_key][-1] + 1
        pops = list(range(start, end))
        for i in pops:
            sums.pop(i)
    if len(sums) == 0 or (len(sums) == 1 and list(sums.values())[0] == 0) :
        return None
    if len(sums) == 1 :
        key = list(sums.keys())[0]
        for _ in range(key):
            head = head.next
        head.next = None
        return head
    while head.val == 0:
        head = head.next
    node = head
    i = 1
    while node and len(sums) > 1:
        if sums.get(i, None):
            node = node.next
        else:
            j = i
            while not sums.get(i, None):
                i += 1
            cur_node = node.next
            for _ in range(i-j):
                cur_node = cur_node.next
            node.next = cur_node
            node = node.next
        sums.pop(i)
        i += 1
    return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(-3)
d = ListNode(3)
e = ListNode(-2)
# f = ListNode(3)

a.next = b
b.next = c
c.next = d
# d.next = e

removeZeroSumSublists(a)