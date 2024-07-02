// Given an array of integers, return a new array with each value doubled.

// For example:

// [1, 2, 3] --> [2, 4, 6]

export function maps(x: number[]): number[]{
    let finalArray: number []= [] ;
    for (let y:number = 0; y < x.length ; y++ ){
      finalArray.push(x[y] * 2)
    }
    return finalArray;
  }