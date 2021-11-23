from flask import Flask, url_for, request, redirect, abort, jsonify

from MoviesDao import moviesDAO


app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/dvds')
def getAll():
    return jsonify(moviesDAO.getAll())


@app.route('/dvds/<int:id>')
def findById(id):
    return jsonify(moviesDAO.findByID(id))


@app.route('/dvds', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    dvd = {
        "id": request.json["id"],
        "title": request.json["title"],
        "director": request.json["director"],
        "genre": request.json["genre"],
        "price": request.json["price"]
    }
    return jsonify(moviesDAO.create(dvd))


@app.route('/dvds/<int:id>', methods=['PUT'])
def update(id):
    foundDvd = []
    if len(foundDvd) == 0:
        return jsonify({}), 404
    currentDvd = foundDvd[0]
    if 'title' in request.json:
        currentDvd['title'] = request.json['title']
    if 'director' in request.json:
        currentDvd['director'] = request.json['director']
    if 'genre' in request.json:
        currentDvd['genre'] = request.json['genre']
    if 'price' in request.json:
        currentDvd['price'] = request.json['price']

    return jsonify(currentDvd)


@app.route('/dvds/<int:id>', methods=['DELETE'])
def delete(id):
    moviesDAO.delete(id)
    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)
