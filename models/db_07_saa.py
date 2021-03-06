# -*- coding: utf-8 -*-
Categorias = db.define_table('saa_categorias'
    , Field('nombre')
    , Field('descripcion', 'text')
    , format='%(nombre)s'
    )

Articulos = db.define_table('saa_articulos'
    , Field('nombre')
    , Field('stock_minimo','integer')
    , Field('stock_maximo','integer')
    , Field('categoria_id', Categorias, default='1')
    , auth.signature
    , format='%(nombre)s'
    )

Egresos = db.define_table('saa_egresos'
    , Field('fecha_entrega','date', notnull=True, default=request.now)
    , Field('agente_id', Agentes)
    , Field('area_id', Areas)
    , Field('articulo_id', Articulos)
    , Field('cantidad_entregada','integer', notnull=True)
    , auth.signature
    )

Ingresos = db.define_table('saa_ingresos'
    , Field('fecha_entrega','date', notnull=True, default=request.now)
    , Field('articulo_id', Articulos)
    , Field('cantidad_recibida','integer', notnull=True)
    , Field('observaciones','text')
    , auth.signature
    )