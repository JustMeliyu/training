# encoding:utf-8

from flask import session, request, redirect, render_template, url_for, Blueprint
from models import Articles, Users
from exts import db

publish = Blueprint('publish', __name__)


@publish.route('/publish/', methods=['GET', 'POST'])
def publish_article():
    if session.get('username'):
        if request.method == 'GET':
            return render_template('publish.html')
        else:
            article_type = 'science'
            title = request.form.get('title')
            content = request.form.get('content')
            article = Articles(type=article_type, title=title, content=content)
            author = Users.query.filter(Users.username == session['username']).first()
            article.author = author
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('article.article_info', article_id=article.id))
    else:
        return redirect(url_for('auth.login'))
