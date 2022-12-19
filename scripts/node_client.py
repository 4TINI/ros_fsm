#! /usr/bin/env python3

# remember to make this file executable (`chmod +x`) before trying to run it

import rospy
from std_srvs.srv import Trigger, TriggerRequest
import roslaunch
import rosnode

def launch_node(node_name):
    package = 'ros_fsm'
    node = roslaunch.core.Node(package, node_name, node_name.split('.')[0], output='screen')   
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()   
    process = launch.launch(node)
    rospy.sleep(1) 
    return process

def start_node(node_name):
    try:
        # Create the connection to the service. Remeber it's a Trigger service
        connection_service = rospy.ServiceProxy(str(node_name.split('.')[0])+'/start', Trigger)
        
        # Create an object of type TriggerRequest. We need a TriggerRequest for a Trigger service
        request = TriggerRequest()
        
        rospy.loginfo("calling start service for %s", node_name)
        
        # Now send the request through the connection
        response = connection_service(request)
        
        if not response:
            rospy.logerr("something went wrong")
        else:
            rospy.loginfo(response)
        
        return response
    
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s"%e)
    
    return response

def stop_node(node_process, node_name):
    try:
        # Create the connection to the service. Remeber it's a Trigger service
        connection_service = rospy.ServiceProxy(str(node_name.split('.')[0])+'/stop', Trigger)
        
        # Create an object of type TriggerRequest. We need a TriggerRequest for a Trigger service
        request = TriggerRequest()
        
        # Now send the request through the connection
        response = connection_service(request)
        
        # Done, let's see the result!
        node_process.stop()
        return response
    
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s"%e)
    
    return response

if __name__ == '__main__':
    # init a node as usual
    rospy.init_node('node_client')
    
    rospy.loginfo("starting the client node")
    
    # Finite State Machine ROS nodes
    node1_name = 'node_server1.py'
    node2_name = 'node_server2.py'
    
    # Launch nodes in dormant mode
    node1_process = launch_node(node1_name)  
    node2_process = launch_node(node2_name) 
    
    # Start Node 1
    node1_response = start_node(node1_name)
    
    '''    
    # Wait for node to kill himself after finishing its tasks. Check in the node how to do this.
    while rosnode.rosnode_ping("/"+str(node1_name), max_count=1):
        rospy.sleep(1.0)
    '''
    
    while rosnode.rosnode_ping("/"+str(node1_name.split('.')[0]), max_count=1):
        rospy.sleep(1.0)
    
    # Start Node 2
    # node2_response = start_node(node2_name)
    '''
    # Execute Node 2 for a specific amount of time (e.g. 5 sec) and then kill it
    rospy.sleep(5)
    node2_response = stop_node(node2_process, node2_name)
    '''
    
    rospy.spin()