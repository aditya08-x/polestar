from polestar import app, initialize_db
import os

if __name__ == '__main__':
    postgres_user = os.getenv('postgres_user', 'postgres')
    postgres_password = os.getenv('postgres_password', 'password')
    postgres_host = os.getenv('postgres_host', 'localhost')
    postgres_port = os.getenv('postgres_port', '5433')
    postgres_db = os.getenv('postgres_db', 'polestar')
    initialize_db(postgres_user, postgres_password, postgres_host, postgres_port, postgres_db)
    app.run(debug=True, port=os.getenv('app_port', '5001'), host=os.getenv('app_host', '127.0.0.1'))