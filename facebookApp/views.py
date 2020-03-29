from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config')

from .utils import find_content


@app.route('/')
@app.route('/index/')
def index():
    if 'img' in request.args:  # return a dictionary
        img = request.args('img')
        og_image = url_for('static', filename='img', _external=True)
        og_url = url_for('index', _external=True)
    else:
        description = """Toi, tu sais comment utiliser la console, t'es jamais 
					à court d'idées pour réaliser ton objectif, tu es déterminé-e et
					et persévérant. Tes amis disent d'ailleurs volontier que 
					tu as du caracctère et que tu ne te laisses pas marcher sur 
					les pieds. un peu hacker sur les bords, tu aimes trouver des 
					solutions à tout problème. N'aurais-tu pas un petit problème 
					d'autorité?"""

        og_image = url_for('static', filename='tmp/sample.jpg', _external=True)
        og_url = url_for('index', _external=True)

    return render_template('index.html',
                           user_name='Julien',
                           user_image=url_for('static',
                                              filename='img/profile.png'),
                           description=description,
                           blur=True,
                           og_url=og_url)


@app.route('/result/')
def result():
    description = find_content()
    gender = request.args.get('gender')
    user_nam = request.args.get('first_name')
    uid = request.args.get('id')
    profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'

    img = request.args.get('img')
    og_url = url_for('index', _external=True, img=img)

    return render_template('result.html',
                           user_name=user_nam,
                           user_image=profile_pic,
                           description=description,
                           blur=False,
                           og_url=og_url)


if __name__ == "__main__":
    app.run()
