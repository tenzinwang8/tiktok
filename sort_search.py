def bubble_sort_2d(arr):
    rows = len(arr)
    cols = len(arr[0])
    n = rows * cols
    
    for i in range(n):
        for j in range(0, n-i-1):
            r1, c1 = j // cols, j % cols
            r2, c2 = (j+1) // cols, (j+1) % cols
            
            if arr[r1][c1] > arr[r2][c2]:
                arr[r1][c1], arr[r2][c2] = arr[r2][c2], arr[r1][c1]

def search_element(arr, target):
    rows = len(arr)
    cols = len(arr[0])
    
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == target:
                print(f"Element {target} found at position: ({i}, {j})")
                return
    print(f"Element {target} is not in the array.")

# Example usage
arr = [[5, 3, 8],
       [9, 1, 7],
       [4, 6, 2]]

print("Original array:")
for row in arr:
    print(row)

bubble_sort_2d(arr)
print("\nSorted array:")
for row in arr:
    print(row)

search = int(input("Enter the element to search in the sorted array: "))
search_element(arr, search)

#Exercise: 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement

def main():
    user_input = input("Enter an array of integers separated by spaces: ")
    arr = list(map(int, user_input.split()))

    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)

    target = int(input("Enter the element you want to replace: "))
    replacement = int(input("Enter the replacement element: "))

    replace_elements(sorted_arr, target, replacement)
    print("Modified array after replacement:", sorted_arr)

if __name__ == "__main__":
    main()

