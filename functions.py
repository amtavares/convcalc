import math
from conversions import *




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







