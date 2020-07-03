from flask import Flask, render_template, request, redirect
from vsearch import search4letters

app= Flask(__name__)

# @app.route('/')
# def hello() -> str:
#     return 'Hello World from flask'

# @app.route('/vsearch')
# def doSearch() -> str:
#     return(str(search4letters('life, the universe, and everything','eiru,!')))

@app.route('/search4',methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results"
    results = str(search4letters(phrase,letters))
    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters =letters,
                            the_title = title,
                            the_result = results)

@app.route('/yash')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Wc to search4letters on the web')

@app.route('/')
def returnredirect() -> '302':
    return redirect('/entry')

if __name__ == '__main__':
    app.run(debug=True)



