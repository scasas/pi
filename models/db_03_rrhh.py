Areas = db.define_table('areas'
    , Field('nombre')
    , Field('observaciones', 'text')
    # , auth.signature
    , format='%(nombre)s'
    )

Agentes = db.define_table('agentes'
    , Field('apellido')
    , Field('nombres')
    , Field('area_id', Areas)
    , Field('domicilio')
    , Field('dni')
    , Field('tel_coorporativo')
    , Field('tel_celular')
    , Field('tel_fijo')
    , Field('sexo', requires=IS_IN_SET(['M', 'F']))
    # , auth.signature
    , format='%(apellido)s %(nombres)s'
    # , common_filter=lambda q: db['agentes'].is_active == True
    )
