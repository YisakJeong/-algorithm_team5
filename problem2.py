import numpy as np

# 반복형 이진탐색색
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

# 재귀형 이진탐색
def binary_search_rec(arr, target, low, high):
  if low > high:
      return "NO"
  mid = (low + high) // 2
  if arr[mid] == target:
      return "YES"
  elif arr[mid] < target:
      return binary_search_rec(arr, target, mid + 1, high)
  else:
      return binary_search_rec(arr, target, low, mid - 1)
 

num=int(input("숫자를 입력하세요:"))
num_lst=np.random.randint(1,101,size=num).tolist()
num_lst.sort()
print(num_lst)
target=int(input("찾고 싶은 숫자를 입력하세요:"))
binary_search_rec(num_lst, target,0,len(num_lst)-1)
  
  
num=int(input("숫자를 입력하세요:"))
num_lst=np.random.randint(1,101,size=num).tolist()
num_lst.sort()
print(num_lst)
target=int(input("찾고 싶은 숫자를 입력하세요:"))

result=binary_search(num_lst, target)
print(result)










############################################################
# 프롬프트 질의 내역