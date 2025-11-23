from classes import Poder
from classes import Personagem
from classes import Guerreiro
from classes import SemiDeus
from classes import Deus
# from classes import ListaPersonagens

deus = []

deus.append (Deus("Zeus",100,
            "Rei dos Deuses, senhor dos céus e relâmpagos.\n"\
            "Seu poder domina qualquer campo de batalha, e\n"\
            "sua presença inspira temor até nos imortais"))

deus.append(Deus("Atena",98,"Deusa da Sabedoria e da estratégia.\n"\
            "cada golpe é calculado, cada defesa é perfeita.\n"\
            "Vence batalhas antes mesmo de tocar a lâmina."))

deus.append(Deus("Ares",99,"A personificaçãoda guerra e da fúria.\n"\
            "Onde ele pisa, o caos nasce. Sua força bruta supera\n"\
            "quase todos os seres do Olimpo"))

deus.append(Deus("Poseidon",97,"Domina oceanos, tempestades e criaturas abissais.\n"\
            "Sua força é tão imprevisível quanto as marés que comanda."))

deus.append(Deus("Hera",95,"Rainha do Olimpo Protetora dos lares e da realeza, mas tão temida\n"\
            " quanto venerada. Sua determinação e poder divino podem subjugar até heróis lendários.\n"))

deus.append(Deus("Hades",100,"Regente das sombras e das almas. Seu poder não explode\n"\
            "— consome. Um deus silencioso, inevitável e tão eterno quanto a morte."))

# for i in range(5):
#     ListaPersonagens.lista_personagens.append(deus[i])