import classes.objetos
import utils

# from utils.functions import *
# from conversions import *

# TODO Quando calcular a area da seção de material, fazer update da propriedade mass_per_lenght no material

# Option settings


# ======================================================================================================================
# Constantes
TABLES_PATH = 'convcalc/tables/'

# Dados de entrada =====================================================================================================

transportador = objetos.Conveyor()
material = objetos.Material()
correia = objetos.Belt


comprimento = 280  # [m]
elevacao    = 24   # [m]
capacidade = 2143  # [ton/h]
densidade_material = 1900  # [kg/m3]
angulo_acomodacao = 20  # [deg]
angulo_roletes    = 45  # [deg]
largura_correia_sm = 54  # [in]



# Conversão das unidades de entrada=====================================================================================

capacidade = tonh2kgs(capacidade)
largura_correia = in2m(largura_correia_sm)

# ======================================================================================================================
# Inicializa todas as tabelas que serão utilizadas durante o calculo

def load_tables(tables_names = None):
    tables = dict()
    if not tables_names:
        tables_names = ['idles_k1', 'idles_kdc']
    
    for table_name in tables_names:
        tables[table_name] = objetos.Table('{}{}.csv'.format(TABLES_PATH,table_name))

    print('Tables loaded:\n{}'.format(tables_names))
    return tables

tables = load_tables()
# t = tables['idles_k1']
# print(   t )
# print(   t.dataframe.index )
# print(   t.get_value(4,150)   )

# ======================================================================================================================

area_secao_material = get_material_cross_section_area(20,45,in2m(54))  # [m2]

# Seleção inicial de largura e velocidade da correia
# A partir de uma largura de correia (chutada) inicialmente, mostra uma tabela de enchimentos em função
# da velocidade, para que o usuário selecione a velocidade desejada
# TODO implementar a possibilidade de mudança da largura da correia

print("Dada uma correia de {:.0f}\":".format(largura_correia_sm))
enchimentos = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
velocidades = []
area_secao_material = get_material_cross_section_area(20,45,largura_correia)

print('\n{:4}  |  {:4}'.format('Enchimento','Velocidade [m/s]'))
for e in enchimentos:
    v = get_required_speed(capacidade, area_secao_material, densidade_material, e )
    velocidades.append(v)
    print('{:10}  |  {:4.3}'.format(e,v))


print('\nEscolhendo correia de {} m e velocidade de {} m/s'.format(largura_correia_sm, 21.9))

# ======================================================================================================================
# Seleção dos roletes

'''[seção 3.2] A seleção correta da classe e do diâmetro dos rolos depende de alguns fatores, tais como
o tipo de serviço, condições de operação, carga e velocidade da correia. Para facilitar a
seleção dos roletes, eles foram divididos em categorias, conforme tabela 2.'''

idle = choose_idle('medium', largura_correia_sm)


# ======================================================================================================================




