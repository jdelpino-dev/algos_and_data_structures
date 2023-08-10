/*
  Divide & Conquer Exercises
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

/** Counts the number of rotations of a sorted array of integers
 *
 * @param {number[]} array // sorted & rotated array of integers
 * @return {number} // number of rotations
 *
 * Given a rotated array of sorted integers, returns the number of rotations.
 * First finds the rotation pivot using a helper function –findRotationPivot()–
 * that uses a divide and conquer approach.
 */
function findRotationCount(array) {
  let rotationPivot = findRotationPivot(array);
  return rotationPivot === -1 ? 0 : rotationPivot + 1;
}

/** Recursively searches for the rotation pivot of a rotated array of sorted
 * integers. Uses a divide and conquer approach.
 * @param {number[]} array // sorted & rotated array of integers
 * @param {number} start // start index of the search in array
 * @param {number} end // end index of the search in array
 * @return {number} // index of the rotation pivot or -1 if not found.
 *                     rotation pivot  = the last element of the
 *                                       left partition of the array.
 */
function findRotationPivot(array, start = 0, end = array.length - 1) {
  // Calculates the length of the search partition.
  let partitionLength = end - start + 1;

  // Base cases:

  // 1. If the partition has one element left or none, then return -1.
  if (partitionLength === 0 || partitionLength === 1) {
    return -1;
    // 2. If the partition has only two elements, either the first is the
    //    pivot or there is no pivot.
  } else if (partitionLength === 2) {
    return array[start] > array[start + 1] ? start : -1;
  }

  // Preparing the recursive call:
  // Calculates the middle index of the array, gets the middle element, and
  // its left and right neighbors.
  let middle = Math.floor(start + (end - start) / 2);
  let middleElem = array[middle];
  let leftNeighbor = array[middle - 1]; // undefined if middle is
  //                                       the first element of the array
  let rightNeighbor = array[middle + 1]; // undefined if middle is
  //                                        the last element of the array

  // There are 2 possible options in order to find the pivot in a partition
  // with 3 ore more elements:
  // 1. The middle element is the pivot. That's the case when it is bigger
  //    than both the element before and after it. If any of the neighbors
  //    is undefined, that won't be a problem: JS will return false
  //    for the comparison.
  if (middleElem > leftNeighbor && middleElem > rightNeighbor) {
    return middle; // We got the pivot!
  }
  // 2. A double recursive case is needed because the middle element
  //    is not the pivot and then we don't know where is it. We need to
  //    look for it in both the left and right sides. We must do 2 recursive
  //    calls, one for each side.
  else {
    // We must include the middle element in the left
    // call because if not we could miss vital information to find the pivot.
    let leftSide = findRotationPivot(array, start, middle);
    let rightSide = findRotationPivot(array, middle + 1, end);
    // We return the result of the recursive calls. If the pivot is not
    // found, then -1 will be returned.
    return leftSide !== -1 ? leftSide : rightSide;
  }
}
