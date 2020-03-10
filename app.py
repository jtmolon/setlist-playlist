from decouple import config
from flask import Flask, request
from repertorio import Repertorio


app = Flask(__name__)
app.secret_key = config("SECRET_KEY", default="secret-key")

setlist_api = Repertorio(config("SETLIST_API_KEY"))


@app.route("/repertorio/artists")
def find_artists():
    try:
        return setlist_api.artists(
            artistName=request.args["artistName"], sort="relevance"
        )
    except KeyError as error:
        return {"error": f"Missing required argument: {error}"}, 400
    except Exception as error:
        return {"error": f"Something went wrong: {error}"}, 400


if __name__ == "__main__":
    app.run(debug=True)
