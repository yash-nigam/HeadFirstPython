from flask import Flask
from vsearch import search4letters

app= Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello World from flask'

@app.route('/vsearch')
def doSearch() -> str:
    return(str(search4letters('life, the universe, and everything','eiru,!')))


app.run();