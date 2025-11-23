from classes import Poder, TipoEfeito


#lista de cartas

poderes_rpg = [
    Poder("Raio de Zeus", 30, 40, TipoEfeito.DANO_IMEDIATO, 0, "Dispara um raio poderoso."),
    Poder("Escudo Divino", 20, 30, TipoEfeito.BUFF_DEFESA, 3, "Aumenta defesa por 3 turnos."),
    Poder("Cura Celestial", 40, 50, TipoEfeito.CURA, 0, "Recupera vida do usuário."),
    Poder("Lâmina do Caos", 35, 45, TipoEfeito.DANO_IMEDIATO, 0, "Ataque brutal com lâminas."),
    Poder("Fúria de Ares", 50, 60, TipoEfeito.DANO_IMEDIATO, 0, "Golpe devastador de guerra."),
    Poder("Sabedoria de Atena", 25, 25, TipoEfeito.BUFF_DEFESA, 4, "Defesa estratégica duradoura."),
    Poder("Maré Violenta", 30, 35, TipoEfeito.DANO_IMEDIATO, 0, "Dano de água contundente."),
    Poder("Toque de Hades", 45, 55, TipoEfeito.DANO_IMEDIATO, 0, "Dano sombrio profundo."),
    Poder("Vigor do Olimpo", 15, 20, TipoEfeito.CURA, 0, "Pequena recuperação de vida."),
    Poder("Barreira Mística", 10, 15, TipoEfeito.BUFF_DEFESA, 2, "Proteção mágica rápida."),
    Poder("Tridente Sísmico", 60, 70, TipoEfeito.DANO_IMEDIATO, 0, "Terremoto causado pelo tridente."),
    Poder("Benção de Hera", 30, 40, TipoEfeito.CURA, 0, "Cura materna e protetora."),
    Poder("Golpe Rápido", 10, 15, TipoEfeito.DANO_IMEDIATO, 0, "Ataque veloz com pouco custo."),
    Poder("Postura Defensiva", 5, 10, TipoEfeito.BUFF_DEFESA, 1, "Defesa leve por 1 turno."),
    Poder("Chama Eterna", 55, 65, TipoEfeito.DANO_IMEDIATO, 0, "Fogo que consome o inimigo.")
]