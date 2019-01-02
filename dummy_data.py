
def dummy_user_details():
    details = [{'username': 'Ari'},
               {'username': 'Ilona'},
               {'username': 'Jeremy'},
               {'username': 'Remy'},
               {'username': 'Yair'}]
    for i in range(len(details)):
        yield details[i]


def dummy_skill_categories():
    details = [{'skill_category': 'Coaching'},
               {'skill_category': 'Tutoring'},
               {'skill_category': 'Home Repair'}]
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
