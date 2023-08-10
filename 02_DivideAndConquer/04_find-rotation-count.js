/*
  Divide & Conquer Exercises
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

/** Recursively counts the number of rotations of a sorted array of integers
 * that was rotated an unknown number of times. Uses a divide and conquer
 * approach.
 *
 * @param {number[]} array // sorted & rotated array of integers
 * @return {number} // number of rotations
 *
 */
function findRotationCount(array, start = 0, end = array.length - 1) {
  // Calculates the length of the search partition.
  let partitionLength = end - start + 1;

  // Base cases:

  // 1. If the partition has one element left or none, then there are no
  //    rotations.
  if (partitionLength === 0 || partitionLength === 1) {
    return 0;
    // 2. If the partition has only two elements, checks if there is a rotation
    //    and returns the result.
  } else if (partitionLength === 2) {
    return array[start] > array[start + 1] ? start : -1;
  }

  // Preparing the recursive call:

  // Initialize the counter of rotations.
  let rotationCounter = 0;

  // Calculates the middle index of the array, gets the middle element, and
  // its left and right neighbors.
  let middle = Math.floor(start + (end - start) / 2);
  let middleElem = array[middle];
  let leftNeighbor = array[middle - 1]; // undefined if middle is
  //                                       the first element of the array
  let rightNeighbor = array[middle + 1]; // undefined if middle is
  //                                        the last element of the array

  // If we found a rotation, we add it to the counter. We found a rotation
  // if the middle element is bigger than both the element before
  //    and after it. If any of the neighbors is undefined,
  //    that won't be a problem: JS will return false for the comparison.
  if (middleElem > leftNeighbor && middleElem > rightNeighbor) {
    rotationCounter++; // We add 1 to the counter because we found a rotation.
  }

  // We need to do double recursive call to calculate the number of rotations
  // in the left and right sides of the array.
  let leftSide = findRotationPivot(array, start, middle);
  let rightSide = findRotationPivot(array, middle + 1, end);
}
