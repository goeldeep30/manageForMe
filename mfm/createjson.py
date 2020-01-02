import json

data = {}
data['standard'] = []
data['standard'].append({
    'number': '1',
    'floor': '1'
})
data['standard'].append({
    'number': '2',
    'floor': '2'
})
data['standard'].append({
    'number': '3',
    'floor': '3'
})
data['AC'] = []
data['AC'].append({
    'number': '1',
    'floor': '1'
})
data['AC'].append({
    'number': '2',
    'floor': '2'
})
data['AC'].append({
    'number': '3',
    'floor': '3'
})

with open('room.json', 'w') as outfile:
    json.dump(data, outfile)
