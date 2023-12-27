class Sort():
    def __init__(self,array) -> None:
        self.array=array
    
    def selectionsort(self) -> None:
        ans=[]
        while(len(self.array)>0):
            a=min(self.array)
            self.array.remove(a)
            ans.append(a)
        print(ans)

li = [2,1,5,3,4,9]

ans = Sort(li) 
ans.selectionsort()


