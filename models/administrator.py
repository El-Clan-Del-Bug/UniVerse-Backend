import datetime
from config.server_conf import db


class AdministratorModel(db.Model):
    __tablename__ = "Administrator"

    # Attributes
    id = db.Column(
        "User_id_user", db.Integer, db.ForeignKey("User.id_user"), primary_key=True
    )
    is_active = db.Column("is_active", db.Boolean, nullable=False, default=True)
    created_at = db.Column(
        "created_at", db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        "updated_at",
        db.DateTime,
        nullable=False,
        default=datetime.datetime.utcnow,
    )

    # Relationships
    administrator_manage_community = db.relationship(
        "AdministratorManageCommunityModel",
        backref="administrator",
    )
    document = db.relationship("DocumentModel", back_populates="administrator")
    topic = db.relationship("TopicModel", back_populates="administrator")

    # Methods
    def __init__(self, id):
        self.id = id