from classes import Poder, TipoEfeito


#lista de cartas

poderes_rpg = [
    Poder("images/cards/raio-de-zeus.jpeg","Raio de Zeus", 30, 70, TipoEfeito.DANO_IMEDIATO, 0, "Dispara um raio poderoso."),
    Poder("images/cards/escudo-divino.jpeg","Escudo Divino", 20, 30, TipoEfeito.BUFF_DEFESA, 3, "Aumenta defesa por 3 turnos."),
    Poder("images/cards/cura-celestial.jpeg","Cura Celestial", 40, 50, TipoEfeito.CURA, 0, "Recupera vida do usuário."),
    Poder("images/cards/furia-de-ares.jpeg","Fúria de Ares", 50, 60, TipoEfeito.DANO_IMEDIATO, 0, "Golpe devastador de guerra."),
    Poder("images/cards/lamina-do-caos.jpeg","Lâmina do Caos", 35, 45, TipoEfeito.DANO_IMEDIATO, 0, "Ataque brutal com lâminas."),
    Poder("images/cards/sabedoria-de-atena.jpeg","Sabedoria de Atena", 25, 25, TipoEfeito.BUFF_DEFESA, 4, "Defesa estratégica duradoura."),
    Poder("images/cards/tridente-de-poseidon.jpeg","Tridente de Poseidon", 30, 35, TipoEfeito.DANO_IMEDIATO, 0, "Dano de água contundente."),
    Poder("images/cards/toque-de-hades.jpeg","Toque de Hades", 45, 55, TipoEfeito.DANO_IMEDIATO, 0, "Dano sombrio profundo."),
    Poder("images/cards/vigor-do-olimpo.jpeg","Vigor do Olimpo", 15, 20, TipoEfeito.CURA, 0, "Pequena recuperação de vida."),
    Poder("images/cards/barreira-mistica.jpeg","Barreira Mística", 10, 15, TipoEfeito.BUFF_DEFESA, 2, "Proteção mágica rápida."),
    Poder("images/cards/abalo-sismico.jpeg","Abalo Sísmico", 60, 70, TipoEfeito.DANO_IMEDIATO, 0, "Terremoto causado pelo tridente."),
    Poder("images/cards/bencao-de-hera.jpeg","Benção de Hera", 30, 40, TipoEfeito.CURA, 0, "Cura materna e protetora."),
    Poder("images/cards/golpe-rapido.jpeg","Golpe Rápido", 10, 15, TipoEfeito.DANO_IMEDIATO, 0, "Ataque veloz com pouco custo."),
    Poder("images/cards/postura-defensiva.jpeg","Postura Defensiva", 5, 10, TipoEfeito.BUFF_DEFESA, 1, "Defesa leve por 1 turno."),
    Poder("images/cards/chama-eterna.jpeg","Chama Eterna", 55, 65, TipoEfeito.DANO_IMEDIATO, 0, "Fogo que consome o inimigo.")
]