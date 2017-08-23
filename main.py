import classes
from functions import *
from conversions import *


# Dados de entrada =====================================================================================================

transportador = classes.Conveyor()
material = classes.Material()
correia = classes.Belt


comprimento = 280  # [m]
elevacao    = 24   # [m]
capacidade = 2143  # [ton/h]
densidade_material = 1900  # [kg/m3]
angulo_acomodacao = 20  # [deg]
angulo_roletes    = 45  # [deg]
largura_correia = 54  # [in]



# Conversão das unidades de entrada=====================================================================================

capacidade = tonh2kgs(capacidade)
largura_correia = in2m(largura_correia)

# ======================================================================================================================

area_secao_material = get_material_cross_section_area(20,45,in2m(54))  # [m2]

# Seleção inicial de largura e velocidade da correia

print("Dada uma correia de {:.0f}\":".format(m2in(largura_correia)))
enchimentos = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
velocidades = []
area_secao_material = get_material_cross_section_area(20,45,largura_correia)  # [ft2]

print('\n{:4}  |  {:4}'.format('Enchimento','Velocidade [m/s]'))
for e in enchimentos:
    v = get_required_speed(capacidade, area_secao_material, densidade_material, e )
    velocidades.append(v)
    print('{:10}  |  {:4.3}'.format(e,v))


print('\nEscolhendo correia de {} m e velocidade de {} m/s'.format(largura_correia, 21.9))

# ======================================================================================================================
# Seleção dos roletes


# ======================================================================================================================




