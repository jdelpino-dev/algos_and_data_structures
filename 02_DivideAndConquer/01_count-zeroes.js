/*
  Divide & Conquer Exercise
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

/** Count Zeroes using Binary Search
 * @param {number[]} array // sorted array of 1s followed by 0s
 * @return {number} // number of zeroes in array
 *
 * Given an array of 1s and 0s which has all 1s first followed by all 0s,
 * this fucntion returns the number of zeroes in the array, using
 * binary search. Time Complexity: O(log n).
 */
function countZeroes(array) {
  let firstZero = findBoundary(array, 0, array.length - 1);
  if (firstZero === -1) {
    return 0;
  }
  return array.length - firstZero;
}

/** Find boundary iteratively using modified binary search.
 * This is a helper function for countZeroes.
 *
 * @param {number[]} array // sorted array of 1s followed by 0s
 * @param {number} start
 */
function findBoundary(array, start, end) {
  while (start <= end) {
    let middle = Math.floor((start + end) / 2);

    // If middle is zero, we have three cases:
    if (array[middle] === 0) {
      // 1. Middle is the first element of the array, so it's the first zero.
      // 2. The element before middle is a one, which means middle is the first zero.
      if (middle === 0 || array[middle - 1] === 1) {
        return middle;
        // 3. Middle is not the first zero, so the boundary is towards the left.
      } else {
        end = middle - 1;
      }
      // If middle is one, we have two cases:
    } else {
      // 1. If the element after middle is one, our boundary is towards the right.
      if (array[middle + 1] === 1) {
        start = middle + 2;
        // 2. If the element after middle is zero, that's the first zero.
      } else {
        return middle + 1;
      }
    }
  }
  return -1; // this is a fallback for debugging
}
