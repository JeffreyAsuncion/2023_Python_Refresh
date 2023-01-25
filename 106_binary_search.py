# Next step
#       enter ordered list
#       use recursion
# Next steps
#       add sorting function to work with an unordered list of integers

def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list)-1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1
    
print(binary_search([10,20,25,30,100], 30))