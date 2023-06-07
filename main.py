# PROJETO FORCA.  Aluno: RAFAEL AUGUSTO KLEIN    R.A.: 1134873
from funcoesForca import *

print("Bem-Vindos ao jogo da Forca!")
aguarde(3)
limparTela()

while True:
    print("Selecione uma opção:")
    print("(0) Sair")
    print("(1) Novo Jogo")
    print("(2) Placar dos líderes")
    opcao = input()
    if opcao == "0":
        print("Até a proxima! XD")
        break

    elif opcao == "1":
        print("Informe os nomes dos jogadores:")
        desafiante = lerString("Nome do desafiante: ")
        competidor = lerString("Nome do competidor: ")
        arquivo = open("forca.jogo", "a")
        arquivo.write(desafiante + "\n" + competidor + "\n")
        arquivo.close()
        print("Nomes inseridos corretamente")
        aguarde(2)
        limparTela()
    
        print("Desafiante, insira a palavra chave e as 3 dicas para o competidor.")
        palavrachave = lerString("Palavra chave: ")
        dica1 = lerString("Dica número 1: ")
        dica2 = lerString("Dica número 2: ")
        dica3 = lerString("Dica número 3: ")
        aguarde(2)
        limparTela()

        listaDica = [dica1, dica2, dica3]
        letrasPendentes = "".join(letraPalavra(palavrachave))
        print(f"Competidor, sua palavra possui {letrasPendentes} letras")
        
        letrasErradas = []
        quantErros = 6
        tentErros = 0
        var2 = 0
        var1 = letraPalavra(palavrachave)
        while True:
            print("Selecione a opção que deseja")
            print("(1) Jogar")
            print("(2) Dica")
            opcao = input()
            if opcao == "1":
                var1, var2, tentErros, letrasErradas = jogar(palavrachave, var1, var2, tentErros,letrasErradas)
                if (int(var2) == len(palavrachave)):
                    print(f"Parabéns {competidor}, você ganhou!" )
                    print("       ___________      ")
                    print("      '._==_==_=_.'     ")
                    print("      .-\\:      /-.    ")
                    print("     | (|:.     |) |    ")
                    print("      '-|:.     |-'     ")
                    print("        \\::.    /      ")
                    print("         '::. .'        ")
                    print("           ) (          ")
                    print("         _.' '._        ")
                    print("        '-------'       ")
                    break
                elif(quantErros <= tentErros):
                    print(f"Parabéns {desafiante}, você ganhou!" )
                    print("       ___________      ")
                    print("      '._==_==_=_.'     ")
                    print("      .-\\:      /-.    ")
                    print("     | (|:.     |) |    ")
                    print("      '-|:.     |-'     ")
                    print("        \\::.    /      ")
                    print("         '::. .'        ")
                    print("           ) (          ")
                    print("         _.' '._        ")
                    print("        '-------'       ")
                    break
            else:
                print("Selecione uma das 3 dicas")
                print("(1) Dica N°1")
                print("(2) Dica N°2")
                print("(3) Dica N°3")
                opcao = input()
                if opcao == "1":
                    print(f"A dica é: {dica1}")
                    aguarde(4)
                    limparTela()
                elif opcao == "2":
                    print(f"A dica é: {dica2}")
                    aguarde(4)
                    limparTela()
                elif opcao == "3":
                    print(f"A dica é: {dica3}")
                    aguarde(4)
                    limparTela()
                else:
                    print("Dica inválida!")

    elif opcao == "2":
        try:
            arquivo = open("forca.jogo", "r")
            dados = arquivo.read()
            print(dados)
            arquivo.close()
            aguarde(5)
            limparTela()
        except:
            print("Nenhum dado encontrado")
            arquivo = open("forca.jogo", "w")
            arquivo.closed()
            aguarde(5)
            limparTela()

    else:
        print("Opção Inválida!")
        aguarde(3)