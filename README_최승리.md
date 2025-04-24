

# 2번
문제:
2번 문제는 숫자 리스트를 정렬하고 타켓 숫자의 첫번째 인덱스와 마지막 인덱스를 더한 값을 반환하는 함수를 만드는 문제이다. 

해결:
- lower bound index를 찾는 함수와 upper bound index를 만드는 함수를 먼저 만든다.
- lower bound index 함수와 upper bound index의 차이는 if arr[mid] < target:와 if arr[mid] <= target: 의 차이이다.  if arr[mid] < target:의 경우 left > right가 될 때에 left가 lower bound index를 가리키게 된다. if arr[mid] <= target: 의 경우 left > right이 될 때에 left가 upper bound index를 가리키게 된다.
- find_target_index_sum()에서 숫자를 먼저 정렬한다. lower bound index와 upper bound index를 구한다. lower bound index와 upper bound index가 같을 경우 해당 타켓이 없다는 것을 알 수 있다.  값이 존재하지 않는 경우 마지막 인덱스 바깥 혹은 첫 인덱스 바깥으로 lower bound와 upper bound는 같은 값을 가지게 된기 때문이다.

# 3번
문제:
숫자리스트를 첫번째 값은 해당 숫자를 두번째 값은 개수를 나타내는 튜플의 리스트로 변환하는 문제이다. 결과값은 첫번째 튜플의 값들의 합이어야 한다.

해결:
- Counter 사용하여 아이템을 key로 카운트를 value로 반환한다.
- sorted을 사용하여 value를 기준으로 내림차순 정렬을 한다.