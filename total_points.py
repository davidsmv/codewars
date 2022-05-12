# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

# For example: ["3:1", "2:2", "0:1", ...]

# Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

# if x > y: 3 points
# if x < y: 0 point
# if x = y: 1 point

def points(games):
    points = 0
    for i in games: 
        x = int((i[0:1]))
        y = int((i[2:3]))
        if x > y:
            points += 3
        elif x < y: 
            points += 0
        elif x == y:
            points += 1
    return points