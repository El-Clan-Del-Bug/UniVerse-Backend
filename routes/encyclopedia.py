# Import resources
from controllers.Encyclopedia import (
    Documents,
    AcceptDocument,
    RejectDocument,
    DocumentsByTopic,
    DocumentsPropose,
    DeleteDocument,
    DocumentsByTopicAndCommunityId,
)


def add_resources(api):
    api.add_resource(Documents, "/api/community/<int:community_id>/documents")
    api.add_resource(
        DocumentsByTopicAndCommunityId,
        "/api/community/<int:community_id>/documents/<int:topic_id>",
    )
    api.add_resource(DocumentsByTopic, "/api/topic/<int:topic_id>/documents")
    api.add_resource(
        RejectDocument, "/api/community/<int:community_id>/reject_document"
    )
    api.add_resource(
        AcceptDocument, "/api/community/<int:community_id>/accept_document"
    )
    api.add_resource(DocumentsPropose, "/api/community/<int:community_id>/propose")
    api.add_resource(
        DeleteDocument,
        "/api/community/<int:community_id>/delete_document/<int:document_id>",
    )
