import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from tkinter import filedialog
import tkinter as tk

# Função para ajustar uma linha de tendência aos dados e calcular o R²
def fit_line(x, y):
    def linear_func(x, a, b):
        return a * x + b

    popt, _ = curve_fit(linear_func, x, y)
    y_pred = linear_func(x, *popt)
    r2 = r2_score(y, y_pred)
    return popt, r2

# Interface gráfica para seleção de arquivo
root = tk.Tk()
root.withdraw()  # Esconder a janela principal
file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

# Carregar os dados do arquivo CSV selecionado
dados = pd.read_csv(file_path, delimiter=";", skiprows=10, skip_blank_lines=True, encoding='latin1')  # Especifique a codificação correta

# Remover as linhas 0 e 1
dados.drop([0, 1], inplace=True)

# Converter as vírgulas para pontos e converter para números
dados = dados.apply(lambda x: x.str.replace(',', '.'))
dados = dados.apply(pd.to_numeric, errors='ignore')

# Remover as linhas que contêm valores 0 ou negativos
dados = dados[(dados[['GlobInc', 'E_Grid', 'T_Amb', 'TArray']] > 0).all(1)]

# Extrair os dados para os gráficos
globinc = dados['GlobInc']
egrid = dados['E_Grid']
t_amb = dados['T_Amb']
t_array = dados['TArray']

# Criar figura e eixos para o primeiro gráfico (GlobInc vs. E_Grid)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(globinc, egrid, label='Dados', color='blue')

# Ajustar uma linha de tendência linear aos dados
params, r2 = fit_line(globinc, egrid)
plt.plot(globinc, params[0] * globinc + params[1], color='red', label=f'Linha de tendência: F(X) = {params[0]:.2f}x + {params[1]:.2f}\n(R²={r2:.2f})')

# Adicionar rótulos e legendas
plt.xlabel('GlobInc (W/m²)')
plt.ylabel('E_Grid (kW)')
plt.title('GlobInc vs. E_Grid')
plt.legend()

# Criar figura e eixos para o segundo gráfico (GlobInc vs. E_Grid com correção de saturação)
plt.subplot(1, 2, 2)

# Encontrar o índice do máximo valor de E_Grid e seu correspondente valor de GlobInc
indice_max_egrid = dados['E_Grid'].idxmax()
limite_saturacao_globinc = dados.loc[indice_max_egrid, 'GlobInc']

# Filtrar os dados para remover os valores de GlobInc maiores que o limite de saturação
dados_filtrados = dados[dados['GlobInc'] <= limite_saturacao_globinc]

# Extrair os dados filtrados para os gráficos
globinc_corrigido = dados_filtrados['GlobInc']
egrid_corrigido = dados_filtrados['E_Grid']

plt.scatter(globinc_corrigido, egrid_corrigido, label='Dados (corrigidos)', color='green')

# Ajustar uma linha de tendência linear aos dados corrigidos
params_corrigidos, r2_corrigidos = fit_line(globinc_corrigido, egrid_corrigido)
plt.plot(globinc_corrigido, params_corrigidos[0] * globinc_corrigido + params_corrigidos[1], color='red', label=f'Linha de tendência (corrigida): F(X) = {params_corrigidos[0]:.2f}x + {params_corrigidos[1]:.2f}\n(R²={r2_corrigidos:.2f})')

# Adicionar rótulos e legendas
plt.xlabel('GlobInc (W/m²)')
plt.ylabel('E_Grid (kW)')
plt.title('GlobInc vs. E_Grid (Corrigido de Saturação)')
plt.legend()

# Ajustar layout
plt.tight_layout()

# Exibir os gráficos
plt.show()

# Imprimir a expressão da função do modelo
print("A função modelo da usina analisada é: F(X) = {:.4f}x + {:.4f}".format(params_corrigidos[0], params_corrigidos[1]))

