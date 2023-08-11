/*
  Divide & Conquer Exercises
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

function findFloor(array, target, start = 0, end = array.length - 1) {
  // Base case
  // If array is empty or target is less than the first element,
  // there is no floor.
  if (array.length === 0 || target < array[start]) {
    return -1;
  } else if (start === end) {
    // If the partition is of size 1, then the floor is the first element
    return array[start];
  }

  // Preparing the recursive case
  // Calculates the middle index of the partition
  let middleIndex = Math.floor((start + end) / 2);
  // And gets the middle element of the partition
  let middle = array[middleIndex];
  let rightNeighbor = array[middleIndex + 1];

  // There are three possible cases for the floor:
  // 1. The floor is middle, either because it is the target or because
  //    it is the last element before the target
  if (target === middle || (target > middle && target < rightNeighbor)) {
    return middle;
    // 2 Recursive case
    // 2.1 It is in the left half of the partition
  } else if (target > middle) {
    return findFloor(array, target, middleIndex + 1, end);
    // 2.3 It is in the right half of the partition
  } else if (target < middle) {
    return findFloor(array, target, start, middleIndex - 1);
  }
}
