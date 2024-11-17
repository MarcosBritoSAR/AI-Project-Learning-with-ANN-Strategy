import random
from rede.neuronio import *
from rede.camadas import *

# Supondo que a classe Neuronio esteja definida aqui

# Função principal para testar a classe Neuronio
def main():
    # Cria uma instância do Neuronio
    neuronio = Neuronio(3,1)
    
    # Define o número de conexões (número de entradas)
    quantidade_conexoes = 3 

    # Define pesos aleatórios
    pesos = [random.uniform(-1, 1) for _ in range(quantidade_conexoes)]
    neuronio.setPesos(pesos)

    # Define entradas aleatórias
    entradas = [random.uniform(0, 1) for _ in range(quantidade_conexoes)]
    neuronio.setEntrada(entradas)

    # Define um valor de bias
    valor_vies = random.uniform(-1, 1)
    neuronio.setValorVies(valor_vies)

    # Realiza o feedforward
    neuronio.realizarFeedForward()

    # Obtém e imprime a saída
    saida = neuronio.getSaida()
    
    print("Entradas:", entradas)
    print("Pesos:", pesos)
    print("Valor de Vies:", valor_vies)
    print("Saída do Neurônio:", saida)

import unittest

class TestCamadas(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.camada = Camadas()
        self.neuronio1 = Neuronio(quantidadeConexoes=3, codigoFuncaoAtivacao=1)
        self.neuronio2 = Neuronio(quantidadeConexoes=3, codigoFuncaoAtivacao=1)
        self.camada.adicionarNeuronio(self.neuronio1)
        self.camada.adicionarNeuronio(self.neuronio2)

    def test_adicionarNeuronio(self):
        self.assertEqual(self.camada.getQuantidadeNeuronios(), 2)

    def test_getPesos(self):
        self.neuronio1.setPesos([0.1, 0.2, 0.3]) 
        self.neuronio2.setPesos([0.4, 0.5, 0.6])
        pesos = self.camada.getPesos()
        print("GetPesos: ",pesos)
        self.assertEqual(pesos, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])

    def test_setPesos(self):
        self.camada.setPesos([0.1, 0.2, 0.3])
        self.assertEqual(self.neuronio1.getPesos(), [0.1, 0.2, 0.3])
        self.assertEqual(self.neuronio2.getPesos(), [0.1, 0.2, 0.3])

    def test_getQuantidadePesos(self):
        self.neuronio1.setPesos([0.1, 0.2, 0.3])
        self.neuronio2.setPesos([0.4, 0.5, 0.6])
        quantidadePesos = self.camada.getQuantidadePesos()
        print("Quantidade de Pesos: ",quantidadePesos)
        self.assertEqual(quantidadePesos, 6)

    def test_setValorViesses(self):
        self.camada.setValorViesses([0.1, 0.2])
        self.assertEqual(self.neuronio1.getValorVies(), 0.1)
        self.assertEqual(self.neuronio2.getValorVies(), 0.2)

    def test_getValorViesses(self):
        self.neuronio1.setValorVies(0.1)
        self.neuronio2.setValorVies(0.2)
        viesses = self.camada.getValorViesses()
        print("GetValorViesses: ",viesses)
        self.assertEqual(viesses, [0.1, 0.2])

    def test_setEntrada(self):
        self.camada.setEntrada([1.0, 2.0, 3.0])
        self.assertEqual(self.neuronio1._entrada, [1.0, 2.0, 3.0])

    def test_realizarFeedForward(self):
        self.neuronio1.setPesos([0.1, 0.2, 0.3])
        self.neuronio1.setValorVies(0.1)

        # Declando o outro neuronio
        self.neuronio2.setPesos([0.2, 0.1, 0.1])
        self.neuronio2.setValorVies(0.2)

        # Ele seta os valore de entrada para todos os neuronios da camada
        self.camada.setEntrada([1.0, 2.0, 3.0])

        self.camada.realizarFeedForward()

        saida = self.neuronio1.getSaida()
        print("RealizarFeedForward: ",saida)
        self.assertIsNotNone(saida)

    def test_getSaida(self):
        # o erro está aqui
        self.neuronio1.setPesos([0.1, 0.2, 0.3])
        self.neuronio1.setValorVies(0.1)

        self.neuronio2.setPesos([0.4, 0.5, 0.6])
        self.neuronio2.setValorVies(0.2)

        self.camada.setEntrada([1.0, 2.0, 3.0])
        self.camada.realizarFeedForward()
        saida = self.camada.getSaidas()
        print("GetSaida: ",saida)
        self.assertIsNotNone(saida)

    def test_getPesosNeuronio(self):
        self.neuronio1.setPesos([0.1, 0.2, 0.3])
        pesos = self.camada.getPesosNeuronio(0)
        self.assertEqual(pesos, [0.1, 0.2, 0.3])

    def test_getQuantidadeConexoesNeuronios(self):
        quantidadeConexoes = self.camada.getQuantidadeConexoesNeuronios(0)
        self.assertEqual(quantidadeConexoes, 3)

    def test_getViessesNeuronio(self):
        self.neuronio1.setValorVies(0.1)
        vies = self.camada.getViessesNeuronio(0)
        self.assertEqual(vies, 0.1)

if __name__ == '__main__':
    #main()
    unittest.main()
    print("Teste de Unidade")
