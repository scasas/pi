# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('PI'),'',
                  _class="navbar-brand",_href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller

    response.menu = [
        (T('Home'), False, URL('default', 'index'), [])
    ]

    # GRUPO COMPUTOS
    if 1 in auth.user_groups or 2 in auth.user_groups:
        response.menu += [
            (T('Equipos'), False, None,
                [
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' PC'),False, URL('equipos', 'pc'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Portatiles'),False, URL('equipos', 'portatiles'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Impresoras'),False, URL('equipos', 'stock_impresoras'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Monitores'),False, URL('equipos', 'stock_monitores'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' UPS | Estabilizador'),False, URL('equipos', 'stock_ups_estabilizador'))
                ]
            ),
            (T('Pedidos'), False, None,
                [
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' ABM'),False, URL('pedidos', 'pedidos')),
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Consulta'),False, URL('pedidos', 'consulta', vars=dict(dispositivo='pedidos',id=0)))
                ]
            ),
        ]

    # GRUPO RRHH
    if 1 in auth.user_groups or 4 in auth.user_groups:
        response.menu += [
            (T('RRHH'), False, None,
                [
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Agentes'),False, URL('rrhh', 'agentes'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Areas'),False, URL('rrhh', 'areas'))
                ]
            ),
        ]

    # GRUPO STOCK
    if 1 in auth.user_groups or 3 in auth.user_groups:
        response.menu += [
            (T('Insumos'), False, None,
                [
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Articulos'),False, URL('saa', 'articulos')),
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Ingresos'),False, URL('saa', 'ingresos')),
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Egresos'),False, URL('saa', 'egresos')),
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Stock'),False, URL('saa', 'stock'))
                ]
            ),
        ]

    # GRUPO LIBRERIA
    if 1 in auth.user_groups or 5 in auth.user_groups:
        response.menu += [
            (T('Art Libreria'), False, None,
                [
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Articulos'),False, URL('libreria', 'articulos')),
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Ingresos'),False, URL('libreria', 'ingresos')),
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Egresos'),False, URL('libreria', 'egresos')),
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Stock'),False, URL('libreria', 'stock'))
                ]
            ),
        ]

    if auth.is_logged_in():
        response.menu += [
            (T('Reportes'), False, None,
                [
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Listados'),False, URL('admin', 'list'))
                ]
            ),
        ]

    # GRUPO ADMIN
    if 1 in auth.user_groups:
        response.menu += [
            (T(' Admin'), False, None,
                [
                    (SPAN(I(_class='glyphicon glyphicon-edit'), ' Panel de Control'),False, URL('admin', 'panel_control'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Marcas'),False, URL('equipos', 'marcas'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Placa Madre'),False, URL('equipos', 'placa_madre'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Microprocesadores'),False, URL('equipos', 'microprocesadores'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Impresoras'),False, URL('equipos', 'impresoras'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Impresoras | Insumos'),False, URL('equipos', 'impresoras_insumos'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Monitores'),False, URL('equipos', 'monitores'))
                    , (SPAN(I(_class='glyphicon glyphicon-edit'), ' UPS | Estabilizador'),False, URL('equipos', 'ups_estabilizador'))
                ]
            ),
        ]

    response.menu += [
        
        (T('Ayuda'), False, None,
            [
                (SPAN(I(_class='glyphicon glyphicon-edit'), ' Acerca de PI'),False, URL('ayuda', 'acerca_de'))
                , (SPAN(I(_class='glyphicon glyphicon-edit'), ' Referencia'),False, URL('ayuda', 'referencias'))
            ]
        ),
    ]




if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu() 
