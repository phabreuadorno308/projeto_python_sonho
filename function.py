import wrapt
import math

def calculate_velocity(target: tuple, current: tuple) -> list:
    """
    Função que calcula velocidade em plano bidimensional

    Args:
        target (tupla): posição alvo do robô ([px, py, yaw])
        current (tupla): posição atual do robô ([rx, ry, ryaw])
    Returns:
        vel (list): lista com comando de velocidade ([vx, w])
    """
    
    # Constantes
    k_a = 0.5 # -> quão angular vai
    k_b = 0.5 # -> quão linear vai

    # vel = [vx, w] -> Padrão nula
    vel = [0.0, 0.0]

    # Primeiro ajusta ângulo via tangente
    dy = target[1] - current[1]
    dx = target[0] - current[0]

    if dx > 0 and dy > 0:
        # Ir para primeiro quadrante
        ...
    
    
    dif_ang = math.atan2()

    if dif_ang > 0:
        avan_ang = k_a * dif_ang
        vel = [0.0, avan_ang]
        return vel

    if dif_ang < 0:
        avan_ang = -(k_a * dif_ang)
        vel = [0.0, avan_ang]
        return vel

    # Ajusta avanço linear
    # só vem pra cá qunaod o dif ang é zero, NUNCA é zero, precisamos de uma tolerância
    delta_x = target[0] - current[0]
    delta_y = target[1] - current[1]
    dif_lin = (delta_x**2 + delta_y**2)**(1/2)

    if dif_lin != 0:
        avan_lin = k_b * dif_lin
        vel = [avan_lin, 0.0]

    return vel


# --- Dúvidas ---
# 1. Código está do jeito que esperam (quão complexo deve ser)
# 2. Se considera vel atual lin e ang (visto que não há como ter histórico sem var estáticas e sem main)
