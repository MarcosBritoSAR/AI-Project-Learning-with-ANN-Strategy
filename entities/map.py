import random
from entities import Agent

class Map:
    # Define os limites máximos do mapa
    MAX_WIDTH = 80
    MAX_HEIGHT = 40
    
    def __init__(self) -> None:
        # Inicializa os dicionários e listas para armazenamento de agentes, blocos e experiência
        self.list_agents = []
        self.agents: dict = {}
        self.blocks: dict = {}
        self.exp: dict = {}
        
        # Armazena posição dos agentes por ID e ID dos agentes por velocidade
        self.pos_by_id: dict = {}
        self.id_by_speed: dict = {}
        
        # Define dimensões aleatórias para o mapa
        self.width: int = random.randint(self.MAX_WIDTH // 2, self.MAX_WIDTH)
        self.height: int = random.randint(self.MAX_HEIGHT // 2, self.MAX_HEIGHT)

    def is_occupied(self, pos: tuple[int]):
        # Verifica se uma posição está ocupada por um agente ou bloco
        return tuple(pos) in self.agents or tuple(pos) in self.blocks

    def add_agent(self, agent: Agent):
        # Adiciona um agente ao mapa se a posição for válida e não ocupada
        if self.is_inbounds(agent.pos) and not self.is_occupied(agent.pos):
            self.agents[agent.pos] = agent
            self.pos_by_id[agent.ID] = agent.pos
            if agent.speed not in self.id_by_speed:
                self.id_by_speed[agent.speed] = []
            self.id_by_speed[agent.speed].append(agent.ID)
            self.list_agents.append(agent)
            return True
        return False
    
    def add_block(self, pos: tuple[int]):
        # Adiciona um bloco ao mapa se a posição for válida e não ocupada
        if self.is_inbounds(pos) and not self.is_occupied(pos):
            self.blocks[pos] = True
            return True
        return False

    def is_inbounds(self, pos: tuple[int]):
        # Verifica se a posição está dentro dos limites do mapa
        return 0 <= pos[0] < self.height and 0 <= pos[1] < self.width

    def agent_move(self, ID: int, direction: int):
        # Move o agente para uma nova posição se for válida e não ocupada
        old_pos = self.pos_by_id[ID]
        new_pos = (old_pos[0] + Agent.DIRECTIONS[direction][0],
                   old_pos[1] + Agent.DIRECTIONS[direction][1])
        if not self.is_occupied(new_pos) and self.is_inbounds(new_pos):
            self.pos_by_id[ID] = new_pos
            self.agents[new_pos] = self.agents.pop(old_pos)
            self.agents[new_pos].move(new_pos)
            agent = self.agents[new_pos]

            # Se o agente se moveu para uma posição com experiência, ele a coleta
            if new_pos in self.exp:
                agent_speed = agent.speed
                agent.get_exp(self.exp.pop(new_pos))
                if agent.speed != agent_speed:
                    self.id_by_speed[agent_speed].remove(agent.ID)
                    if agent.speed not in self.id_by_speed:
                        self.id_by_speed[agent.speed] = []
                    self.id_by_speed[agent.speed].append(agent.ID)

    def agent_attack(self, ID: int):
        # Executa o ataque do agente em seus arredores
        pos = self.pos_by_id[ID]
        agent = self.agents[pos]
        for dx in range(-agent.attack_range, agent.attack_range + 1):
            for dy in range(-agent.attack_range, agent.attack_range + 1):
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos in self.agents and agent.team != self.agents[new_pos].team:
                    self.agents[new_pos].take_hit(agent.strength)

    def clear_dead(self):
        # Remove agentes mortos do mapa e das estruturas de dados
        to_eliminate = [agent for pos, agent in self.agents.items() if agent.life <= 0]
        for agent in to_eliminate:
            self.id_by_speed[agent.speed].remove(agent.ID)
            del self.pos_by_id[agent.ID]
            del self.agents[agent.pos]

    def get_pos_data(self, pos: tuple[int]):
        # Retorna informações sobre uma posição do mapa
        data = [pos[0], pos[1], 0, 1, 0, 0, -1, -1, -1]
        if not self.is_inbounds(pos):
            data[2] = 1
        if pos in self.blocks:
            data[3] = 0
            data[4] = 1
        elif pos in self.agents:
            data[3] = 0
            data[5] = 1
            data[6] = self.agents[pos].ID
            data[7] = self.agents[pos].team
            data[8] = self.agents[pos].life
        return data

    def get_view(self, pos: tuple[int]):
        # Retorna uma visão do mapa em torno de uma posição
        RANGE = Agent.RANGE
        data = {}
        for i in range(pos[0] - RANGE, pos[0] + RANGE + 1):
            for j in range(pos[1] - RANGE, pos[1] + RANGE + 1):
                data[(i, j)] = self.get_pos_data((i, j))
        return data
    
    def generate_exp(self):
        # Gera experiência em uma posição aleatória e não ocupada do mapa
        x, y = random.randint(0, self.height), random.randint(0, self.width)
        while self.is_occupied((x, y)):
            x, y = random.randint(0, self.height), random.randint(0, self.width)
        self.exp[(x, y)] = self.exp.get((x, y), 0) + 1

    def total_life(self):
        # Calcula a vida total de cada time
        teams = [0, 0]
        for agent in self.agents.values():
            teams[agent.team] += agent.life
        return teams

    def __str__(self) -> str:
        # Representa o mapa como uma string com agentes, blocos e experiência
        s = ""
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.agents:
                    s += f"{self.agents[(i, j)].ID} "
                elif (i, j) in self.blocks:
                    s += "* "
                elif (i, j) in self.exp:
                    s += "e "
                else:
                    s += "- "
            s += "\n"
        for i, team_life in enumerate(self.total_life()):
            s += f"Team {i} life: {team_life}\n"
        return s