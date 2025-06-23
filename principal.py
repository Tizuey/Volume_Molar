#importando as funções que serão utilizadas
from Vmol.vmol import vmol


#Calcular a massa específica 
def calcular_massaEspecifica(V, massa_molar):
    """massaEspecifica = massa molar / volume molar."""
    return massa_molar / V  # em g/cm³


def main():
    # Dados do Cloreto de Metila (exemplo)
    substancias = {
        '1': {
            'nome': 'Cloreto de Metila',
            'massa_molar': 50.488,  
            'Tc': 416.3,           
            'Pc': 66.80             
        },
        '2': {
            'nome': 'Metano',
            'massa_molar': 16.043, 
            'Tc': 190.56,           
            'Pc': 45.99             
        },
        '3': {
            'nome': 'Etano',
            'massa_molar': 30.07,  
            'Tc': 305.32,           
            'Pc': 48.72             
        }
    }

    #Inicio do programa
    print("Calculo de volume e massa molecucar (Liquido & Gasoso)")
    print("-----------------------------------------------------")
    print("")
    print("S U B S T Â N C I A S      D E     E X E M P L O")
    print(substancias['1'])
    print(substancias['2'])
    print(substancias['3'])
    print("")
    print("-----------------------------------------------------")
    # Pega os dados para o calculo do volume
    print("ATENÇÃO SEPARE OS DECIMAIS COM . E NÃO ,")
    print("")
    nomeSubs = input("Digite o nome do composto: ").strip()
    massaMolar = float(input(f"Digite a massa molar de {nomeSubs} [g/mol]: "))
    tc = float(input(f"Digite a temperatura crítica (Tc) de {nomeSubs} [K]: "))
    pc = float(input(f"Digite a pressão crítica (Pc) de {nomeSubs} [bar]: "))
    celsius = float(input("Digite a temperatura de operação (T) [°C]: "))
    bar = float(input("Digite a pressão de operação (P) [bar]: "))


    # Converter temperatura para Kelvin
    kelvin = celsius + 273.15 

    # Criando os "vetores" CRT e COND 
    crt = [tc, pc]
    cond = [kelvin, bar]

    modelo = input("Escolha o modelo (vdW/RK/PR): ").strip().upper()

    resultados = []
    for fase in ['L','V']:
        try:
            V = vmol(modelo,fase,crt,cond)
            massaEspecifica = calcular_massaEspecifica(V, massaMolar)
            
            resultados.append({
                'Substância':  nomeSubs,  
                'Modelo': modelo,
                'Fase': 'Líquido' if fase == 'L' else 'Vapor',
                'Volume Molar (cm³/mol)': round(V, 4),
                'Massa Específica (g/cm³)': round(massaEspecifica, 6) 
            })
        except ValueError as e:
            print(f"Erro: {e}")
            continue
        

    # Salvar em TXT
    try:
        with open('resultados.txt', 'a', encoding='utf-8') as file:
            file.write("=== RESULTADOS ===\n")
            file.write(f"Substância: {nomeSubs}\n")
            file.write(f"Modelo: {modelo}\n")
            file.write(f"Temperatura: {kelvin:.2f} K ({celsius:.2f} °C)\n")
            file.write(f"Pressão: {bar} bar\n\n")
            
            file.write("=== DADOS CALCULADOS ===\n")
            for res in resultados:
                file.write(f"\nFase: {res['Fase']}\n")
                file.write(f"Volume Molar: {res['Volume Molar (cm³/mol)']} cm³/mol\n")
                file.write(f"Massa Específica: {res['Massa Específica (g/cm³)']} g/cm³\n")
        
        print("\nResultados salvos em:")
        print("- resultados.txt (TXT)")
    
    except Exception as e:
        print(f"\nErro ao salvar o arquivo TXT: {e}")
    
    
if __name__ == "__main__":
    main()