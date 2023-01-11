# crated by:Foxy
# for: help with math
#########################################################################
delta  =  b ** 2  -  4  *  a  *  c
x1 = (-b + delta**(1/2)) / (2 * a)
x2 = (-b - delta**(1/2)) / (2 * a)

print('Delta = ',delta)
print('x1 = ',x1)
print('x2 = ',x2)

print('Se a conta saiu etranha e por que os valores tao errados tente novamente')
#######################################################################

cat1  =  float ( input ( 'Escreva o cateto adjacente ' ))
cat2  =  float ( input ( 'Escreva o cateto oposto ' ))

hpt = cat1**2 + cat2**2
ptint('O quadrado da hipotenuza vale: ', hpt)
