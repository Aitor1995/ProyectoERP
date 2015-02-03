# -*-coding:utf-8-*-

from openerp.osv import fields
from openerp.osv.orm import Model


class pokemon_tipos(Model):
    _name = "pokemon.tipos"


class pokemon_pokemon(Model):
    _name = "pokemon.pokemon"
    _rec_name = "nombre"
    _columns = {
        "nombre": fields.char("Nombre", size=30, required=True),
        # "tipos":fields.char("Nombre",size=30,required=True),
        "peso": fields.float("Peso", digits=(5, 2)),
        "altura": fields.float("Altura", digits=(4, 2)),
        # "habilidad":fields.char("Nombre",size=30,required=True),
        #"habilidad_oculta":fields.char("Nombre",size=30,required=True),
        "generacion": fields.selection((('1', "Primera"), ('2', "Segunda"), ('3', "Tercera"), ('4', "Cuarta"),
                                        ('5', "Quinta"), ('6', "Sexta")), required=True),
    }


pokemon_pokemon()