def second_largest(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two elements")
    first = second = float('-inf')
    for n in nums:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n
    if second == float('-inf'):
        raise ValueError("No distinct second largest element")
    return second
