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
    print("Iniciando Calculo de volume e massa molecucar (Liquido & Gasoso)")
    print("AMBIENTE ->   T = 60 C  e  P = 13,76 b")
    nomeSubs = input("Digite o nome da Substancia:  ")
    massaMolar = float(input("Digite a massa molar em vez de virgula uso  (.):  "))
    Tc = float(input("Digite a Temperatura Critica (Tc) em vez de virgula uso  (.):  "))
    Pc = float(input("Digite a pressão Critica (Pc) em vez de virgula uso  (.):  "))

    modelo = input("Escolha o modelo (vdW/RK/PR): ").strip().upper()

    # Cálculo para ambas as fases
    resultados = []
    for fase in ['L', 'V']:
        try:
            if modelo == 'VDW':  
                V = vdw.volumeMolar(fase, Tc, Pc, T, P)
            elif modelo == 'RK':
                V = rk.volumeMolar(fase, Tc, Pc, T, P)
            elif modelo == 'PR':
                V = pr.volumeMolar(fase, Tc, Pc, T, P)
            rho = calcular_massaEspecifica(V, massaMolar)
            
            resultados.append({
                'Substância': dados['nome'],  
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
    try:
        df.to_excel('resultados.xlsx', index=False)
        print("\nResultados salvos em:")
        print("- resultados.xlsx (Excel)")
    except PermissionError:
        print("\nERRO: Não foi possível salvar o arquivo 'resultados.xlsx'!")
        print("Por favor, feche o arquivo Excel se estiver aberto e tente novamente.")
        input("Pressione Enter para continuar...")
        return  # Sai da função main() sem continuar
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao salvar o Excel: {e}")
        input("Pressione Enter para continuar...")
        return
    

    print("\nResultados salvos em:")
    print("- resultados.xlsx (Excel)")
    
    
if __name__ == "__main__":
    main()