from entities import Agent, Map  # Importa as classes Agent e Map do módulo entities
from ai.ai import AI  # Importa a classe AI do módulo ai.ai
import random, json, os, time, math  # Importa módulos padrão do Python

class Match:
    NEW_EXP_EVERY = 10  # Define a constante que indica a cada quantos turnos uma nova experiência é gerada
    NUM_ADD_EXP = 15  # Define a constante que indica o número de experiências adicionais
    MAX_TURN = 60  # Define a constante que indica o número máximo de turnos
    NUM_BLOCKS = 5  # Define a constante que indica o número de blocos

    ACTIONS = [
        "MOVE RIGHT", "MOVE DOWN-RIGHT", "MOVE DOWN", "MOVE DOWN-LEFT", "MOVE LEFT", "MOVE TOP-LEFT", "MOVE TOP", "MOVE TOP-RIGHT", 
        "ATTACK",  # Define a ação de ataque
        "IDLE"  # Define a ação de ficar parado
    ]

    def __init__(self, team_size: int, team_0_ai, team_1_ai, 
                 print_log: bool = False, presentation: bool = False,
                 train: bool = False, keep_log: bool = False, 
                 sleep_time: float = 0.005) -> None:
        self.print_log = print_log  # Define se o log deve ser impresso
        self.presentation = presentation  # Define se é uma apresentação
        self.keep_log = keep_log  # Define se o log deve ser mantido
        self.sleep_time = sleep_time  # Define o tempo de espera entre as ações

        self.map = Map()  # Cria uma instância da classe Map

        self.ais: list[AI] = [team_0_ai, team_1_ai]  # Cria uma lista de instâncias de AI para os dois times

        self.turn_actions: dict = {}  # Inicializa um dicionário para armazenar as ações de cada turno