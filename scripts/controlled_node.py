import rospy
from std_srvs.srv import EmptyResponse
from std_srvs.srv import Trigger, TriggerResponse
import sys

class Node(object):
    """Launch a Node with service calls to control start and stop"""

    def __init__(self, start_from_startup_=False):
        self.started = False
        self.stopped = False
        self.name = rospy.get_name()
        if start_from_startup_:
            self.start_srv()

    def start_srv(self, service_message=None):
        if self.started:
            rospy.logwarn("%s node has already started - nothing to be done", self.name)
        else:
            self.started = True
            # rospy.loginfo("%s node started", self.name)
            print(service_message)
            return TriggerResponse(
                success=True,
                message=str(self.name) + " node started"
            )

    def stop_srv(self, service_message=None):
        self.stopped = True
        # rospy.loginfo("%s node stopped", self.name)
        return TriggerResponse(
            success=True,
            message=str(self.name) + " node stopped"
        )