#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x200")

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)

def lt():
	print("lt")
	cmd = Twist()
	cmd.linear.y = 1.0
	cmd.angular.z= 0.0
	pub.publish(cmd)
	
def rt():
	print("rt")
	cmd = Twist()
	cmd.linear.y = -1.0
	cmd.angular.z= 0.0
	pub.publish(cmd)



frame.mainloop()    
    
    
    
