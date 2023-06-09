from controllers.Topic import (
    TopicList,
    TopicId,
    TopicName,
    Topic,
    TopicListByCommunity,
    MostRecentTopic,
)


# Add resources to the API
def add_resources(api):
    api.add_resource(TopicList, "/api/topics")
    api.add_resource(TopicId, "/api/topic/id/<int:topic_id>")
    api.add_resource(TopicName, "/api/topic/name/<string:name>")
    api.add_resource(Topic, "/api/topic")
    api.add_resource(TopicListByCommunity, "/api/topics/community/<int:community_id>")
    api.add_resource(MostRecentTopic, "/api/topics/recent_topic/<int:community_id>")
