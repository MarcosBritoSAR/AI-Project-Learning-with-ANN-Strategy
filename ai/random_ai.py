from ai.ai import AI  # Importa a classe AI do módulo ai.ai
import random  # Importa o módulo random do Python

class RandomAI(AI):
    def get_action(self, agent, view: dict):
        """ 
            Parâmetros:
                view: dados de cada célula dentro do campo de visão do agente
            Retorno:
                action: ação que o agente toma, variando de 0 a 9, onde 0-7 são ações de movimento em direções correspondentes, 8 é ataque e 9 é ficar parado.
        """
        return random.randint(0, 9)  # Retorna uma ação aleatória entre 0 e 9
    
    def turn_reward(self, team: int, action: int, list_agents: list) -> None:
        pass  # Método vazio, não faz nada
    
    def get_reward(self, agents: dict, *args):
        return 0  # Retorna 0 como recompensa

class DumbAI(AI):
    def get_action(self, agent, view: dict):
        """ 
            Parâmetros:
                view: dados de cada célula dentro do campo de visão do agente
            Retorno:
                action: ação que o agente toma, variando de 0 a 9, onde 0-7 são ações de movimento em direções correspondentes, 8 é ataque e 9 é ficar parado.
        """