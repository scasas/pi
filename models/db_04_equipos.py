Stock_impresoras = db.define_table('stock_impresoras'
    , Field('identificador')
    , Field('impresora_id', Impresoras)
    , Field('responsable_id', Agentes)
    , Field('area_id', Areas)
    , Field('estado', requires=IS_IN_SET(tab_estado, error_message='Debes seleccionar el estado de la impresora'))
    , Field('nro_serie')
    , Field('fecha_compra', 'date')
    , Field('observaciones', 'text')
    # , auth.signature
    )

Stock_monitores = db.define_table('stock_monitores'
    , Field('identificador')
    , Field('monitor_id', Monitores)
    , Field('responsable_id', Agentes)
    , Field('area_id', Areas)
    , Field('estado', requires=IS_IN_SET(tab_estado))
    , Field('nro_serie')
    , Field('fecha_compra', 'date')
    , Field('observaciones', 'text')
    # , auth.signature
    )

Stock_ups_estabilizador = db.define_table('stock_ups_estabilizador'
    , Field('identificador')
    , Field('ups_estabilizador_id', Ups_estabilizador)
    , Field('responsable_id', Agentes)
    , Field('area_id', Areas)
    , Field('estado', requires=IS_IN_SET(tab_estado))
    , Field('nro_serie')
    , Field('fecha_compra', 'date')
    , Field('observaciones', 'text')
    #, auth.signature
    )


Pc = db.define_table('pc'
    , Field('identificador')
    , Field('microprocesador_id', Microprocesadores)
    , Field('placa_madre_id', Placa_madre)
    , Field('disco', requires=IS_IN_SET(tab_disco))
    , Field('memoria', requires=IS_IN_SET(tab_memoria))
    , Field('so', requires=IS_IN_SET(tab_so))
    , Field('unidad_optica', requires=IS_IN_SET(tab_unidad_optica))
    , Field('observaciones', 'text')
    , Field('area_id', Areas)
    , Field('responsable_id', Agentes)
    , Field('estado', requires=IS_IN_SET(tab_estado))
    # , auth.signature
    )

# PORTATILES ----------------------------------------------------------------------
Portatiles = db.define_table('portatiles'
    , Field('identificador')
    , Field('responsable_id', Agentes)
    , Field('area_id', Areas)
    , Field('tipo', requires=IS_IN_SET(['Notebook', 'All in One']))
    , Field('marca_id', Marcas)
    , Field('modelo')
    , Field('microprocesador_id', Microprocesadores)
    , Field('disco', requires=IS_IN_SET(tab_disco))
    , Field('memoria', requires=IS_IN_SET(tab_memoria))
    , Field('pulgadas', requires=IS_IN_SET(tab_pulgadas))
    , Field('unidad_optica', requires=IS_IN_SET(tab_unidad_optica))
    , Field('so', requires=IS_IN_SET(tab_so))
    , Field('propietario', requires=IS_IN_SET(['Vivienda', 'Particular | Personal']), default='Vivienda')
    , Field('estado', requires=IS_IN_SET(tab_estado))
    , Field('observaciones', 'text')
    # , auth.signature
    )


# DIRECCION DE RED ----------------------------------------------------------------------
IP = db.define_table('direcciones_ip'
    , Field('direccion', notnull=True, length=12, unique=True)
    , Field('dispositivo_tipo', requires=IS_IN_SET(tab_dispositivo, error_message='Debes seleccionar el dispositivo') )
    , Field('dispositivo_id')
    , Field('dispositivo_otro', label="Vinculacion")
    # , auth.signature
    )

MAC = db.define_table('direcciones_mac'
    , Field('direccion', notnull=True, length=17, unique=True)
    , Field('dispositivo_tipo', requires=IS_IN_SET(tab_dispositivo, error_message='Debes seleccionar el dispositivo') )
    , Field('dispositivo_id')
    , Field('dispositivo_otro', label="Vinculacion")
    # , auth.signature
    )