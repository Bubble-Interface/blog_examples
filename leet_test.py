def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # [1,2,3,4,5,6,7], k = 3
    # [1,2], k = 5 -> -3
    import math
    "d".is
    i = math.inf
    j = math.inf
    for n in nums:
        if n <= i:
            i = n
        elif n <= j:
            j = n
        else:
            return True
    return False

        

print(rotate([1,1,-2,6], 5))