from tortoise import fields, models


class Settings(models.Model):
    name = fields.CharField(pk=True, max_length=64)
    value = fields.TextField()
    type = fields.CharField(max_length=64)

class Items(models.Model):
    name = fields.CharField(max_length=64, unique=True)

class Votes(models.Model):
    phone = fields.CharField(max_length=16)
    item = fields.ForeignKeyField(
        model_name='models.Items',
        related_name='votes'
    )
