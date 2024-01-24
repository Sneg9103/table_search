from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import get_database_schema, search_table_in_database
from .serializers import DatabaseCredentialsSerializer, DatabaseSchemaSerializer, TableSearchSerializer


class DatabaseCredentialsView(APIView):
    """
    API view to handle the submission of database credentials.

    POST method is used to submit credentials, which are then validated and processed.
    """

    def post(self, request):
        """
        Handles POST request to submit database credentials.

        Parameters:
        request (HttpRequest): The HTTP request object containing the credentials.

        Returns:
        Response: HTTP response with status indicating the result of the operation.
        """
        serializer = DatabaseCredentialsSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"status": "Credentials received"})
        return Response(serializer.errors, status=400)


class DatabaseSchemaView(APIView):
    """
    API view to retrieve database schema information.

    GET method is used to request schema information for a specified database.
    """

    def get(self, request, db_name):
        """
        Handles GET request to retrieve the schema of a specified database.

        Parameters:
        request (HttpRequest): The HTTP request object.
        db_name (str): Name of the database for which schema information is requested.

        Returns:
        Response: HTTP response containing the database schema or errors if any.
        """
        schema_data = get_database_schema(db_name) 
        serializer = DatabaseSchemaSerializer(data=schema_data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TableSearchView(APIView):
    """
    API view to search for a specific table within a database.

    GET method is used to perform the search based on the database name and table name.
    """

    def get(self, request, db_name, table_name):
        """
        Handles GET request to search for a specific table in a given database.

        Parameters:
        request (HttpRequest): The HTTP request object.
        db_name (str): Name of the database in which the search is to be performed.
        table_name (str): Name of the table to be searched.

        Returns:
        Response: HTTP response containing the search result or errors if any.
        """
        search_result = search_table_in_database(db_name, table_name) 
        serializer = TableSearchSerializer(data=search_result)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
