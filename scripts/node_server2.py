#! /usr/bin/env python
# remember to make this file executable (`chmod +x`) before trying to run it

import rospy
from std_srvs.srv import Trigger, TriggerResponse

def trigger_response(request):
    rospy.logwarn("----")
    rospy.logwarn("performing operation 2")
    rospy.sleep(5)
    
    return TriggerResponse(
        success=True,
        message="Hey, roger that; we'll be right there!"
    )

rospy.init_node('sos_service') 
my_service = rospy.Service('/srv_2', Trigger, trigger_response)

rospy.spin()