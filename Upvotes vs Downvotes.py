def get_vote_count(votes):
	return votes["upvotes"] - votes["downvotes"]                  # taking value of upvote and value of downvote then calculating difference
print(get_vote_count({ "upvotes": 2, "downvotes": 33 }))
