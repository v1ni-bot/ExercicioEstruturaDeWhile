# -*- coding: utf-8 -*-
"""23.02.2024.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WX4VTkg-177Jqopt9UGpiQPqXe2XgvJ4

FOR
"""

N = int(input("Informe um numero: "))
neg = -1
pos = 1
for i in range(N):
  resultado = pos * (N - i)
  pos *= neg
  print(resultado)

"""WHILE"""

N = int(input("Informe um numero: "))
neg = -1
pos = 1
i = 0
while i < N:
  i += 1
  resultado = pos * (N - i)
  pos *= neg
  print(resultado)