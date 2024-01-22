'''

Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

'''

## solution

def bmi(weight, height):
    result = weight / (height ** 2)
    
    if result <= 18.5:
        return 'Underweight'
    elif result <= 25.0:
        return 'Normal'
    elif result <= 30:
        return 'Overweight'
    elif result > 30:
        return 'Obese'