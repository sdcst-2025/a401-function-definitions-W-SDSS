#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""
import math

def hypotenuse(numbers):
    isinstance(numbers, list)
    while True:
      min == min(numbers)
      middle = max(numbers)
      hypo = math.sqrt(min**2+middle**2)
      print(f"the hypotenuse is {hypo}")
    else:
       largest = max(numbers)
       #amarino number no **2
       side = largest**2-
       print(f"the side is {side}")

if __name__ == "__main__":
    assert hypotenuse([3,4],True) == 5
    assert hypotenuse([5,12],True) == 13
    assert hypotenuse([3,5],False) == 4
    assert hypotenuse([13,12],False) == 5