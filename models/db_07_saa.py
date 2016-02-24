# -*- coding: utf-8 -*-
Categorias = db.define_table('saa_categorias'
    , Field('nombre')
    , Field('descripcion')
    , format='%(nombre)s'
    )

Articulos = db.define_table('saa_articulos'
    , Field('nombre')
    , Field('stock_minimo','integer')
    , Field('stock_maximo','integer')
    , Field('categoria_id', Categorias)
    , auth.signature
    , format='%(nombre)s'
    )

# Articulos = db.define_table('si_stock_articulos'
#     , Field('si_tab_articulos_id', Tab_insumos)
#     , Field('cantidad')
#     )

Egresos = db.define_table('saa_egresos'
    , Field('fecha_entrega','date', notnull=True, default=request.now)
    , Field('agente_id', Agentes)
    , Field('area_id', Areas)
    , Field('articulo_id', Articulos)
    , Field('cantidad_entregada','integer')
    , auth.signature
    )

Ingresos = db.define_table('saa_ingresos'
    , Field('fecha_entrega','date', notnull=True, default=request.now)
    , Field('articulo_id', Articulos)
    , Field('cantidad_recibida','integer')
    , Field('observaciones','text')
    , auth.signature
    )
