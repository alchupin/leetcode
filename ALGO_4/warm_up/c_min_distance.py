from math import atan2, pi


file_path = 'input.txt'
file_path = '/home/alexey/study/leetcode-1/ALGO_4/warm_up/data/c_min_distance.txt'


def find_distance_through_arc(long_r, short_r, angle):
    arc = pi*short_r*angle/180
    distance_through_arc = arc + long_r - short_r
    return distance_through_arc


def find_min_distance(x1, y1, x2, y2):
    dist_to_centre_1 = (x1**2 + y1**2)**0.5
    dist_to_centre_2 = (x2**2 + y2**2)**0.5
    distance_through_centre = dist_to_centre_1 + dist_to_centre_2

    angle_1 = atan2(y1, x1)/pi*180
    angle_2 = atan2(y2, x2)/pi*180
    angle_between = abs(angle_2 - angle_1)
    if angle_between > 180:
        angle_between = 360 - angle_between
    
    if dist_to_centre_1 >= dist_to_centre_2:
        distance_through_arc = find_distance_through_arc(dist_to_centre_1, dist_to_centre_2, angle_between)
    else:
        distance_through_arc = find_distance_through_arc(dist_to_centre_2, dist_to_centre_1, angle_between)

    min_diststance = min(distance_through_centre, distance_through_arc)

    return min_diststance


with open(file_path, 'r') as f:
    x1, y1, x2, y2 = map(int, f.readline().split())
    print(find_min_distance(x1, y1, x2, y2))