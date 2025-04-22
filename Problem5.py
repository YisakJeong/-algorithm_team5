import sys

def main():
    input = sys.stdin.read  # 전체 입력을 한 번에 읽기
    data = list(map(int, input().split()))
    
    n = data[0]
    numbers = data[1:]

    # 내장 정렬 (Timsort, O(n log n))
    numbers.sort()

    # 출력
    sys.stdout.write(' '.join(map(str, numbers)) + '\n')

if __name__ == "__main__":
    main()
