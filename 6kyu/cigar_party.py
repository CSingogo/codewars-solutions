#cigar party

"""


When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True

"""

#solution

def cigar_party(cigars, is_weekend):
  
  if cigars >= 40 and cigars <= 60 and not is_weekend:
    return True
  elif cigars >= 40 and is_weekend:
    return True
  else:
    return False
