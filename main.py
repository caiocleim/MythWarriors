import tkinter as tk
from PIL import Image, ImageTk
import time
import characters
import banco_cartas
import random

TELA_WIDTH=1000
TELA_HEIGHT=650

VERSAO_GAME="Pre-Alfa 1.0"

class MythWarriorsApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Myth Warriors")
        self.root.geometry(f"{TELA_WIDTH}x{TELA_HEIGHT}")
        self.root.resizable(False, False)

        self.botao_pressionado = tk.BooleanVar(value=False)
    
    def carregar_background(self):
        self.frame_tela_inicial = tk.Frame(self.root,width=TELA_WIDTH,height=TELA_HEIGHT)
        self.frame_tela_inicial.place(x=0,y=0)

        #aqui está a configuração do background do menun inicial
        img_background = Image.open("images/background/tela-menu-inicial.png")
        img_background = img_background.resize((TELA_WIDTH,TELA_HEIGHT))
        img_tk = ImageTk.PhotoImage(img_background)

        bg = tk.Label(self.frame_tela_inicial,image=img_tk)
        bg.image = img_tk
        bg.place(x=0,y=0,relwidth=1,relheight=1)

    def menuInicial(self):
        self.carregar_background()
        #---------------------------------------------------
        #botões do menu inicial
        btn_iniciar = tk.Button(self.frame_tela_inicial,text="Partida Rápida",command=self.tela_escolha_personagens)
        btn_iniciar.place(x=27,y=257,width=200,height=55)

        btn_opcoes = tk.Button(self.frame_tela_inicial,text="Opções de Jogo")
        btn_opcoes.place(x=97,y=357,width=200,height=55)

        btn_creditos = tk.Button(self.frame_tela_inicial,text="Créditos")
        btn_creditos.place(x=167,y=457,width=200,height=55)

        btn_sair = tk.Button(self.frame_tela_inicial,text="Sair")
        btn_sair.place(x=237,y=557,width=200,height=55)

        root.wait_variable(self.botao_pressionado)

    def desenhar_blocos(self):
        self.selecao_group = []

        self.selecao_group.append(tk.Frame(self.frame_abas,bg=self.frame_abas["bg"],width=720,height=240))
        self.selecao_group[0].place(relx=0.5,rely=0.3,anchor="center")

        self.selecao_group.append(tk.Frame(self.frame_abas,bg=self.frame_abas["bg"],width=720,height=240))
        self.selecao_group[1].place(relx=0.5,y=390,anchor="center")

        #bloco dos personagens

        self.bl_personagens=[]
        self.label_bl_personagens = []
        self.nome_personagens = []

        self.bl_personagens.append(tk.Frame(self.selecao_group[0],bg="white",width=200,height=200))
        self.bl_personagens[0].place(relx=0.2,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[0]))
        self.label_bl_personagens[0].place(relx=0.5,rely=0.5,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[0],bg="white",width=200,height=200))
        self.bl_personagens[1].place(relx=0.5,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[1]))
        self.label_bl_personagens[1].place(relx=0.5,rely=0.5,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[0],bg="white",width=200,height=200))
        self.bl_personagens[2].place(relx=0.8,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[2]))
        self.label_bl_personagens[2].place(relx=0.5,rely=0.5,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[1],bg="white",width=200,height=200))
        self.bl_personagens[3].place(relx=0.2,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[3]))
        self.label_bl_personagens[3].place(relx=0.5,rely=0.5,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[1],bg="white",width=200,height=200))
        self.bl_personagens[4].place(relx=0.5,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[4]))
        self.label_bl_personagens[4].place(relx=0.5,rely=0.5,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[1],bg="white",width=200,height=200))
        self.bl_personagens[5].place(relx=0.8,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[5]))
        self.label_bl_personagens[5].place(relx=0.5,rely=0.5,anchor="center")

    def aumentar_aba(self):
        self.botao_pressionado.set(True)
        if self.aba ==3:
            self.aba=1
        else:
            self.aba+=1
    
    def diminuir_aba(self):
        self.botao_pressionado.set(True)
        if self.aba ==1:
            self.aba=3
        else:
            self.aba-=1
    
    def colocar_no_bloco(self,i,deus):

        imagem = Image.open(f"{deus.caminho_imagem}")
        imagem_red = imagem.resize((200, 200), Image.LANCZOS)

        imagem_tk = ImageTk.PhotoImage(imagem_red)

        self.label_bl_personagens[i].image = imagem_tk

        self.label_bl_personagens[i].configure(image=imagem_tk)

        self.label_bl_personagens[i].place(relx=0.5, rely=0.5,anchor="center")


        

    def tela_escolha_personagens(self):
        self.redefinir()
        root.update()
        self.carregar_background()

        tela_escolha=True

        self.aba=1

        #-- TELA DE ESCOLHA DOS PERSONAGENS
        self.frame_personagens = tk.Frame(root,bg="#FDEBDD",width=720,height=550)
        self.frame_personagens.place(x=245,y=65)

        txt_escolha = "Escolha seu Personagem:"
            
        txt_label = tk.Label(self.frame_personagens,text=txt_escolha,bg=self.frame_personagens["bg"],fg="black",font=("Arial",14,"bold"))
        txt_label.place(relx=0.5, y=29, anchor="center")
        while tela_escolha==True:
            self.frame_abas = tk.Frame(self.frame_personagens,width=720,height=510,bg=self.frame_personagens["bg"])
            self.frame_abas.place(x=0,y=45)

            txt_label_Deuses = tk.Label(self.frame_abas,bg=self.frame_abas["bg"],fg="black",font=("Arial",14,"bold"))
            txt_label_Deuses.place(relx=0.5, y=10, anchor="center")

            self.desenhar_blocos()
            match(self.aba):
                case 1:
                    txt_label_Deuses.configure(text="Guerreiros")
                    
                    guerreiros = characters.guerreiros

                    for i,guerreiro in enumerate(guerreiros):
                        self.colocar_no_bloco(i,guerreiro)
                        btn_personagem = tk.Button(self.bl_personagens[i],text=f"{guerreiro.nome}",command=lambda g=guerreiro: self.iniciarJogo(g))
                        btn_personagem.place(relx=0.5,rely=0.8,anchor="center")
                    
                case 2:
                    txt_label_Deuses.configure(text="Semi-Deuses")

                    semideus = characters.semideus

                    for i,semi in enumerate(semideus):
                        self.colocar_no_bloco(i,semi)
                        btn_personagem = tk.Button(self.bl_personagens[i],text=f"{semi.nome}",command=lambda s=semi: self.iniciarJogo(s))
                        btn_personagem.place(relx=0.5,rely=0.8,anchor="center")

                case 3:
                    txt_label_Deuses.configure(text="Deuses")

                    deuses = characters.deus

                    for i,deus in enumerate(deuses):
                        self.colocar_no_bloco(i,deus)
                        btn_personagem = tk.Button(self.bl_personagens[i],text=f"{deus.nome}",command=lambda d=deus: self.iniciarJogo(d))
                        btn_personagem.place(relx=0.5,rely=0.8,anchor="center")
            


            btn_aba_esquerda= tk.Button(root,text="<--",command=lambda:self.diminuir_aba())
            btn_aba_esquerda.place(x=500,y=630,anchor="center",width=100,height=20)
                
            btn_aba_direita= tk.Button(root,text="-->",command=lambda:self.aumentar_aba())
            btn_aba_direita.place(x=650,y=630,anchor="center",width=100,height=20)

            btn_voltar_menu = tk.Button(root,text="Voltar ao menu",command=self.menuInicial)
            btn_voltar_menu.place(x=100,y=630,anchor="center",width=100,height=30)
            root.wait_variable(self.botao_pressionado)

    def resetar_todos_personagens(self):
        for personagem in self.lista_personagens:
            personagem.vida = 100
            personagem.energia = 100
            personagem.efeitos_ativos = []
            personagem.mao = []
            personagem.deck_poderes = []

    def carrega_HUD(self):
        #carrega as os frames
        #personagem jogador um
        hud1 = tk.Frame(self.frame_tela_inicial,bg="#FDEBDD",width=260,height=160)
        hud1.place(relx=0,rely=0.76)

        txt_nome = tk.Label(hud1,text=f"{self.jogador.nome}",font=("Arial",10,"bold"),bg="#FDEBDD")
        txt_nome.place(relx=0.5,rely=0.05,anchor="center")

        txt_vida = tk.Label(hud1,text="Vida:",font=("Arial",10,"bold"),bg="#FDEBDD")
        txt_vida.place(relx=0.5,rely=0.2,anchor="center")

        txt_energia = tk.Label(hud1,text="Energia:",font=("Arial",10,"bold"),bg="#FDEBDD")
        txt_energia.place(relx=0.55,rely=0.5,anchor="center")

        
        


        #hud de cartas jogador 1

        fr_cartaAtk_comum = tk.Frame(self.frame_tela_inicial,bg="#FDEBDD",width=140,height=171)
        fr_cartaAtk_comum.place(x=350,rely=0.89,anchor="center")

        fr_cartaMagica = tk.Frame(self.frame_tela_inicial,bg="#FDEBDD",width=400,height=171)
        fr_cartaMagica.place(x=650,rely=0.89,anchor="center")

        txt_cartaAtk_comum = tk.Label(fr_cartaAtk_comum,text="Ataque Comum",bg="#FDEBDD",font=("Arial",9,"bold"))
        txt_cartaAtk_comum.place(relx=0.5,rely=0.03,anchor="center")

        txt_cartaMagica = tk.Label(fr_cartaMagica,text="Cartas de Magia",bg="#FDEBDD",font=("Arial",9,"bold"))
        txt_cartaMagica.place(relx=0.5,rely=0.03,anchor="center")

        #personagem jogador dois
        hud2 = tk.Frame(self.frame_tela_inicial,bg="#FDEBDD",width=260,height=160)
        hud2.place(relx=0.76,rely=0)

        txt_nome2 = tk.Label(hud2,text=f"{self.computador.nome}",font=("Arial",10,"bold"),bg="#FDEBDD")
        txt_nome2.place(relx=0.5,rely=0.05,anchor="center")

        txt_vida2 = tk.Label(hud2,text="Vida:",font=("Arial",10,"bold"),bg="#FDEBDD")
        txt_vida2.place(relx=0.5,rely=0.2,anchor="center")

        txt_energia2 = tk.Label(hud2,text="Energia:",font=("Arial",10,"bold"),bg="#FDEBDD")
        txt_energia2.place(relx=0.55,rely=0.5,anchor="center")

        #imagem do jogador um
        img_deus_jogador = Image.open(self.jogador.caminho_imagem)
        img_deus_jogador = img_deus_jogador.resize((100,100))
        img_deus_jogador_tk = ImageTk.PhotoImage(img_deus_jogador)

        label_img_jogador = tk.Label(hud1,image=img_deus_jogador_tk)
        label_img_jogador.image = img_deus_jogador_tk
        label_img_jogador.place(relx=0.2,rely=0.45,anchor="center")

        #imagem do jogador um
        img_deus_jogador_dois = Image.open(self.computador.caminho_imagem)
        img_deus_jogador_dois = img_deus_jogador_dois.resize((100,100))
        img_deus_jogador_dois_tk = ImageTk.PhotoImage(img_deus_jogador_dois)

        label_img_jogador_dois = tk.Label(hud2,image=img_deus_jogador_dois_tk)
        label_img_jogador_dois.image = img_deus_jogador_dois_tk
        label_img_jogador_dois.place(relx=0.2,rely=0.45,anchor="center")

        #cartas

        self.fr_cartas_j1 = []
        self.lbl_cartas_j1 = []

        #ataque comum
        self.fr_cartas_j1.append(tk.Frame(fr_cartaAtk_comum,bg="white",width=115,height=145))
        self.fr_cartas_j1[0].place(relx=0.5,rely=0.5,anchor="center")
        self.lbl_cartas_j1.append(tk.Label(self.fr_cartas_j1[0],bg=self.fr_cartas_j1[0]["bg"],width=115,height=145))
        self.lbl_cartas_j1[0].place(relx=0.5,rely=0.5,anchor="center")
        self.importar_carta(0,self.jogador)

        #cartas magica
        self.fr_cartas_j1.append(tk.Frame(fr_cartaMagica,bg="white",width=115,height=145))
        self.fr_cartas_j1[1].place(relx=0.2,rely=0.5,anchor="center")
        self.lbl_cartas_j1.append(tk.Label(self.fr_cartas_j1[1],bg=self.fr_cartas_j1[1]["bg"],width=115,height=145))
        self.lbl_cartas_j1[1].place(relx=0.5,rely=0.5,anchor="center")
        self.importar_carta(1,self.jogador)

        self.fr_cartas_j1.append(tk.Frame(fr_cartaMagica,bg="white",width=115,height=145))
        self.fr_cartas_j1[2].place(relx=0.5,rely=0.5,anchor="center")
        self.lbl_cartas_j1.append(tk.Label(self.fr_cartas_j1[2],bg=self.fr_cartas_j1[2]["bg"],width=115,height=145))
        self.lbl_cartas_j1[2].place(relx=0.5,rely=0.5,anchor="center")
        self.importar_carta(2,self.jogador)

        self.fr_cartas_j1.append(tk.Frame(fr_cartaMagica,bg="white",width=115,height=145))
        self.fr_cartas_j1[3].place(relx=0.8,rely=0.5,anchor="center")
        self.lbl_cartas_j1.append(tk.Label(self.fr_cartas_j1[3],bg=self.fr_cartas_j1[3]["bg"],width=115,height=145))
        self.lbl_cartas_j1[3].place(relx=0.5,rely=0.5,anchor="center")
        self.importar_carta(3,self.jogador)

    def importar_carta(self,label,player):
        #aqui está a configuração do background do menun inicial
        img_carta = Image.open(f"{player.mao[label].caminho_imagem}")
        img_carta = img_carta.resize((115,145))
        img_tk = ImageTk.PhotoImage(img_carta)

        bg = tk.Label(self.lbl_cartas_j1[label],image=img_tk)
        bg.image = img_tk
        bg.place(relx=0.5,rely=0.5,anchor="center")

    def carregar_tabuleiro(self):
        #carrega o background do tabuleiro
        self.frame_tela_inicial = tk.Frame(self.root,width=TELA_WIDTH,height=TELA_HEIGHT)
        self.frame_tela_inicial.place(x=0,y=0)

        #aqui está a configuração do background do tabuleiro
        img_background = Image.open("images/background/background-tabuleiro.png")
        img_background = img_background.resize((TELA_WIDTH,TELA_HEIGHT))
        img_tk = ImageTk.PhotoImage(img_background)

        bg = tk.Label(self.frame_tela_inicial,image=img_tk)
        bg.image = img_tk
        bg.place(x=0,y=0,relwidth=1,relheight=1)

    def configurar_decks(self):
        todos = banco_cartas.poderes_rpg
        for p in self.lista_personagens:
            p.deck_poderes = random.sample(todos, k=10)

    def iniciarJogo(self,personagem_escolhido):
        self.jogador = personagem_escolhido

        self.lista_personagens = characters.deus + characters.guerreiros + characters.semideus
        self.resetar_todos_personagens()
        self.configurar_decks()
        
        #remove o jogador da lista de opções do computador
        for p in self.lista_personagens:
            if p == self.jogador:
                self.lista_personagens.remove(p)
        
        self.computador = random.choice(self.lista_personagens)

        #configurar primeira mao
        self.jogador.comprar_cartas()
        self.computador.comprar_cartas()

        #fluxo principal do jogo
        self.redefinir()
        self.carregar_tabuleiro()
        #carrega hud dos jogadores
        self.carrega_HUD()



    def redefinir(self):
        for widget in root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MythWarriorsApp(root)
    app.menuInicial()
    root.mainloop()