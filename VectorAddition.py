import math

vecA = {
	'length': float(input('Input the length of Vector A: ')),
	'angle': math.radians(float(input('Input the angle of Vector A in degrees: ')))
}
vecB = {
	'length': float(input('Input the length of Vector B: ')),
	'angle': math.radians(float(input('Input the angle of Vector B in degrees: ')))
}

vecA['x'] = vecA['length'] * (math.cos(vecA['angle']))
vecA['y'] = vecA['length'] * (math.sin(vecA['angle']))
vecB['x'] = vecB['length'] * (math.cos(vecB['angle']))
vecB['y'] = vecB['length'] * (math.sin(vecB['angle']))


vecC = {'x': vecA['x'] + vecB['x'], 'y': vecA['y'] + vecB['y']}

vecC['length'] = round(math.sqrt((vecC['x']**2) + (vecC['y']**2)), 1)
vecC['angle'] = round(math.degrees(math.atan(vecC['y']/vecC['x'])), 1)

if vecC['angle'] == 0 and vecC['x'] < 0:
	vecC['angle'] = 180

elif not (0 < vecC['angle'] < 180) and vecC['y'] > 0:
	vecC['angle'] += 180

while not (180 < vecC['angle']) and vecC['y'] < 0:
	vecC['angle'] += 180

print('({}, {} degrees)'.format(vecC['length'], vecC['angle']))