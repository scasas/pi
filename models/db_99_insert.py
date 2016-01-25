### First Execution After of Install.
if install:
    # add User Root
    if db(db.auth_user).isempty():
        
        items = [
            {
                'id' : 1,
                'first_name' : 'root',
                'last_name' : 'root',
                'username' : 'root',
                'password' : 'pbkdf2(1000,20,sha512)$9a059bd4c356d5b5$b61230375be4ae67527e79201730f15d6b179efc'
            },
            {
                'id' : 2,
                'first_name' : 'usuario',
                'last_name' : 'usuario',
                'username' : 'usuario',
                'password' : 'pbkdf2(1000,20,sha512)$8039f601d161c607$29b6accea95adaf89f0106eeaceaa6a52b349849'
            }
        ]
        db.auth_user.bulk_insert(items)

    # add groups
    if db(db.auth_group).isempty():
        items = [
            {'id': 1, 'role': 'admin', 'description': 'Administación'},
            {'id': 2, 'role': 'user', 'description': 'usuarios'}
        ]
        db.auth_group.bulk_insert(items)
        db.auth_membership(user_id=1, group_id=1)
        db.auth_membership(user_id=2, group_id=2)

    # add marcas
    if db(db.tab_marcas).isempty():
        items = [
        {
        'id' : 1,
        'nombre' : 'SAMSUNG',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'T',
        'memoria_ram' : 'T',
        'monitor' : 'T',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'T'
        },
        {
        'id' : 2,
        'nombre' : 'MAXTOR',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'T',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 3,
        'nombre' : 'SEAGATE',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'T',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 4,
        'nombre' : 'WESTER DIGITAL',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'T',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 5,
        'nombre' : 'LG',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'T',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 6,
        'nombre' : 'KINGSTON',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'T',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 7,
        'nombre' : 'NVIDIA',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'T',
        'impresora' : 'F'
        },
        {
        'id' : 8,
        'nombre' : 'GIGABYTE',
        'placa_madre' : 'T',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 9,
        'nombre' : 'ASROCK',
        'placa_madre' : 'T',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 10,
        'nombre' : 'INTEL',
        'placa_madre' : 'T',
        'microprocesador' : 'T',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 11,
        'nombre' : 'AMD',
        'placa_madre' : 'F',
        'microprocesador' : 'T',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'T',
        'impresora' : 'F'
        },
        {
        'id' : 12,
        'nombre' : 'HP',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'T',
        'monitor' : 'T',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'T'
        },
        {
        'id' : 13,
        'nombre' : 'KOZUMI',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'T',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 14,
        'nombre' : 'TRV',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'T',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 15,
        'nombre' : 'ATOMLUX',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'T',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 16,
        'nombre' : 'ASUS',
        'placa_madre' : 'T',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'T',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 17,
        'nombre' : 'ACER',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'T',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 18,
        'nombre' : 'BANGHO',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'T',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'F'
        },
        {
        'id' : 19,
        'nombre' : 'EPSON',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'T'
        },
        {
        'id' : 20,
        'nombre' : 'CANON',
        'placa_madre' : 'F',
        'microprocesador' : 'F',
        'disco_rigido' : 'F',
        'memoria_ram' : 'F',
        'monitor' : 'F',
        'ups_estabilizador' : 'F',
        'placa_video' : 'F',
        'impresora' : 'T'
        }
        ]
        db.tab_marcas.bulk_insert(items)

    # add motherboard
    if db(db.tab_placa_madre).isempty():
        items = [
        {
        'id' : 1,
        'marca_id' : 16,
        'modelo' : 'M5A78LM'
        },
        {
        'id' : 2,
        'marca_id' : 16,
        'modelo' : 'P5SD2-VM'
        },
        {
        'id' : 4,
        'marca_id' : 16,
        'modelo' : 'P5VDC-X'
        },
        {
        'id' : 7,
        'marca_id' : 8,
        'modelo' : 'b4567'
        }
        ]

        db.tab_placa_madre.bulk_insert(items)

    # add microprocesadoes
    if db(db.tab_microprocesadores).isempty():
        items = [
        {
        'id' : 1,
        'marca_id' : 10,
        'modelo' : 'Core i3 3120M',
        'frecuencia_trabajo' : '2.5'
        },
        {
        'id' : 2,
        'marca_id' : 10,
        'modelo' : 'Core i7 4770K',
        'frecuencia_trabajo' : '3.50'
        },
        {
        'id' : 3,
        'marca_id' : 10,
        'modelo' : 'Pentium Dual-Core E5300',
        'frecuencia_trabajo' : '2.6'
        },
        {
        'id' : 4,
        'marca_id' : 10,
        'modelo' : 'Core i5-4440',
        'frecuencia_trabajo' : '3.10'
        },
        {
        'id' : 5,
        'marca_id' : 10,
        'modelo' : 'Core i5-2310',
        'frecuencia_trabajo' : '2.9'
        },
        {
        'id' : 6,
        'marca_id' : 10,
        'modelo' : 'Core 2 Duo E6550',
        'frecuencia_trabajo' : '2.33'
        }
        ]

        db.tab_microprocesadores.bulk_insert(items)

    # add print
    if db(db.tab_impresoras).isempty():

        items = [
        {
        'id' : 1,
        'marca_id' : 12,
        'modelo' : 'LASERJET P1102W',
        'observaciones' : ''
        },
        {
        'id' : 2,
        'marca_id' : 12,
        'modelo' : 'PSC 1210',
        'observaciones' : ''
        },
        {
        'id' : 3,
        'marca_id' : 12,
        'modelo' : 'DESKJET F380',
        'observaciones' : ''
        },
        {
        'id' : 4,
        'marca_id' : 12,
        'modelo' : 'LASERJET P1006',
        'observaciones' : ''
        },
        {
        'id' : 5,
        'marca_id' : 1,
        'modelo' : 'ML2165w',
        'observaciones' : ''
        },
        {
        'id' : 6,
        'marca_id' : 12,
        'modelo' : 'PHOTOSMART D110 ALL IN ONE',
        'observaciones' : ''
        },
        {
        'id' : 7,
        'marca_id' : 12,
        'modelo' : 'Deskjet F4100',
        'observaciones' : ''
        },
        {
        'id' : 8,
        'marca_id' : 12,
        'modelo' : 'Deskjet F2100',
        'observaciones' : ''
        },
        {
        'id' : 9,
        'marca_id' : 12,
        'modelo' : 'OfficeJet 7610 e-All In One',
        'observaciones' : ''
        },
        {
        'id' : 10,
        'marca_id' : 20,
        'modelo' : 'STYLUS TX235W',
        'observaciones' : ''
        },
        {
        'id' : 11,
        'marca_id' : 12,
        'modelo' : 'OfficeJet 7500A',
        'observaciones' : ''
        },
        {
        'id' : 12,
        'marca_id' : 12,
        'modelo' : 'Deskjet F4620',
        'observaciones' : ''
        },
        {
        'id' : 13,
        'marca_id' : 20,
        'modelo' : 'STYLUS TX105',
        'observaciones' : ''
        },
        {
        'id' : 14,
        'marca_id' : 20,
        'modelo' : 'STYLUS OFFICE TX320F',
        'observaciones' : ''
        },
        {
        'id' : 15,
        'marca_id' : 12,
        'modelo' : 'OfficeJet Pro 8100',
        'observaciones' : ''
        },
        {
        'id' : 16,
        'marca_id' : 12,
        'modelo' : 'PHOTOSMART C4400',
        'observaciones' : ''
        },
        {
        'id' : 17,
        'marca_id' : 12,
        'modelo' : 'Color LaserJet CP2020',
        'observaciones' : ''
        }
        ]
        db.tab_impresoras.bulk_insert(items)

    # add monitores
    if db(db.tab_monitores).isempty():
        items = []
        db.tab_monitores.bulk_insert(items)

    # add ups | estabilizadores
    if db(db.tab_impresoras).isempty():
        items = [
        {
        'marca_id' : 14,
        'modelo' : 'NEO 500',
        'tipo' : 'UPS',
        'potencia' : '500'
        }
        ]
        db.tab_impresoras.bulk_insert(items)