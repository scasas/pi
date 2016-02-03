def control_reponsable_id(reg):
    if (reg.responsable_id > 0):
        auxiliar = str(reg.responsable_id.apellido) + ', ' + str(reg.responsable_id.nombres)
    else:
        auxiliar = ' '
    return auxiliar