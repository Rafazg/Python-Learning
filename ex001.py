# Faça um programa que leia um numero inteiro e mostra o seu sucessor e antecesor

num = int(input('Digite um número inteiro: '))
print('O antecessor de {} é {} e o sucessor é {}.'.format(num, num-1, num+1))

#Crie um algortimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número inteiro: '))
print('O dobro de {} é {} e o triplo é {} e a raiz quadrada é {:.2f}.'.format(num, num*2, num*3, num**(1/2)))

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média é {:.1f}.'.format(media))


