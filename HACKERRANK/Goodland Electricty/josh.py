def pylons(k, arr):
    count = 0
    i=0
    while i < n:
        placed = False
        for j in range(min(n-1, i+k-1), max(-1,i-k), -1):
            if arr[j] == 1:
                count +=1
                i=j+k
                placed = True
                break
        if not placed:
            return -1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
