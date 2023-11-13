from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
computers = {
    1: {
        "name": "DEXP",
        "price": 20500
    },

    2: {
        "name": "Hyper PC",
        "price": 67000
    },

    3: {
        "name": "sandalina",
        "price": 600
    }
}


@app.route('/computers/', methods=['GET'])
def returnComputersInfo():
    id = request.args.get("id")
    return jsonify(computers[int(id)])


computer_games = {
    1: {
        "name": "DOOM",
        "price": 3999
    },

    2: {
        "name": "DOOM ETERNAL",
        "price": 4999
    },

    3: {
        "name": "DOOM 2",
        "price": 799
    }
}


@app.route('/download')
def download():
    return send_file('text.txt', as_attachment=True)


@app.route('/computer_games/', methods=['GET'])
def returnComputer_gamesInfo():
    id = request.args.get("id")
    return jsonify(computer_games[int(id)])


@app.route('/film', methods=['GET'])
def returnFilm(film=None):
    film = {
        1: "10/10 film",
        2: "1/10 film"
    }
    return jsonify(film)


if __name__ == "__main__":
    app.run(debug=True)
