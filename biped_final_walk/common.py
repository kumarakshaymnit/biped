angles_start = [[0.0 for x in range(6)] for y in range(2)]
angles_end = [[0.0 for x in range(6)] for y in range(2)]
length_const = [47.0,65.0,115.0,95.0,60.0,40.0,52.0,53.0]
#mean_pos = [[-90.0,-90.0,-90.0,-90.0,-90.0,-90.0],[-90.0,-90.0,-90.0,-90.0,-90.0,-90.0]]
mean_pos = [[270.0,270.0,270.0,270.0,270.0,270.0],[270.0,270.0,270.0,270.0,270.0,270.0]]
speed=10
pos_start = [[90, 90, 90, 0, 90, 90],[90, 90, 90, 0, 90, 90]]
pos_end = [[90, 90, 90, 0, 90, 90],[90, 90, 90, 0, 90, 90]]
pwm_start = [[0.0 for x in range(6)] for y in range(2)]
pwm_end = [[0.0 for x in range(6)] for y in range(2)]

pwm_min = [[275,275,285,260,295,250],[225,255,195,250,295,250]]
pwm_max = [[1125,1125,1135,1120,1145,1150],[1075,1105,1045,1110,1145,1150]]
correction = [[90,90,90,0,90,90],[-90,-90,-90,0,90,-90]] 
target = [[0 for x in range(6)] for y in range(2)]
RIGHT=0
LEFT=1
counter=0
tilt =15.0
bend=-10.0
