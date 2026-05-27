# 1. give colleciton of numbers
# 2. take collection and find matching pair that is equal to a ggiven sum
# 3. find pair of numbers that add up to 8 9example)
# 4. can be in memory or array - may assume they are ordered
# 5. cant repeat same element at same index twice but same number may appear 
# 6. assume always integars, negative can happen
# 7. something better than quadratic (not loop in loops)


# ── A set or dict/hash map: gives O(1) lookup
#    Checks if key exists instantly regardless of size

#   Loops through list once
#   For ea. num. 'x', check if 'target - x' already in set
#   If yes, found pair
#   If no, add 'x' to set and continue

# ── If use list it stores nums & algo becomes O(n²)
#    b/c for every num. scans entire seen list
# ── Set keeps it O(n)
#    one pass through input, instant lookup ea. time

# ── List [ 1, 2, 4, 4] target 8
#    walk through list one num at a time
# ── See 1 — looking for 7, not in set. Add 1
# ── See 2 — looking for 6, not in set. Add 2
# ── See 4 — looking for 4, not in set. Add 4
# ── See 4 again — looking for 4, it is in set. Found it.


def has_pair_with_sum(numbers, target):
    seen = set()
    for num in numbers:
        if target - num in seen:
            return True
        seen.add(num)   
    return False


print(has_pair_with_sum([1, 2, 3, 9], 8))  # should print False
print(has_pair_with_sum([1, 2, 4, 4], 8))  # should print True