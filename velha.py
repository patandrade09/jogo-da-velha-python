class JogoDaVelha:
#classe construtora, inicializa o objeto ao criar uma instância desta classe
#eu quero que ao user 1 seja atribuído o X, então consigo fazer isso no próprio parâmetro. 
#O self é um parâmetro obrigatório que receberá a instância criada.
    # criamos então o jogo na ordem de teclado numérico em forma de DICIONARIO {chave : valor}
    velha = {"7":" ", "8":" ", "9":" ",
            "4":" ", "5":" ", "6":" ",
            "1":" ", "2":" ", "3":" "}
    vez = None
#O None é uma palavra-chave especial em Python. Isso não significa que o valor é zero, mas o valor é NULL ou não disponível. 
    def __init__(self, jogador1="X"):
        self.vez = jogador1   
# agora crio um método para exibir o jogo
# nos colchetes ele não vai aceitar aspas duplas porque está dentro de uma string
    def mostra_velha(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.velha['7']} │ {self.velha['8']} │ {self.velha['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.velha['4']} │ {self.velha['5']} │ {self.velha['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.velha['1']} │ {self.velha['2']} │ {self.velha['3']} │")
        print("└───┴───┴───┘")
# método para checar se a jogada é válida 
# o if de fora ta verificando se a jogada escolhida é umas das 9 posições possíveis no tabuleiro, usa o método Keys.
# o if de dentro ta verificando se a posição escolhida ainda ta vazia, chama o jogo na [posição da jogada]
    def verifica_jogada(self, jogada):
        if jogada in self.velha.keys():
            if self.velha[jogada] == " ":
                return True
        else:
            return False

# método de dicionários .keys serve para obter todas as chaves de um dicionário, no caso, retornar 7,8,9


# metodos essencial: o método verifica o ESTADO do tabuleiro, verificando se o jogador preencheu três casas consecutivas.
    def verifica_velha(self):
        # verificando as 3 posições verticais
        if self.velha["7"] == self.velha["4"] == self.velha["1"] != " ":
            return self.velha["7"] 
            #aqui ele ta retornando o jogador que ganhou, se foi O ou X. 
        elif self.velha["8"] == self.velha["5"] == self.velha["2"] != " ":
            return self.velha["8"]
        elif self.velha["9"] == self.velha["6"] == self.velha["3"] != " ":
            return self.velha["9"]
        # verificando as três posições horizontais
        elif self.velha["7"] == self.velha["8"] == self.velha["9"] != " ":
            return self.velha["7"]
        elif self.velha["4"] == self.velha["5"] == self.velha["6"] != " ":
            return self.velha["4"]
        elif self.velha["1"] == self.velha["2"] == self.velha["3"] != " ":
            return self.velha["1"]
        
        #verificando as duas posições diagonais
         # diagonal contra-barra
        elif self.velha["7"] == self.velha["5"] == self.velha["3"] != " ":
            return self.velha["7"]
         # diagonal barra
        elif self.velha["9"] == self.velha["5"] == self.velha["1"] != " ":
            return self.velha["9"]
# agora vamos verificar se o jogo deu empate
        elif [*self.velha.values()].count(" ") == 0:
            return "empate"
        else:
            return [*self.velha.values()].count(" ")
# aqui foi feito o desempacotamento dos VALUES do dicionário JOGO e em seguida e contagem desses values que estão com espaço em branco. 
# Caso algum jogador tenha preenchido 3 casas consecutivas é retornado o vencedor.
# Caso a condição acima não ocorra, e caso todas as casas já estejam ocupadas(a quantidade de casas vazias seja igual a zero), é retornado empate.
# Se nem uma das duas condições forem verdadeiras, é retornado a quantidade de casas que ainda faltam serem preenchidas.

# agora vamos ao jogo de fato! agr vem os métodos que serão responsáveis pela comunicação com os jogadores.
# enquanto a função jogar for verdadeira, ela vai mostrar o velha e printar a frase de inicio. 


    def jogar(self):
        while True:
            
            print("Digite os números correspondentes para escolher a posição do seu jogo2:")
            print("┌───┬───┬───┐")
            print(f"│ 7 │ 8 │ 9 │")
            print("├───┼───┼───┤")
            print(f"│ 4 │ 5 │ 6 │")
            print("├───┼───┼───┤")
            print(f"│ 1 │ 2 │ 3 │")
            print("└───┴───┴───┘")
            print(f"Vez de {self.vez}, qual sua jogada?")        
            # enquanto o jogador não faz uma jogada válida (while dentro de while)
            self.mostra_velha()
            while True:
                jogada = input("Jogada:")    
                # agora ele verifica se o valor digitado pra jogar é valido.
                if self.verifica_jogada(jogada): # Se a jogada for válida
                    break # Encerra o loop
                else: #se não..
                    print(f"Posição {jogada} já foi marcada")
            #insere o caractere no tabuleiro
            self.velha[jogada] = self.vez
            
            #verifica como ficou o tabuleiro a partir da ultima jogada
            state = self.verifica_velha()
            
            if state == "X":
                self.mostra_velha()
                print("Parabéns X, você venceu!")
                break
            elif state == "0":
                self.mostra_velha()
                print("O é o vencedor!!!")
                break

            if state == "empate":
                self.mostra_velha()
                print("EMPATE!!!")
                break
            # Troca o jogador do próximo turno
            self.vez = "X" if self.vez == "O" else "O"
            
            
            
#instanciando a classe para iniciar um novo jogo. 
jogo = JogoDaVelha()
jogo.jogar()           
