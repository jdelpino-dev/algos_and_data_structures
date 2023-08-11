from random import randint


def count_invs_and_sort(nums, start=0, end=None):
    """
    Function to count inversions and sort a list of numbers.
    Recursive function, uses divide-and-conquer piggybacking on MergeSort.

    Parameters:
    nums (list): the list of numbers
    start (int): the starting index of the sublist (included), default is 0
    end (int): the ending index of the sublist (excluded), default is None,
               in which case it will be set to len(nums).

    Returns:
    sorted_nums (list): a list of numbers sorted in ascending order
    total_revinvs (int): the total number of inversions in the
    original list.

    DocTests:

        >>> count_invs_and_sort([1, 2, 3])[1]
        0

        >>> count_invs_and_sort([6, 1, 2, 7])[1]
        2

        >>> count_invs_and_sort([5, 4, 3, 2, 1])[1]
        10

        >>> count_invs_and_sort([])[1]
        0

        >>> count_invs_and_sort(
        ...     [28, 8, 44, 17, 9, 31, 60, 101, 82, 2]
        ... )[1]
        17

        >>> count_invs_and_sort(
        ...     [258, 478, 342, 236, 70, 264, 316, 168, 91, 200]
        ... )[1]
        31

        >>> count_invs_and_sort([24, 46, 8, 4])[1]
        5

        >>> count_invs_and_sort([10, 16, 46, 11, 17, 49, 35])[1]
        5

        >>> count_invs_and_sort(
        ...     [129, 169, 315, 349, 355, 33, 85, 362, 230, 499]
        ... )[1]
        14

        >>> count_invs_and_sort(
        ...     [470, 461, 263, 200, 476, 365, 276, 104, 85, 357]
        ... )[1]
        32

        >>> count_invs_and_sort(
        ...    [
        ...        285, 531, 634, 46, 458, 897, 696, 459, 380, 343, 284, 596,
        ...        45, 597, 143, 331, 716, 314, 341, 784
        ...        ]
        ... )[1]
        97

        >>> count_invs_and_sort([188, 819, 466, 493, 641])[1]
        3

        >>> medium_array = array_from_file("03_data/"
        ...                                "03_Medium_IntegerArray.txt")
        >>> count_invs_and_sort(medium_array)[1]
        14696

        >>> big_array = array_from_file('03_data/03_Big_IntegerArray.txt')
        >>> count_invs_and_sort(big_array)[1]
        2407905288

    """

    if end is None:
        end = len(nums)

    # Base case, if the list is of length 0 or 1, return it as it is and
    # 0 inversions.
    if end - start < 2:
        return nums[start:end], 0

    # Calculates the middle index for dividing the list.
    pivot = (end - start) // 2

    # Recursive calls for each half of the list.
    nums_half1, inv_half1 = count_invs_and_sort(nums, start, start + pivot)
    nums_half2, inv_half2 = count_invs_and_sort(nums, start + pivot, end)

    # Merge the two sorted halves and count the split inversions.
    sorted_nums, split_invs = merge_count_split_invs(
        nums_half1, nums_half2)

    # The total of inversions is the sum of the inversions
    # from each half and the split inversions from the merge.
    total_invs = inv_half1 + inv_half2 + split_invs

    return sorted_nums, total_invs


def merge_count_split_invs(nums_half1, nums_half2):
    """
    Helper function to merge two sorted lists and count the inversions
    between them.

    Parameters:
    nums_half1 (list): the first sorted list of numbers
    nums_half2 (list): the second sorted list of numbers

    Returns:
    sorted_nums (list): a merged list of numbers sorted in ascending order
    split_invs (int): the number of inversions between nums_half1
                      and nums_half2
    """

    split_revinvs = 0  # initialize count of split inversions.

    # Calculates the length of all the lists.
    length_half_1 = len(nums_half1)
    length_half_2 = len(nums_half2)
    # including the length of the bigger list.
    length = length_half_1 + length_half_2

    # Initializes the empty list for the sorted numbers.
    sorted_nums = [None] * (length)

    # Initializes the loop indexes for each list. i for nums_half1,
    # j for nums_half2 and k for the sorted list.
    i, j, k = 0, 0, 0

    # While there are elements to compare in either half.
    while k < length:
        # There is not inversions to count if there are no elements or
        # the elements are in order.
        if (
            (i < length_half_1)
            and (j >= length_half_2 or nums_half1[i] <= nums_half2[j])
        ):
            # Places the current element from nums_half1 on the sorted list
            # and moves to the next element in nums_half1.
            sorted_nums[k] = nums_half1[i]
            i += 1
        elif (
            i < length_half_1
            and j < length_half_2 and nums_half1[i] > nums_half2[j]
        ):
            # Otherwise, place the current element from nums_half2
            # on the sorted list and increase the count of split inversions
            # by the number of elements remaining in nums_half1.
            sorted_nums[k] = nums_half2[j]
            # length_half_1 - i - 1 represents the number of elements
            # remaining in nums_half1.
            split_revinvs += length_half_1 - i
            # Move to the next element in nums_half2.
            j += 1
        elif j < length_half_2:
            # If there are no elements in nums_half1 or the elements
            # are in order, place the current element from nums_half2
            # on the sorted list and move to the next element in nums_half2.
            sorted_nums[k] = nums_half2[j]
            j += 1
        k += 1  # Move to the next position in the sorted list.

    return sorted_nums, split_revinvs


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


def count_inv_naive(nums):
    """
    Function that count inversions and sort a list of numbers using a naive
    approach with complexity O(n^2).

    DocTests:

        >>> count_inv_naive([1, 2, 3])
        0

        >>> count_inv_naive([6, 1, 2, 7])
        2

        >>> count_inv_naive([5, 4, 3, 2, 1])
        10

        >>> count_inv_naive([])
        0

        >>> count_inv_naive(
        ...     [28, 8, 44, 17, 9, 31, 60, 101, 82, 2]
        ... )
        17

        >>> count_inv_naive(
        ...     [258, 478, 342, 236, 70, 264, 316, 168, 91, 200]
        ... )
        31

        >>> count_inv_naive([24, 46, 8, 4])
        5

        >>> count_inv_naive([10, 16, 46, 11, 17, 49, 35])
        5

        >>> count_inv_naive(
        ...     [129, 169, 315, 349, 355, 33, 85, 362, 230, 499]
        ... )
        14

        >>> count_inv_naive(
        ...     [470, 461, 263, 200, 476, 365, 276, 104, 85, 357]
        ... )
        32

        >>> count_inv_naive(
        ...    [
        ...        285, 531, 634, 46, 458, 897, 696, 459, 380, 343, 284, 596,
        ...        45, 597, 143, 331, 716, 314, 341, 784
        ...        ]
        ... )
        97

        >>> count_inv_naive([188, 819, 466, 493, 641])
        3
    """
    nums_length = len(nums)
    followed_by_big = 0

    i, j = 0, 0
    for i in range(0, nums_length - 1):
        for j in range(i + 1, nums_length):
            if nums[i] > nums[j]:
                followed_by_big += 1

    return followed_by_big


def random_list(min_val, max_val, length):
    return [randint(min_val, max_val) for _ in range(length)]
