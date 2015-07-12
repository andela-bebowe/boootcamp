import turtle
'''
Drawing polygons as many as u need with different number of sides
'''
def draw_shapes(no_of_sides, no_of_polygon):
	window = turtle.Screen()
	window.bgcolor("black")
	drawer = turtle.Turtle()
	drawer.shape("turtle")
	drawer.color("red")
	drawer.speed(3)
	n = no_of_sides
	ang = ((n-2)*180)/n
	while no_of_polygon>0:
		for i in range(0,n):
			drawer.fd(30)
			drawer.lt(180-ang)
		drawer.fd(30)
		no_of_polygon -= 1
	window.exitonclick()