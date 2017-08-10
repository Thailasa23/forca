import random
#faz com que importa a boblioteca padrão do python 

palavras = []
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def inserir():
    while True:
        x = input('Escreve uma palavra?')
        palavras.append(x)
        if x == '':
            break


#A instrução def é ultilizada em Pyton para criar funções.Você pode ver que ao utilizar uma linguagem de programação existem nas bibliotecas diversas funções pré-definidas que irão realizar determinadas açõesde acordo como o programador a criou, mas você pode criar suas próprias funções.  

def principal():
    """
    Função Princial do programa
    """
    print('F O R C A')
    inserir()

#A função print() é utilizada para o programa exibir mensagens,tudo que você colocar em print vai aparecer.Se você colocar um   print()  que recebeu dois valores separados por vírgula,uma string (entre aspas) e um nome de uma variável, o string é impresso diretamente (pois esse é o seu valor) e, ao invés de imprimir o nome da variável soma, o print() exibe o valor ao qual a variável soma se refere, ou, dito mais simplesmente, o valor da variável soma. e


    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)
    
# o while True é usado como uma condição, ele fica repetindo enquento a condição for verdadeira. Um 'while (true)' fica repetindo para sempre, pois a sua condição é a constante lógica true. 

    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!! ┌( ಠ_ಠ)┘ ')
            break            

#A instrução if  é chamada de condição. Se ela é verdadeira (true), então a instrução endentada é executada. Se não, nada acontece.


#A instrução break finaliza a iteração, e o Script continua a execução normalmente, se a expressão for igual a True, será impresso uma mensagem no console e a instrução break executada, o que ocasionará, na interrupção da execução do laço de repetição while.(Parar o loop)


#Uma variável global é aquela que não foi definida dentro do escopo da função que a está utilizando.Você pode declarar um valor para a variável global dentro da função. Isto faz com que o valor desta variável assuma o valor escrito dentro da função, deste ponto em diante dentro do código. 


#A estrutura else por sua vez, é uma instrução complementar da estrutura if. A palavra else do Inglês, significa SENÃO e com esta, definiremos o bloco de instrução a ser executado todas as vezes que a expressão definida for igual a falso.

        
def perdeuJogo():
    global FORCAIMG
    if len(letrasErradas) == len(FORCAIMG):
        return True
    else:
        return False
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou        
        
#O return, como o nome diz, retorna um valor em memória, é uma resposta a um chamado anteriormente feito no programa a uma função que vai responder com o return, ou também pode ser a resposta de um "programa" ao chamado de outro "programa".

# O for vai gerar um loop dentro da lista

# O operador in verifica se o operando a sua esquerda, está contido na lista a sua direita.A palavra in, do Inglês, significa, "contido em".

# O operador not verifica o contrário , que significa não. 

# True significa verdadeiro.

# False significa falso 

# A função len() retorna um valor do tipo inteiro, representando a quantidade quantidade de caracteres contido na string.

def receberPalpite():

# Um programa pode utilizar a função input() para receber os dados ou valores que um usuário fornece através do teclado.O valor que o usuário fornece e que será retornada pelo input() é sempre um string e não um número.

# O elif é uma mistura de if com else. Ele é um else, logo só é executado se o if não ocorrer, só que além de else ele também é um if, então pro bloco elif ser executado além do primeiro if não ser executado, deve-se atender a uma determinada condição.

# O or significa (ou)

    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     
#O in significa em 
def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()
