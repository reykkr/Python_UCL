def binary(data,k):
   low = 0
   high = len(data) - 1
   while low <= high:
       mid = (low + high) // 2
       if k < data[mid]:
            high = mid - 1
       elif k == data[mid]:
           return mid
       else:
            low = mid + 1
   return -9
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("elements: "))
    lst.append(ele)
lst.sort()
j = eval(input("enter a number"))
print(binary(lst,j))