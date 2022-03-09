import json
from flask import Flask,render_template,request,redirect,flash,url_for, abort
import urllib.request
from datetime import date, datetime
from io import BytesIO
import json

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club, clubs=clubs, competitions=competitions)        
    except:
        print('Error: wrong email adress')
        return render_template('index.html', error=True)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    if int(club['points']) < placesRequired:
        error = "more_points_than_club"
        return render_template('booking.html',club=club, competition=competition, error=error, point=club['points'], place=placesRequired)
    if placesRequired > 12:
        error = "more_than_12_places"
        return render_template('booking.html',club=club, competition=competition, error=error)
    today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    today_formatted = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
    competition_date = datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S')
    if today_formatted > competition_date:
        error = "past_competition"
        return render_template('welcome.html',club=club, competitions=competitions, error=error)        
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    club['points'] = int(club['points']) - placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

# if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=5050, debug=True)    