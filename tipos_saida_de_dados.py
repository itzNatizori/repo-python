num1 =input("digite um numero: ")
print(type(num1))

# teste
num2 =int(input("Digite outro numero: "))
print(type(num2))
 #tipos de saidas diferentes

 #desafio extra;
n1 =int(input("Digite um número: "))
n2 =int(input("Digite outro número: "))
result = n1 + n2
print("A soma entre, {} e {} É IGUAL A: {}".format(n1, n2, result))

# bool e float conversão
n =bool(input("Digite um valor: ")) # se nada for digitado, ele retorna o valor "false", caso contrario, "true".
print(n)

m =float(input("Converter valor, digite um número: ")) # retornara um número com ponto flutuante
print(m)

#-------- é numerico? teste ----------
numb =input("Digite algo: ")
print(numb.isnumeric())

#-------- são letras? teste ----------
test =input("Digite: ")
print(numb.isalpha())

#-------- é alfa numerico? teste ----------
test =input("Digite alf: ")
print(test.isalnum())

