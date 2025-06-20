import numpy as np  # Para cálculos numéricos

# Constante dos gases (cm³·bar / mol·K)
R = 83.14

# -----------------------------------------------------------------------------
def volumeMolar(fase, Tc, Pc, T, P):
    """
    Calcula o volume molar (cm³/mol) pelo modelo Redlich–Kwong.
    
    Parâmetros
    ----------
    fase : str
        'L' para líquido ou 'V' para vapor.
    Tc, Pc : float
        Temperatura e pressão críticas (K, bar).
    T, P : float
        Temperatura e pressão do processo (K, bar).
    
    Retorno
    -------
    float
        Volume molar em cm³/mol.
    """
    # Garante que tudo é numérico (caso venham strings do input())
    Tc, Pc, T, P = map(float, (Tc, Pc, T, P))
    
    # Parâmetros a e b do RK
    a = 0.42748 * R**2 * Tc**2.5 / Pc
    b = 0.08664 * R * Tc / Pc
    
    # Parâmetros adimensionais
    A = a * P / (R**2 * T**2.5)
    B = b * P / (R * T)
    
    # Equação cúbica em Z: Z³ - Z² + (A - B - B²) Z - A B = 0
    coef = [1, -1, A - B - B**2, -A * B]
    Z = np.roots(coef)
    
    # Filtra raízes reais
    Z_real = sorted(z.real for z in Z if abs(z.imag) < 1e-6)
    if not Z_real:
        raise ValueError("Nenhuma raiz real encontrada para Z.")
    
    # Seleciona raiz apropriada
    if fase == 'L':
        Z_chosen = Z_real[0]      # menor raiz → líquido
    elif fase == 'V':
        Z_chosen = Z_real[-1]     # maior raiz → vapor
    else:
        raise ValueError("Fase deve ser 'L' (líquido) ou 'V' (vapor).")
    
    # Converte para volume molar
    V = Z_chosen * R * T / P      # cm³/mol
    
    # Checagem física mínima
    if V <= b:
        raise ValueError(f"Volume inválido (V ≤ b) na fase {'líquida' if fase == 'L' else 'vapor'}.")
    
    return V
