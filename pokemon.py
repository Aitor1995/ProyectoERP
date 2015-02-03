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
        "nombre": fields.char("Nombre", size=30, required=True),
        "tipos": fields.one2many('pokemon.tipos', 'Tipos', required=True),
        "peso": fields.float("Peso", digits=(5, 2)),
        "altura": fields.float("Altura", digits=(4, 2)),
        "habilidades": fields.one2many('pokemon.habilidades', "Habilidad", required=True),
        "habilidad_oculta": fields.many2one('pokemon.habilidades', "Habilidad oculta"),
        "generacion": fields.selection((('1', "Primera"), ('2', "Segunda"), ('3', "Tercera"), ('4', "Cuarta"),
                                        ('5', "Quinta"), ('6', "Sexta")), required=True),
    }


pokemon_pokemon()