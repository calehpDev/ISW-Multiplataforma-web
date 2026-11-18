from app import create_app

app = create_app()

if __name__ == '__main__':
    # El puerto 5000 debe coincidir con el permitido en tu Security Group sg-web
    app.run(host='0.0.0.0', port=5000, debug=True)