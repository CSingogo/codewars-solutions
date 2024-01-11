/*

* Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

*/

/**
 * solution
 */

const removeExclamationMarks = (str) =>{
  
    arr = str.split('');
    arr2 = arr.filter((s) => s !=='!');
    str2 = arr2.join('');
    
    return str2;
  } 