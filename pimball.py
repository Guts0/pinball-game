import tkinter as tk
import random

class PinballGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Pinball Game")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        
        self.level = 1
        self.balls = []
        self.ball_speed = 5
        self.player_name = ""
        self.active_balls = 0

        # Configuração da tela inicial
        self.setup_start_screen()

    def setup_start_screen(self):
        # Tela inicial com opções para colocar nome e selecionar a dificuldade
        self.start_frame = tk.Frame(self.root, bg="black")
        self.start_frame.place(relwidth=1, relheight=1)

        title = tk.Label(self.start_frame, text="Mini Pinball Game", font=("Arial", 24), fg="white", bg="black")
        title.pack(pady=20)

        # nome do jogador
        name_label = tk.Label(self.start_frame, text="Digite seu nome:", font=("Arial", 14), fg="white", bg="black")
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.start_frame, font=("Arial", 14))
        self.name_entry.pack(pady=5)

        # seleção do nível
        level_label = tk.Label(self.start_frame, text="Selecione o nível:", font=("Arial", 14), fg="white", bg="black")
        level_label.pack(pady=10)
        
        self.level_var = tk.StringVar(value="Easy")
        easy_button = tk.Radiobutton(self.start_frame, text="Easy", font=("Arial", 12), variable=self.level_var, value="Easy", bg="black", fg="white", selectcolor="black")
        easy_button.pack(pady=2)
        
        hardcore_button = tk.Radiobutton(self.start_frame, text="Hardcore", font=("Arial", 12), variable=self.level_var, value="Hardcore", bg="black", fg="white", selectcolor="black")
        hardcore_button.pack(pady=2)

        # Botão para iniciar o jogo
        start_button = tk.Button(self.start_frame, text="Iniciar Jogo", font=("Arial", 14), command=self.start_game)
        start_button.pack(pady=20)

    def start_game(self):
        # captura o nome do jogador e o nível selecionado
        self.player_name = self.name_entry.get()
        selected_level = self.level_var.get()

        # para definir a dificuldade
        self.level = 1 if selected_level == "Easy" else 2

        # Limpa a tela inicial e inicia a tela de jogo
        self.start_frame.destroy()
        self.setup_game_screen()

    def setup_game_screen(self):
        # configuração da tela de jogo
        self.canvas = tk.Canvas(self.root, bg="black", width=600, height=400)
        self.canvas.pack()

        # para exibir o nome do jogador
        self.canvas.create_text(300, 20, text=f"Jogador: {self.player_name}", fill="white", font=("Arial", 12))

        # setinha para controlar durante o game
        self.paddle = self.canvas.create_rectangle(250, 350, 350, 360, fill="blue")
        self.paddle_speed = 20

        # para adicionar as 3 bolas no nivel hardcore
        self.create_ball()

        # movimentação
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        
        self.play_game()

    def create_ball(self):
        self.active_balls = 1 if self.level == 1 else 3
        if self.level == 1:  # nível Easy (1 bola)
            ball = self.canvas.create_oval(290, 50, 310, 70, fill="red")
            self.balls.append({"id": ball, "x_speed": self.ball_speed, "y_speed": self.ball_speed})
        elif self.level == 2:  # nível Hardcore (3 bolas)
            for _ in range(3):
                x_start = random.randint(50, 550)
                y_start = random.randint(30, 100)
                ball = self.canvas.create_oval(x_start, y_start, x_start + 20, y_start + 20, fill="red")
                x_speed = random.choice([-self.ball_speed, self.ball_speed])
                y_speed = random.choice([-self.ball_speed, self.ball_speed])
                self.balls.append({"id": ball, "x_speed": x_speed, "y_speed": y_speed})

    def move_left(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.paddle)
        if x1 > 0:
            self.canvas.move(self.paddle, -self.paddle_speed, 0)

    def move_right(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.paddle)
        if x2 < 600:
            self.canvas.move(self.paddle, self.paddle_speed, 0)

    def update_ball_position(self):
        for ball in self.balls:
            x1, y1, x2, y2 = self.canvas.coords(ball["id"])
            if x1 <= 0 or x2 >= 600:
                ball["x_speed"] = -ball["x_speed"]
            if y1 <= 0 or (y2 >= 350 and self.check_paddle_collision(ball["id"])):
                ball["y_speed"] = -ball["y_speed"]
            elif y2 >= 400:
                # remove a bola do jogo se ela ultrapassar o limite inferior
                self.canvas.delete(ball["id"])
                self.balls.remove(ball)
                self.active_balls -= 1
                # verifica se todas as bolas sumiram para encerrar o jogo
                if self.active_balls <= 0:
                    self.end_game("Game Over")
                return

            self.canvas.move(ball["id"], ball["x_speed"], ball["y_speed"])

    def check_paddle_collision(self, ball_id):
        paddle_coords = self.canvas.coords(self.paddle)
        ball_coords = self.canvas.coords(ball_id)
        if paddle_coords[0] < ball_coords[2] and paddle_coords[2] > ball_coords[0]:
            return True
        return False

    def play_game(self):
        self.update_ball_position()
        if self.active_balls > 0:
            self.root.after(30, self.play_game)

    def end_game(self, message):
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text=message, fill="white", font=("Arial", 24))
        
        # botões de "Retry" e "Tela Inicial" na tela de "Game Over"
        retry_button = tk.Button(self.root, text="Retry", font=("Arial", 14), command=self.reset_game)
        retry_button_window = self.canvas.create_window(250, 250, window=retry_button)
        
        back_button = tk.Button(self.root, text="Tela Inicial", font=("Arial", 14), command=self.return_to_start)
        back_button_window = self.canvas.create_window(350, 250, window=back_button)

    def reset_game(self):
        # reinicia o jogo com o mesmo jogador e nível
        self.balls = []
        self.canvas.delete("all")
        self.setup_game_screen()

    def return_to_start(self):
        # retorna à tela inicial
        self.balls = []
        self.canvas.delete("all")
        for widget in self.root.pack_slaves():
            widget.destroy()
        self.setup_start_screen()

# inicialização do game

root = tk.Tk()
game = PinballGame(root)
root.mainloop()
