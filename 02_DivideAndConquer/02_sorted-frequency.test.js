/*
  Divide & Conquer Exercises
  Unit 19 of Springboard SWE Bootcamp
   
  Solution by José Delpino
*/

describe("#sortedFrequency", function () {
  it("returns the frequency", function () {
    expect(sortedFrequency([1, 2, 3, 4, 4, 6, 7, 8], 4)).toBe(2);
    expect(sortedFrequency([1, 2, 3, 4, 4, 6, 7, 8], 3)).toBe(1);
    expect(sortedFrequency([1, 2, 3, 4, 4, 6, 7, 8], 6)).toBe(1);
    expect(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 2)).toBe(4);
    expect(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 3)).toBe(1);
    expect(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 1)).toBe(2);
    expect(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 4)).toBe(-1);
    expect(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 0)).toBe(-1);
    expect(sortedFrequency([1, 1, 2, 2, 2, 3, 3], 3)).toBe(2);
    expect(
      sortedFrequency(
        [
          45, 46, 143, 284, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285,
          285, 285, 285, 314, 331, 341, 343, 380, 458, 459, 531, 596, 597, 634,
          696, 716, 784, 897,
        ],
        285
      )
    ).toBe(13);
    expect(
      sortedFrequency(
        [
          45, 45, 45, 45, 45, 45, 46, 143, 284, 285, 314, 331, 341, 343, 380,
          458, 459, 531, 596, 597, 634, 696, 716, 784, 897,
        ],
        45
      )
    ).toBe(6);
    expect(
      sortedFrequency(
        [
          45, 45, 45, 45, 45, 45, 46, 143, 284, 285, 314, 331, 341, 343, 380,
          458, 459, 531, 596, 597, 634, 696, 716, 784, 897,
        ],
        143
      )
    ).toBe(1);
    expect(
      sortedFrequency(
        [
          45, 46, 143, 284, 285, 314, 331, 341, 343, 380, 458, 459, 531, 596,
          597, 634, 696, 716, 784, 897, 897, 897, 897, 897, 897, 897, 897, 897,
          897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897,
        ],
        897
      )
    ).toBe(21);
    expect(
      sortedFrequency(
        [
          45, 46, 143, 284, 285, 314, 331, 341, 343, 380, 458, 458, 458, 458,
          459, 531, 596, 597, 634, 696, 716, 784, 897,
        ],
        458
      )
    ).toBe(4);
    expect(
      sortedFrequency(
        [
          45, 46, 143, 284, 285, 314, 331, 341, 343, 380, 458, 459, 531, 531,
          531, 531, 531, 531, 531, 531, 596, 597, 634, 696, 716, 784, 897,
        ],
        531
      )
    ).toBe(8);
  });
});
