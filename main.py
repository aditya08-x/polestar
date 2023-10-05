from polestar import app, initialize_db

if __name__ == '__main__':
    postgres_user = 'postgres'
    postgres_password = 'password'
    postgres_host = 'localhost'
    postgres_port = '5433'
    postgres_db = 'polestar'
    initialize_db(postgres_user, postgres_password, postgres_host, postgres_port, postgres_db)
    app.run(debug=True)