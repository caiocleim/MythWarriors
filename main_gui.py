import tkinter as tk
from tkinter import messagebox
import random
import json
import os
import classes
import characters
import banco_cartas

ARQUIVO_PLACAR = "placar.json"

class MythWarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Myth Warriors - Battle of Gods")
        self.root.geometry("800x650")
        self.root.resizable(False, False)
        
        self.jogador = None
        self.computador = None
        self.rodada = 1
        self.turno_jogador = True
        
        self.placar = {"vitorias": 0, "derrotas": 0}
        self.carregar_placar()
        
        self.font_title = ("Arial", 16, "bold")
        self.font_text = ("Arial", 10)
        
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        
        self.mostrar_tela_selecao()

    def carregar_placar(self):
        if os.path.exists(ARQUIVO_PLACAR):
            try:
                with open(ARQUIVO_PLACAR, "r") as f:
                    self.placar = json.load(f)
            except:
                self.placar = {"vitorias": 0, "derrotas": 0}

    def salvar_placar(self):
        with open(ARQUIVO_PLACAR, "w") as f:
            json.dump(self.placar, f)

    def resetar_todos_personagens(self):
        for char in characters.deus:
            char.vida = 100
            char.energia = 100
            char.efeitos_ativos = []
            char.mao = []
            char.deck_poderes = []

    def mostrar_tela_selecao(self):
        self.resetar_todos_personagens()
        
        for widget in self.container.winfo_children():
            widget.destroy()
            
        tk.Label(self.container, text="Escolha seu Personagem", font=("Arial", 24, "bold")).pack(pady=10)
        
        texto_placar = f"Ranking Global - Vitórias: {self.placar['vitorias']} | Derrotas: {self.placar['derrotas']}"
        tk.Label(self.container, text=texto_placar, font=("Arial", 14), fg="blue").pack(pady=5)
        
        frame_chars = tk.Frame(self.container)
        frame_chars.pack(pady=10)
        
        chars = characters.deus
        
        for i, char in enumerate(chars):
            btn = tk.Button(frame_chars, text=f"{char.nome}\n(Vida: {char.vida})", 
                            font=self.font_title, width=20, height=3,
                            command=lambda c=char: self.iniciar_jogo(c))
            btn.grid(row=i//2, column=i%2, padx=10, pady=10)

    def iniciar_jogo(self, personagem_escolhido):
        self.jogador = personagem_escolhido
        
        opcoes_pc = [c for c in characters.deus if c != self.jogador]
        self.computador = random.choice(opcoes_pc)
        
        self.configurar_decks([self.jogador, self.computador])
        
        self.rodada = 1
        self.turno_jogador = True 
        
        self.jogador.comprar_cartas(3)
        
        self.construir_tela_batalha()
        self.atualizar_interface()
        self.log_evento(f"Batalha Iniciada! {self.jogador.nome} vs {self.computador.nome}")

    def configurar_decks(self, lista_personagens):
        todos = banco_cartas.poderes_rpg
        for p in lista_personagens:
            p.deck_poderes = random.sample(todos, k=10)

    def construir_tela_batalha(self):
        for widget in self.container.winfo_children():
            widget.destroy()
            
        frame_topo = tk.Frame(self.container, pady=10)
        frame_topo.pack(fill="x")
        
        self.lbl_pc_nome = tk.Label(frame_topo, text="PC", font=self.font_title, fg="red")
        self.lbl_pc_nome.pack(side="right", padx=20)
        self.lbl_pc_stats = tk.Label(frame_topo, text="", font=self.font_text)
        self.lbl_pc_stats.pack(side="right", padx=10)
        
        self.lbl_player_nome = tk.Label(frame_topo, text="Você", font=self.font_title, fg="blue")
        self.lbl_player_nome.pack(side="left", padx=20)
        self.lbl_player_stats = tk.Label(frame_topo, text="", font=self.font_text)
        self.lbl_player_stats.pack(side="left", padx=10)
        
        frame_meio = tk.Frame(self.container, bd=2, relief="sunken")
        frame_meio.pack(fill="both", expand=True, padx=20, pady=10)
        
        scrollbar = tk.Scrollbar(frame_meio)
        scrollbar.pack(side="right", fill="y")
        self.txt_log = tk.Text(frame_meio, height=15, state="disabled", yscrollcommand=scrollbar.set)
        self.txt_log.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.txt_log.yview)
        
        self.frame_acoes = tk.Frame(self.container, pady=20, height=150)
        self.frame_acoes.pack(fill="x", side="bottom")
        
    def atualizar_interface(self):
        self.lbl_player_nome.config(text=self.jogador.nome)
        self.lbl_player_stats.config(text=f"HP: {self.jogador.vida} | EN: {self.jogador.energia}")
        
        self.lbl_pc_nome.config(text=self.computador.nome)
        self.lbl_pc_stats.config(text=f"HP: {self.computador.vida} | EN: {self.computador.energia}")
        
        for widget in self.frame_acoes.winfo_children():
            widget.destroy()
            
        if self.turno_jogador:
            tk.Label(self.frame_acoes, text="Sua vez de ATACAR!", font=("Arial", 12, "bold")).pack()
            
            frame_botoes = tk.Frame(self.frame_acoes)
            frame_botoes.pack(pady=5)
            
            btn_atq = tk.Button(frame_botoes, text="Ataque Comum\n(Custo: 0)", bg="#ffcccb", width=15, height=3,
                                command=self.acao_ataque_comum)
            btn_atq.pack(side="left", padx=5)
            
            for i, carta in enumerate(self.jogador.mao):
                estado = "normal" if self.jogador.energia >= carta.custo_energia else "disabled"
                texto = f"{carta.nome}\nCost: {carta.custo_energia}\nForça: {carta.forca}"
                btn = tk.Button(frame_botoes, text=texto, width=18, height=3, state=estado,
                                command=lambda idx=i: self.acao_usar_carta(idx))
                btn.pack(side="left", padx=5)
        else:
            tk.Label(self.frame_acoes, text="Turno do Computador...", font=("Arial", 12, "bold")).pack()
            self.root.after(1500, self.turno_computador)

    def log_evento(self, texto):
        self.txt_log.config(state="normal")
        self.txt_log.insert("end", texto + "\n")
        self.txt_log.see("end")
        self.txt_log.config(state="disabled")

    def verificar_fim_jogo(self):
        if self.computador.vida <= 0:
            self.placar["vitorias"] += 1
            self.salvar_placar()
            messagebox.showinfo("Fim de Jogo", f"Vitória! {self.jogador.nome} derrotou {self.computador.nome}!")
            self.mostrar_tela_selecao()
            return True
        elif self.jogador.vida <= 0:
            self.placar["derrotas"] += 1
            self.salvar_placar()
            messagebox.showerror("Fim de Jogo", f"Derrota! {self.computador.nome} venceu!")
            self.mostrar_tela_selecao()
            return True
        return False

    def processar_efeitos(self, personagem):
        personagem.aplicar_efeitos_inicio_turno()

    def acao_ataque_comum(self):
        dano_base = random.randint(1, 100)
        self.resolver_ataque(self.jogador, self.computador, dano_base, 0, "Ataque Comum")

    def acao_usar_carta(self, index):
        carta = self.jogador.mao.pop(index)
        self.jogador.energia -= carta.custo_energia
        
        bonus = 0
        nome_acao = carta.nome
        
        if carta.tipo_efeito == classes.TipoEfeito.DANO_IMEDIATO:
            bonus = carta.forca
        elif carta.tipo_efeito == classes.TipoEfeito.BUFF_DEFESA:
            self.jogador.adicionar_efeito(carta)
            self.log_evento(f">>> {self.jogador.nome} usou {carta.nome} (Defesa +{carta.forca})")
            self.finalizar_turno_jogador() 
            return
        elif carta.tipo_efeito == classes.TipoEfeito.CURA:
            cura = carta.forca
            self.jogador.vida = min(100, self.jogador.vida + cura)
            self.log_evento(f">>> {self.jogador.nome} usou {carta.nome} e curou {cura} HP.")
            self.finalizar_turno_jogador()
            return

        dano_base = random.randint(1, 100)
        self.resolver_ataque(self.jogador, self.computador, dano_base, bonus, nome_acao)

    def resolver_ataque(self, atacante, defensor, forca_base, bonus_carta, nome_ataque):
        defesa_base = random.randint(1, 100)
        defesa_total = defensor.calcular_defesa_total(defesa_base)
        
        ataque_total = forca_base + bonus_carta
        dano = ataque_total - defesa_total
        
        self.log_evento(f"--- {atacante.nome} ataca! ---")
        self.log_evento(f"Tipo: {nome_ataque} | Força Total: {ataque_total}")
        self.log_evento(f"Defesa de {defensor.nome}: {defesa_total} (Base {defesa_base} + Buffs)")
        
        if dano > 0:
            defensor.vida -= dano
            self.log_evento(f"RESULTADO: {dano} de DANO em {defensor.nome}!")
        else:
            self.log_evento("RESULTADO: Bloqueado totalmente!")
            
        if not self.verificar_fim_jogo():
            if self.turno_jogador:
                self.finalizar_turno_jogador()
            else:
                self.finalizar_turno_pc()

    def finalizar_turno_jogador(self):
        while len(self.jogador.mao) < 3 and len(self.jogador.deck_poderes) > 0:
            self.jogador.mao.append(self.jogador.deck_poderes.pop(0))
            
        self.turno_jogador = False
        self.atualizar_interface()

    def finalizar_turno_pc(self):
        self.processar_efeitos(self.jogador)
        self.processar_efeitos(self.computador)
        self.rodada += 1
        self.turno_jogador = True
        self.log_evento(f"\n--- INÍCIO RODADA {self.rodada} ---")
        self.atualizar_interface()

    def turno_computador(self):
        atk_basico = random.randint(1, 100)
        
        carta_usada = None
        if self.computador.deck_poderes and self.computador.energia > 20:
            if random.random() > 0.5: 
                potencial = random.choice(self.computador.deck_poderes)
                if self.computador.energia >= potencial.custo_energia:
                    carta_usada = potencial
                    self.computador.energia -= carta_usada.custo_energia

        if carta_usada:
            bonus = 0
            if carta_usada.tipo_efeito == classes.TipoEfeito.DANO_IMEDIATO:
                bonus = carta_usada.forca
                self.resolver_ataque(self.computador, self.jogador, atk_basico, bonus, carta_usada.nome)
            elif carta_usada.tipo_efeito == classes.TipoEfeito.BUFF_DEFESA:
                self.computador.adicionar_efeito(carta_usada)
                self.log_evento(f"PC usou {carta_usada.nome} e aumentou a defesa.")
                self.finalizar_turno_pc()
            elif carta_usada.tipo_efeito == classes.TipoEfeito.CURA:
                self.computador.vida = min(100, self.computador.vida + carta_usada.forca)
                self.log_evento(f"PC usou {carta_usada.nome} e se curou.")
                self.finalizar_turno_pc()
            else:
                self.resolver_ataque(self.computador, self.jogador, atk_basico, 0, "Ataque Comum")
        else:
            self.resolver_ataque(self.computador, self.jogador, atk_basico, 0, "Ataque Comum")

if __name__ == "__main__":
    root = tk.Tk()
    app = MythWarApp(root)
    root.mainloop()