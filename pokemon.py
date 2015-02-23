# -*-coding:utf-8-*-
from openerp.osv import fields
from openerp.osv.orm import Model


class pokemon_tipos(Model):
    _name = "pokemon.tipos"
    _rec_name = "nombre"
    _columns = {
        "nombre": fields.char("Nombre", size=30, required=True),
    }


pokemon_tipos()


class pokemon_habilidades(Model):
    _name = "pokemon.habilidades"
    _rec_name = "nombre"
    _columns = {
        "nombre": fields.char("Nombre", size=50, required=True),
        "efecto": fields.text("Efecto"),
    }


pokemon_habilidades()


class pokemon_pokemon(Model):
    _name = "pokemon.pokemon"
    _rec_name = "nombre"
    _columns = {
        "numero": fields.integer("Número", required=True),
        "nombre": fields.char("Nombre", size=30, required=True),
        "generacion": fields.selection((('1', "Primera"), ('2', "Segunda"), ('3', "Tercera"), ('4', "Cuarta"),
                                        ('5', "Quinta"), ('6', "Sexta")), "Generación", required=True),
        "imagen": fields.binary('Imagen', help='Imágen del pokemon'),
        "descripcion_pokedex": fields.text('Descripción Pokédex'),
        "tipo": fields.many2one('pokemon.tipos', 'Tipo', required=True),
        'tiene_tipo_2': fields.boolean('¿Dos tipos?'),
        "tipo2": fields.many2one('pokemon.tipos', 'Tipo 2'),
        "peso": fields.float("Peso", digits=(5, 2)),
        "altura": fields.float("Altura", digits=(4, 2)),
        "habilidad": fields.many2one('pokemon.habilidades', 'Habilidad', required=True),
        'tiene_habilidad_2': fields.boolean('¿Dos habilidades?'),
        "habilidad2": fields.many2one('pokemon.habilidades', 'Habilidad 2'),
        "habilidad_oculta": fields.many2one('pokemon.habilidades', "Habilidad oculta"),
        "ps_base": fields.integer("PS"),
        "ataque_base": fields.integer("Ataque"),
        "defensa_base": fields.integer("Defensa"),
        "ataque_especial_base": fields.integer("Ataque especial"),
        "defensa_especial_base": fields.integer("Defensa especial"),
        "velocidad_base": fields.integer("Velocidad"),
        'color': fields.integer('Color Index'),
    }


pokemon_pokemon()