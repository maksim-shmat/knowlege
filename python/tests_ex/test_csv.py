"""Testing CSV generator."""

#1

import os
import csv
from copy import deepcopy

from marshmallow import Schema, fields, pre_load
from marshmallow.validate import Length, Range


class UserSchema(Schema):
    """Represent a *valid* user."""
    email = fields.Email(required=True)
    name = fields.String(required=True, validate=Length(min=1))
    age = fields.Integer(
            required=True, validate=Range(min=18, max=65)
    )
    role = fields.String()

    @pre_load(pass_many=False)
    def strip_name(self, data):
        data_copy = deepcopy(data)

        try:
            data_copy['name'] = data_copy['name'].strip()
        except (AttributeError, KeyError, TypeError):
            pass
        
        return data_copy

schema = UserSchema()
