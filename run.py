"""Main entry point."""
from api import factory

app = factory.setup_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
