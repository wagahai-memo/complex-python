# coding: utf-8


class Complex:
  element_type = None

  @classmethod
  def set_element_type(clazz, elem_type):
    Complex.element_type = elem_type

  @classmethod
  def _0(clazz):
    t = Complex.element_type
    if t == int:
      return Complex(0, 0)
    elif t == float:
      return Complex(0.0, 0.0)
    else:
      return Complex(t._0(), t._0())

  @classmethod
  def _1(clazz):
    t = Complex.element_type
    if t == int:
      return Complex(1, 0)
    elif t == float:
      return Complex(1.0, 0.0)
    else:
      return Complex(t._1(), t._0())


  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary

  def __str__(self):
    return str(self.real) + "+" + str(self.imaginary) + "i"

#--- end of class Complex ---


if __name__ == '__main__':
  Complex.set_element_type(float)
  print(Complex._0())
  print(Complex._1())
  x = Complex(1.0, 2.0)
  print(x)
