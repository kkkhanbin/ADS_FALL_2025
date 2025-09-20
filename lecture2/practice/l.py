class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
# implement this function
# don't change anything else
def findMaxSum(n: int, head: ListNode) -> int:
	max_summ = 0
	summ = 0
	cur = head
	max_number = head.val
	for _ in range(n):
		# print(f'cur - {cur.val}. sum - {summ}', end=" ")
		if cur.val > max_number:
			max_number = cur.val
		if summ + cur.val <= 0:
			# print("ZEROD")
			summ = 0
		else:
			# print("TAKEN")
			summ += cur.val
		if summ > max_summ:
			# print("NEW RECORD!!!! - ", summ)
			max_summ = summ
		cur = cur.next
		
	if max(max_summ, summ) == 0:
		return max_number
	return max(max_summ, summ)
 
n = int(input())
a = list(map(int, input().split()))
head = ListNode(0)
tail = ListNode(0)
 
for i in range(n):
	tmp = ListNode(a[i])
	if i == 0:
		head = tmp
		tail = tmp
	else:
		tail.next = tmp
		tail = tmp
 
print(findMaxSum(n, head))