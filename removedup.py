def removeDuplicates(arr,n):
    j=-1
    for i in range(n):
        if j==-1 or arr[j]!=arr[i]:
            j+=1
            arr[j]=arr[i]
            print(arr[i],end =" ")
    return j+1
    

    
a=[1,1,2,3,3,4,4,4,4,4,4,5,6,6,7,7,8]
l=len(a)    

x=removeDuplicates(a,l)
print("\nLength of  array is ",x)
