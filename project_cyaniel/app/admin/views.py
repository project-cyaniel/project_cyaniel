from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import CharacterForm
from .. import db
from ..models import Character


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# Character Views


@admin.route('/characters', methods=['GET', 'POST'])
@login_required
def list_characters():
    """
    List all characters
    """
    check_admin()

    characters = Character.query.all()

    return render_template('admin/characters/characters.html',
                           characters=characters, title="Characters")


@admin.route('/characters/add', methods=['GET', 'POST'])
@login_required
def add_character():
    """
    Add a characters to the database
    """
    check_admin()

    add_character = True

    form = CharacterForm()
    if form.validate_on_submit():
        character = Character(character_name=form.character_name.data)

        try:
            # add characters to the database
            db.session.add(character)
            db.session.commit()
            flash('You have successfully added a new characters.')
        except:
            # in case characters name already exists
            flash('Error: characters name already exists.')

        # redirect to characters page
        return redirect(url_for('admin.list_characters'))

    # load characters template
    return render_template('admin/characters/character.html', action="Add",
                           add_character=add_character, form=form,
                           title="Add Character")


@admin.route('/characters/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_character(id):
    """
    Edit a characters
    """
    check_admin()

    add_character = False

    character = Character.query.get_or_404(id)
    form = CharacterForm(obj=character)
    if form.validate_on_submit():
        character.character_name = form.character_name.data
        character.last_update = form.last_update.data
        character.id = form.id.data
        db.session.commit()
        flash('You have successfully edited the characters.')

        # redirect to the characters page
        return redirect(url_for('admin.list_characters'))

    form.character_name.data = character.character_name
    return render_template('admin/characters/character.html', action="Edit",
                           add_character=add_character, form=form,
                           character=character, title="Edit Character")


@admin.route('/characters/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_character(id):
    """
    Delete a characters from the database
    """
    check_admin()

    character = Character.query.get_or_404(id)
    db.session.delete(character)
    db.session.commit()
    flash('You have successfully deleted the characters.')

    # redirect to the characters page
    return redirect(url_for('admin.list_characters'))

    return render_template(title="Delete Character")