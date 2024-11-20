using System.Collections.Generic;
using System.Linq;

public class Fixer
{
  public static List<int> PipeFix(List<int> numbers)
  {
    List<int> result = new List<int>();
    
    for(int c = numbers.First(); c <= numbers.Last(); c++)
      {
        result.Add(c);
      }
    return result;
  }
}