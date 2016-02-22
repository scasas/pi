# para hacer uso de la funcion usamos 
# from applications.pi.modules.tools import *

def control_reponsable_id(reg):
    if (reg.responsable_id > 0):
        auxiliar = str(reg.responsable_id.apellido) + ', ' + str(reg.responsable_id.nombres)
    else:
        auxiliar = ' '
    return auxiliar.upper()

def control_placa_madre_id(reg):
    if reg.placa_madre_id > 0:
        placa_madre = reg.placa_madre_id.marca_id.nombre + ' ' + reg.placa_madre_id.modelo
    else:
        placa_madre = ''

    return placa_madre.upper()

def control_microprocesador_id(reg):
    if reg.microprocesador_id > 0:
        micro = reg.microprocesador_id.marca_id.nombre + ' ' + reg.microprocesador_id.modelo
    else:
        micro = ''
    return micro.upper()