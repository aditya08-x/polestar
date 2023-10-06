from polestar import app, initialize_db
import os

if __name__ == '__main__':
    postgres_user = os.getenv('POSTGRES_USER', 'postgres')
    postgres_password = os.getenv('POSTGRES_PASSWORD', 'password')
    postgres_host = os.getenv('POSTGRES_HOST', 'localhost')
    postgres_port = os.getenv('POSTGRES_PORT', '5433')
    postgres_db = os.getenv('POSTGRES_DB', 'polestar')
    initialize_db(postgres_user, postgres_password, postgres_host, postgres_port, postgres_db)
    app.run(debug=True, port=os.getenv('APP_PORT', '5001'), host=os.getenv('APP_HOST', '127.0.0.1'))