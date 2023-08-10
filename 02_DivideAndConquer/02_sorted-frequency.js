/*
  Divide & Conquer Exercises
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

/** Sorted frequency using Binary Search
 * @param {number[]} array // sorted array of numbers
 * @param {number} target // number to search for
 * @return {number} // number of times the target appears in the array
 *
 * Given a sorted array and a number, write a function called sortedFrequency
 * that counts the occurrences of the number in the array using
 * binary search. Time Complexity: O(log n).
 */
function sortedFrequency(array, target) {
  // Finds the index of one instance of target using binary search.
  let firstFound = binarySearch(array, target);

  // If target is not found, returns 0 (edge case)
  if (firstFound === -1) {
    return -1;
  }

  // Calculates the array's length.
  let length = array.length;
  // Finds the boundaries of target's block of instances using a modified form
  // of binary search.
  // 1. Finds the first instance of target a modified form of binary search.
  let first = findExtreme(array, target, "first", 0, firstFound - 1);
  // 2. Finds the last instance of target a modified form of binary search.
  let last = findExtreme(array, target, "last", firstFound, length - 1);

  // Returns the number of instances of target doing a simple subtraction.
  return last - first + 1;
}

/** Recursively finds the first or last instance of target's block using
 * modified binary search. This is a helper function for sortedFrequency.
 *
 * @param {number[]} array // sorted array of numbers
 * @param {string} type // "first" or "last"
 * @param {number} start // starting index
 * @param {number} end // ending index
 */
function findExtreme(array, target, type, start, end) {
  if (start > end) {
    return type === "first" ? start : end;
  }
  let middle = Math.floor((start + end) / 2);
  let middleElem = array[middle];

  // Defines the next start and end indexes depending on the type of search
  // and the value of middleElem.
  // 1. If middleElem is equal to target, then keep searching in the right
  //    direction: if type is "first", then keep searching to the left,
  //    otherwise keep searching to the right.
  if (middleElem === target) {
    if (type === "first") {
      return findExtreme(array, target, type, start, middle - 1);
    } else {
      return findExtreme(array, target, type, middle + 1, end);
    }
    // 2. If middleElem is not equal to target when we are searching for the
    //    first instance, then keep searching to the right. If we are searching
    //    for the last instance, then keep searching to the left.
  } else if (type === "first") {
    return findExtreme(array, target, type, middle + 1, end);
  } else {
    return findExtreme(array, target, type, start, middle - 1);
  }
}

/** Binary Search
 * @param {number[]} arr // sorted array
 * @param {number} target // target to search
 * @return {number} // index of target or -1 if not found
 * Given an array of integers nums which is sorted in ascending order,
 * and an integer target, write a function to search target in nums.
 * If target exists, then return its index. Otherwise, return -1.
 */
function binarySearch(arr, target, start = 0, end = arr.length - 1) {
  if (start > end) {
    return -1;
  }

  let middle = Math.floor(start + (end - start) / 2);
  let middleElem = arr[middle];
  if (middleElem === target) {
    return middle;
  }

  if (middleElem < target) {
    return binarySearch(arr, target, middle + 1, end);
  }
  if (middleElem > target) {
    return binarySearch(arr, target, start, middle - 1);
  }
}
