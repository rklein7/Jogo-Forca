import os
import time

def limparTela():
    os.system("clear")

def aguarde(segundos=1):
    time.sleep(segundos)

def lerString(mensagem):
    while True:
        variavel = input(mensagem)
        if len(variavel)>1:
            return variavel
        else:
            print("Nome inválido")

def letraPalavra(palavrachave):
    return["*" for letra in palavrachave]

def jogar(palavrachave, var1, acertos, erros, letrasErradas):
    var_letraserradas = ",".join(letrasErradas)
    print(f"Letras erradas: {var_letraserradas}")
    letra = input("Digite uma letra: ")
    palavraexibida = ''.join(var1)
    if letra in palavrachave:
        for i in range(len(palavrachave)):
            if letra == palavrachave [i]:
                print("Você acertou uma letra!")
                var1[i] = letra
                acertos = acertos+1
                palavraexibida = ''.join(var1)
                aguarde(1)
                limparTela()
    else:
        erros = erros + 1
        letrasErradas.append(letra)
        print("LETRA INVÁLIDA!")
                      
    print(palavraexibida)
    
    return var1, acertos, erros, letrasErradas