has_membership = True
if not has_membership:
    print("Take membership")
else:
    print("Welcome member")    
# program 2
is_logged_in = True
is_blocked = False
if is_logged_in and not is_blocked:
    print("access granted")
else:
    print("access denied")    

# program 4
age = int(input("Enter your age"))
has_exam_hall_ticket = True
has_valid_id = False
accomplained_by_parents = True
if age >= 18 and has_exam_hall_ticket and (has_valid_id or accomplained_by_parents):
   print("allow access")
else:
   print("access denied")