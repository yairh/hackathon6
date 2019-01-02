
def dummy_user_details():
    details = [{'username': 'Ari', 'city': 'Tel Aviv'},
               {'username': 'Ilona', 'city': 'Tel Aviv'},
               {'username': 'Jeremy', 'city': 'Tel Aviv'},
               {'username': 'Remy', 'city': 'Tel Aviv'},
               {'username': 'Yair', 'city': 'Tel Aviv'}]
    for i in range(len(details)):
        yield details[i]


def dummy_skill_categories():
    details = [{'skill_category': 'Coaching', 'image': 'placeholder'},
               {'skill_category': 'Tutoring', 'image': 'placeholder'},
               {'skill_category': 'Home Repair', 'image': 'placeholder'},
               {'skill_category': 'Being Yair', 'image': 'placeholder'}]
    for i in range(len(details)):
        yield details[i]


def dummy_skills():
    details = [{'skill': 'Mathematics', 'skill_category': 'Tutoring', 'image': 'placeholder'},
               {'skill': 'Physics', 'skill_category': 'Tutoring', 'image': 'placeholder'},
               {'skill': 'Electrician', 'skill_category': 'Home Repair', 'image': 'placeholder'},
               {'skill': 'Plumber', 'skill_category': 'Home Repair', 'image': 'placeholder'},
               {'skill': 'Self-help book provider', 'skill_category': 'Coaching', 'image': 'placeholder'},
               {'skill': 'Is Yair', 'skill_category': 'Being Yair', 'image': 'placeholder'},
               {'skill': 'Professional Wizard', 'skill_category': 'Being Yair', 'image': 'placeholder'}]
    for i in range(len(details)):
        yield details[i]


def dummy_statuses():
    details = [{'status': 'Available'},
               {'status': 'Pending'},
               {'status': 'Complete'}]
    for i in range(len(details)):
        yield details[i]


def dummy_person_skills():
    details = [{'username': 'Yair', 'skill': 'Self-help book provider'},
               {'username': 'Yair', 'skill': 'Is Yair'},
               {'username': 'Ilona', 'skill': 'Mathematics'},
               {'username': 'Jeremy', 'skill': 'Self-help book provider'},
               {'username': 'Ilona', 'skill': 'Physics'},
               {'username': 'Yair', 'skill': 'Mathematics'},
               {'username': 'Remy', 'skill': 'Plumber'},
               {'username': 'Yair', 'skill': 'Electrician'},
               {'username': 'Yair', 'skill': 'Professional Wizard'},
               {'username': 'Yair', 'skill': 'Electrician'},
               {'username': 'Yair', 'skill': 'Physics'}]
    for i in range(len(details)):
        yield details[i]

def dummy_jobs():
    details = [{'username': 'Ari', 'skill': 'Self-help book provider'},
               {'username': 'Ari', 'skill': 'Mathematics'},
               {'username': 'Ari', 'skill': 'Physics'},
               {'username': 'Ari', 'skill': 'Electrician'},
               {'username': 'Ari', 'skill': 'Plumber'},
               {'username': 'Ari', 'skill': 'Self-help book provider'},
               {'username': 'Ilona', 'skill': 'Electrician'},
               {'username': 'Jeremy', 'skill': 'Professional Wizard'},
               {'username': 'Remy', 'skill': 'Electrician'},
               {'username': 'Jeremy', 'skill': 'Plumber'},
               {'username': 'Ilona', 'skill': 'Professional Wizard'},
               {'username': 'Ari', 'skill': 'Is Yair'}]
    for i in range(len(details)):
        yield details[i]
