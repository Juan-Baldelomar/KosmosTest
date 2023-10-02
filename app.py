from flask import Flask, request, jsonify
import spacy 

# create Flask App and load NER model
app = Flask(__name__)
nlp = spacy.load("es_core_news_sm")

@app.route('/ner', methods=['POST'])
def perform_ner():
    # get data
    data = request.get_json()
    oraciones = data['oraciones']
    resultado = {'resultado': []}

    # traverse each sentence and get the entities
    for oracion in oraciones:
        doc = nlp(oracion)
        entities = {'oracion': oracion, 'entidades': {e.text: e.label_ for e in doc.ents}}
        resultado['resultado'].append(entities)


    # return the entities in json format
    return jsonify(resultado)


# main to test the app
if __name__ == '__main__':
    app.run(debug=True)