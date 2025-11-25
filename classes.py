from abc import ABC, abstractmethod
from enum import Enum
import random

class TipoEfeito(Enum):
    DANO_IMEDIATO = 1
    BUFF_DEFESA = 2    
    ATAQUE_DUPLO = 3   
    CURA = 4
    DANO_CONTINUO = 5  

class Poder:
    def __init__(self, caminho_imagem,nome, custo_energia, forca, tipo_efeito, duracao, descricao):
        """
        duracao: 0 para imediato, >0 para número de turnos, -1 para até o fim do jogo.
        """
        self.caminho_imagem = caminho_imagem
        self.nome = nome
        self.custo_energia = custo_energia # Refere-se ao minEnergia/gasto
        self.forca = forca       # Valor do efeito (ex: 50 de dano, ou 20 de defesa extra)
        self.tipo_efeito = tipo_efeito
        self.duracao = duracao
        self.descricao = descricao

    def __repr__(self):
        return f"[{self.nome}] Custo: {self.custo_energia} | {self.descricao}"

class Personagem(ABC):
    @abstractmethod
    def __init__(self, caminho_imagem,nome, descricao):
        self.caminho_imagem = caminho_imagem
        self.nome = nome
        self.energia = 100
        self.vida = 100
        self.descricao = descricao
        
        # Inventário de Poderes (o "Deck" do personagem)
        self.deck_poderes = [] 
        
        # Mão atual (cartas disponíveis no turno)
        self.mao = []
        
        # Efeitos ativos no personagem (ex: Buff de defesa ativo por 2 turnos)
        self.efeitos_ativos = [] 

    def comprar_cartas(self, quantidade=4):
        """Pega poderes aleatórios do deck e coloca na mão."""
        self.mao = random.choices(self.deck_poderes, k=quantidade)

    def aplicar_efeitos_inicio_turno(self):
        """
        Processa efeitos duradouros (reduz contadores de turno, aplica veneno, etc).
        Deve ser chamado no início de cada rodada no loop do jogo.
        """
        novos_efeitos = []
        for efeito in self.efeitos_ativos:
            # Lógica de exemplo: se for buff, só mantemos. Se fosse dano continuo, aplicaria aqui.
            print(f"Efeito ativo em {self.nome}: {efeito['poder'].nome} ({efeito['turnos']} turnos restantes)")
            
            # Reduz duração
            if efeito['turnos'] > 0:
                efeito['turnos'] -= 1
            
            # Se turnos > 0 ou duracao é -1 (infinito), mantem o efeito
            if efeito['turnos'] > 0 or efeito['turnos'] == -1:
                novos_efeitos.append(efeito)
            else:
                print(f"O efeito de {efeito['poder'].nome} acabou.")
        
        self.efeitos_ativos = novos_efeitos

    def calcular_defesa_total(self, defesa_base_randomica):
        """
        Calcula defesa somando a defesa aleatória do turno + buffs de cartas ativas.
        """
        bonus = 0
        for efeito in self.efeitos_ativos:
            if efeito['poder'].tipo_efeito == TipoEfeito.BUFF_DEFESA:
                bonus += efeito['poder'].forca
        return defesa_base_randomica + bonus

    def adicionar_efeito(self, poder):
        """Registra que um efeito de carta está ativo no personagem."""
        self.efeitos_ativos.append({
            'poder': poder,
            'turnos': poder.duracao
        })

# As classes filhas (Guerreiro, SemiDeus, Deus) continuam herdando daqui...
class Guerreiro(Personagem):
    def __init__(self, caminho_imagem,nome, forca_base, descricao):
        super().__init__(caminho_imagem,nome, descricao)
        self.forca_base = forca_base # Força base para ataques comuns

class SemiDeus(Personagem):
    def __init__(self, caminho_imagem,nome, forca_base, descricao):
        super().__init__(caminho_imagem,nome, descricao)
        self.forca_base = forca_base

class Deus(Personagem):
    def __init__(self, caminho_imagem,nome, forca_base, descricao):
        super().__init__(caminho_imagem,nome, descricao)
        self.forca_base = forca_base