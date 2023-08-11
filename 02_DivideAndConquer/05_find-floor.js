/*
  Divide & Conquer Exercises
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

function findFloor(array, target, start = 0, end = array.length - 1) {
  // Base cases:
  // 1. No floor if array is empty or target smaller than the array's min.
  if (array.length === 0 || target < array[start]) {
    return -1;
    // 2. Instead, if the partition is of size 1,
    //    then the floor is the first element
  } else if (start === end) {
    return array[start];
  }

  // Main case:
  let middleIndex = Math.floor((start + end) / 2);
  let middle = array[middleIndex];
  let rightNeighbor = array[middleIndex + 1];

  // There are two options  :
  // 1. We found the floor and is the middle:
  if (target === middle || (target > middle && target < rightNeighbor)) {
    return middle;
    // 2. We execute the recursive call to find the floor:
    // 2.1 To the left half of the partition:
  } else if (target > middle) {
    return findFloor(array, target, middleIndex + 1, end);
    // 2.2 Or to the right half of the partition:
  } else if (target < middle) {
    return findFloor(array, target, start, middleIndex - 1);
  }
}
