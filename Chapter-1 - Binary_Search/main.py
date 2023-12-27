# The BinarySearch class implements a binary search algorithm to find the index of a target element in a sorted array.


class BinarySearch():

    def __init__(self,sortedarray):
        self.array=sortedarray

    def binSearch(self,target):
        left,right = 0 , len(self.array) - 1
        while left <= right :

            mid = (left+right) // 2
            mid_ele = self.array[mid]
            
            if mid_ele == target:
                return mid
            
            if mid_ele < target :
                left = mid + 1
            
            else:
                right =  mid - 1
        
        return None

list = [1,2,3,4,5,6]
binarysearch=BinarySearch(list)

target = 5 

result = binarysearch.binSearch(target)
result1 = binarysearch.binSearch(10)

print("The first result is : " , result)
print("The second result is : " ,result1 )


