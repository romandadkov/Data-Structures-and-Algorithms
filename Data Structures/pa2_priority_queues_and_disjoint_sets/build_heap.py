# python3

def left_child_idx(idx):
    return 2 * idx + 1

def right_child_index(idx):
    return 2 * idx + 2

def sift_down(data, swaps, i):
    j = i
    left = left_child_idx(j)
    right = right_child_index(j)

    if left < len(data) and data[j] > data[left]:
        j = left

    if right < len(data) and data[j] > data[right]:
        j = right

    if i != j:
        swaps.append((i, j))
        data[i], data[j] = data[j], data[i]
        sift_down(data, swaps, j)

    return swaps

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []

    for i in range(int((len(data)) / 2), -1, -1):
        sift_down(data, swaps, i)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
