class QuickSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        self._quicksort(0, len(self.array) - 1)

    def _quicksort(self, low, high):
        if low < high:
            # Find the partition index such that elements smaller than pivot are on the left,
            # and elements greater than pivot are on the right
            partition_index = self._partition(low, high)

            # Recursively sort the sub-arrays on both sides of the partition
            self._quicksort(low, partition_index - 1)
            self._quicksort(partition_index + 1, high)

    def _partition(self, low, high):
        # Choose the rightmost element as the pivot
        pivot = self.array[high]
        i = low - 1

        # Iterate through the array and move elements smaller than pivot to the left
        # and elements greater than pivot to the right
        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        # Move the pivot element to its correct position
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]

        # Return the index of the pivot element
        return i + 1

    def display(self):
        print(self.array)

# Example usage:
arr = [64, 25, 12, 22, 11]
sorter = QuickSort(arr)

print("Original array:")
sorter.display()

sorter.sort()

print("Sorted array:")
sorter.display()
