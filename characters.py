from classes import Poder
from classes import Personagem
from classes import Guerreiro
from classes import SemiDeus
from classes import Deus
# from classes import ListaPersonagens

deus = []

deus.append (Deus("images/characters/zeus.png","Zeus",100,
            "Rei dos Deuses, senhor dos céus e relâmpagos.\n"\
            "Seu poder domina qualquer campo de batalha, e\n"\
            "sua presença inspira temor até nos imortais"))

deus.append(Deus("images/characters/atena.png","Atena",98,"Deusa da Sabedoria e da estratégia.\n"\
            "cada golpe é calculado, cada defesa é perfeita.\n"\
            "Vence batalhas antes mesmo de tocar a lâmina."))

deus.append(Deus("images/characters/ares.png","Ares",99,"A personificaçãoda guerra e da fúria.\n"\
            "Onde ele pisa, o caos nasce. Sua força bruta supera\n"\
            "quase todos os seres do Olimpo"))

deus.append(Deus("images/characters/poseidon.png","Poseidon",97,"Domina oceanos, tempestades e criaturas abissais.\n"\
            "Sua força é tão imprevisível quanto as marés que comanda."))

deus.append(Deus("images/characters/hera.png","Hera",95,"Rainha do Olimpo Protetora dos lares e da realeza, mas tão temida\n"\
            " quanto venerada. Sua determinação e poder divino podem subjugar até heróis lendários.\n"))

deus.append(Deus("images/characters/hades.png","Hades",100,"Regente das sombras e das almas. Seu poder não explode\n"\
            "— consome. Um deus silencioso, inevitável e tão eterno quanto a morte."))

semideus = []

semideus.append(SemiDeus("images/characters/hercules.png","Hércules",85,
            "Filho de Zeus e de Alcmena, Hércules possui força sobre-humana.\n"
            "Enfrenta monstros e desafios sem hesitar, deixando um rastro de glória."))

semideus.append(SemiDeus("images/characters/perseus.png","Perseu",80,
            "Filho de Zeus e Danae, Perseu é ágil e astuto.\n"
            "Derrotou a Medusa e protegeu a humanidade de criaturas terríveis."))

semideus.append(SemiDeus("images/characters/achilles.png","Aquiles",90,
            "Filho de Peleu e da deusa Tétis, Aquiles é quase invulnerável.\n"
            "Sua fúria em batalha é temida por deuses e mortais."))

semideus.append(SemiDeus("images/characters/theseus.png","Teseu",82,
            "Filho de Egeu, Teseu é herói de Atenas.\n"
            "Venceu o Minotauro e libertou seu povo de perigos ancestrais."))

semideus.append(SemiDeus("images/characters/helena.png","Helena de Troia",78,
            "Filha de Zeus e Leda, Helena é conhecida por sua beleza lendária.\n"
            "Seu destino desencadeou a famosa Guerra de Troia."))

semideus.append(SemiDeus("images/characters/orpheus.png","Orfeu",75,
            "Filho de Apolo e da musa Calíope, Orfeu é músico lendário.\n"
            "Sua lira encanta deuses, mortais e até monstros do submundo."))

guerreiros = []

guerreiros.append(Guerreiro("images/characters/leonidas.png","Leonidas",70,
            "Um guerreiro mortal treinado em combate corpo a corpo.\n"
            "Sua coragem é maior que sua força, sempre enfrentando inimigos de frente."))

guerreiros.append(Guerreiro("images/characters/drakon.png","Drakon",65,
            "Veterano de inúmeras batalhas, Drakon é rápido e letal.\n"
            "Usa estratégia e astúcia para superar adversários mais fortes."))

guerreiros.append(Guerreiro("images/characters/areson.png","Areson",68,
            "Um combatente disciplinado, exímio com espada e escudo.\n"
            "Seu treinamento militar o torna um oponente temido no campo de batalha."))

guerreiros.append(Guerreiro("images/characters/kratos.png","Kratos",95,
            "Conhecido como o Fantasma de Esparta, Kratos é um guerreiro brutal e incansável.\n"
            "Marcado por batalhas contra deuses e monstros, sua força e fúria superam a de qualquer mortal.\n"
            "Mesmo sem divindade, sua determinação o torna uma lenda viva no campo de batalha."))

guerreiros.append(Guerreiro("images/characters/tarkus.png","Tarkus",66,
            "Especialista em ataques rápidos e precisos.\n"
            "Consegue derrubar inimigos antes que percebam sua presença."))

guerreiros.append(Guerreiro("images/characters/brakus.png","Brakus",69,
            "Um guerreiro feroz e determinado.\n"
            "Sua fúria em batalha pode virar o curso de qualquer combate."))

# for i in range(5):
#     ListaPersonagens.lista_personagens.append(deus[i])