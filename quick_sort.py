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
    return arr

def main():
    # Prompt user for input array
    input_array = input("Enter array of integers separated by spaces: ")
    arr = [int(x) for x in input_array.split()]

    # Sort the array using Quick Sort algorithm
    sorted_arr = quick_sort(arr)
    print("Sorted Array:", sorted_arr)

    # Allow user to specify target element to search for
    target = int(input("Enter the target element to search for: "))

    # Search for the target element in sorted array
    if target in sorted_arr:
        # If target element found, prompt user for replacement element
        replacement = int(input("Enter the replacement element: "))
        # Replace all occurrences of target element with replacement element
        modified_arr = replace_elements(sorted_arr, target, replacement)
        print("Modified Array:", modified_arr)
    else:
        print("Target element not found in the array.")

if __name__ == "__main__":
    main()
