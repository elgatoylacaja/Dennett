from dennett.trials.models import Trial
from bson.json_util import dumps
from flask import render_template
from . import admin


@admin.route('', methods=['GET'])
def index():
    return render_template('admin.html')
