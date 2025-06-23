# Constante dos gases (cm³·bar / mol·K)
R = 83.14

# -----------------------------------------------------------------------------

#Gera os parâmetros 'a' e 'b' da Equação de Peng-Robinson (PR)
def gerar_ab(Tc,Pc):
    a = (0.45724 * R**2 * Tc**2) / Pc
    b = (0.07780 * R * Tc) / Pc
    return a , b

