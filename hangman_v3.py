# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

  # Windows
  if name == 'nt':
    _ = system('cls')

  # Mac e Linux
  else:
    _ = system('clear')

# Board (tabuleiro)
board = ['''
+---+
|   |
|
|
|
|
=========''', '''
+---+
|   |
|   O
|
|
|
=========''', '''
+---+
|   |
|   O
|   |
|
|
=========''', '''
+---+
|   |
|   O
|  /|
|
|
=========''', '''
+---+
|   |
|   O
|  /|\ 
|
|
=========''', '''
+---+
|   |
|   O
|  /|\ 
|  /
|
=========''', '''
+---+
|   |
|   O
|  /|\ 
|  / \ 
|
=========''']


# Classe
class Hangman:

	# Método Construtor
  def __init__(self, palavra):
    self.palavra = palavra
    self.letras_erradas = []
    self.letras_escolhidas = []

	# Método para adivinhar a letra
  def adivinha(self, letra):
    if letra in self.palavra and letra not in self.letras_escolhidas:
      self.letras_escolhidas.append(letra)
    elif letra not in self.palavra and letra not in self.letras_erradas:
      self.letras_erradas.append(letra)
    else:
      return False
    return True

	# Método para verificar se o jogo terminou
  def fim_jogo(self):
    return self.ganhou() or (len(self.letras_erradas) == 6)

	# Método para verificar se o jogador venceu
  def ganhou(self):
    if '_' not in self.esconde_palavra():
      return True
    return False

	# Método para não mostrar a letra no board
  def esconde_palavra(self):
    esconde = ''
    for letra in self.palavra:
      if letra not in self.letras_escolhidas:
        esconde += '_'
      else:
        esconde += letra
    return esconde

	# Método para checar o status do game e imprimir o board na tela
  def status_jogo(self):
    limpa_tela()
    print("\n>>>>>>>>>>Hangman<<<<<<<<<<\n")
    print(board[len(self.letras_erradas)])
    print('\nPalavra: ' + self.esconde_palavra())
    print('\nLetras erradas:',' '.join(self.letras_erradas), '\n')
    print('Letras corretas:', ' '.join(self.letras_escolhidas), '\n')

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():

  # Lista de palavras para o jogo
  palavras = ['casa', 'carro', 'computador', 'notebook', 'celular', 'teclado', 'mouse', 'monitor', 'cadeira', 'mesa', 'ventilador', 'cama', 'sofa', 'armario', 'cozinha', 'banheiro', 'escritorio', 'sala', 'quarto', 'janela', 'porta', 'chave', 'garagem', 'estacionamento', 'elevador', 'escada', 'corredor', 'varanda', 'sacada', 'churrasqueira']

  # Escolhe randomicamente uma palavra
  palavra = random.choice(palavras)
  
  return palavra

# Função Main - Execução do Programa
def main():
  while True:
    limpa_tela()

    # cria o objeto e seleciona uma palvra randomicamente
    game = Hangman(rand_palavra())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.fim_jogo():
      # Status do game
      game.status_jogo()
      # Recebe input do terminal
      user_input = input('\nDigite uma letra: ')
      # Verifica se a letra digitada faz parte da palavra
      game.adivinha(user_input)

    # Verifica o status do jogo
    game.status_jogo()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.ganhou():
      print('\nParabéns! Você venceu!!')
    else:
      print('\nGame over! Você perdeu.')
      print('A palavra era ' + game.palavra)

    # Pergunta ao usuário se ele quer jogar novamente
    escolha = input('\nDeseja jogar novamente? (Sim / Não): ').lower()
    if escolha != 'sim':
      print('\nFoi bom jogar com você! Agora vá estudar!\n')
      break

# Executa o programa
if __name__ == "__main__":
  main()