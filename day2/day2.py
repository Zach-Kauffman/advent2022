def main():

    # map each opponent's choice with a winning/tying/losing throw
    rpsmap = {
        'A': {
            'X': 'C', 
            'Y': 'A', 
            'Z': 'B',
        },
        'B': {
            'X': 'A', 
            'Y': 'B', 
            'Z': 'C',
        },
        'C': {
            'X': 'B', 
            'Y': 'C', 
            'Z': 'A',
        },
    }

    # points associated with each action
    scoremap = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    f = open('./day2input.txt', 'r')
    lines = f.readlines()
    
    score = 0
    for line in lines:
        oppChoice = line[0]
        outcome = line[2]
        myChoice = rpsmap[oppChoice][outcome]
        
        score += scoremap[myChoice]
        score += scoremap[outcome]
    
    print(score)
    
main()