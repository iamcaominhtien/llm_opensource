from marshmallow import fields, Schema


class OllamaAPIGetSchema(Schema):
	question = fields.String(required=True)
