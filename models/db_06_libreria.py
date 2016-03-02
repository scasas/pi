# -*- coding: utf-8 -*-
Articulos_lib = db.define_table('lib_articulos'
    , Field('nombre')
    , Field('stock_minimo','integer')
    , Field('stock_maximo','integer')
    , auth.signature
    , format='%(nombre)s'
    )

Egresos_lib = db.define_table('lib_egresos'
    , Field('fecha_entrega','date', notnull=True, default=request.now)
    , Field('agente_id', Agentes)
    , Field('area_id', Areas)
    , Field('articulo_id', Articulos_lib)
    , Field('cantidad_entregada','integer', notnull=True)
    , auth.signature
    )

Ingresos_lib = db.define_table('lib_ingresos'
    , Field('fecha_entrega','date', notnull=True, default=request.now)
    , Field('articulo_id', Articulos_lib)
    , Field('cantidad_recibida','integer', notnull=True)
    , Field('observaciones','text')
    , auth.signature
    )