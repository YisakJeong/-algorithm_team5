import numpy as np

def binary_search(arr,target):
  low,high=0,len(arr)-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
      return "YES"
    elif arr[mid]<target:
      low=mid+1
    else:
      high=mid-1
  return "NO"
  
num=int(input("숫자를 입력하세요:"))
num_lst=np.random.randint(1,101,size=num).tolist()
num_lst.sort()
print(num_lst)
target=int(input("찾고 싶은 숫자를 입력하세요:"))

result=binary_search(num_lst, target)
print(result)









############################################################
# 프롬프트 질의 내역