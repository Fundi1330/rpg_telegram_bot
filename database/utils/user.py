from config import db


class User():
    @staticmethod
    def get_stats(user_id: int):
        """Gets user's stats by telegram_id"""
        return db.statstable.get_first(user_id)