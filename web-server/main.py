import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # HTML Format

# instance
app = FastAPI()

# Main page


@app.get('/')  # decorator
def get_list():
    return [1, 2, 3, 4]

# Contact page


@app.get('/contact', response_class=HTMLResponse)  # decorator
def get_list():
    return '''
    <h1>Hola, Titulo</h1>
    <p>Hola, Párrafo</p>
    '''


def run():
    store.get_categories()


if __name__ == '__main__':
    run()
