from flask import Flask, render_template_string
import mysql.connector
import sys

app = Flask(__name__)

def get_db_connection():
    try:
        # Verbinding via de hostname 'ops-server' (Docker DNS op OSI Laag 3)
        connection = mysql.connector.connect(
            host="ops-server",
            user="root",
            password="test1234!",
            database="OperatingSystems",
            port=3306
        )
        return connection
    except Exception as e:
        print(f"Error connecting to MariaDB: {e}")
        return None

@app.route('/')
def index():
    db = get_db_connection()
    if not db:
        return "<h1>Fout!</h1><p>Kon geen verbinding maken met de database-server op poort 3306.</p>"
    
    cursor = db.cursor(dictionary=True)
    
    # We halen data op uit de 3 tabellen voor de demo
    cursor.execute("SELECT * FROM commands LIMIT 5")
    commands = cursor.fetchall()
    
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    cursor.execute("SELECT * FROM server_logs ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    
    db.close()

    # Eenvoudige HTML om de data te tonen (De Frontend rol)
    html_template = """
    <html>
        <head><title>OS & Netwerken Demo</title></head>
        <body style="font-family: sans-serif; padding: 20px;">
            <h1>Systeem Dashboard (3-Tier Demo)</h1>
            <hr>
            <h2>1. Gebruikers (Tabel: users)</h2>
            <ul> {% for user in users %} <li>{{ user.username }} - Rol: {{ user.role }}</li> {% endfor %} </ul>
            
            <h2>2. Monitoring (Tabel: server_logs)</h2>
            <table border="1">
                <tr><th>Event</th><th>Tijdstip</th></tr>
                {% for log in logs %} <tr><td>{{ log.event }}</td><td>{{ log.timestamp }}</td></tr> {% endfor %}
            </table>

            <h2>3. OS Commando's (Tabel: commands)</h2>
            <p>Eerste 5 commando's uit de database: 
               {% for cmd in commands %} <b>{{ cmd.commandName }}</b>, {% endfor %} ...
            </p>
        </body>
    </html>
    """
    return render_template_string(html_template, users=users, logs=logs, commands=commands)

if __name__ == '__main__':
    # host='0.0.0.0' zorgt dat de app bereikbaar is buiten de container
    app.run(host='0.0.0.0', port=5000)

