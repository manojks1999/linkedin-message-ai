from app import application

if __name__ == "__main__":
    # app.init_db()
    application.run(host='0.0.0.0', port=5000)