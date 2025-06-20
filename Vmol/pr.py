import numpy as np
# Constante dos gases
R = 83.14  # cm³·bar/(mol·K)

# -----------------------------------------------------------------------------
def volumeMolar(fase, Tc, Pc, T, P, max_iter=100, tol=0.001):
    a = (0.45724 * R**2 * Tc**2) / Pc
    b = (0.07780 * R * Tc) / Pc

    # Inicialmente, não temos volume, mas vamos iterar até convergir

    # Função auxiliar para calcular Z roots da equação cúbica de PR
    def calc_roots(P, T, a, b):
        A = a * P / (R**2 * T**2)
        B = b * P / (R * T)

        # Coeficientes da cúbica Z³ + c2*Z² + c1*Z + c0 = 0
        c2 = -(1 - B)
        c1 = A - 3*B**2 - 2*B
        c0 = -(A*B - B**2 - B**3)

        coef = [1, c2, c1, c0]
        roots = np.roots(coef)
        roots_real = np.real(roots[np.isreal(roots)])
        return roots_real

    # Inicial: escolha Z baseado no chute para líquido e vapor
    if fase == 'L':
        Z = b * P / (R * T)  # chute líquido (aprox. volume mínimo)
    else:
        Z = 1  # chute vapor (aprox. volume ideal)

    for _ in range(max_iter):
        Z_antigo = Z
        roots = calc_roots(P, T, a, b)

        # Seleciona raiz para fase
        if fase == 'L':
            Z = min(roots)
        else:
            Z = max(roots)

        if abs(Z - Z_antigo) < tol:
            V = Z * R * T / P
            if V <= b:
                raise ValueError(f"Volume inválido (V <= b) na fase {'líquida' if fase == 'L' else 'vapor'}")
            return V

    raise ValueError(f"Não houve convergência na fase {'líquida' if fase == 'L' else 'vapor'}")