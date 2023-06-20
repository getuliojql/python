x = float(input('Digite a largura da parede: '))
y = float(input('Digite a altura da parede: '))
print('Uma parede de {}m X {}m tem {}m² de área. Logo, serão necessários {:.3f}l ' ''
      'de tinta para pintá-la.'.format(x, y, x*y, x*y/2))
