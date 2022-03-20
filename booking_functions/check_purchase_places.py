import json
from flask import Flask,render_template,request,redirect,flash,url_for, abort
import urllib.request
from datetime import date, datetime
from io import BytesIO
import json


def check_club_has_enough_points(club, placesRequired):
    """
    Check if the club has enough points to book a competition
    """
    if int(club['points']) < placesRequired*3:
        return False


def check_less_than_12(placesRequired):
    """
    Return an error message when booking more than 12 places
    """
    print(placesRequired)
    if placesRequired > 12:
        error = "more_than_12_places"
        return False


def check_competition_in_future(competition):
    """
    Return an error message when booking a past competition
    """
    today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    today_formatted = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
    competition_date = datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S')
    if today_formatted > competition_date:
        error = "past_competition"
        return False

