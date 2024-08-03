from .base import BaseTable

class StatsTable(BaseTable):
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            user_id INTEGER NOT NULL,
            strength INTEGER NOT NULL,
            agility INTEGER NOT NULL,
            stamina INTEGER NOT NULL,    
            stat_points INTEGER NOT NULL,
            energy INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user(telegram_id)                                                 
        )
        ''')

    def get_all(self):
        with self.connection:
            self.cursor.execute('''
                SELECT * FROM stats
            ''')

            return self.cursor.fetchall()

    def get_first(self, telegram_id):

        with self.connection:
            self.cursor.execute('''
                SELECT * FROM stats WHERE user_id=:telegram_id
            ''', [telegram_id])


            return self.cursor.fetchone()

    def insert(self, values):
        if not self.row_exists(values[0]):
            with self.connection:
                self.cursor.execute('''
                    INSERT INTO stats 
                    (user_id, strength, agility, stamina, stat_points, energy)
                    VALUES (:user_id, :strength, :agility, :stamina, :stat_points, :energy)
                ''', values)

    def update(self, telegram_id, **kwargs):
        if not self.row_exists(telegram_id):
            update_params = ' '.join([f'{k} = {v}' for k, v in kwargs.items()])
            with self.connection:
                self.cursor.execute(f'''
                    UPDATE stats SET {update_params} WHERE user_id=:telegram_id
                ''', telegram_id)

    def delete(self, telegram_id) -> None:
        '''Delete tow from table'''
        if self.row_exists(telegram_id):
            with self.connection:
                self.cursor.execute('''
                    DELETE FROM stats WHERE user_id=:telegram_id
                ''', telegram_id)