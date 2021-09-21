def find_big_diameter(angle_of_edge, big_radius):
    re = 180 - (angle_of_edge * 2)
    big_diameter = (re / 180) * big_radius

    return big_diameter

user_input_angle = int(input("enter the angle of the edge: "))
user_input_big_radius = int(input("enter the big radius: "))

result = (find_big_diameter(user_input_angle, user_input_big_radius)) / 10
print(round(result))