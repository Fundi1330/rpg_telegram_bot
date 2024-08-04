from sqlite_migrate import Migrations

migration = Migrations("travelrpg")

@migration()
def add_weight(db):
    db["user"].add_column("first_name", str)
    db["user"].add_column("last_name", str)