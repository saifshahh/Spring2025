### Question 1:

```
def find_peak(int N):
    left = 0
    right = N

    while left < right:
        mid = (left + right)
        if query(mid) < query(mid + 1):
            left = mid + 1
        else:
            right = mid
    return left
```
