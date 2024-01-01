// Complete the solution so that it reverses the string passed into it.

// 'world'  =>  'dlrow'
// 'word'   =>  'drow'


function solution(str) {
    // Initialize an empty array to store reversed characters
    let reverseArray = [];
    
    // Convert the input string into an array of characters
    let stringArray = str.split('');
  
    // Loop through the characters in reverse order
    for (let i = str.length - 1; i >= 0; i--) {
      // Push each character to the reverseArray
      reverseArray.push(stringArray[i]);
    }
  
    // Join the reversed characters back into a string and return
    return reverseArray.join('');
  }
  