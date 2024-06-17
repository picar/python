

def two_sum(nums, target):
    ''''
    h = { n:k for k, n in enumerate(nums) }
    for k, n in enumerate(nums):
        i = h.get(target-n, None)
        if  k != i and i is not None:
            return {k, i}
    '''

    h = {}
    for k, n in enumerate(nums):
        c = target-n
        if c in h:
            return {k, h[c]}
        h[n] = k
    