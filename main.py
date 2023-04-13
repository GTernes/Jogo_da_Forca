import random


def main():
    palavras = []
    with open('palavras.txt', 'r', encoding='utf-8') as f:
        linhas = f.read()
        lista = linhas.split(', ')
        for each in lista:
            palavras.append(each)
    print("Bem Vindo ao Jogo da Forca!!")
    input("Pressione ENTER para iniciar!")
    palavra = selecionarPalavra(palavras)
    espacos = criarDiagrama(palavra)
    print(f"A palavra é {espacos}")
    global flag
    flag = True
    loop(flag, palavra, espacos)

def selecionarPalavra(palavras):
    x = random.choice(palavras)
    return x

def criarDiagrama(palavra):
    diagrama = '_ ' * len(palavra)
    return diagrama

def guess():
    flag = True
    while(flag):
        x = input("\nDigite uma letra: ").lower()
        if len(x) < 1:
            print("Por favor insira uma letra!")
        elif len(x) != 1:
            print("\nApenas um dígito é permitido\n")
        elif x == int:
            print("\nApenas letras são permitidas")
        elif x in guesses:
            print("\nEssa letra já foi utilizada")    
        else:
            return x

def verificarLetra(letra, palavra):
    if letra in palavra:
        print(f"\nVocê acertou a letra '{letra.upper()}' e ela aparece {palavra.count(letra)} vez(es)!")
        return findAll(letra, palavra)
    else:
        print(f"\nA letra '{letra.upper()}' não existe na palavra!!\n")
    
def findAll(letra, palavra):
    index = []
    a = 0
    for each in palavra:
        indexLetra = palavra.index(each, a)
        a+= 1
        if letra == each:
            index.append(indexLetra)
    return index

def substituirDiagrama(index, letra, diagrama):
    dg = diagrama
    for each in index:
        valor = int(each * 2)
        dg = dg[:valor] + f'{letra} ' + dg[valor+2:]
    print(dg)
    return dg

def verificarVitoria(espacos):
    if not '_' in espacos:
        print('\nparabéns, você ganhou')
        return False
    else:
        return True

def loop(controlador, palavra, espacos):
    flag = controlador
    a = 0
    global guesses
    guesses = ''
    while flag:
        char = guess() 
        if not char in guesses:
            guesses += f'{char}, '
        index = verificarLetra(char, palavra)
        
        if char in palavra:
            espacos = substituirDiagrama(index, char, espacos).strip()
            print(f'\nLetras já utilizadas: {guesses.upper()}')
            flag = verificarVitoria(espacos)
        else:
            a += 1
            verificaErros(a)
            print(f'\nLetras já utilizadas: {guesses.upper()}')
            if a==6:
                print(f'A palavra era "{palavra.upper()}"')
                return
        

    if flag == False:
        return

def verificaErros(a):
    match a:
        case 1:
            print('''
              O
      
            ''')
        case 2:    
            print('''
              O
              |      
            ''')
        case 3:
            print('''
              O
             /|\\
            
            ''')
        case 4:
            print('''
              O
             /|\\
             ---
            
            ''')
        case 5:
            print('''
              O
             /|\\
             ---
             / \\
            ''')
        case 6:
            print('''
              O
             /|\\
             ---
             / \\
            /   \\
            ''')

            print('O jogo acabou! Você matou o coitadinho!')

verificador = True

while verificador:
    main()
    print("=~=~=~=~=~=~=~=~=~==~=~=~=~=~=~=~=~=~=~=~=~=~=~=")
    a = input(str("\nDeseja jogar novamente? (S/N)")).lower()
    if a == "n":
        verificador = False
    print("\n=~=~=~=~=~=~=~=~=~==~=~=~=~=~=~=~=~=~=~=~=~=~=~=\n")
     
