
# Batalha Naval - Player vs Computador

Este é um jogo simples de Batalha Naval implementado com a biblioteca `tkinter` em Python. O jogo é entre um jogador humano e o computador.

## Como jogar

- O tabuleiro do **computador** está à esquerda.
- O seu próprio tabuleiro está à direita.
- Clique em uma célula do tabuleiro do computador para atirar.
- Se você acertar um navio, a célula ficará **vermelha** com um "X".
- Se errar, ela ficará **cinza claro** com um "O".
- Após sua jogada, o **computador joga automaticamente** escolhendo uma posição aleatória.
- Seu tabuleiro mostrará seus navios como "N" em azul.
- Quando o computador jogar, seu tabuleiro será atualizado com "X" (acerto) ou "O" (erro).

## Condições de vitória

- Ganha quem **destruir todos os navios inimigos** primeiro.
- Uma mensagem de vitória aparecerá para indicar o vencedor.

## Funcionalidades extras

- O botão **Reiniciar** permite começar um novo jogo a qualquer momento.
- Os navios são colocados aleatoriamente a cada nova partida.
- Ao final do jogo, todos os navios restantes do computador serão revelados.

## Requisitos

- Python 3.x instalado
- Biblioteca `tkinter` (normalmente já incluída no Python padrão)

## Como executar

1. Extraia o arquivo `batalha_naval_gui.zip`.
2. Execute o script Python com o seguinte comando:

```bash
python batalha_naval_gui.py
```

Divirta-se jogando!
