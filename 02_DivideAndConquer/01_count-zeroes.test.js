/*
  Divide & Conquer Exercise
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

// const countZeroes = require("./01_count-zeroes");

describe("#countZeroes", function () {
  it("counts the number of zeroes", function () {
    expect(countZeroes([1, 1, 1, 1, 0, 0])).toBe(2);
    expect(countZeroes([1, 0, 0, 0, 0])).toBe(4);
    expect(countZeroes([0, 0, 0])).toBe(3);
    expect(countZeroes([1, 1, 1, 1])).toBe(0);
  });
});
