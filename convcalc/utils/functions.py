import math
from conversions import *
import objetos


# General, non specific functions ==============================================================

def findlower(array, target):
    '''Return the last value in the array smaller than target and its index'''

    array = [float(x) for x in array]
    if target in array:
        return target, array.index(target)
    if target >= array[-1]:
        return array[-1], (len(array)-1)
    for i in range(len(array)-1):
        if array[i] < target and array[i+1] > target:
            return array[i], i


def findupper(array, target):
    '''Return the first value in the array greater than target and its index'''
    
    array = [float(x) for x in array]
    if target in array:
        return target, array.index(target)

    if target <= array[0]:
        return array[0], 0

    for i in range(1,len(array)):
        if array[i-1] < target and array[i] > target:
            return array[i], i

# Conveyor specific functions =======================================================================


def get_weight_on_idle():

    idles_k1

    crc = (W_b + (W_m * k1) * SI)

    return crc


def get_required_speed(capacity=None, material_cross_section_area=None, rho=None, filling=None):
    '''Return the belt speed in [m/s] to achieve a given filling ratio
    capacity: [kg/s]
    material_cross_section_area:[m2]
    rho:[kg/m3]
    '''

    beltspeed = capacity / (material_cross_section_area* filling * rho)
    return beltspeed

def get_required_speed_sm(capacity=None, material_cross_section_area=None, rho=None, filling=None):
    '''Return the belt speed in [fpm] to achieve a given filling ratio'''

    beltspeed = capacity / (material_cross_section_area* filling * rho)
    return beltspeed

def get_belt_filling(capacity=None, material_cross_section_area=None, rho=None, beltspeed=None):
    '''Return the belt filling ratio [] (CEMA ratio) '''

    filling = capacity / (material_cross_section_area* beltspeed * rho)
    return filling

def get_belt_filling_sm(capacity=None, material_cross_section_area=None, rho=None, beltspeed=None):
    '''Return the belt filling ratio [] (CEMA ratio) '''

    filling = capacity / (material_cross_section_area* beltspeed * rho)
    return filling


def get_material_cross_section_area(surcharge_angle=None, idle_angle=None, belt_width=None):

    """Return the area of the cross section of the material. In [m2]
    surcharge_angle: [degrees]
    idle_angle: [degrees]
    belt_width: [m]
    """

    # Entrada--------------------------------
    alpha = math.radians(surcharge_angle)
    beta = math.radians(idle_angle)
    b = belt_width


    # Trapezoidal area A_b---------------------------------
    c = 0.055 * b + in2m(0.9)
    lenght = 0.371 * b + in2m(0.25)
    m = (b - lenght - 2 * c) / 2
    f = m * math.cos(beta)
    j = m * math.sin(beta)
    lenght1 = lenght + 2 * f

    A_b = ((lenght + lenght1) / 2) * j

    # Surcharge area A_s --------------------------------
    r = 0.5 * lenght1 / math.sin(alpha)
    A_s = r ** 2 * (math.pi * math.degrees(alpha) / 180 - math.sin(2 * alpha) / 2)

    # Total area A_t-------------------------------------
    A_total = A_b + A_s  # [m²]
    # A_total = A_total / 144  # [ft2]
    # A_total = sqft2sqm(A_total)  # [m2]


    # print('A_b = {}  A_s = {}  A_t = {}'.format(A_b, A_s, A_t))

    return A_total


def get_material_cross_section_area_sm(surcharge_angle=None, idle_angle=None, belt_width = None):

    """Return the area of the cross section of the material. In [ft2]"""

    # Entrada--------------------------------
    alpha = math.radians(surcharge_angle)
    beta = math.radians(idle_angle)
    b = belt_width
    # Calculadas ----------------------------
    # A_s
    # A_b
    # j
    # m
    # r
    # lenght
    # lenght1
    # f
    # c

    # Trapezoidal area A_b---------------------------------
    c = 0.055*b + 0.9
    lenght = 0.371*b + 0.25
    m = (b - lenght - 2*c) / 2
    f = m * math.cos(beta)
    j = m * math.sin(beta)
    lenght1 = lenght + 2*f

    A_b = ((lenght + lenght1)/2) * j

    # Surcharge area A_s --------------------------------
    r = 0.5*lenght1/math.sin(alpha)
    A_s = r**2 * (math.pi * math.degrees(alpha)/180 - math.sin(2*alpha)/2)

    # Total area A_t-------------------------------------
    A_total = A_b + A_s  # [in²]
    A_total = A_total/144  # [ft2]

    return A_total


