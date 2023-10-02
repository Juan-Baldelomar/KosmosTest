# KosmosTest
Technical test for Kosmos Application

### Installation

To get started with this project, follow these steps:
1. Clone the repository:
2. Install the required Python libraries

### Execution
1. (Option 1) python app.py
2. (Option 2, if using windows) waitress-serve --listen=0.0.0.0:8000 app:app

If you use option 1, requests should be made (usually) to http://127.0.0.1:5000/ner
If you use option 2, requests should be made to http://0.0.0.0:8000/ner

To test you can send requests using postman or curl. Send a POST request with the header "Content-Type: application/json" the body message in the following format:

{"oraciones":["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.", "San Tomas considera prohibir los robots de entrega en la acera."]}
