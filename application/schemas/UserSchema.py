from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError, pre_load

# Custom validator


def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(data_key='some_name')
    email = fields.Str(required=True, validate=must_not_be_blank)
    bio = fields.Str()
    created = fields.DateTime(dump_only=True)
    tags = fields.Raw()
    formatted_name = fields.Method("format_name", dump_only=True)

    def format_name(self, author):
        return "{}, {}".format(author.id, author.email)

    # Allow client to pass author's full name in request body
    # e.g. {"author': 'Tim Peters"} rather than {"first": "Tim", "last": "Peters"}
    @pre_load
    def process_author(self, data, **kwargs):
        author_name = data.get("author")
        if author_name:
            first, last = author_name.split(" ")
            author_dict = dict(first=first, last=last)
        else:
            author_dict = {}
        data["author"] = author_dict
        return data
