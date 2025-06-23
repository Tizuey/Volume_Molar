# Constante dos gases
R = 83.14  # cm³·bar/(mol·K)

#---------------------------------------------------------------------------------------------------

#Gera os parâmetros 'a' e 'b' de van der Waals (vdW)
def gerar_ab(Tc,Pc):
    a = (27 * R**2 * Tc**2) / (64 * Pc)
    b = (R * Tc) / (8 * Pc)
    return a , b


