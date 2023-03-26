# Q3. Consider an ongoing test cricket series. Following are the names of the players and their
# scores in the test1 and 2.
# Test Match 1 :
# Dhoni : 56 , Balaji : 94
# Test Match 2 :
# Balaji : 80 , Dravid : 105
# Calculate the highest number of runs scored by an individual cricketer in both of the matches.
# Create a python function Max_Score (M) that reads a dictionary M that recognizes the player
# with the highest total score. This function will return ( Top player , Total Score ) . You can
# consider the Top player as String who is the highest scorer and Top score as Integer .
# Input : Max_Score({‘test1’:{‘Dhoni’:56, ‘Balaji : 85}, ‘test2’:{‘Dhoni’ 87, ‘Balaji’’:200}})
# Output : (‘Balaji ‘ , 200)


class Cricket_Series:
    def __init__(self):
        pass

    def Max_Score(self, m: {}):
        list2 = []
        for k, v in m.items():
            for k1,v1 in v.items():
                list2.append(v1)

        for k3, v3 in m.items():
            for k4,v4 in v3.items():
                if v4 == max(list2):
                    return (k4, v4)

#cricketObj = Cricket_Series()


#output = cricketObj.Max_Score({"test1":{"Dhoni":56, "Balaji":85}, "test2":{"Dhoni":87, "Balaji":200}})
#print(output)



from collections import Counter

def Max_Score(M):
    res = [ ]
    for key, val in M.items():
        cnt = Counter(val)
        res.append({ key: cnt.most_common(1)[ 0 ] })
    return res

Score = Max_Score({ 'test1': { 'Dhoni': 56, 'Balaji': 85 }, 'test2': { 'Dhoni': 87, 'Balaji': 200 } })

Highest_Score = (Score[1].get('test2'))
print(Highest_Score)
