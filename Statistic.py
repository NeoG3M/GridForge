import sqlite3


class Statistic:
    def __init__(self):
        self.connection = sqlite3.connect("data/statistic_db")

    def add_victory(self):
        self.connection.cursor().execute("UPDATE user_statistic SET victories = victories + 1")

    def get_count_of_victories(self):
        return self.connection.cursor().execute("SELECT victories FROM user_statistic").fetchone()[0]

    def add_shot(self):
        self.connection.cursor().execute("UPDATE user_statistic SET shots_count = shots_count + 1")

    def get_count_of_shots(self):
        return self.connection.cursor().execute("SELECT shots_count FROM user_statistic").fetchone()[0]

    def add_upgrade(self):
        self.connection.cursor().execute("UPDATE user_statistic SET upgrades_count = upgrades_count + 1")

    def get_count_of_upgrades(self):
        return self.connection.cursor().execute("SELECT upgrades_count FROM user_statistic").fetchone()[0]

    def add_game(self):
        self.connection.cursor().execute("UPDATE user_statistic SET games_count = games_count + 1")

    def get_count_of_games(self):
        return self.connection.cursor().execute("SELECT games_count FROM user_statistic").fetchone()[0]

    def add_towers(self):
        self.connection.cursor().execute("UPDATE user_statistic SET towers_count = towers_count + 1")

    def get_count_of_towers(self):
        return self.connection.cursor().execute("SELECT towers_count FROM user_statistic").fetchone()[0]

    def add_enemy(self):
        self.connection.cursor().execute("UPDATE user_statistic SET killed_enemies = killed_enemies + 1")

    def get_count_of_enemies(self):
        return self.connection.cursor().execute("SELECT killed_enemies FROM user_statistic").fetchone()[0]

    def add_money(self, money):
        self.connection.cursor().execute("UPDATE user_statistic SET money = money + {}", (money,))

    def get_count_of_money(self):
        return self.connection.cursor().execute("SELECT money FROM user_statistic").fetchone()[0]

    def close(self):
        self.connection.close()

    def delete_achievements(self):
        self.connection.cursor().execute(
            """UPDATE user_statistic SET 
                (killed_enemies, victories, games_count, towers_count, upgrades_count, shots_count) =
                (0, 0, 0, 0, 0, 0)
            """
        )

    def get_victory_percent(self):
        return (self.get_count_of_victories() / self.get_count_of_games()) * 100