# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key-value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show them the final result when quiz is completed
import random


quiz_dict = {
    "question1"  : {"state"   : "Alabama",     "capital" : "Montgomery"},
    "question2"  : {"state"   : "Alaska",      "capital" : "Juneau"},
    "question3"  : {"state"   : "Arizona",     "capital" : "Phoenix"},
    "question4"  : {"state"   : "Arkansas",    "capital" : "Little Rock"},
    "question5"  : {"state"   : "California",  "capital" : "Sacramento"},
    "question6"  : {"state"   : "Colorado",    "capital" : "Denver"},
    "question7"  : {"state"   : "Connecticut", "capital" : "Hartford"},
    "question8"  : {"state"   : "Delaware",    "capital" : "Dover"},
    "question9"  : {"state"   : "Florida",     "capital" : "Tallahassee"},
    "question10" : {"state"   : "Georgia",     "capital" : "Atlanta"},
    "question11" : {"state"   : "Hawaii",      "capital" : "Honolulu"},
    "question12" : {"state"   : "Idaho",       "capital" : "Boise"},
    "question13" : {"state"   : "Illinois",    "capital" : "Springfield"},
    "question14" : {"state"   : "Indiana",     "capital" : "Indianapolis"},
    "question15" : {"state"   : "Iowa",        "capital" : "Des Moines"},
    "question16" : {"state"   : "Kansas",      "capital" : "Topeka"},
    "question17" : {"state"   : "Kentucky",    "capital" : "Frankfort"},
    "question18" : {"state"   : "Louisiana",   "capital" : "Baton Rouge"},
    "question19" : {"state"   : "Maine",       "capital" : "Augusta"},
    "question20" : {"state"   : "Maryland",    "capital" : "Annapolis"},
    "question21" : {"state"   : "Massachusetts","capital" : "Boston"},
    "question22" : {"state"   : "Michigan",    "capital" : "Lansing"},
    "question23" : {"state"   : "Minnesota",   "capital" : "Saint Paul"},
    "question24" : {"state"   : "Mississippi", "capital" : "Jackson"},
    "question25" : {"state"   : "Missouri",    "capital" : "Jefferson City"},
    "question26" : {"state"   : "Montana",     "capital" : "Helena"},
    "question27" : {"state"   : "Nebraska",    "capital" : "Lincoln"},
    "question28" : {"state"   : "Nevada",      "capital" : "Carson City"},
    "question29" : {"state"   : "New Hampshire","capital" : "Concord"},
    "question30" : {"state"   : "New Jersey",  "capital" : "Trenton"},
    "question31" : {"state"   : "New Mexico",  "capital" : "Santa Fe"},
    "question32" : {"state"   : "New York",    "capital" : "Albany"},
    "question33" : {"state"   : "North Carolina","capital" : "Raleigh"},
    "question34" : {"state"   : "North Dakota","capital" : "Bismarck"},
    "question35" : {"state"   : "Ohio",        "capital" : "Columbus"},
    "question36" : {"state"   : "Oklahoma",    "capital" : "Oklahoma City"},
    "question37" : {"state"   : "Oregon",      "capital" : "Salem"},
    "question38" : {"state"   : "Pennsylvania","capital" : "Harrisburg"},
    "question39" : {"state"   : "Rhode Island","capital" : "Providence"},
    "question40" : {"state"   : "South Carolina","capital" : "Columbia"},
    "question41" : {"state"   : "South Dakota","capital" : "Pierre"},
    "question42" : {"state"   : "Tennessee",   "capital" : "Nashville"},
    "question43" : {"state"   : "Texas",       "capital" : "Austin"},
    "question44" : {"state"   : "Utah",        "capital" : "Salt Lake City"},
    "question45" : {"state"   : "Vermont",     "capital" : "Montpelier"},
    "question46" : {"state"   : "Virginia",    "capital" : "Richmond"},
    "question47" : {"state"   : "Washington",  "capital" : "Olympia"},
    "question48" : {"state"   : "West Virginia","capital" : "Charleston"},
    "question49" : {"state"   : "Wisconsin",    "capital" : "Madison"},
    "question50" : {"state"   : "Wyoming",      "capital" : "Cheyenne"}  
}

def create_random_range(num_of_questions):
    a = range(1,51)
    list_choices = list(a)
    
    random_range = []
    for i in range(num_of_questions):
        random_pick = random.choice(list_choices)
        random_range.append(random_pick)
    
    return random_range

def play_quiz(random_range):
    score = 0
    
    for i in random_range:
        a = input(f"What is the capital of {quiz_dict['question'+str(i)]['state']}? : ")
        if a == quiz_dict['question'+str(i)]['capital']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect Answer!")
    
    print(f"\nTotal Score : {score}")


if __name__ == '__main__':
    
    random_range = create_random_range(10)
    play_quiz(random_range)