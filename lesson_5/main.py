# Префиксная сумма

def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]

    return prefixsum


def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]
