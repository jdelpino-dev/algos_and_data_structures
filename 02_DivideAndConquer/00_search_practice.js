/** Linear Search
 * @param {number[]} arr // sorted array
 * @param {number} target // target to search
 * @return {number} // index of target or -1 if not found
 *
 * Given an array of integers nums and an integer target,
 * return the index of the target if it exists in nums.
 * Otherwise, return -1.

*/
function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) return i;
  }
  return -1;
}
/*
  Divide & Conquer Exercise
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

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
