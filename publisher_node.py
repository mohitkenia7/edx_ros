import rospy
from std_msgs.msg import String

def simplePublisher():
    simple_publisher = rospy.Publisher('mohit', String, queue_size =10)
    rospy.init_node('node_1', anonymous = False)
    rate = rospy.Rate(10)

    mohit_content = "my first ros topic"
    while not rospy.is_shutdown():
	simple_publisher.publish(mohit_content)
	rate.sleep()

if __name__== '__main__':
    try:
	simplePublisher()
    except rospy.ROSInterruptException:
	pass
