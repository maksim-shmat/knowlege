import sqlite3
conn = sqlite3.connect("datafile.db")

cursor = conn.cursor()

cursor.execute("""create table weather (id integer primary key, \
        state text, state_code text, year_text, year_code text, \
        avg_max_temp real, max_temp_count integer, max_temp_low real, \
        max_temp_high real, mac_temp_count integer, min_temp_low real, \
        min_temp_high real, heat_index real, heat_index_count integer, \
        heat_index_low real, heat_index_hegh real,heat_index_coverage \
        text)
        """)
conn.commit()

