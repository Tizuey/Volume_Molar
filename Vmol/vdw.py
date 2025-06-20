# Constante dos gases
R = 83.14  # cm³·bar/(mol·K)

#---------------------------------------------------------------------------------------------------

# Calcular o volume molar (líquido e vapor) usando o modelo van der Waals (vdW)
def volumeMolar(fase, Tc, Pc, T, P, max_iter=100, tol=0.001):
    # Calcula parâmetros a e b do modelo vdW
    a = (27 * R**2 * Tc**2) / (64 * Pc)
    b = (R * Tc) / (8 * Pc)

    # Chute inicial: líquido -> V = b (volume mínimo); vapor -> V = RT/P (volume ideal)
    V = b if fase == 'L' else (R * T) / P

    for i in range(max_iter):
        V_antigo = V

        # Equação de van der Waals resolvida para V (forma iterativa):
        # P = (RT)/(V - b) - a/V² → Isolando V:
        V = (R * T) / (P + a / (V_antigo ** 2)) + b

        # Verifica convergência
        if abs(V - V_antigo) < tol:
            # Garante que V > b (fisicamente válido)
            if V <= b:
                raise ValueError(f"Volume inválido (V <= b) na fase {'líquida' if fase == 'L' else 'vapor'}")
            return V

    raise ValueError(f"Não houve convergência na fase {'líquida' if fase == 'L' else 'vapor'}")