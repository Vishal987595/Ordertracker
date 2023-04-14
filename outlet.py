from flask import render_template, session, flash, request, redirect, url_for, Blueprint

outlet = Blueprint('outlet', __name__)

from app import mysql