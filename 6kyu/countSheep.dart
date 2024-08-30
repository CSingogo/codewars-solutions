/**
 * If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


 */

String countSheep(numb) {
  // your code here
  String sheep = "";
  for (int count = 1; count <= numb; count++ ){
    sheep +="$count sheep...";
  }
  return sheep;
}