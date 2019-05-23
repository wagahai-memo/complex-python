# coding: utf-8


class Complex:
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary

  def __str__(self):
    return str(self.real) + "+" + str(self.imaginary) + "i"

#--- end of class Complex ---


if __name__ == '__main__':
  x = Complex(1, 2)
  print(x)
