class solution:
    def select(self,arr,index,k):
        curr=arr[index]
        pre=index-1
        while pre>=0:
            if arr[pre]>curr:
              arr[pre+1]=arr[pre]
            else:
                break
            pre-=1
        arr[pre+1]=curr
        
        
    
    def insertion(self,arr,n):
        if n==1:
            return
        for unsorted in range(1,n):
            self.select(arr,unsorted,n)

arr=[10,20,3,55,4,35,67]
n=len(arr)
obj=solution()
obj.insertion(arr,n)
print(arr)
