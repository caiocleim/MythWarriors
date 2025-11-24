import tkinter as tk
from PIL import Image, ImageTk
import time
import characters

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
        self.nome_personagens.append(tk.Label(self.selecao_group[0]))
        self.nome_personagens[0].place(relx=0.2,y=230,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[0],bg="white",width=200,height=200))
        self.bl_personagens[1].place(relx=0.5,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[1]))
        self.label_bl_personagens[1].place(relx=0.5,rely=0.5,anchor="center")
        self.nome_personagens.append(tk.Label(self.selecao_group[0]))
        self.nome_personagens[1].place(relx=0.5,y=230,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[0],bg="white",width=200,height=200))
        self.bl_personagens[2].place(relx=0.8,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[2]))
        self.label_bl_personagens[2].place(relx=0.5,rely=0.5,anchor="center")
        self.nome_personagens.append(tk.Label(self.selecao_group[0]))
        self.nome_personagens[2].place(relx=0.8,y=230,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[1],bg="white",width=200,height=200))
        self.bl_personagens[3].place(relx=0.2,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[3]))
        self.label_bl_personagens[3].place(relx=0.5,rely=0.5,anchor="center")
        self.nome_personagens.append(tk.Label(self.selecao_group[1]))
        self.nome_personagens[3].place(relx=0.2,y=230,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[1],bg="white",width=200,height=200))
        self.bl_personagens[4].place(relx=0.5,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[4]))
        self.label_bl_personagens[4].place(relx=0.5,rely=0.5,anchor="center")
        self.nome_personagens.append(tk.Label(self.selecao_group[1]))
        self.nome_personagens[4].place(relx=0.5,y=230,anchor="center")

        self.bl_personagens.append(tk.Frame(self.selecao_group[1],bg="white",width=200,height=200))
        self.bl_personagens[5].place(relx=0.8,rely=0.5, anchor="center")
        self.label_bl_personagens.append(tk.Label(self.bl_personagens[5]))
        self.label_bl_personagens[5].place(relx=0.5,rely=0.5,anchor="center")
        self.nome_personagens.append(tk.Label(self.selecao_group[1]))
        self.nome_personagens[5].place(relx=0.8,y=230,anchor="center")

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

        self.nome_personagens[i].configure(text=f"{deus.nome}",font=("Arial",9,"bold"),bg=self.frame_abas["bg"])

        

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
                    for i in range(6):
                        self.colocar_no_bloco(i,characters.guerreiros[i])
                    
                case 2:
                    txt_label_Deuses.configure(text="Semi-Deuses")

                    for i in range(6):
                        self.colocar_no_bloco(i,characters.semideus[i])

                case 3:
                    txt_label_Deuses.configure(text="Deuses")

                    for i in range(6):
                        self.colocar_no_bloco(i,characters.deus[i])
            


            btn_aba_esquerda= tk.Button(root,text="<--",command=lambda:self.diminuir_aba())
            btn_aba_esquerda.place(x=500,y=630,anchor="center",width=100,height=20)
                
            btn_aba_direita= tk.Button(root,text="-->",command=lambda:self.aumentar_aba())
            btn_aba_direita.place(x=650,y=630,anchor="center",width=100,height=20)

            btn_voltar_menu = tk.Button(root,text="Voltar ao menu",command=self.menuInicial)
            btn_voltar_menu.place(x=100,y=630,anchor="center",width=100,height=30)
            root.wait_variable(self.botao_pressionado)
        


    def redefinir(self):
        for widget in self.frame_tela_inicial.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MythWarriorsApp(root)
    app.menuInicial()
    root.mainloop()