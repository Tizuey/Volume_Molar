#importando as funções que serão utilizadas
from Vmol import vdw, rk, pr
import pandas as pd  # Para criação de DataFrames e exportação para Excel


#Calcular a massa específica 
def calcular_massaEspecifica(V, massa_molar):
    """massaEspecifica = massa molar / volume molar."""
    return massa_molar / V  # em g/cm³


def main():
    # Dados do Cloreto de Metila (exemplo)
    dados = {
        'nome': 'Cloreto de Metila',
        'massa_molar': 50.488,  # g/mol
        'Tc': 416.3,  # K
        'Pc': 66.80   # bar
    }
    T = 60 + 273.15  # Conversão para Kelvin
    P = 13.76        # bar

    # Seleção do modelo
    modelo = input("Escolha o modelo (vdW/RK/PR): ").strip().upper()

    # Cálculo para ambas as fases
    resultados = []
    for fase in ['L', 'V']:
        try:
            if modelo == 'VDW':  
                V = vdw.volumeMolar(fase, dados['Tc'], dados['Pc'], T, P)
            elif modelo == 'RK':
                V = rk.volumeMolar(fase, dados['Tc'], dados['Pc'], T, P)
            elif modelo == 'PR':
                V = pr.volumeMolar(fase, dados['Tc'], dados['Pc'], T, P)
            rho = calcular_massaEspecifica(V, dados['massa_molar'])
            
            resultados.append({
                'Modelo': modelo,
                'Fase': 'Líquido' if fase == 'L' else 'Vapor',
                'Volume Molar (cm³/mol)': round(V, 4),
                'Massa Específica (g/cm³)': round(rho, 6) 
            })
        except ValueError as e:
            print(f"Erro: {e}")
            continue
    # Exporta para Excel (opcional)
    df = pd.DataFrame(resultados)
    df.to_excel('resultados.xlsx', index=False)
    

    print("\nResultados salvos em:")
    print("- resultados.xlsx (Excel)")
    
    
if __name__ == "__main__":
    main()