class SQLGenerator:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        sql = 'SELECT '
        if fields is None:
            sql += '*'
        else:
            sql += ', '.join(fields)
        sql += f' FROM {self.table_name}'
        if condition is not None:
            sql += f' WHERE {condition}'
        sql += ';'
        return sql

    def insert(self, data):
        fields = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        sql = f'INSERT INTO {self.table_name} ({fields}) VALUES ({values});'
        return sql

    def update(self, data, condition):
        sets = ', '.join(f'{key} = \'{value}\'' for key, value in data.items())
        sql = f'UPDATE {self.table_name} SET {sets} WHERE {condition};'
        return sql

    def delete(self, condition):
        sql = f'DELETE FROM {self.table_name} WHERE {condition};'
        return sql

    def select_female_under_age(self, age):
        sql = f'SELECT * FROM {self.table_name} WHERE age < {age} AND gender = \'female\';'
        return sql

    def select_by_age_range(self, min_age, max_age):
        sql = f'SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};'
        return sql