using System.Collections.Generic;
using System.Linq; 
public class Kata
{
  public static string[] AddLength(string str)
  {
    string[] strArr = str.Split(" ");
    List<string> strList = strArr.ToList();
    int strCount = strList.Count;
    List<string> result = new List<string>();
    
    for (int x = 0; x < strCount; x++){
      result.Add($"{strList[x]} {strList[x].Length}");
    }
    
    return result.ToArray();
  }
}
