from flask import render_template, request
import requests
import json
from nfl import app

leagues_url = 'https://hamren-nlf-api.herokuapp.com/leagues'
divisions_url = 'https://hamren-nlf-api.herokuapp.com/divisions'
teams_url = 'https://hamren-nlf-api.herokuapp.com/teams'

@app.route('/')
@app.route('/home')
def home():
    league_req = requests.get(leagues_url)
    league_data = json.loads(league_req.content)
    division_req = requests.get(divisions_url)
    division_data = json.loads(division_req.content)
    team_req = requests.get(teams_url)
    team_data = json.loads(team_req.content)
    
    return render_template('home.html', league_data=league_data, division_data=division_data, team_data=team_data)

@app.route('/league/<int:league_id>')
def league(league_id):
    league_req = requests.get(leagues_url)
    league_data = json.loads(league_req.content)
    
    league = {}
    for leagues in league_data:
        if leagues['id'] == league_id:
            league = leagues
    
    return render_template('league.html', data=league)