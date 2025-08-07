class SQLGenerator:
    def __init__(self, table_name):
        """
        Initialize the table name.
        """
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :return: str. The generated SQL statement.
        """
        fields_part = ', '.join(fields) if fields else '*'
        condition_part = f" WHERE {condition}" if condition else ''
        return f"SELECT {fields_part} FROM {self.table_name}{condition_part};"

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :return: str. The generated SQL statement.
        """
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        return f"INSERT INTO {self.table_name} ({columns}) VALUES ({values});"

    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :return: str. The generated SQL statement.
        """
        set_part = ', '.join(f"{key} = '{value}'" for key, value in data.items())
        condition_part = f" WHERE {condition}" if condition else ''
        return f"UPDATE {self.table_name} SET {set_part}{condition_part};"

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :return: str. The generated SQL statement.
        """
        condition_part = f" WHERE {condition}" if condition else ''
        return f"DELETE FROM {self.table_name}{condition_part};"

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :return: str. The generated SQL statement.
        """
        return f"SELECT * FROM {self.table_name} WHERE gender = 'female' AND age < {age};"

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :return: str. The generated SQL statement.
        """
        return f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"