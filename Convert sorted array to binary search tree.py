class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def sortedarray(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = Node(nums[mid])
    root.left = sortedarray(nums[:mid])
    root.right = sortedarray(nums[mid+1:])
    return root
