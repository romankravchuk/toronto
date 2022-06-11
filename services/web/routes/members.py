from math import ceil
from flask import Blueprint, flash, abort
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from config import Config
from database.models import Member
from database.models import Guild
from database.member import member_system
from database.guild import guild_system
from logger import logger


members = Blueprint('members', __name__, template_folder='templates', url_prefix='/members')


@members.route('/')
@login_required
@logger.catch
def index():
    page = request.args.get('page', default=1, type=int)
    
    page_size = (page - 1) * Config.QUERY_LIMIT
    members_count = member_system.count()
    last_page = ceil(members_count / Config.QUERY_LIMIT)

    logger.debug(f"page: {page}, page_size: {page_size} "
                 f"members_count: {members_count}, last_page: {last_page}")
    
    members = member_system.get_members(limit=Config.QUERY_LIMIT, offset=page_size)
    logger.debug(f'Get members: {members}')

    context = {
        "page" : page,
        "last_page" : last_page,
        "members" : members
    }

    return render_template('members/members.html', **context)


@members.route('/member', methods=['GET'])
@login_required
@logger.catch
def member():
    member_id = request.args.get('id', type=str)
    member = member_system.get_member(id=member_id)

    logger.debug(f"Get member: {member}")

    if not member:
        abort(404)    

    context = {
        "member" : member,
        "guilds" : member.guilds
    }

    return render_template('members/member.html', **context)


@members.route('/edit')
@login_required
@logger.catch
def edit():
    member_id = request.args.get('id', type=str)
    member = member_system.get_member(id=member_id)

    logger.debug(f"Get member: {member}")

    if not member:
        abort(404)

    return render_template('members/edit.html', member=member)


@members.route('/edit', methods=['POST'])
@logger.catch
@login_required
def edit_post():
    member_id = request.args.get('id', type=str)
    member = member_system.get_member(id=member_id)

    logger.debug(f"Get member: {member}")

    if not member:
        abort(404)

    name = request.form['name']
    email = request.form['email']
        
    member.name = name
    member.email = email

    logger.debug(f"{member} updated successfully")
    flash(f"{member.name} updated successfully", "info")

    return redirect(url_for('members.members'))



@members.route('/delete', methods=['POST'])
@login_required
@logger.catch
def delete():
    member_id = request.args.get('id', type=str)
    member = member_system.get_member(id=member_id)

    logger.debug(f"Get member: {member}")

    if member_system.delete(member_id):
        logger.debug(f"{member} deleted successfully")
        flash(f"{member.name} deleted successfully", 'info')

    return redirect(url_for('members.index'))