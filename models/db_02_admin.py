Marcas = db.define_table('tab_marcas'
    , Field('nombre'
        , required=True
        , notnull=True
        , requires=IS_NOT_EMPTY('Ingrese el nombre de la Marca')
        , label=T('Marca'))
    , Field('placa_madre', 'boolean', default=False)
    , Field('microprocesador', 'boolean', default=False)
    , Field('disco_rigido', 'boolean', default=False)
    , Field('memoria_ram', 'boolean', default=False)
    , Field('monitor', 'boolean', default=False)
    , Field('ups_estabilizador', 'boolean', default=False)
    , Field('placa_video', 'boolean', default=False)
    , Field('impresora', 'boolean', default=False)
    # , auth.signature
    , format='%(nombre)s'
    )


# IMPRESORAS -------------------------------------------------------------------
Impresoras = db.define_table('tab_impresoras'
    , Field('marca_id', Marcas)
    , Field('modelo')
    , Field('costo_aproximado')
    , Field('conexion_red', requires=IS_IN_SET(['No Posee','Ethernet', 'Wifi']))
    , Field('observaciones', 'text')
    # , auth.signature
    , format=lambda r: r.marca_id.nombre + ' ' + r.modelo or 'anónimo'
    )

Impresoras_insumos = db.define_table('impresoras_insumos'
    , Field('impresora_id', Impresoras)
    , Field('tipo', requires=IS_IN_SET(['Toner', 'Cartucho']))
    , Field('modelo')
    , Field('Color', requires=IS_IN_SET(['Negro', 'Amarillo', 'Cyan', 'Magenta', 'Tricolor']))
    , Field('observaciones', 'text')
    )


# MONITORES --------------------------------------------------------------------
Monitores = db.define_table('tab_monitores'
    , Field('marca_id', Marcas)
    , Field('modelo')
    , Field('pulgadas'
        , requires=IS_IN_SET(tab_pulgadas)
        )
    , Field('tipo'
        , requires=IS_IN_SET(['CRT','LCD','LED','PLASMA'])
        )
    , Field('observaciones', 'text')
    # , auth.signature
    , format=lambda r: r.marca_id.nombre + ' ' + r.modelo + ' ' + r.pulgadas + '" ' + r.tipo or 'anónimo'
    )


# UPS | ESTABILIZADORES --------------------------------------------------------
Ups_estabilizador = db.define_table('tab_ups_estabilizador'
    , Field('marca_id', Marcas)
    , Field('modelo')
    , Field('tipo', requires=IS_IN_SET(['UPS','ESTABILIZADOR']))
    , Field('potencia', requires=IS_IN_SET(['500', '650', '800', '1000', '1200', '1500', '2000' ]))
    # , Field('autonomia', 'boolean', default=True)
    , format=lambda r: r.marca_id.nombre + ' ' + r.modelo + ' ' + r.tipo or ' '
    )

# PC & COMPONENTES ------------------------------------------------------------
Microprocesadores = db.define_table('tab_microprocesadores'
    , Field('marca_id', Marcas)
    , Field('modelo')
    , Field('frecuencia_trabajo')
    , Field('observaciones')
    # , auth.signature
    , format=lambda r: r.marca_id.nombre + ' ' + r.modelo + ' ' + r.frecuencia_trabajo
    )

Placa_madre = db.define_table('tab_placa_madre'
    , Field('marca_id', Marcas)
    , Field('modelo')
    , Field('observaciones')
    # , auth.signature
    , format=lambda r: r.marca_id.nombre + ' ' + r.modelo
    )