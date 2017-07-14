#Vote Goal Calculator

# The vote goal calculator needs a few inputs: past election results (1-3), past registration rates (1-3), current voter registration rate, number of candidates in the race

print("Welcome to the Vote Goal Calcualtor!")
print("To begin, first collect the voter turnout and registration totals from the three most recent, revelant elections for your office. In addition, find out how many voters are currently registered in the district.")

#Here we're collecting election turnout and voter registration rates.

election1turnout = int(input("How many people voted in the most recent, relevant election? "))
registration1 = int(input("How many people were registered to vote in your district at that time? "))

election2turnout = int(input("How many people voted in this second most recent, relevant election? "))
registration2 = int(input("How many people were registered to vote in your district at that time? "))

election3turnout = int(input("How many people voted in this third most recent, relevant election? "))
registration3 = int(input("How many people were registered to vote in your district at that time? "))

registration_now = int(input("How many people are currently registered to vote in your district? "))

# Calculating average turnout rates, registration rates and projected voter turnout

avgelectionturnout = float(((election1turnout + election2turnout + election3turnout)/3))
avgregistration = float(((registration1 + registration2 + registration3)/3))

avgvoterturnout = float((avgelectionturnout/avgregistration))

projected_turnout = int((avgvoterturnout*registration_now))

print("Awesome! You're projected to have a turnout of %s voters in your election." %(projected_turnout))

# Calculating vote goal given total number of candidates and projected turnout.

candidates = int(input("Now that you have your projected turnout, tell us how many candidates are running: "))

if candidates <=3:
	vote_goal = int(projected_turnout*.52)
	
else:
	vote_goal = int(projected_turnout*.40)

print("Congratulations! Your goal is %s votes!" %(vote_goal))

print("To review: Your current voter registration rate is %s, your projected turnout %s, there are %s candidates in your race and your vote goal is %s." %(registration_now,projected_turnout,candidates,vote_goal))
