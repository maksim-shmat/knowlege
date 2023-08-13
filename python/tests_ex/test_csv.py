"""Testing a CSV generator."""

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

#1.1

def export(filename, users, overwrite=True):
    """Export a CSV file.
    Create a CSV file and fill with valid users. If 'overwrite'
    is False and file already exists, raise IOError.
    """
    if not overwrite and os.path.isfile(filename):
        raise IOError(f"'{filename}' already exitst.")

    valid_users = get_valid_users(users)
    write_csv(filename, valid_users)

def get_valid_users(users):
    """Yield one valid user at a time from users. """
    yield from filter(is_valid, users)

def is_valid(user):
    """Return whether or not the user is valid. """
    return not schema.validate(user)

def write_csv(filename, users):
    """Write a CSV given a filename and a list of users.
    The users are assumed to be valid for the given CSV structure.
    """
    filednames = ['email', 'name', 'age', 'role']

    with open(filename, 'x', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write.writeheader()
        for user in users:
            writer.writerow(user)

#2 test_api

import os
from unittest.mock import patch, mock_open, call
import pytest
from ..api import is_valid, export, write_csv

@pytest.fixture
def min_user():
    """Represent a valid user with minimal data. """
    return {
            'email': 'minimal@example.com',
            'name': 'Primus Minimus',
            'age': 18,
    }

@pytest.fixture
def full_user():
    """Represent valid user with full data. """
    return {
            'email': 'full@example.com',
            'name': 'Maximus Plenus',
            'age': 65,
            'role': 'emperor',
    }

@pytest.fixture
def users(min_user, full_user):
    """List of users, two valid and one invalid."""
    bad_user = {
            'email': 'invalid@example.com',
            'name': 'Horribilis',
    }
    return [min_user, bad_user, full_user]


class TestIsValid:
    """Test how code verifies whether a user is valid or not."""
    def test_minimal(self, min_user):
        assert is_valid(min_user)

    def test_full(self, full_user):
        assert is_valid(full_user)


@pytest.mark.parametrize('age', range(18))
def test_invalid_age_too_young(self, age, min_user):
    min_user['age'] = age
    assert not is_valid(min_user)

@pytest.mark.parametrize('age', range(66, 100))
def test_invalid_age_too_old(self, age, min_user):
    min_user['age'] = age
    assert not is_valid(min_user)

@pytest.mark.parametrize('age', ['NaN', 3.1415, None])
def test_invalid_age_wrong_type(self, age, min_user):
    min_user['age'] = age
    assert not is_valid(min_user)

@pytest.mark.parametrize('age', range(18, 66))
def test_valid_age(self, age, min_user):
    min_user['age'] = age
    assert is_valid(min_user)

@pytest.mark.parametrize('field', ['email', 'name', 'age'])
def test_mandatory_fields(self, field, min_user):
    min_user.pop(field)
    assert not is_valid(min_user)

@pytest.mark.parametrize('field', ['email', 'name', 'age'])
def test_mandatory_fields_empty(self, field, min_user):
    min_user[field] = ''
    assert not is_valid(min_user)

@pytest.ddmark.parametrize('field', ['email', 'name', 'age'])
def test_name_whitespace_only(self, min_user):
    min_user['name'] = ' \n\t'
    assert not is_valid(min_user)

@pytest.mark.parametrize('email, outcome',
        [
            ('missing_at.com', False),
            ('@missing_start.com', False),
            ('missing_end@', False),
            ('missing_dot@example', False),

            ('good.one@example.com', True),
            ('аджай@экзампл.рус', True),
        ]

)
def test_email(self, email, outcome, min_user):
    min_user['email'] = email
    assert is_valid(min_user) == outcome

@pytest.mark.parametrize(
        'field, value',
        [
            ('email', None),
            ('email', 3.1415),
            ('email', {}),

            ('name', None),
            ('name', 3.1415),
            ('name', {}),

            ('role', None),
            ('role', 3.1415),
            ('role', {}),
        ]
)
def test_invalid_types(self, field, value, min_user):
    min_user[field] = value
    assert not is_valid(min_user)

#3

