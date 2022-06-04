from flask import render_template
import requests
import json
from nfl import app

leagues_url = 'https://hamren-nlf-api.herokuapp.com/leagues'
divisions_url = 'https://hamren-nlf-api.herokuapp.com/divisions'
teams_url = 'https://hamren-nlf-api.herokuapp.com/teams'

@app.context_processor
def get_balance():
    league_req = requests.get(leagues_url)
    league_data = json.loads(league_req.content)
    division_req = requests.get(divisions_url)
    division_data = json.loads(division_req.content)
    team_req = requests.get(teams_url)
    team_data = json.loads(team_req.content)
    
    return dict(league_data=league_data,  division_data=division_data, team_data=team_data)

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
    division_req = requests.get(divisions_url)
    division_data = json.loads(division_req.content)
    
    league = {}
    for leagues in league_data:
        if leagues['id'] == league_id:
            league = leagues
    
    divisions = []
    for division in division_data:
        if division['league_id'] == league_id:
            divisions.append(division)
            
    return render_template('league.html', data=league, divisions=divisions)

@app.route('/division/<int:division_id>')
def division(division_id):
    division_req = requests.get(divisions_url)
    division_data = json.loads(division_req.content)
    team_req = requests.get(teams_url)
    team_data = json.loads(team_req.content)
    
    division = {}
    for divisions in division_data:
        if divisions['id'] == division_id:
            division = divisions
            
    teams = []
    for team in team_data:
        if team['division_id'] == division_id:
            teams.append(team)
            
    return render_template('division.html', data=division, teams=teams)

@app.route('/team/<int:team_id>')
def team(team_id):
    league_req = requests.get(leagues_url)
    league_data = json.loads(league_req.content)
    division_req = requests.get(divisions_url)
    division_data = json.loads(division_req.content)
    team_req = requests.get(teams_url)
    team_data = json.loads(team_req.content)
    
    team = {}
    for teams in team_data:
        if teams['id'] == team_id:
            team = teams   
    
    
        
    return render_template('team.html', data=team)
