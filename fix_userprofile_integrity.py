import sqlite3

# Connect to your SQLite database (ensure the path is correct)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Run your SQL query to find invalid user_id values (use 'user_id' field)
cursor.execute("SELECT * FROM webapp_userprofile WHERE user_id NOT IN (SELECT id FROM auth_user);")
rows = cursor.fetchall()

# Print out the results (optional)
if rows:
    print("Found invalid user_id values:")
    for row in rows:
        print(row)
else:
    print("No invalid user_id values found.")

# If you need to delete the invalid rows
cursor.execute("DELETE FROM webapp_userprofile WHERE user_id NOT IN (SELECT id FROM auth_user);")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Integrity fixed and invalid rows deleted.")
