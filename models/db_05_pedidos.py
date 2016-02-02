# PEDIDOS ----------------------------------------------------------------------
Pedidos = db.define_table('pedidos'
    , Field('identificador')
    , Field('personal_id', Agentes)
    # , Field('dispositivo', requires=IS_IN_SET(['pc', 'monitor', 'notebook', 'impresora', 'UPS | Estabilizador', 'celular', 'ninguno de los anteriores']))
    , Field('fecha_solicitud', 'date', notnull=True, default=request.now)
    , Field('problema_tipo', requires=IS_IN_SET(['Compartida', 'Internet', 'Impresion', 'Ofimatica', 'Virus', 'Software', 'Hardware', 'Sistemas', 'Otros']))
    , Field('problema_detalle', 'text', notnull=True)
    , Field('problema_solucion_propuesta', 'text')
    , Field('problema_estado', requires=IS_IN_SET(['Realizado', 'Inconcluso', 'Pendiente']))
    , Field('personal_computos_id',Agentes)
    , Field('observaciones', 'text')
    # , Field('reparar', 'boolean', default=False)
    # , auth.signature
    )