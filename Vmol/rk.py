# Constante dos gases (cm³·bar / mol·K)
R = 83.14

# -----------------------------------------------------------------------------

#Gera os parâmetros 'a' e 'b' da Equação de Redlich-Kwong (RK)
def gerar_ab(Tc,Pc):
    a = (0.42748 * R**2 * Tc**2.5) / Pc
    b = (0.08664 * R * Tc) / Pc
    return a , b

