/**
You need to write a function that reverses the words in a given string. Words are always separated by a single space.

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
*/

using System;

public class Kata
{
  public static string Reverse(string text)
  {
    string [] words = text.Split(" ");
    string? result = null;
    
    for (int x = words.Length - 1; x >= 0; x-- )
      {
        result = result + " " + words[x];
      }
    return result.Trim();
  }
}