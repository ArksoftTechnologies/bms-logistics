"""Application entry point."""
from CLIENTS import create_app

app = create_app()

if __name__ == "__main__":
    #run on local server
    app.run(host="0.0.0.0", port=5001)
