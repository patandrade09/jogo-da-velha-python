class JogoDaVelha:
#classe construtora, inicializa o objeto ao criar uma instância desta classe
#eu quero que ao user 1 seja atribuído o X, então consigo fazer isso no próprio parâmetro. 
#O self é um parâmetro obrigatório que receberá a instância criada.
    jogada = None
#O None é uma palavra-chave especial em Python. Isso não significa que o valor é zero, mas o valor é NULL ou não disponível. 
    def __init__(self, user1="X"):
        self.jogada = user1
# criamos então o jogo na ordem de teclado numérico em forma de DICIONARIO {chave : valor}
        jogo = {"7":" ", "8":" ", "9":" ",
                     "4":" ", "5":" ", "6":" ",
                     "1":" ", "2":" ", "3":" "}
# agora crio um método para exibir o jogo
# nos colchetes ele não vai aceitar aspas duplas porque está dentro de uma string
    def mostra_jogo(self):
        print("┌───┬───┬───┐")
        print(f"|{self.jogo['7']} | {self.jogo['8']} | {self.jogo['9']}")
        print("├───┼───┼───┤")
        print(f"|{self.jogo['4']} | {self.jogo['5']} | {self.jogo['6']}")
        print("├───┼───┼───┤")
        print(f"|{self.jogo['1']} | {self.jogo['2']} | {self.jogo['3']}")
        print("└───┴───┴───┘")
# método para checar se a jogada é válida 
# o if de fora ta verificando se a jogada escolhida é umas das 9 posições possíveis no tabuleiro, usa o método Keys.
# o if de dentro ta verificando se a posição escolhida ainda ta vazia, chama o jogo na [posição da jogada]
    def valida_jogada(self, jogada_valida):
        if jogada_valida in self.jogo.keys():
            if self.jogo[jogada_valida] == " ":
                return True
        else:
            return False

# método de dicionários .keys serve para obter todas as chaves de um dicionário, no caso, retornar 7,8,9


# metodos essencial: o método verifica o ESTADO do tabuleiro, verificando se o jogador preencheu três casas consecutivas.
    def verifica_jogo(self):
        # verificando as 3 posições verticais
        if self.jogo["7"] == self.jogo["4"] == self.jogo["1"] != " ":
            return self.jogo["7"] 
            #aqui ele ta retornando o jogador que ganhou, se foi O ou X. 
        elif self.jogo["8"] == self.jogo["5"] == self.jogo["2"] != " ":
            return self.jogo["8"]
        elif self.jogo["9"] == self.jogo["6"] == self.jogo["3"] != " ":
            return self.jogo["9"]
        
        # verificando as três posições horizontais
        elif self.jogo["7"] == self.jogo["8"] == self.jogo["9"] != " ":
            return self.jogo["7"]
        elif self.jogo["4"] == self.jogo["5"] == self.jogo["6"] != " ":
            return self.jogo["4"]
        elif self.jogo["1"] == self.jogo["2"] == self.jogo["3"] != " ":
            return self.jogo["1"]
        
        #verificando as duas posições diagonais
         # diagonal contra-barra
        elif self.jogo["7"] == self.jogo["5"] == self.jogo["3"] != " ":
            return self.jogo["7"]
         # diagonal barra
        elif self.jogo["9"] == self.jogo["5"] == self.jogo["1"] != " ":
            return self.jogo["9"]

# agora vamos verificar se o jogo deu empate
        if [*self.jogo.values()].count(" ") == 0:
            return "Jogo Empatado"
        else:
            return [*self.jogo.values()].count(" ")
# aqui foi feito o desempacotamento dos VALUES do dicionário JOGO e em seguida e contagem desses values que estão com espaço em branco. 
# Caso algum jogador tenha preenchido 3 casas consecutivas é retornado o vencedor.
# Caso a condição acima não ocorra, e caso todas as casas já estejam ocupadas(a quantidade de casas vazias seja igual a zero), é retornado empate.
# Se nem uma das duas condições forem verdadeiras, é retornado a quantidade de casas que ainda faltam serem preenchidas.

# agora vamos ao jogo de fato! 
    def jogar(self):

        jogo = self.mostra_jogo
        for jogando in jogo:

            if jogando == True:
                print(f"Turno do {self.jogada}, qual sua jogada?")
        
        # Enquanto o jogador não fizer uma jogada válida
            vai_jogar = input("Jogada: ")
            for aguardando in vai_jogar:
                if aguardando == True:
                    return self.valida_jogada[vai_jogar]

