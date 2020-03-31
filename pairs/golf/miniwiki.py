import glob
import os
import time

import markdown2
from flask import Flask, redirect, request, send_from_directory

app = Flask(__name__)


# add cute favicon!
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'mouse.png')


# show the main page
@app.route("/<page>")
def show(page):

    if not os.path.exists("pages/" + page):

        open("pages/" + page, 'w').write("New page. Edit here")

        return redirect("/" + page + "/edit")

    heading = f"<h1> {page} </h1>"
    body = markdown2.markdown_path("pages/" + page)
    ending = f"<a href='/{page}/edit'>edit</a> <br> last edit was {time.ctime(os.path.getmtime('pages/' + page))}"

    return heading + body + ending


# re-route default
@app.route('/')
def base():
    return redirect("/miniwiki")


# edit
@app.route("/<page>/edit")
def edit(page):

    raw_md = open("pages/" + page, 'r').read()

    return f"""<h1>Edit {page}</h1><form method=post action="/{page}/write"><textarea name=new>{raw_md}</textarea>
    <input type=submit></form>"""


# write
@app.route("/<page>/write", methods=['POST'])
def write(page):

    open("pages/" + page, 'w').write(request.form['new'])

    return redirect(f"/{page}")


if __name__ == '__main__':
    app.run(debug=True)
