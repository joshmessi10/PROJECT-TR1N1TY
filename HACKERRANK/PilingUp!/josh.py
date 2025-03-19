def eval():
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        left = 0
        right = n - 1
        is_possible = True
        last = float('inf')
        while left <= right:
            if arr[left] >= arr[right] and arr[left] <= last:
                last = arr[left]
                left += 1
            elif arr[right] <=last:
                last = arr[right]
                right -= 1
            else:
                is_possible = False
                break
        
        results.append("Yes" if is_possible else "No")
    return results

if __name__ == "__main__":
    results = eval()
    for result in results:
        print(result)
