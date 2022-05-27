from ..database import db


guild_members = db.Table('guild_members',
    db.Column('guild_id', db.BigInteger, db.ForeignKey('guilds.id'), primary_key=True),
    db.Column('member_id', db.BigInteger, db.ForeignKey('members.id'), primary_key=True),
)

guild_roles = db.Table('guild_roles',
    db.Column('role_id', db.BigInteger, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('guild_id', db.BigInteger, db.ForeignKey('guilds.id'), primary_key=True),
)


class Guild(db.Model):
    __tablename__ = "guilds"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(), nullable=False)
    members = db.relationship('Member', secondary=guild_members, lazy='subquery',
                            backref=db.backref('guilds', lazy=True))
    roles = db.relationship('Role', secondary=guild_roles, lazy='subquery',
                            backref=db.backref('guilds', lazy=True))


    def __init__(self, id, name, icon):
        self.id = id
        self.name = name
        self.icon = icon

    def __repr__(self) -> str:
        return f'<GUILD: {self.id} {self.name}>'
