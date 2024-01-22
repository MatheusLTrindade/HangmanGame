# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

# Imports
from ast import While
import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():

  # Windows
  if name == 'nt':
    _ = system('cls')

  # Mac ou Linux
  else:
    _ = system('clear')

# Função cabeçalho
def print_cabecalho():

  limpa_tela()
  # Imprime o cabeçalho do jogo
  print("*******************************")
  print("  Bem vindo ao jogo da forca!")
  print("*******************************")
  print("\nAdivinhe a palavra abaixo:\n")

# Função que desenha a forca na tela
def display_hagman(chances):

  # Lista de stágios da forca
  stages = [
    # estágio 6 (final)
    """
      --------
      |      |
      |      O
      |     \\|/
      |      |
      |     / \\
      -
    """,
    # estágio 5
    """
      --------
      |      |
      |      O
      |     \\|/
      |      |
      |     /
      -
    """,
    # estágio 4
    """
      --------
      |      |
      |      O
      |     \\|/
      |      |
      |
      -
    """,
    # estágio 3
    """
      --------
      |      |
      |      O
      |     \\|
      |      |
      |
      -
    """,
    # estágio 2
    """
      --------
      |      |
      |      O
      |      |
      |      |
      |
      -
    """,
    # estágio 1
    """
      --------
      |      |
      |      O
      |
      |
      |
      -
    """,
    # estágio 0
    """
      --------
      |      |
      |
      |
      |
      |
      -
    """
  ]
  return stages[chances]

# Função de inicio do game
def game():

  # Chama a função cabeçalho
  print_cabecalho()

  # Lista de palavras para o jogo
  palavras = ["abacaxi", "amarelo", "arvore", "bola", "cachorro", "casa", "computador", "dinheiro", "elefante", "escola", "futebol", "gato", "internet", "janela", "limao", "livro", "mochila", "moto", "mundo", "notebook", "onibus", "papel", "paralelepipedo", "porta", "professor", "programa", "python", "quadrado", "quintal", "radio", "sapato", "teclado", "telefone", "television", "uva", "vaca", "ventilador", "xilofone", "zebra"]

  # Escolhe randomicamente uma palavra
  palavra = random.choice(palavras)

  # List comprehension
  letras_descobertas = ['_' for letra in palavra]

  # Número de chances
  chances = 6

  # Lista para as letras erradas
  letras_erradas = []

  # Loop enquanto o número de chances for maior do que zero
  while chances > 0:

    # Imprime o dessenho da forca
    print(display_hagman(chances))

    # Imprime a lista de letras descobertas
    print(" ".join(letras_descobertas))

    # Imprime o número de chances
    print(f"Chances restantes: {chances}")

    # Imprime as letras erradas
    print("Letras erradas:", " ".join(letras_erradas))

    # Tentativa - Pede uma letra ao usuário
    tentativa = input("\nDigite uma letra: ").lower()

    # Chama a função cabeçalho
    print_cabecalho()

    # Verifica se a tentativa é uma letra
    if tentativa in palavra:
      # Adiciona a letra certa na posição correta na lista das letras
      index = 0
      # Percorre a lista de letras e encontra a letra digitada
      for letra in palavra:
        # Se a letra digitada for igual a letra da palavra
        if tentativa == letra:
          # Substitui o '_' pela letra digitada
          letras_descobertas[index] = letra
        index += 1
    else:
      print("Ops. Essa letra não está na palavra!")
      # Diminui o número de chances
      chances -= 1
      # Adiciona a letra errada na lista de letras erradas
      letras_erradas.append(tentativa)
    
    # Checa se todas as letras foram descobridas
    if '_' not in letras_descobertas:
      limpa_tela()
      # Imprime a mensagem de vitória
      print("\nParabéns, você venceu!\nA palavra era:", palavra)
      break
    
  # Checa se alguma letra não foi descoberta
  if '_' in letras_descobertas:
    limpa_tela()
    print(display_hagman(0))
    # Imprime a mensagem de derrota
    print("\nVocê perdeu!\nA palavra era:", palavra)
  
# Bloco main
if __name__ == "__main__":

  while True:
    game()
    # Pergunta se o usuário quer jogar novamente
    jogar = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar != 's':
      # Imprime a mensagem de agradecimento
      print("\nObrigado por jogar!")
      break