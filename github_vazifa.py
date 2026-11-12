def majority_element(nums: list) -> int:
    if not nums:
        return -1

    new = {}

    for son in nums:
        if son not in new:
            new[son] = 1
        else:
            new[son] += 1

    natija = max(new, key=new.get)
    return natija


print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
print(majority_element([])) 