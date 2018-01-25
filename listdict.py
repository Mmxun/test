cities={
    'China':{'country':'BJ','population':'1000000'},
    'America':{'country':'Washington, D.C','population':'2000000'},
    'Japan':{'country':'Tokyo','population':'3000000'}
}
cities['England']={'country':'London','population':'4000000'}

for a,b in cities.items():
    print('info:'+a+str(b))
