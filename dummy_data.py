
def dummy_user_details():
    details = [{'username': 'Ari'},
               {'username': 'Ilona'},
               {'username': 'Jeremy'},
               {'username': 'Remy'},
               {'username': 'Yair'}]
    for i in range(len(details)):
        yield details[i]


def dummy_skill_categories():
    details = [{'skill_category': 'Coaching', 'image': 'https://images.unsplash.com/photo-1512291313931-d4291048e7b6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'},
               {'skill_category': 'Builder', 'image':'https://i.imgur.com/JZRAKsX.jpg'},
               {'skill_category': 'Gardener', 'image':'https://i.imgur.com/1brRN53.jpg'},
               {'skill_category': 'Mechanic', 'image':'https://i.imgur.com/wXwUYku.jpg'},
               {'skill_category': 'Mover', 'image': 'https://i.imgur.com/yHsNqQL.jpg'},
               {'skill_category': 'Beauty Care', 'image': 'https://i.imgur.com/N39z4Eh.jpg'},
               {'skill_category': 'Cooking', 'image': 'https://i.imgur.com/NbjQbsJ.jpg'},
               {'skill_category': 'Computer', 'image': 'https://i.imgur.com/QTWApEe.jpg'},
               {'skill_category': 'Cleaning', 'image': 'https://i.imgur.com/dJPwwln.jpg'},
               {'skill_category': 'Tutoring', 'image': 'https://i.imgur.com/bvYF7QZ.jpg'},
               {'skill_category': 'Plumber', 'image': 'https://i.imgur.com/P6TLN7H.jpg'},
               {'skill_category': 'Electrician', 'image': 'https://i.imgur.com/eshLvdh.jpg'},
               {'skill_category': 'Baby-sitter', 'image': 'https://i.imgur.com/oXbFh6M.jpg'},
               {'skill_category': 'Dog-sitter', 'image': 'https://i.imgur.com/b1V0dO8.jpg'},
               {'skill_category': 'Groceries', 'image': 'https://i.imgur.com/VzE4sCw.jpg'}
               ]
    for i in range(len(details)):
        yield details[i]


def dummy_skills():
    details = [{'skill': 'Mathematics', 'skill_category': 'Tutoring'},
               {'skill': 'Physics', 'skill_category': 'Tutoring'},
               {'skill': 'Electrician', 'skill_category': 'Home Repair'},
               {'skill': 'Plumber', 'skill_category': 'Home Repair'},
               {'skill': 'Self-help book provider', 'skill_category': 'Coaching'}]
    for i in range(len(details)):
        yield details[i]


def dummy_job_status():
    details = [{'status': 'Available'},
               {'status': 'Pending'},
               {'status': 'Complete'}]
    for i in range(len(details)):
        yield details[i]


def dummy_person_skills():
    details = [{'skill': 'Mathematics', 'skill_category': 'Tutoring'},
               {'skill': 'Physics', 'skill_category': 'Tutoring'},
               {'skill': 'Electrician', 'skill_category': 'Home Repair'},
               {'skill': 'Plumber', 'skill_category': 'Home Repair'},
               {'skill': 'Self-help book provider', 'skill_category': 'Coaching'}]
    for i in range(len(details)):
        yield details[i]


# a = dummy_user_details()
# for i in dummy_skills():
#     print(i)
# print(list(a))
