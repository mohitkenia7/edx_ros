import rosypy
from std_msgs.msg import String

def stringListenerCallback(data):
    rospy.loginfo(' The content of topic: %s',data.data)

def string.ListenerCallback(data):
    rospy.init_node('node-2', anonumous = False)

    rospy.Subscrobe('mohit', String, stringListenerCallback)

    rospy.spin()

if __name__=='__main__':
    stringListener()

