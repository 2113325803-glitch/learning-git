import pymysql
from models import Experiment

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Hds060608@",      # ⚠️ 换成你自己的 MySQL 密码！
    "charset": "utf8mb4"
}

def get_connection(db_name="chemical_lab"):
    config = DB_CONFIG.copy()
    config["database"] = db_name
    return pymysql.connect(**config)

def load_experiments(db_name="chemical_lab"):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT id, exp_id, temperature, pressure, catalyst, yield_rate FROM experiments")
    rows = cursor.fetchall()
    experiments = []
    for row in rows:
        e = Experiment(exp_id=row[1], temperature=row[2], pressure=row[3], catalyst=row[4], yield_rate=row[5], id=row[0])
        experiments.append(e)
    cursor.close()
    conn.close()
    return experiments

def save_experiments(experiments, db_name="chemical_lab"):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM experiments")
    for e in experiments:
        cursor.execute(
            "INSERT INTO experiments (exp_id, temperature, pressure, catalyst, yield_rate) VALUES (%s, %s, %s, %s, %s)",
            (e.exp_id, e.temperature, e.pressure, e.catalyst, e.yield_rate)
        )
    conn.commit()
    cursor.close()
    conn.close()