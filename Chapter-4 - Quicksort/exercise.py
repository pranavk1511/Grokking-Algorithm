#4.1

def sum(a):
    if not a:  #Base Case 
        return 0
    else:
        ans=a.pop()+sum(a)  
    return ans

a= sum([1,2,4,5])
print("The Sum is : ",a)

# Pop is used to remove and return the item at a specific index (default is the last item if no index is specified).It modifies the list in place and returns the removed element.

# remove is used to remove the first occurrence of a specific value.It modifies the list in place and does not return any value (returns None).

#4.2

def count(a):
    if not a :
        return 0 
    else:
        a.pop()
        return 1+count(a)
        

a=[1,2,3,4,25,6]
print("The count is : ",count(a))

#4.3

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        max_left = find_max(arr[:mid])
        max_right = find_max(arr[mid:])
        return max(max_left, max_right)

a=[1,2,3,4,25,6]
print("The Max is : ",max(a))

#4.5 O(n)
#4.6 O(n)
#4.7 O(1)
#4.8 O(n2)