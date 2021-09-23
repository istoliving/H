# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from app.home.target.view import *
from app.home.scanconfig.view import *
from app.home.sysconfig.view import *

@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html', segment='index')

@blueprint.route('/target')
@login_required
def targetroute():
    return target();

@blueprint.route('/targetadd', methods=['GET', 'POST'])
@login_required
def targetaddroute():
    return targetadd();

@blueprint.route('/tagetinfo', methods=['GET', 'POST'])
@login_required
def targetinforoute():
    return targetinfo();

@blueprint.route('/scanmethod', methods=['GET', 'POST'])
@login_required
def scanmethodroute():
    return scanmethod();

@blueprint.route('/scancron', methods=['GET', 'POST'])
@login_required
def scancronroute():
    return scancron();

@blueprint.route('/sysconfig', methods=['GET', 'POST'])
@login_required
def sysconfigroute():
    return sysconfig();




@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith( '.1' ):
            template += '.1'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
