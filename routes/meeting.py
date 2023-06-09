# Import resources
from controllers.Meeting import (
    MeetingsList,
    MeetingCommunity,
    MeetingId,
    SearchMeetingDate,
    NextMeeting,
)


def add_resources(api):
    api.add_resource(MeetingsList, "/api/meetings")
    api.add_resource(MeetingCommunity, "/api/community/<int:comm_id>/meetings")
    api.add_resource(MeetingId, "/api/meeting/id/<int:id>")
    api.add_resource(SearchMeetingDate, "/api/meetings/community/<int:comm_id>")
    api.add_resource(NextMeeting, "/api/community/<int:comm_id>/next_meeting")
