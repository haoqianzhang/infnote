import bson

from rest_framework import serializers


class ObjectIdField(serializers.CharField):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return bson.ObjectId(data)


class TimestampField(serializers.DateTimeField):
    def to_representation(self, value):
        timestring = super(TimestampField, self).to_representation(value)
        return int(timestring)

    def to_internal_value(self, value):
        super(TimestampField, self).to_internal_value(str(value))
