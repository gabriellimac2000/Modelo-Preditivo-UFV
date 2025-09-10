# Modelo Preditivo para Análise de Eficiência de Usinas Fotovoltaicas

[cite_start] Este projeto contém um script em Python para avaliar o desempenho de usinas fotovoltaicas, conforme descrito no artigo "AVALIAÇÃO DA EFICIÊNCIA DE USINAS SOLARES: INTEGRAÇÃO DE SIMULAÇÕES PVSYST E ANÁLISE COM PYTHON"[cite: 15].

[cite_start] O script utiliza dados de simulação do software PVsyst e aplica o método dos mínimos quadrados para criar um modelo preditivo de geração de energia.

## Funcionalidades

* [cite_start] Carrega dados de um arquivo `.csv` gerado pelo PVsyst[cite: 177].
* [cite_start] Realiza o pré-processamento dos dados, removendo valores inválidos e corrigindo a formatação[cite: 178].
* [cite_start] Aplica um ajuste de curva com correção de saturação para melhorar a precisão do modelo[cite: 241].
* [cite_start] Gera gráficos de dispersão (GlobInc vs. E_Grid) com a linha de tendência e o coeficiente de determinação (R²)[cite: 208].
* [cite_start] Exibe a equação final do modelo preditivo[cite: 181].

## Bibliotecas Utilizadas

[cite_start] Para executar o script, as seguintes bibliotecas Python são necessárias[cite: 63, 64, 65, 66]:

* `pandas`
* `matplotlib`
* `numpy`
* `scipy`
* `scikit-learn`
* `tkinter`

## Como Usar

1.  Execute o script Python.
2.  Uma janela se abrirá para que você selecione o arquivo `.csv` com os dados exportados do PVsyst.
3.  O script irá processar os dados e exibir dois gráficos com a análise e a linha de tendência. A equação do modelo será impressa no console.
