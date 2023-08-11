from typing import Callable
from statistics import median
from random import randint


def quick_sort(
    array: list, start: int, end: int,
    choose_pivot: Callable[[list, int, int], int],
    count_comparisons=False
) -> None:
    """
    This function sorts an array using quicksort algorithm
    and a variable method for choosing the pivot.

    Args:
        * array: array to be sorted
        * choose_pivot_func: method for choosing the pivot
        * count_comparisons: whether to count comparisons or not

    Return:
        * If count_comparisons is False, return sorted array
        * If count_comparisons is True, return a tuple of
        sorted array and number of comparisons
    """
    pivot = choose_pivot(array, start, end)
    # Moves the pivot to the beggining of the partition
    swap(start, pivot)


def partition(array: list, start: int, end: int) -> None:
    """
    This function partitions an array around the first element.

    Args:
        * array: array to be partitioned
        * start: starting index of the array
        * end: ending index of the array

    Return:
        * index of the pivot element
    """

    # The boundary is the first element bigger than pivot.
    pivot = start
    partition_boundary = pivot + 1

    for current in range(start + 1, end + 1):
        if array[next] < pivot:  # else do nothing
            swap(partition_boundary, current)
            # Restores partition invariant arounf pivot
            partition_boundary = + 1
        # Places the pivot in the right place with a swap.
        swap(pivot, partition_boundary - 1)


def swap(array: list, element1: int, element2: int):
    """
    This function swaps two elements in an array.

    Arguments:
        * array: array
        * element1: index of the first element
        * element2: index of the second element
    """
    array[element1], array[element2] = array[element2], array[element1]


def pivot_first(array: list, start: int, end: int) -> int:
    """
    This function partitions an array around the first element.
    """
    return 0


def pivot_last(array: list, start: int, end: int) -> int:
    """
    This function partitions an array around the last element.

    """
    return len(array)


def pivot_median_of_three(array: list, start: int, end: int) -> int:
    """
    This function partitions an array around the median of
    the first, middle and last element.
    """
    first = array[start]
    last = array[len(array)]

    middle_index = (end - start // 2) + start
    middle = array[middle_index]

    return median(first, middle, last)


def pivot_random(array: list, start: int, end: int) -> int:
    """
    This function partitions an array around a random element.
    """
    return randint(0, len(array))


def array_from_file(filename):
    """
    Helper function to create an array of integers from a text file.

    Parameters:
    filename (str): the name of the file containing the array of integers

    Returns:
    nums (list): a list of integers
    """

    with open(filename) as file:
        nums = [int(line) for line in file]

    return nums


def main():
    """
    This function runs the main program.
    """
    ...


if __name__ == "__main__":
    main()
