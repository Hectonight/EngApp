import math

vecA = {
	'magnitude': float(input('Input the magnitude of Vector A: ')),
	'user_angle': float(input('Input the angle of Vector A in degrees: ')),
	'direct_angle': [input(f'Input the direction of Vector A (N, S, E, W): ').upper()]
}
if vecA['user_angle'] != 0:
	if vecA['direct_angle'][0] in ['N', 'S']:
		vecA['direct_angle'].append(input('of (E, W): ').upper())
	else:
		vecA['direct_angle'].append(input('of (N, S): ').upper())

vecB = {
	'magnitude': float(input('Input the magnitude of Vector B: ')),
	'user_angle': float(input('Input the angle of Vector B in degrees: ')),
	'direct_angle': [input('Input the direction of Vector B (N, S, E, W): ').upper()]

}

if vecB['user_angle'] != 0:
	if vecB['direct_angle'][0] in ['N', 'S']:
		vecB['direct_angle'].append(input('of (E, W): ').upper())
	else:
		vecB['direct_angle'].append(input('of (N, S): ').upper())


for vec in [vecA, vecB]:
	if vec['direct_angle'] == ['E']:
		vec['angle'] = 0
	elif vec['direct_angle'] == ['N']:
		vec['angle'] = 90
	elif vec['direct_angle'] == ['W']:
		vec['angle'] = 180
	elif vec['direct_angle'] == ['S']:
		vec['angle'] = 270
	elif vec['direct_angle'] == ['N', 'E']:
		vec['angle'] = vec['user_angle']
	elif vec['direct_angle'] == ['E', 'N']:
		vec['angle'] = 90 - vec['user_angle']
	elif vec['direct_angle'] == ['W', 'N']:
		vec['angle'] = 90 + vec['user_angle']
	elif vec['direct_angle'] == ['N', 'W']:
		vec['angle'] = 180 - vec['user_angle']
	elif vec['direct_angle'] == ['S', 'W']:
		vec['angle'] = 180 + vec['user_angle']
	elif vec['direct_angle'] == ['W', 'S']:
		vec['angle'] = 270 - vec['user_angle']
	elif vec['direct_angle'] == ['E', 'S']:
		vec['angle'] = 270 + vec['user_angle']
	elif vec['direct_angle'] == ['S', 'E']:
		vec['angle'] = 360 - vec['user_angle']
	else:
		raise ValueError('Direction angle has not been input properly')

	vec['x'] = vec['magnitude'] * (math.cos(math.radians(vec['angle'])))
	vec['y'] = vec['magnitude'] * (math.sin(math.radians(vec['angle'])))

vecC = {'x': vecA['x'] + vecB['x'], 'y': vecA['y'] + vecB['y']}

vecC['magnitude'] = round(math.sqrt((vecC['x']**2) + (vecC['y']**2)), 1)
vecC['angle'] = round(math.degrees(math.atan(vecC['y']/vecC['x'])), 1)

if vecC['angle'] == 0 and vecC['x'] < 0:
	vecC['angle'] = 180

while 180 > vecC['angle'] and vecC['y'] < 0:
	vecC['angle'] += 180

if vecC['angle'] > 315:
	final_angle = f"{round(360-vecC['angle'], 1)}° S of E"
elif vecC['angle'] > 270:
	final_angle = f"{round(270+vecC['angle'], 1)}° E of S"
elif vecC['angle'] == 270:
	final_angle = '0° S'
elif vecC['angle'] > 225:
	final_angle = f"{round(270-vecC['angle'], 1)}° W of S"
elif vecC['angle'] > 180:
	final_angle = f"{round(180+vecC['angle'], 1)}° S of West"
elif vecC['angle'] == 180:
	final_angle = '0° W'
elif vecC['angle'] > 135:
	final_angle = f"{round(180-vecC['angle'], 1)}° N of W"
elif vecC['angle'] > 90:
	final_angle = f"{round(90+vecC['angle'], 1)}° W of N"
elif vecC['angle'] == 90:
	final_angle = '0° N'
elif vecC['angle'] > 45:
	final_angle = f"{round(90-vecC['angle'], 1)}° E of N"
elif vecC['angle'] > 0:
	final_angle = f"{round(vecC['angle'], 1)}° N of E"
else:
	final_angle = '0° E'


print('{} units at {}'.format(vecC['magnitude'], final_angle))