#! /usr/bin/env python

# remember to make this file executable (`chmod +x`) before trying to run it

import rospy
from std_srvs.srv import Trigger, TriggerRequest

if __name__ == '__main__':
    # init a node as usual
    rospy.init_node('node_client')
    
    rospy.loginfo("starting the client node")
    
    rospy.wait_for_service('/srv_1')

    try:
        # Create the connection to the service. Remeber it's a Trigger service
        connection_service1 = rospy.ServiceProxy('/srv_1', Trigger)
        
        # Create an object of type TriggerRequest. We need a TriggerRequest for a Trigger service
        request1 = TriggerRequest()
        
        # Now send the request through the connection
        response1 = connection_service1(request1)
        
        # Done, let's see the result!
        print(response1)
        
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
    
    rospy.loginfo("send request to server 2")
    rospy.wait_for_service('/srv_2')

    try:
        connection_service2 = rospy.ServiceProxy('/srv_2', Trigger)
        request2 = TriggerRequest()
        response2 = connection_service2(request2)
        print(response2)
        
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)