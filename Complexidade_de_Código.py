"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
# o código precisa ser fácil de ser lido

velocidade = 61 #velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velociade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

vel_car_pass_radar_1 = velocidade > RADAR_1
carro_multado = local_carro >= local_carro >=(LOCAL_1 - RADAR_RANGE) and \
    local_carro <=(LOCAL_1 + RADAR_RANGE)

if vel_car_pass_radar_1:
    print('Velocidade do carro passou do radar 1')
    
if carro_multado and vel_car_pass_radar_1:
    print('Carro multado em radar 1')