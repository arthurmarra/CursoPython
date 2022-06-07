import math

an = float(input('Digite um angulo: '))

seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))

print('O seno do ângulo vale {:.2f}\nO cosseno do ângulo vale {:.2f}\nA tangente do ângulo vale {:.2f}'.format(seno, cos, tg))