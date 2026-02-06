
import task1


def test1():
  assert task1.sum(11,2.5) == 13.5

def test2():
  assert task1.sum(8,-2) == 6
  
if __name__ == "__main__":
  test1()
  test2()


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
