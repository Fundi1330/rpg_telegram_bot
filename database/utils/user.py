from config import db


class User():
    @staticmethod
    def get_stats(user_id: int):
        """Gets user's stats by telegram_id"""
        return db.statstable.get_first(user_id)
    
    @staticmethod
    def get_full_name(user_id: int):
        """Gets user's full name by telegram_id"""
        user = db.usertable.get_first(user_id)
        return f'{user[2]} {user[3]}'