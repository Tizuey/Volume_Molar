from . import vdw, rk, pr
# Constante dos gases (cm³·bar / mol·K)
R = 83.14

# -----------------------------------------------------------------------------

#Função para calcular o Volume Molar
def vmol(modelo,fase,crt,cond):

    # Extrai os valores dos vetores de entrada CRT e COND
    Tc, Pc = crt[0], crt[1]
    T, P = cond[0], cond[1]

    #Pega o modelo escolhido
    if modelo == 'VDW':  
        a , b = vdw.gerar_ab(Tc,Pc)
    elif modelo == 'RK':
        a , b = rk.gerar_ab(Tc,Pc)
    elif modelo == 'PR':
        a , b = pr.gerar_ab(Tc,Pc)
    

    # Define a estimativa inicial para o volume molar (Vi) de acordo com sua Fase
    if fase == 'L': #liquida
        Vi = b
    else: # vapor
        Vi = R*T/P

    #Parametros para o calculo iterativo
    tol = 0.001 # tolerancia , no qual vai definir a precisao do resultado
    ite = 0 # contador para registrar as vezes das interações
    dif = float('inf') # para inicar o loop haja visto que ainda não nenhum valor a comparar, mas aqui ficara a diferença dos valores de do Vi e do Vi+1

    while dif > tol and ite < 100 :

        # um filtro para que o denominador não fique zero
        if P == 0 or Vi == 0 or (Vi + b) == 0:
             raise ValueError(f"Divisão por zero iminente na fase {fase}. Verifique as condições de entrada ou a estimativa inicial.")

        # Calcula o denominador da Eq. 1
        denominador = (T**0.5) * P * Vi * (Vi + b) # raiz quadrada tambem pode ser um numero na potencia de 1/2

        
        #calcula o Vi + 1
        vi_mais1 = (R * T) / P + b - (a * (Vi - b)) / denominador

        #aqui se mede a diferença sem se importar com o sinal
        dif = abs(vi_mais1 - Vi)

        # Atualiza Vi para a próxima iteração
        Vi = vi_mais1
        ite += 1 #adiciona +1 a cada iteração
    
    # Verificação de Convergência 
    if ite >= 100 and dif > tol:
        if fase.upper() == 'L':
            raise ValueError("Não houve convergência na fase líquida (mais de 100 iterações).")
        else:
            raise ValueError("Não houve convergência na fase vapor (mais de 100 iterações).")
    
    #Verificação de validade física
    if Vi <= b:
        raise ValueError(f"Volume inválido (V <= b) para a fase {'líquida' if fase.upper() == 'L' else 'vapor'}. "
                         "Isso pode indicar que as condições (T, P) não são fisicamente possíveis para esta fase com este modelo.")
        
    return Vi
    
     