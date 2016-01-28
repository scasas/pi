Stock_impresoras = db.define_table('stock_impresoras'
    , Field('identificador')
    , Field('impresora_id', Impresoras)
    , Field('responsable_id', Agentes)
    , Field('area_id', Areas)
    , Field('estado', requires=IS_IN_SET(['BUENO', 'REGULAR', 'MALO']))
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
    , Field('estado', requires=IS_IN_SET(['BUENO', 'REGULAR', 'MALO']))
    , Field('nro_serie')
    , Field('fecha_compra', 'date')
    , Field('observaciones', 'text')
    , auth.signature
    )

Stock_ups_estabilizador = db.define_table('stock_ups_estabilizador'
    , Field('identificador')
    , Field('ups_estabilizador_id', Ups_estabilizador)
    , Field('responsable_id', Agentes)
    , Field('area_id', Areas)
    , Field('estado', requires=IS_IN_SET(['BUENO', 'REGULAR', 'MALO']))
    , Field('nro_serie')
    , Field('fecha_compra', 'date')
    , Field('observaciones', 'text')
    #, auth.signature
    )


Pc = db.define_table('pc'
    , Field('identificador')
    , Field('microprocesador_id', Microprocesadores)
    , Field('placa_madre_id', Placa_madre)
    , Field('disco', requires=IS_IN_SET([0, 40, 80, 160, 300, 500, 640, 1024, 2048]))
    , Field('memoria', requires=IS_IN_SET([0, 128, 256, 512, 1024, 2048, 4096, 8192]))
    , Field('so', requires=IS_IN_SET(['Windows XP', 'Windows Vista', 'Windows 7', 'Windows 8', 'Windows 10', 'Linux', 'Windows | Linux']))
    , Field('unidad_optica', requires=IS_IN_SET(['No Posee', 'CD-R', 'CD-RW', 'DVD-R', 'DVD-RW']))
    , Field('propiedad', requires=IS_IN_SET(['Particular', 'Vivienda']))
    , Field('observaciones', 'text')
    , Field('area_id', Areas)
    , Field('responsable_id', Agentes)
    # , auth.signature
    )