#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, BooleanField
from wtforms import SelectField, FieldList, FormField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane. Spierdalaj :).'

class OdpForm(FlaskForm):
    id = HiddenField("Odpowiedz id")
    pytanie = HiddenField("Pytanie id")
    odpowiedz = StringField("Opowiedź: ",
                            validators=[Required(message=blad1)],
                            render_kw={'class': 'form-control'})
    odpok = BooleanField('Poprawna: ', render_kw={'class': 'form-control'})
    
class PytanieForm(FlaskForm):
    pytanie = StringField("Treść Pytania: ",
                            validators=[Required(message=blad1)],
                            render_kw={'class': 'form-control'})
    kategoria = SelectField('Kategoria')
    odpowiedzi = FieldList(FormField(OdpForm), min_entries = 3)
