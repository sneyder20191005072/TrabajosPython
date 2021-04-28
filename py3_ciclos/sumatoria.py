def sumatoria_suma(A,B,C):
  n=leng(A)
  acumulador=0
  for i in range(n):
    d=A[i]*B[i]
    e= C[i]+d
    acumulador=acumulador +e
  resultado =acumulador+(pow(n))
  return resultado