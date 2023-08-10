/*
  Divide & Conquer Exercises
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

describe("#findRotationPivot", function () {
  it("returns the correct index", function () {
    expect(findRotationPivot([3, 4, 1, 2])).toBe(1);
    expect(findRotationPivot([6, 7, 8, 9, 1, 2, 3, 4])).toBe(3);
    expect(findRotationPivot([6, 7, 8, 9, 10, 1, 2, 3, 4])).toBe(4);
    expect(findRotationPivot([37, 44, 66, 102, 10, 22])).toBe(3);
    expect(findRotationPivot([6, 7, 8, 9, 1, 2, 3, 4])).toBe(3);
    expect(findRotationPivot([5, 6, 7, 8, 9, 10, 1, 2, 3, 4])).toBe(5);
    expect(findRotationPivot([9, 1])).toBe(0);
    expect(findRotationPivot([1, 9])).toBe(-1);
    expect(findRotationPivot([1])).toBe(-1);
    expect(findRotationPivot([])).toBe(-1);
    expect(findRotationPivot([1, 2, 3])).toBe(-1);
    expect(findRotationPivot([1, 2, 3, 0])).toBe(2);
    expect(findRotationPivot([3, 0, 1, 2, 3])).toBe(0);
  });
});

describe("#findRotatedIndex", function () {
  it("returns the correct index", function () {
    expect(findRotatedIndex([3, 4, 1, 2], 4)).toBe(1);
    expect(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8)).toBe(2);
    expect(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)).toBe(6);
    expect(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)).toBe(-1);
    expect(findRotatedIndex([37, 44, 66, 102, 10, 22], 14)).toBe(-1);
    expect(findRotatedIndex([37, 44, 66, 102, 10, 22], 37)).toBe(0);
    expect(findRotatedIndex([37, 44, 66, 102, 10, 22], 44)).toBe(1);
    expect(findRotatedIndex([37, 44, 66, 102, 10, 22], 66)).toBe(2);
    expect(findRotatedIndex([37, 44, 66, 102, 10, 22], 102)).toBe(3);
    expect(findRotatedIndex([37, 44, 66, 102, 10, 22], 10)).toBe(4);
    expect(findRotatedIndex([37, 44, 66, 102, 10, 22], 22)).toBe(5);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)).toBe(0);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 7)).toBe(1);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 8)).toBe(2);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 9)).toBe(3);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 10)).toBe(4);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)).toBe(5);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 2)).toBe(6);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 3)).toBe(7);
    expect(findRotatedIndex([6, 7, 8, 9, 10, 1, 2, 3, 4], 4)).toBe(8);
    expect(findRotatedIndex([1, 2, 0], 1)).toBe(0);
    expect(findRotatedIndex([1, 2, 0], 2)).toBe(1);
    expect(findRotatedIndex([1, 2, 0], 0)).toBe(2);
    expect(findRotatedIndex([9, 1], 9)).toBe(0);
    expect(findRotatedIndex([9, 1], 1)).toBe(1);
    expect(findRotatedIndex([1, 9], 1)).toBe(0);
    expect(findRotatedIndex([1, 9], 9)).toBe(1);
    expect(findRotatedIndex([1], 1)).toBe(0);
    expect(findRotatedIndex([1], 3)).toBe(-1);
    expect(findRotatedIndex([], 1)).toBe(-1);
  });
});
