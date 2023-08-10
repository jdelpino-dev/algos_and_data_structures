/*
  Divide & Conquer Exercises
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

function findFloor(array, target, start = 0, end = array.length - 1) {
  // Calculates the partition length
  let partitionLength = end - start + 1;

  // Gets first and last elements of the array
  let first = array[start];
  let last = array[end];

  // Base cases
  // 1. If array is empty or target is less than first element,
  // there is no floor: returns -1.
  if (partitionLength === 0 || target < first) {
    return -1;
    // 2. If target is equal to first element, the floor trivially
    // the target itself.
  } else if (target === first) {
    return target;
  } else if (target >= last) {
    // 3. If target is greater than or equal to last element, the floor
    // is the last element or the target itself.
    return last;
  }

  // Preparing the recursive case: target's floor is between first and last elements of the
  // array partition. We need to find the middle element of the partition.

  // Updates the start and end indexes of the partition
  // to narrow down the search.
  start++;
  end--;

  // Calculates the middle index of the partition
  let middleIndex = Math.floor((start + end) / 2);
  // And gets the middle element of the partition
  let middle = array[middleIndex];

  // There are three possible cases for the floor:
  // 1. It is the target itself and/or the middle element of the partition
  if (target >= middle && target < array[middleIndex + 1]) {
    return middle;
    // 2. It is in the in the left half of the partition
  } else if (target > middle) {
    return findFloor(array, target, middleIndex + 1, end);
    // 3. It is in the right half of the partition
  } else if (target < middle) {
    return findFloor(array, target, start, middleIndex - 1);
  }
}
