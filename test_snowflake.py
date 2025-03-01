import snowflake.connector

conn = snowflake.connector.connect(
    user="CHANDRA1702",
    account="XRTSYAM-JY92126",
    authenticator="externalbrowser"
)

cur = conn.cursor()
cur.execute("SELECT CURRENT_USER(), CURRENT_ROLE();")
print( cur.fetchall() )

cur.close()
conn.close()
