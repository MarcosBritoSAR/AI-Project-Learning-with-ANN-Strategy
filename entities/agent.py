class Agent:
    # Constantes que definem características e comportamento do agente
    CUR_ID = 0              # Variável estática para atribuir um ID único a cada agente
    RANGE = 5               # Alcance máximo para o ataque do agente
    MAX_STRENGTH = 5        # Força máxima que o agente pode alcançar
    MAX_LIFE = 10           # Pontos de vida máximos com os quais o agente começa
    LEVEL_UP = 3            # Pontos de experiência necessários para o agente subir de nível
    DIRECTIONS = [          # Direções possíveis para movimento do agente (8 direções)
        (0, 1), (1, 1),     # DIREITA, DIREITA-BAIXO
        (1, 0), (1, -1),    # BAIXO, ESQUERDA-BAIXO
        (0, -1), (-1, -1),  # ESQUERDA, ESQUERDA-CIMA
        (-1, 0), (-1, 1)    # CIMA, DIREITA-CIMA
    ]
    
    def __init__(self, team: int, pos: tuple[int], print_log: bool = False):
        # Inicializa o agente com propriedades básicas e ID único
        self.print_log = print_log  # Define se as ações devem ser logadas
        self.ID = Agent.CUR_ID      # Atribui um ID único ao agente
        Agent.CUR_ID += 1           # Incrementa o ID para o próximo agente
        self.team = team            # Define o time do agente
        self.pos = pos              # Define a posição inicial do agente
        
        # Define as propriedades iniciais do agente
        self.life = Agent.MAX_LIFE      # Pontos de vida atuais do agente
        self.level = 0                  # Nível inicial do agente
        self.exp = 0                    # Experiência atual
        self.total_exp = 0              # Experiência total acumulada
        self.needed_exp = Agent.LEVEL_UP # Experiência necessária para o próximo nível
        self.attack_range = 1           # Alcance de ataque inicial
        self.strength = 1               # Força inicial do agente
        self.speed = 1                  # Velocidade inicial
        self.last_action = 9            # Última ação executada (valor default)

    def move(self, new_pos: tuple[int]):
        # Move o agente para uma nova posição
        if self.print_log: 
            print(f"Agent {self.ID} moved from {self.pos} to {new_pos}")
        self.pos = new_pos

    def take_hit(self, strength):
        # Aplica dano ao agente com base na força do ataque recebido
        self.life -= strength
        if self.print_log: 
            print(f"\tAgent {self.ID} takes {strength} damage. CURRENT: {self.life}")

    def get_exp(self, exp):
        # Aumenta a experiência do agente e verifica se ele deve subir de nível
        if self.print_log: 
            print(f"Agent {self.ID} got {exp} exp points.")
        self.exp += exp               # Incrementa experiência atual
        self.total_exp += exp         # Incrementa experiência total acumulada

        # Verifica se o agente ganhou experiência suficiente para subir de nível
        if self.exp >= self.needed_exp:
            self.exp -= self.needed_exp      # Reseta a experiência acumulada após o level up
            self.needed_exp += Agent.LEVEL_UP # Aumenta a experiência necessária para o próximo nível
            self.level += 1                  # Incrementa o nível do agente

            if self.print_log: 
                print(f"\tLEVEL UP: {self.level}")
            
            # Aumenta as habilidades do agente com base no nível atual
            if self.level % 3 == 0:           # A cada 3 níveis, aumenta a velocidade
                self.speed += 1
                if self.print_log: 
                    print(f"\tSpeed increased to {self.speed}")
            elif self.level % 2 == 0:         # A cada 2 níveis, aumenta o alcance do ataque
                self.attack_range = min(self.attack_range+1, Agent.RANGE)
                if self.print_log: 
                    print(f"\tAttack range increased to {self.attack_range}")
            else:                             # Nos outros níveis, aumenta a força
                self.strength = min(self.strength+1, Agent.MAX_STRENGTH)
                if self.print_log: 
                    print(f"\tStrength increased to {self.strength}")