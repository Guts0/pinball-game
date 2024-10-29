# Mini Pinball Game

Mini Pinball Game é um jogo de pinball simples desenvolvido em Python com a biblioteca Tkinter. Este projeto foi inspirado pela nostalgia e lembranças da infância, trazendo de volta a diversão dos jogos de pinball de forma acessível e interativa. O objetivo é controlar uma seta para manter uma ou mais bolinhas em movimento na tela. O jogo possui dois níveis de dificuldade e permite que o jogador insira seu nome e escolha o nível antes de começar.

## Funcionalidades

- **Nome do Jogador**: O jogador pode inserir seu nome na tela inicial.
- **Seleção de Nível**:
  - **Easy**: Um jogo com apenas uma bolinha.
  - **Hardcore**: O jogo é mais desafiador, com três bolinhas em movimento ao mesmo tempo.
- **Game Over e Opções**: O jogo termina apenas quando todas as bolinhas desaparecem. A tela de "Game Over" oferece opções para reiniciar o jogo ou voltar à tela inicial.

## Instruções de Instalação

1. **Pré-requisitos**:
   - Certifique-se de que você tem o Python 3 instalado. Para verificar, abra um terminal ou prompt de comando e digite:
     ```bash
     python --version
     ```
   - Instale a biblioteca Tkinter, se ainda não estiver instalada. Tkinter já vem instalada em versões padrão do Python. Para sistemas baseados em Linux, use o comando:
     ```bash
     sudo apt-get install python3-tk
     ```

2. **Clone o Repositório**:
   Clone este repositório para o seu computador:
   ```bash
   git clone <URL_DO_REPOSITORIO>


3. Executar o Jogo: Navegue até o diretório do projeto e execute o arquivo principal:
python mini_pinball_game.py

Como Jogar
Na tela inicial, insira seu nome no campo fornecido.
Escolha o nível de dificuldade entre "Easy" (1 bolinha) e "Hardcore" (3 bolinhas).
Clique em "Iniciar Jogo".
Use as setas Esquerda e Direita do teclado para mover a seta na parte inferior da tela.
Mantenha as bolinhas em movimento para evitar o "Game Over".
Quando o "Game Over" ocorrer (todas as bolinhas sumirem), você pode:
Retry: Jogar novamente no mesmo nível.
Tela Inicial: Voltar para a tela inicial e inserir outro nome ou selecionar um novo nível.
Escolhas de Design da Interface
Tela Inicial: A interface inicial foi projetada para ser intuitiva, com um campo para inserir o nome do jogador e opções de nível em botões de seleção. As cores escuras foram escolhidas para dar um contraste agradável com o texto branco.
Níveis de Dificuldade: O jogo oferece dois níveis para adequar-se tanto a jogadores iniciantes quanto avançados, com um nível mais fácil (Easy) e outro mais desafiador (Hardcore).
Game Over: A tela de "Game Over" fornece opções claras para permitir que o jogador reinicie rapidamente ou volte à tela inicial, facilitando uma nova tentativa ou a escolha de outras configurações.

