# Modelo Preditivo para Análise de Eficiência de Usinas Fotovoltaicas

Este projeto contém um script em Python para avaliar o desempenho de usinas fotovoltaicas, conforme descrito no artigo "AVALIAÇÃO DA EFICIÊNCIA DE USINAS SOLARES: INTEGRAÇÃO DE SIMULAÇÕES PVSYST E ANÁLISE COM PYTHON".

O script utiliza dados de simulação do software PVsyst e aplica o método dos mínimos quadrados para criar um modelo preditivo de geração de energia.

## Funcionalidades

* **Carregamento de Dados**: O script lê dados de um arquivo `.csv` que contém informações de simulação, como irradiância solar e energia gerada.
* **Pré-processamento**: Realiza a limpeza dos dados, removendo valores inválidos (como zeros e negativos) e convertendo a formatação para análise numérica.
* **Correção de Saturação**: Identifica o ponto de saturação da geração de energia e filtra os dados para criar um modelo linear mais preciso, aumentando o coeficiente de determinação (R²) de 0,96 para 0,99.
* **Análise e Visualização**: Gera gráficos de dispersão que relacionam a Irradiância Global (GlobInc) e a Energia Gerada (E_Grid). Os gráficos incluem a linha de tendência ajustada e o valor de R².
* **Exportação do Modelo**: Ao final, exibe e imprime a equação da linha de tendência, que representa o modelo de geração da usina.

## Bibliotecas Utilizadas

Para executar o script, as seguintes bibliotecas Python são necessárias:

* `pandas`: Para manipulação e análise de dados.
* `matplotlib.pyplot`: Para a criação dos gráficos.
* `numpy`: Para operações numéricas.
* `scipy` (curve_fit): Para utilizar o método dos mínimos quadrados no ajuste de curvas.
* `scikit-learn` (r2_score): Para o cálculo do coeficiente de determinação (R²).
* `tkinter`: Para criar a interface gráfica de seleção de arquivos.

## Como Usar

1.  Execute o script Python.
2.  Uma janela do sistema se abrirá, solicitando que você selecione o arquivo `.csv` com os dados exportados do PVsyst.
3.  Após a seleção, o script processará os dados e exibirá dois gráficos com a análise. A equação final do modelo preditivo será impressa no console.
