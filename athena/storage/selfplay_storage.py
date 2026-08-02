import sqlite3
from dataclasses import asdict

from athena.selfplay.history import MatchHistory


class SelfPlayStorage:


    def __init__(self, db_path="selfplay.db"):

        self.db_path = db_path

        self._init_db()



    def _connect(self):

        return sqlite3.connect(
            self.db_path
        )



    def _init_db(self):

        conn = self._connect()

        cursor = conn.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS matches (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                model_a TEXT,

                model_b TEXT,

                winner TEXT,

                score_a REAL,

                score_b REAL,

                elo_a_before REAL,

                elo_b_before REAL,

                elo_a_after REAL,

                elo_b_after REAL,

                episodes INTEGER,

                timestamp TEXT

            )
            """
        )


        conn.commit()

        conn.close()



    # compatibility layer
    def save(self, match: MatchHistory):

        return self.save_match(match)



    def save_match(self, match: MatchHistory):

        data = asdict(match)


        conn = self._connect()

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO matches (

                model_a,
                model_b,
                winner,
                score_a,
                score_b,
                elo_a_before,
                elo_b_before,
                elo_a_after,
                elo_b_after,
                episodes,
                timestamp

            )

            VALUES (?,?,?,?,?,?,?,?,?,?,?)

            """,

            (

                data["model_a"],
                data["model_b"],
                data["winner"],
                data["score_a"],
                data["score_b"],
                data["elo_a_before"],
                data["elo_b_before"],
                data["elo_a_after"],
                data["elo_b_after"],
                data.get("episodes", 1),
                data["timestamp"]

            )
        )


        conn.commit()

        conn.close()


        return match



    def get_all(self):

        conn = self._connect()

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT

            model_a,
            model_b,
            winner,
            score_a,
            score_b,
            elo_a_before,
            elo_b_before,
            elo_a_after,
            elo_b_after,
            episodes,
            timestamp

            FROM matches

            ORDER BY id ASC

            """
        )


        rows = cursor.fetchall()


        conn.close()


        return rows



    def count(self):

        conn = self._connect()

        cursor = conn.cursor()


        cursor.execute(
            "SELECT COUNT(*) FROM matches"
        )


        result = cursor.fetchone()[0]


        conn.close()


        return result



    def clear(self):

        conn = self._connect()

        cursor = conn.cursor()


        cursor.execute(
            "DELETE FROM matches"
        )


        conn.commit()

        conn.close()