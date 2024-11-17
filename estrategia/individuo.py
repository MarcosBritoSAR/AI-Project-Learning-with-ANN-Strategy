#import rede.redeNeural as rede
from estrategia.genes import *

class Individuo:

  def __init__(self, redeNeural : rede.RedeNeural ,quntidadeDegenes: int ) -> None:
    """
    Objetivo: Armazenar os genes do indivíduo.
    Funcionalidade: É uma instância da classe Genes, que contém a quantidade de genes especificada no momento da criação do indivíduo.
    """
    self._gene = Genes(quntidadeDegenes) 
    """
    Objetivo: Representar a rede neural associada ao indivíduo.
    Funcionalidade: É uma instância da classe RedeNeural. Os pesos da rede neural são configurados com base nos genes do indivíduo.
    """
    self._rede = redeNeural
    self._rede.setPesos(self._gene.getQuantidadeGenes())
    """
    Objetivo: Armazenar a aptidão do indivíduo.
    Funcionalidade: Inicialmente definido como None, este atributo será usado para armazenar a aptidão calculada do indivíduo, que é uma medida de quão bem o indivíduo realiza a tarefa para a qual foi projetado.
    """
    self._aptidao = None


  """
  Objetivo: Definir o valor de um gene específico.
  Funcionalidade: Atribui o valor fornecido ao gene no índice especificado.
  """
  def setGene(self, indice : int, gene : float) -> None:
    self._gene[indice] = gene
  """
  Objetivo: Obter o valor de um gene específico.
  Funcionalidade: Retorna o valor do gene no índice especificado.
  """
  def getGene(self, indice : int) -> float:
    return self._gene[indice]
  """"
  Objetivo: Definir a aptidão do indivíduo.
  Funcionalidade: Atribui o valor fornecido ao atributo _aptidao.
  """

  def setAptidao(self, aptidao : float) -> None:
    self._aptidao = aptidao

  def getAptidao(self) -> float:
    return self._aptidao

  """"
  Objetivo: Criar um clone do indivíduo atual.
  Funcionalidade: Cria uma nova instância de Individuo com a mesma rede neural e quantidade de genes, copia os genes e a aptidão do indivíduo atual para o clone, e retorna o clone.
  """
def getClone(self) -> 'Individuo':
    clone = Individuo(self._rede, self._gene.getQuantidadeGenes())
    clone._gene = self._gene.getClone()
    clone._aptidao = self._aptidao
    return clone