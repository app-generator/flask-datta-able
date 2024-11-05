# -*- encoding: utf-8 -*-
from flask import render_template, redirect, request, url_for, flash, session
from flask_login import (
    current_user,
    login_user,
    logout_user
)
from flask_dance.contrib.github import github
from werkzeug.security import check_password_hash, generate_password_hash

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import User, Users
from apps.authentication.util import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.login'))

# Login & Registration


@blueprint.route("/github")
def login_github():
    """ Github login """
    if not github.authorized:
        return redirect(url_for("github.login"))

    res = github.get("/user")
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    msg = None

    if 'login' in request.form:
        # Read form data
        user_id = request.form['username']  # We can have here username OR email
        password = request.form['password']

        # Locate user
        user = Users.find_by_username(user_id)

        # If user not found
        if not user:
            user = Users.find_by_email(user_id)
            if not user:
                return render_template('accounts/login.html',
                                       msg='Unknown User or Email',
                                       form=login_form)

        # Check the password
        if verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('authentication_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               msg='Wrong user or password',
                               form=login_form)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('authentication_blueprint.dashboard'))
        else:
            msg = 'Invalid credentials. Please try again.'

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form, msg=msg)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('authentication_blueprint.login'))
    return 'Welcome to the dashboard!'


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check username exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = Users(**request.form)
        db.session.add(user)
        db.session.commit()

        # Delete user from session
        logout_user()

        return render_template('accounts/register.html',
                               msg='User created successfully.',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))

# Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
