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

#curl -X PUT -H "content-type:application/json" -d "{\"title\":\"Aliens\", \"director\":\"David Cameron\", \"genre\":\"Science Fiction\", \"price\":20}" http://127.0.0.1:5000/dvds/2
@app.route('/dvds/<int:id>', methods=['PUT'])
def update(id):
    foundDvd = moviesDao.findById(id)
    if not foundDvd:
        abort(404)
    if not request.json:
        abort(404)
    reqJson=request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)
    if 'title' in reqJson:
        foundDvd['title']=reqJson['title']
    if 'director' in reqJson:
        foundDvd['director']=reqJson['director']
    if 'genre' in reqJson:
        foundDvd['genre']=reqJson['genre']
    if 'price' in reqJson:
        foundDvd['price']=reqJson['price']
    values=(foundDvd['title'], foundDvd['director'], foundDvd['genre'], foundDvd['price'])
    moviesDao.update(values)
    return jsonify(foundDvd)

# curl -X DELETE http://127.0.0.1:5000/dvds/87
@app.route('/dvds/<int:id>', methods=['DELETE'])
def delete(id):
    moviesDao.delete(id)
    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)