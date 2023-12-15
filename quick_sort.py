class solution:
    def partition(self,arr,low,high):
        pi=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j<=pi]:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
   
    def quick_sort(self,arr,low,high):
        if low<high:
            pi=self.partition(arr,low,high)
            self.quick_sort(arr,pi+1,high)
            self.quick_sort(arr,low,pi-1)
           
    def minimize_value(self,arr,x):
        self.quick_sort(arr,0,len(arr)-1)
        z=x
        for i in range(len(arr)):
            if arr[i]>x:
                z+=1
                if z not in arr:
                    return z
        return z+1
s=solution()
arr=[int(i) for i in input('enter the element in array').split(' ')]
e=int(input('enter the element for finding minimizing value:'))
print('the required minimizing element is :',s.minimize_value(arr,e))