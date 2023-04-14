from flask import render_template, session, request, flash, Blueprint, url_for, redirect
from datetime import datetime

customer = Blueprint('customer', __name__)

from app import mysql
