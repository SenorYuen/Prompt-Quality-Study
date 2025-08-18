'''
# This class generates SQL statements for common operations on a table, such as SELECT, INSERT, UPDATE, and DELETE.

class SQLGenerator:
    def __init__(self, table_name):
        """
        Initialize the table name.
        """

    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :return: str. The generated SQL statement.
        """

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :return: str. The generated SQL statement.
        """


    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :return: str. The generated SQL statement.
        """

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :return: str. The generated SQL statement.
        """

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :return: str. The generated SQL statement.
        """

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :return: str. The generated SQL statement.
        """
'''


class SQLGenerator:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        if fields is None:
            fields = "*"
        else:
            fields = ", ".join(fields)
        sql = f"SELECT {fields} FROM {self.table_name}"
        if condition is not None:
            sql += f" WHERE {condition}"
        return sql + ";"

    def insert(self, data):
        fields = ", ".join(data.keys())
        values = ", ".join([f"'{value}'" for value in data.values()])
        sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({values})"
        return sql + ";"

    def update(self, data, condition):
        set_clause = ", ".join([f"{field} = '{value}'" for field, value in data.items()])
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}"
        return sql + ";"

    def delete(self, condition):
        sql = f"DELETE FROM {self.table_name} WHERE {condition}"
        return sql + ";"

    def select_female_under_age(self, age):
        condition = f"age < {age} AND gender = 'female'"
        return self.select(condition=condition)

    def select_by_age_range(self, min_age, max_age):
        condition = f"age BETWEEN {min_age} AND {max_age}"
        return self.select(condition=condition)
