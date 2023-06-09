from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.question import QuestionModel
from models.label import LabelModel
from models.community import CommunityModel
from models.label_has_community import LabelHasCommunityModel
from models.user_belongs_to_community import UserBelongsToCommunityModel
from models.community_has_document_and_topic import CommunityHasDocumentAndTopicModel


class QuestionsPerCommunity(Resource):
    @jwt_required()
    def get(self, community_id):
        return {
            "num_questions": QuestionModel.num_of_question_per_community(community_id)
        }


class NumUserPerCommunityId(Resource):
    @jwt_required()
    def get(self, community_id):
        return {
            "num_users": UserBelongsToCommunityModel.num_of_users_per_community_id(
                community_id
            )
        }


class TopicsPerCommunity(Resource):
    @jwt_required()
    def get(self, community_id):
        return {
            "num_topics": CommunityHasDocumentAndTopicModel.num_of_topics_per_community(
                community_id
            )
        }


class ListUsersPerComm(Resource):
    @jwt_required()
    def get(self):
        res = UserBelongsToCommunityModel.num_of_users_per_community()
        data = {}

        for key, value in res.items():
            comm = CommunityModel.find_by_id(key)
            if comm:
                data[comm.name] = value
        return data


class CommunitiesPerLabel(Resource):
    @jwt_required()
    def get(self):
        labels = LabelModel.query.filter_by(is_active=True).all()
        data = {}

        for label in labels:
            data[label.name] = LabelHasCommunityModel.num_of_communities_per_label(
                label.id
            )

        return data
