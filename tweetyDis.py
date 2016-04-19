import tweepy
from sys import *

auth = tweepy.OAuthHandler("Gv8QCJGNXEmSEZa28vTPyzuwK", "HTJx1dXSWiNUXNt9h17ImUGxODPYblUxiC2o5u3aBCpX1c0uVi")
auth.set_access_token("722402471453196289-o43vj9p8eKR8OaCmZAfH7CQpZAwamTB", "wPkoeBLa8BBPCc1aveddW73AzxuPMMmJlGCJndeiUAKSN")

api = tweepy.API(auth)

text = argv[1]

api.update_status(text)
print ("Done!")