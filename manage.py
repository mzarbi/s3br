from startup import on_startup
on_startup()

from server import init_app

app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')