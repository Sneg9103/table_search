from rest_framework import serializers

class DatabaseCredentialsSerializer(serializers.Serializer):
    host = serializers.CharField(max_length=100)
    port = serializers.IntegerField()
    database_name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class TableSearchSerializer(serializers.Serializer):
    table_name = serializers.CharField()
    columns = serializers.JSONField()

class DatabaseSchemaSerializer(serializers.Serializer):
    database_name = serializers.CharField()
    tables = TableSearchSerializer(many=True)