age = 19
has_voter_id = True
if age >= 18:
    if has_voter_id:
        print("You are eligible to vote.")
    else:
        print("You need a voter ID to vote.")
else:
    print("You are not eligible to vote.")