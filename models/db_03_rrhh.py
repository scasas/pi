Areas = db.define_table('areas'
    , Field('nombre')
    , Field('observaciones', 'text')
    , auth.signature
    , format='%(nombre)s'
    )

Agentes = db.define_table('agentes'
    , Field('apellido')
    , Field('nombres')
    , Field('domicilio')
    , Field('dni')
    , Field('tel_coorporativo')
    , Field('tel_celular')
    , Field('tel_fijo')
    , Field('area_id', Areas)
    , auth.signature
    , format='%(apellido)s %(nombres)s'
    # , migrate=True
    )