def choose_idle(duty=None, belt_width_inches=None, material, tables):
    '''Return the recommended idle. Calculated from NBR6678

    belt: A Belt object
    material: A Material object
    tables: A dicionary of Table objects
    conveyor: A Conveyor object
    '''
    
    # idle_placement: load, return
    # idle_type: triple, double, plane
    # rolls_angle: [degree]
    # qm: [kg/m] Material mass for length unit
    # qc: [kg/m] Belt mass for linegth unit
    # spacing: [m] Spacing between idles
    # mpm: [kg] Mass of moving parts
    
    #TODO Adicionar o calculo da força para curvas convexas (seção 7.4.4)
    

    belt_width_inches = belt.width_sm
    qm = material.mass_per_lenght
    qc = belt.mass_per_lenght
    


    g = 9.81 # Gravity [m/s²]
    kc_table = {20:0.56, 35:0.60, 45:0.64}
    kdc_table = tables['idles_kdc']
    kdr = 1.2

    # Following the calculation guide in Section 7.1
    # ========================================================
    # a) Calcular a carga atuante P_a em um rolo (secao 7.3)
    # b) Calculate P_s

    if idle_placement == 'load':
        ac = spacing
        kdc = kdc_table.get_value(material.max_lumpsize, material.density)

        if idle_type == 'triple':
            kc = kc_table[rolls_angle]
            P_a = kc * qm * ac * g
            P_s = kdc * P_a + (2/5)*qc*ac*g + mpm*g

        elif idle_type == 'double':
            P_a = (1/2) * qm * ac * g
            P_s = 1.2 * (kdc * P_a + (1/2)*qc*ac*g) + mpm*g

        elif idle_type == 'plane':
            P_a = qm * ac * g
            P_s = kdc*P_a + qc*ac*g + mpm*g
    
    if idle_placement == 'return':
        ar = spacing
        if idle_type == 'double':
            P_a = (1/2) * qc * ar * g
            P_s = 1.2*kdr * P_a + mpm*g

        elif idle_type == 'plane':
            P_a = qc * ar * g
            P_s = kdr*P_a + mpm*g

    # ========================================================
    # c) With P_s, choose the best roll in table 6

    # Find the colum of the belt width
    beltcolumns = [400,500,600,650,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]
    columnindex = beltcolumns.index(belt.width)

    # Determine wich table to use from the type from the type of idle being selected
    if idle_placement == 'load':
        if idle_type == 'double' or idle_type == 'triple':
            admissible_load_table = table1
        if idle_type == 'plane':
            admissible_load_table = table2
    if idle_placement == 'return':
        if idle_type == 'double':
            admissible_load_table = table3
        if idle_type == 'plane':
            admissible_load_table = table2

    # Find the line in the admissible load table
    columnvalues = get_column_values(admissible_load_table, columnindex)  #TODO Implementar essa função get column
    admissible_load, lineindex = findupper(columnvalues, P_s)

    series = colum_of_series(lineindex)  # TODO Implementar
    has_scale = colum_of_scale(lineindex)  # TODO Implementar


    # Construct the idle object from selected parameters
    idle = objetos.Idle()
    idle.series = series
    idle.rolls_diameter = 
    idle.scale = has_scale
    idle.number_of_rolls = {'plane':1, 'double':2, 'triple':3}[idle_type]
    idle.admissible_load = admissible_load

    return idle

def get_bearing_life():
    '''Return the expected bearing life, in []
    '''

    x = idle.number_of_rolls
    P_eq = P_s/2
    C_table = {15:7800,20:12700,}
    C = idles_dynamic_load

    l10h = (1000000/60*n) * ( (C/P_eq) ** x)

    

def banana():
    '''It just return banana'''

    return 'banana'


