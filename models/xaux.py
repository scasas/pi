def agente_equipos(row):
    """ Se muestra el botón equipos en SQLFORM.grid """

    btn = A(I(_class='glyphicon glyphicon-eye-close'), 
            ' equipos',
            _href=URL(c='rrhh', f='agente', vars=dict(id=row.id)),
            _class='button btn btn-default')
    return btn

def area_equipos(row):
    """ Se muestra el botón equipos en SQLFORM.grid """

    btn = A(I(_class='glyphicon glyphicon-info-sign'), 
            ' equipos',
            _href=URL(c='rrhh', f='area', vars=dict(id=row.id)),
            _class='button btn btn-default')
    return btn
