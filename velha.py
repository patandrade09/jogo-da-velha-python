class JogoDaVelha:
#classe construtora, inicializa o objeto ao criar uma instância desta classe
#eu quero que ao user 1 seja atribuído o X, então consigo fazer isso no próprio parâmetro. 
#O self é um parâmetro obrigatório que receberá a instância criada.
    jogada = None
#O None é uma palavra-chave especial em Python. Isso não significa que o valor é zero, mas o valor é NULL ou não disponível. 
    def __init__(self, user1="X"):
        self.jogada = user1
# criamos então o jogo na ordem de teclado numérico em forma de DICIONARIO
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

# método de dicionários .keys serve para obter todas as chaves de um dicionário, no caso,retornar 7,8,9
# agora vamos ao jogo de fato! o método verifica o ESTADO do tabuleiro, verificando se o jogador preencheu três casas consecutivas.
# https://www.covildodev.com.br/artigo/jogo-da-velha-python
    
        



    



    
