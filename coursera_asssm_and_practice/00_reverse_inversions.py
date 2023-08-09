def sort_count_revinvs(nums, start=0, end=None):
    """
    Function to count reverse inversions and sort the list of numbers.
    Recursive function, uses divide-and-conquer strategy similar to MergeSort.

    Parameters:
    nums (list): the list of numbers
    start (int): the starting index of the sublist (included), default is 0
    end (int): the ending index of the sublist (excluded), default is None,
               in which case it will be set to len(nums).

    Returns:
    sorted_nums (list): a list of numbers sorted in ascending order
    total_revinvs (int): the total number of reverse inversions in the
    original list.

    DocTests:

        >>> sort_count_revinvs([1, 2, 3])[1]
        3

        >>> sort_count_revinvs([6, 1, 2, 7])[1]
        4

        >>> sort_count_revinvs([5, 4, 3, 2, 1])[1]
        0

        >>> sort_count_revinvs([])[1]
        0

        >>> sort_count_revinvs(
        ...     [28, 8, 44, 17, 9, 31, 60, 101, 82, 2]
        ... )[1]
        28

        >>> sort_count_revinvs(
        ...     [258, 478, 342, 236, 70, 264, 316, 168, 91, 200]
        ... )[1]
        14

        >>> sort_count_revinvs([24, 46, 8, 4])[1]
        1

        >>> sort_count_revinvs([10, 16, 46, 11, 17, 49, 35])[1]
        16

        >>> sort_count_revinvs(
        ...     [129, 169, 315, 349, 355, 33, 85, 362, 230, 499]
        ... )[1]
        31

        >>> sort_count_revinvs(
        ...     [470, 461, 263, 200, 476, 365, 276, 104, 85, 357]
        ... )[1]
        13

        >>> sort_count_revinvs(
        ...    [
        ...        285, 531, 634, 46, 458, 897, 696, 459, 380, 343, 284, 596,
        ...        45, 597, 143, 331, 716, 314, 341, 784
        ...        ]
        ... )[1]
        93

        >>> sort_count_revinvs([188, 819, 466, 493, 641])[1]
        7
    """

    if end is None:
        end = len(nums)

    # Base case, if the list is of length 0 or 1, return as it is.
    if end - start < 2:
        return nums[start:end], 0

    # Calculate the middle index for dividing the list.
    pivot = (end - start) // 2

    # Recursive calls for each half of the list.
    nums_half1, notinv_half1 = sort_count_revinvs(nums, start, start + pivot)
    nums_half2, notinv_half2 = sort_count_revinvs(nums, start + pivot, end)

    # Merge the two sorted halves and count the split reverse inversions.
    sorted_nums, split_revinvs = merge_count_splits_revinvs(
        nums_half1, nums_half2)

    # The total reverse inversions is the sum of the reverse inversions
    # from each half and the split reverse inversions from the merge.
    total_revinvs = notinv_half1 + notinv_half2 + split_revinvs

    return sorted_nums, total_revinvs


def merge_count_splits_revinvs(nums_half1, nums_half2):
    """
    Helper function to merge two sorted lists and count the reverse inversions
    between them.

    Parameters:
    nums_half1 (list): the first sorted list of numbers
    nums_half2 (list): the second sorted list of numbers

    Returns:
    sorted_nums (list): a merged list of numbers sorted in ascending order
    split_revinvs (int): the number of reverse inversions between nums_half1
                         and nums_half2
    """

    split_revinvs = 0  # initialize count of split reverse inversions.

    # Iitialize the sorted list with None
    sorted_nums = [None] * (len(nums_half1) + len(nums_half2))

    # Initialize indices for nums_half1, nums_half2, and sorted_nums.
    i = len(nums_half1) - 1
    j = len(nums_half2) - 1
    k = len(sorted_nums) - 1

    # While there are elements to compare in either half.
    while k >= 0:
        # If the current element in nums_half1 is greater
        # than or equal to the current element in nums_half2.
        if i >= 0 and (j < 0 or nums_half1[i] >= nums_half2[j]):
            # Place it in the sorted list and move to the next element
            # in nums_half1.
            sorted_nums[k] = nums_half1[i]
            i -= 1
        else:
            # Otherwise, place the current element from nums_half2
            # on the sorted list and increase the count of split reverse
            # inversions by the number of elements remaining in nums_half1.
            sorted_nums[k] = nums_half2[j]
            # i + 1 represents the number of elements remaining in nums_half1.
            split_revinvs += i + 1
            j -= 1
        k -= 1  # Move to the next position in the sorted list.

    return sorted_nums, split_revinvs
