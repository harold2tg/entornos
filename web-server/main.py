import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def get_list():
    return ['Cebolla', 'Tomate', 'Aguacate']

@app.get('/name')
def get_name():
    return{
        'name': 'harold'
    }
    
@app.get("/html", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>mi web</title>
        </head>
        <body>
            <h1>Harold Torres Gallo!</h1>
        </body>
    </html>
    """    

def run():
    store.get_categories()
    


if __name__ == '__main__':
    run()