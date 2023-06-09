import datetime
from models.user import UserModel
from config.server_conf import db


class QuestionModel(db.Model):
    __tablename__ = "Question"

    # Attributes
    id = db.Column("id_question", db.Integer, primary_key=True)
    title = db.Column("title", db.String(60), nullable=False)
    description = db.Column("description", db.String(120), nullable=True)
    score = db.Column("score", db.Integer, nullable=False, default=0)
    topic_id = db.Column(
        "Topic_id_topic",
        db.Integer,
        db.ForeignKey("Topic.id_topic", ondelete="CASCADE"),
        nullable=False,
    )
    community_id = db.Column(
        "Community_id_community",
        db.Integer,
        db.ForeignKey("Community.id_community", ondelete="CASCADE"),
        nullable=False,
    )
    user_id = db.Column(
        "User_id_user", db.Integer, db.ForeignKey("User.id_user"), nullable=False
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
    def __init__(self, title, description, topic_id, community_id, user_id):
        self.title = title
        self.description = description
        self.topic_id = topic_id
        self.community_id = community_id
        self.user_id = user_id

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "score": self.score,
            "topic_id": self.topic_id,
            "community_id": self.community_id,
            "user_id": self.user_id,
        }

    def save_to_db(self):
        self.updated_at = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        self.is_active = False
        self.updated_at = datetime.datetime.utcnow()
        db.session.delete(self)
        db.session.commit()

    def update_score(self, increment):
        self.score += increment
        self.save_to_db()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id, is_active=True).first()

    @classmethod
    def find_all(cls):
        return cls.query.filter_by(is_active=True).all()

    @classmethod
    def find_more_recent(cls, community_id):
        return (
            cls.query.filter_by(community_id=community_id, is_active=True)
            .order_by(cls.created_at.desc())
            .first()
        )

    @classmethod
    def find_by_community_and_topic(cls, community_id, topic_id):
        return cls.query.filter_by(
            community_id=community_id, topic_id=topic_id, is_active=True
        ).all()

    @classmethod
    def find_by_community(cls, community_id):
        return cls.query.filter_by(community_id=community_id, is_active=True).all()

    @classmethod
    def change_user_id_for_user_name(cls, questions):
        for question in questions:
            user = UserModel.find_by_id(question["user_id"])

            if user is None:
                return {"message": "User not found"}, 404

            name = user.name
            del question["user_id"]
            question["user_name"] = name
        return questions

    @classmethod
    def find_by_topic(cls, topic_id):
        return cls.query.filter_by(topic_id=topic_id, is_active=True).all()

    @classmethod
    def num_of_question_per_community(cls, community_id):
        return cls.query.filter_by(is_active=True, community_id=community_id).count()

    @classmethod
    def find_more_voted(cls):
        return cls.query.filter_by(is_active=True).order_by(cls.score.desc()).first()

    @classmethod
    def num_of_topics_per_community(
        cls,
    ):
        return cls.query.filter_by(is_active=True).count().group_by(cls.topic_id).all()
