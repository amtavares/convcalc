
# Lenght units=======================================

def in2m(value):
    return value*0.0254

def m2in(value):
    return value/0.0254

def ft2m(value):
    return value*0.3048

def m2ft(value):
    return value/0.3048

# Area units =======================================

def sqft2sqm(value):
    return value * 0.092903

def sqm2sqft(value):
    return value / 0.092903

# Speed units ====================================

def fpm2mps(value):
    return value * 5.08E-3

def mps2fpm(value):
    return value / 5.08E-3

# Material flow =================================

def tonh2kgs(value):
    return value*(1000/3600)

def tonh2kgs(value):
    return value/(1000/3600)

# Density ========================================

def lbft32kgm3(value):
    return value * 16.016949

def kgm32lbft3(value):
    return value / 16.016949
