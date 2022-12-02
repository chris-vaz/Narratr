# from crypt import methods
from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.model_note import Note
from flask_app.models.model_user import User


@app.route('/new/note')
def new_note():
    if 'users_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['users_id']
    }
    return render_template("new_note.html",user=User.get_by_id(data))


@app.route('/create/note',methods=['POST'])
def create_note():
    if 'users_id' not in session:
        return redirect('/logout')
    if not Note.validate_note(request.form):
        return redirect('/new/note')
    data = {
        "title": request.form["title"],
        "date_of_note": request.form["date_of_note"],
        "note": request.form["note"],
        "users_id": session["users_id"]
    }
    Note.save(data)
    return redirect('/dashboard')

@app.route('/edit/note/<int:id>')
def edit_note(id):
    if 'users_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['users_id']
    }
    return render_template("edit_note.html",edit=Note.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/note',methods=['POST'])
def update_note():

    data = {
        "title": request.form["title"],
        "note": request.form["note"],
        "date_of_note": request.form["date_of_note"],
        "id": request.form["id"]
    }
    id=request.form['id']
    if 'users_id' not in session:
        return redirect('/logout')
    if not Note.validate_note(request.form):
        return redirect(f'/edit/note/{id}') 
    Note.update(data)
    return redirect('/dashboard')

@app.route('/note/<int:id>')
def show_note(id):
    if 'users_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['users_id']
    }
    return render_template("show_note.html",user=User.get_by_id(user_data),note=Note.get_one(data))

@app.route('/destroy/note/<int:id>')
def destroy_note(id):
    if 'users_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Note.destroy(data)
    return redirect('/dashboard')