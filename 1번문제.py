#선택정렬
def selection_sort(arr):
  n=len(arr)
  for i in range(n): # 배열의 길이만큼 반복
    min_idx=i
    for j in range(i+1,n):   # 첫 원소의 뒤부터 끝까지 반복하며 최소 인덱스 업데이트
      if arr[j]<arr[min_idx]:
        min_idx=j
    arr[i],arr[min_idx]=arr[min_idx],arr[i] # i와 최소 인덱스와 위치 변경
    return arr

  

#삽입정렬
def insertion_sort(arr):
  for i in range(1,len(arr)): # 두번째 원소부터 시작
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key: # 앞의 원소 인덱스가 0보다 같거나 크고 key 값보다 크면 계속 시행
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=key
  return arr
  
#quick 정렬
def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot=arr[len(arr)//2]
  left=[x for x in arr if x<pivot]
  middle=[x for x in arr if x==pivot]
  right=[x for x in arr if x>pivot ]
  return quick_sort(left)+middle+quick_sort(right)
  
 # 병합정렬
def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr)//2
  left=merge_sort(arr[:mid])
  right=merge_sort(arr[mid:])
  return merge(left,right)
  
def merge(left,right):
  result=[]
  j=i=0
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
  result.extend(left[i:])
  result.extend(right[j:])
  
# 버블정렬
def bubble_sort(arr):
  n=len(arr)
  for i in range(n):
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]  
  
import numpy as np
n=int(input("숫자를 입력하세요:"))
num_lst=np.random.randint(1,101,size=n).tolist()
num_lst






###############################################################################
# 프롬프트 질의 내역
