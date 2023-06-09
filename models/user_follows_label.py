import datetime
from config.server_conf import db


class UserFollowsLabelModel(db.Model):
    __tablename__ = "User_follows_label"

    # Attributes
    user_id = db.Column(
        "User_id_user",
        db.Integer,
        db.ForeignKey("User.id_user", ondelete="CASCADE"),
        primary_key=True,
    )
    label_id = db.Column(
        "Label_id_label",
        db.Integer,
        db.ForeignKey("Label.id_label", ondelete="CASCADE"),
        primary_key=True,
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

    # Methods
    def __init__(self, user_id, label_id):
        self.user_id = user_id
        self.label_id = label_id
