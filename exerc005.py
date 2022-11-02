# bool e float conversão
n =bool(input("Digite um valor: ")) # se nada for digitado, ele retorna o valor "false", caso contrario, "true".
print(n)

m =float(input("Converter valor, digite um número: ")) # retornara um número com ponto flutuante
print(m)

#-------- é numerico? teste ----------
numb =input("Digite algo: ")
print(numb.isnumeric())
print(type(numb))
#-------- são letras? teste ----------
test =input("Digite: ")
print(numb.isalpha())
print(type(test))
#-------- é alfa numerico? teste ----------
test2 =input("Digite alf: ")
print(test2.isalnum())
print(type(test2))

