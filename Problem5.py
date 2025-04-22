# 파일을 읽고 df로 저장
import pandas as pd
numbers = pd.read_csv("numbers.csv") # 파일명 변환 필요
#numbers = df['values'].tolist() # 리스트화가 되어있지 않을 경우

# sort() 사용 - 내장 정렬 함수
basic_sorted = numbers.sort()
print("sort():", numbers)

# 병합 정렬 (Merge Sort)
def merge_sort(arr):
    #기본 조건: 리스트 길이가 1 이하이면 그대로 반환(정렬할 필요 없음)
    if len(arr) <= 1:
        return arr

    # 중간 인덱스를 배열을 반으로 나눔
    mid = len(arr) // 2

    # 왼쪽 절반을 재귀적으로 정렬
    left = merge_sort(arr[:mid])

    # 오른쪽 절반을 재귀적으로 정렬
    right = merge_sort(arr[mid:])

    #두 개의 정렬된 리스트를 병합하는 함수 호출후 반환
    return merge(left, right)

# 두 개의 정렬된 리스트를 병합하는 함수
def merge(left, right):
    result = [] # 병합된 결과를 저장할 리스트
    i = j = 0 # 각 기스트의  연재 배고 위치를 나타내는 인덱스

    # 두 리스트를 비교하며 작은 값부터 결과 리스트에 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]: #왼쪽 리스트의 값이 작으면 추가
            result.append(left[i])
            i += 1
        else: #오른쪽 리스트의 값이 작으면 추가
            result.append(right[j])
            j += 1

    # 남은 요소들을 결과 리스트에 추가(왼쪽 리스트에 남아 있는 경우)
    result.extend(left[i:])

    # 남은 요소들을 결과 리스트에 추가(오른쪽 리스트에 남아 있는 경우)
    result.extend(right[j:])

    return result #최종 정렬된 리스트 반환

merge_sorted = merge_sort(numbers)

# 퀵 정렬
def quick_sort(arr):
    # 종료 조건: 리스트의 길이가 1 이하이면 이미 정렬된 상태이므로 그대로 반환
    if len(arr) <= 1:
        return arr

    # Pivot(기준 값)을 리스트의 중간값으로 설정
    pivot = arr[len(arr) // 2]

    # 리스트를 Pivot을 기준으로 나누기
    left = [x for x in arr if x < pivot]     # Pivot보다 작은 값들
    middle = [x for x in arr if x == pivot]  # Pivot과 같은 값들
    right = [x for x in arr if x > pivot]    # Pivot보다 큰 값들

    # 재귀 호출을 통해 left와 right를 정렬하고, middle과 함께 합쳐서 반환
    return quick_sort(left) + middle + quick_sort(right)

quick_sorted = quick_sort(numbers)