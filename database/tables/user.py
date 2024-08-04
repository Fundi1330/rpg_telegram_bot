from .base import BaseTable

class UserTable(BaseTable):
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            telegram_id INTEGER UNIQUE,
            first_name TEXT,
            last_name TEXT
        )
        ''')

    def get_all(self):
        with self.connection:
            self.cursor.execute('''
                SELECT * FROM user
            ''')

            return self.cursor.fetchall()

    def get_first(self, telegram_id):

        with self.connection:
            self.cursor.execute('''
                SELECT * FROM user WHERE telegram_id=:telegram_id
            ''', [telegram_id])


            return self.cursor.fetchone()

    def insert(self, values):
        if not self.row_exists(values[0]):
            with self.connection:
                self.cursor.execute('''
                    INSERT INTO user (telegram_id) VALUES (:telegram_id)
                ''', values)

    def update(self, telegram_id, **kwargs):
        if self.row_exists(telegram_id):
            update_params = ' '.join([f'{k} = "{v}"' for k, v in kwargs.items()])
            with self.connection:
                self.cursor.execute(f'''
                    UPDATE user SET {update_params} WHERE telegram_id=:telegram_id
                ''', [telegram_id])

    def delete(self, telegram_id) -> None:
        '''Delete tow from table'''
        if self.row_exists(telegram_id):
            with self.connection:
                self.cursor.execute('''
                    DELETE FROM user WHERE telegram_id=:telegram_id
                ''', telegram_id)