from math import sin, cos, tan, radians
x = int(input('Digite o valor do ângulo: '))
print('O seno de {}º é igual a {:.2f}. \nO cosseno de {}º é igual a {:.2f}. \nA tangente de {}º é '
      'igual a {:.2f}'.format(x, sin(radians(x)), x, cos(radians(x)), x, tan(radians(x))))
