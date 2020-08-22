from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

from contactList import app, db, bcrypt
from contactList.models import User, Contacts
from contactList.forms import LoginForm, SignUpForm, CreateContactForm, UpdateContactForm

#-----------------------------------------------Home-------------------------------------------------

@app.route("/")
@app.route("/contacts")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    contacts = Contacts.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', contacts=contacts)

#-------------------------------------------Login/Logout-------------------------------------------

@app.route("/accounts/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Your username and password didn't match. Please try again.", 'danger')
    return render_template('login.html', form=form)


@app.route("/accounts/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

#----------------------------------------------SignUp----------------------------------------------

@app.route("/accounts/signup", methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hash)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        flash('Account created!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)

#----------------------------------------------Contacts----------------------------------------------

@app.route("/contacts/new", methods=['GET', 'POST'])
@login_required
def new_contact():
    form = CreateContactForm()
    if form.validate_on_submit():
        contact = Contacts(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, phone_number=form.phone_number.data, notes=form.notes.data, user_id=current_user.id)
        db.session.add(contact)
        db.session.commit()
        flash('Contact has been created.', 'success')
        return redirect(url_for('home'))
    return render_template('create_contact.html', form=form, legend='New Contact')


@app.route("/contacts/<int:contact_id>")
@login_required
def contact(contact_id):
    contact = Contacts.query.get_or_404(contact_id)
    return render_template('contact.html', contact=contact)


@app.route("/contacts/<int:contact_id>/edit", methods=['GET', 'POST'])
@login_required
def update_contact(contact_id):
    form = UpdateContactForm()
    contact = Contacts.query.get_or_404(contact_id)
    if form.validate_on_submit():
        contact.first_name = form.first_name.data
        contact.last_name = form.last_name.data
        contact.email = form.email.data
        contact.phone_number = form.phone_number.data
        contact.notes = form.notes.data
        db.session.add(contact)
        db.session.commit()
        flash('Contact has been updated.', 'success')
        url_for('contact', contact_id=contact.id)
        return redirect(url_for('contact', contact_id=contact.id))
    if request.method == 'GET':
        form.first_name.data = contact.first_name
        form.last_name.data = contact.last_name
        form.email.data = contact.email
        form.phone_number.data = contact.phone_number
        form.notes.data = contact.notes
    return render_template('create_contact.html', form=form, legend='Edit Contact')


@app.route("/contacts/<int:contact_id>/delete", methods=['POST'])
@login_required
def delete_contact(contact_id):
    contact = Contacts.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact has been deleted!', 'success')
    return redirect(url_for('home'))
