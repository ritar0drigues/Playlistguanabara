import math
angulo = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
print("O angulo de {} tem o seno de {:.2f}".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print("O angulo de {} tem o cosseno de {:.2f}".format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem tangente de {:.2f}".format(angulo,tangente))

from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo: "))
seno = sin(angulo)
print("O angulo de {} tem o seno de {:.2f}".format(angulo,seno))
cosseno = cos(angulo)
print("O angulo de {} tem o cosseno de {:.2f}".format(angulo,cosseno))
tangente = tan(angulo)
print("O angulo de {} tem tangente de {:.2f}".format(angulo,tangente))
