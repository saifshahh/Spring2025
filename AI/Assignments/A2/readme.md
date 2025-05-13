### Question 1:

`py
def find_peak(N: int) -> int:
    left = 0
    right = N

    while left < right:
        mid = (left + right) // 2
        if query(mid) < query(mid + 1):
            left = mid + 1
        else:
            right = mid

    return left
`
