from abc import ABC, abstractmethod  # Importa as classes ABC e abstractmethod do módulo abc
import torch, torch.nn as nn  # Importa o PyTorch e o módulo de redes neurais do PyTorch

class AI(nn.Module, ABC):
    def __init__(self, team: int) -> None:
        super(AI, self).__init__()  # Inicializa a classe base nn.Module e ABC
        self.team = team  # Define o time do agente

    @abstractmethod
    def get_action(self, view: dict):
        """ 
        Método abstrato para obter a ação do agente.
            Parâmetros:
                view: dados de cada célula dentro do campo de visão do agente
            Retorno:
                action: ação que o agente toma, variando de 0 a 9, onde 0-7 são ações de movimento em direções correspondentes, 8 é ataque e 9 é ficar parado.
        """
        pass

    @abstractmethod
    def turn_reward(self, team: int, action: int, list_agents: list) -> None:
        """
        Método abstrato chamado após cada turno em uma geração, pode ser usado para calcular a aptidão modularmente.
            Parâmetros:
                team: int, time do agente
                action: int, ação tomada pelo agente
                list_agents: list[Agent], lista de agentes em uma partida
            Retorno: None
        """
        pass