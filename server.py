from flask import Flask, url_for, request, redirect, abort, jsonify

from MoviesDao import moviesDao


app = Flask(__name__, static_url_path='', static_folder='template')

# curl "http://127.0.0.1:5000/dvds"
@app.route('/dvds')
def getAll():
    return jsonify(moviesDao.getAll())

# curl "http://127.0.0.1:5000/dvds/1"
@app.route('/dvds/<int:id>')
def findById(id):
    return jsonify(moviesDao.findById(id))

# curl  -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"89\",\"title\":\"The Hateful Eight\",\"director\":\"Quentin Tarantino\",\"genre\":\"Western\", \"price\":14}" http://127.0.0.1:5000/dvds
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

    return jsonify(moviesDao.create(dvd))


@app.route('/dvds/<int:id>', methods=['PUT'])
def update(id):
    foundDvd = moviesDao.findById(id)
    print(foundDvd)
    if (foundDvd) == {}:
        return jsonify({}), 404
    currentDvd = foundDvd
    if 'title' in request.json:
        currentDvd['title'] = request.json['title']
    if 'director' in request.json:
        currentDvd['director'] = request.json['director']
    if 'genre' in request.json:
        currentDvd['genre'] = request.json['genre']
    if 'price' in request.json:
        currentDvd['price'] = request.json['price']
    moviesDao.update(currentDvd)
    return jsonify(currentDvd)

# curl -X DELETE http://127.0.0.1:5000/dvds/87
@app.route('/dvds/<int:id>', methods=['DELETE'])
def delete(id):
    moviesDao.delete(id)
    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)