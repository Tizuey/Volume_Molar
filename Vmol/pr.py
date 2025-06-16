# Constante dos gases
R = 83.14  # cm³·bar/(mol·K)

#---------------------------------------------------------------------------------------------------

#Calcular o volume molar (liquido e vapor) usando o modelo Peng-Robinson (PR)
def volumeMolar(fase, Tc, Pc, T, P, max_iter=100, tol=0.001):
    
    #Gera valores das variaveis A (atração molecular) e B (volume molecular)do modelo Peng-Robinson (PR)
    a = (0.45724 * R**2 * Tc**2) / Pc
    b = (0.07780 * R * Tc) / Pc
    # O v vai ser b se a fase for líquida, ou (RT/P) se for vapor
    V = b if fase == 'L' else (R * T) / P
    
    for i in range(max_iter):
        # Armazena o volume antigo para verificar convergência
        V_antigo = V
        
        V = (R * T) / P + b - (a * (V_antigo - b)) / (P * V_antigo * (V_antigo + b) + b * (V_antigo - b))
        
        # Verifica convergência
        if abs(V - V_antigo) < tol:
            return V
    
    # Se não convergiu
    raise ValueError(f"Não houve convergência na fase {'líquida' if fase == 'L' else 'vapor'}")      