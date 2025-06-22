
import tkinter as tk
import random

TAMANHO = 10
NAVIOS = 5

class BatalhaNavalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Batalha Naval - Player vs Computador")

        self.criar_interface()

    def criar_interface(self):
        self.jogador_tabuleiro = [["~"] * TAMANHO for _ in range(TAMANHO)]
        self.computador_tabuleiro = [["~"] * TAMANHO for _ in range(TAMANHO)]
        self.botao_grid_comp = [[None] * TAMANHO for _ in range(TAMANHO)]
        self.botao_grid_jogador = [[None] * TAMANHO for _ in range(TAMANHO)]

        self.posicionar_navios(self.jogador_tabuleiro)
        self.posicionar_navios(self.computador_tabuleiro)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        tk.Label(self.frame, text="Tabuleiro do Computador").grid(row=0, column=0, columnspan=TAMANHO)
        tk.Label(self.frame, text="Seu Tabuleiro").grid(row=0, column=TAMANHO+1, columnspan=TAMANHO)

        for i in range(TAMANHO):
            tk.Label(self.frame, text=str(i)).grid(row=1, column=i+1)
            tk.Label(self.frame, text=str(i)).grid(row=1, column=i+TAMANHO+2)

        for y in range(TAMANHO):
            tk.Label(self.frame, text=str(y)).grid(row=y+2, column=0)
            tk.Label(self.frame, text=str(y)).grid(row=y+2, column=TAMANHO+1)

            for x in range(TAMANHO):
                btn_comp = tk.Button(self.frame, text="~", width=3, height=1,
                                     command=lambda x=x, y=y: self.jogada_jogador(x, y))
                btn_comp.grid(row=y+2, column=x+1)
                self.botao_grid_comp[y][x] = btn_comp

                texto = "N" if self.jogador_tabuleiro[y][x] == "N" else "~"
                cor = "blue" if texto == "N" else "SystemButtonFace"
                btn_jog = tk.Button(self.frame, text=texto, width=3, height=1, bg=cor, state="disabled")
                btn_jog.grid(row=y+2, column=x+TAMANHO+2)
                self.botao_grid_jogador[y][x] = btn_jog

        self.status_label = tk.Label(self.root, text="Sua vez!", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.reiniciar_btn = tk.Button(self.root, text="Reiniciar", font=("Arial", 12), command=self.reiniciar_jogo)
        self.reiniciar_btn.pack(pady=5)

    def posicionar_navios(self, tabuleiro):
        count = 0
        while count < NAVIOS:
            x = random.randint(0, TAMANHO - 1)
            y = random.randint(0, TAMANHO - 1)
            if tabuleiro[y][x] == "~":
                tabuleiro[y][x] = "N"
                count += 1

    def jogada_jogador(self, x, y):
        celula = self.computador_tabuleiro[y][x]
        if celula in ["X", "O"]:
            self.status_label.config(text="Você já atirou aqui!")
            return

        if celula == "N":
            self.computador_tabuleiro[y][x] = "X"
            self.botao_grid_comp[y][x].config(text="X", bg="red")
            self.status_label.config(text="Acertou um navio!")
        else:
            self.computador_tabuleiro[y][x] = "O"
            self.botao_grid_comp[y][x].config(text="O", bg="lightgray")
            self.status_label.config(text="Errou!")

        if self.verificar_vitoria(self.computador_tabuleiro):
            self.status_label.config(text="Você venceu!")
            self.revelar_navios_computador()
            self.desativar_botoes()
            return

        self.root.after(1000, self.jogada_computador)

    def jogada_computador(self):
        while True:
            x = random.randint(0, TAMANHO - 1)
            y = random.randint(0, TAMANHO - 1)
            if self.jogador_tabuleiro[y][x] not in ["X", "O"]:
                break

        if self.jogador_tabuleiro[y][x] == "N":
            self.jogador_tabuleiro[y][x] = "X"
            self.botao_grid_jogador[y][x].config(text="X", bg="red")
            self.status_label.config(text=f"Computador acertou em ({x},{y})")
        else:
            self.jogador_tabuleiro[y][x] = "O"
            self.botao_grid_jogador[y][x].config(text="O", bg="lightgray")
            self.status_label.config(text=f"Computador errou em ({x},{y})")

        if self.verificar_vitoria(self.jogador_tabuleiro):
            self.status_label.config(text="Computador venceu!")
            self.revelar_navios_computador()
            self.desativar_botoes()

    def verificar_vitoria(self, tabuleiro):
        for linha in tabuleiro:
            if "N" in linha:
                return False
        return True

    def desativar_botoes(self):
        for y in range(TAMANHO):
            for x in range(TAMANHO):
                self.botao_grid_comp[y][x].config(state="disabled")

    def revelar_navios_computador(self):
        for y in range(TAMANHO):
            for x in range(TAMANHO):
                if self.computador_tabuleiro[y][x] == "N":
                    self.botao_grid_comp[y][x].config(text="N", bg="blue")

    def reiniciar_jogo(self):
        self.frame.destroy()
        self.status_label.destroy()
        self.reiniciar_btn.destroy()
        self.criar_interface()

if __name__ == '__main__':
    root = tk.Tk()
    app = BatalhaNavalGUI(root)
    root.mainloop()
