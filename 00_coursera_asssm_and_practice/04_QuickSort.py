def quick_sort(array, partition_func, count_comparisons=False):
    """
    This function sorts an array using quicksort algorithm with
    a partition functions provided as argument.

    Args:
        * array: array to be sorted
        * partition_func: partition function to be used
        * count_comparisons: whether to count comparisons or not

    Return:
        * If count_comparisons is False, return sorted array
        * If count_comparisons is True, return a tuple of
        sorted array and number of comparisons
    """
    ...


def partition_first(array, start, end):
    """
    This function partitions an array around the first element.

    Args:
        * array: array to be partitioned
        * start: starting index of the array
        * end: ending index of the array

    Return:
        * index of the pivot element
    """
    ...


def partition_last(array, start, end):
    """
    This function partitions an array around the last element.

    Args:
        * array: array to be partitioned
        * start: starting index of the array
        * end: ending index of the array

    Return:
        * index of the pivot element
    """
    ...


def partition_median_of_three(array, start, end):
    """
    This function partitions an array around the median of
    the first, middle and last element.

    Args:
        * array: array to be partitioned
        * start: starting index of the array
        * end: ending index of the array

    Return:
        * index of the pivot element
    """
    ...


def partition_random(array, start, end):
    """
    This function partitions an array around a random element.

    Args:
        * array: array to be partitioned
        * start: starting index of the array
        * end: ending index of the array

    Return:
        * index of the pivot element
    """
    ...


def main():
    """
    This function runs the main program.
    """
    ...


if __name__ == "__main__":
    main()
