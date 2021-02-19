from datetime import datetime
from flask import current_app as app
from flask import request, render_template
from flask.helpers import make_response, url_for
from .models import db,User

@app.route('/', methods=['GET'])
def users():
    username = request.args.get('user')
    email = request.args.get('email')

    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()

        if(existing_user):
            return make_response(f'{username} {email} já foi criado!')

        new_user = User(
            username=username,
            email=email,
            created_date=datetime.now(),
            bio="",
            admin=False
        )
        db.session.add(new_user)
        db.session.commit()

        return(url_for("user_records"))
    return render_template('users.html', users=User.query.all())