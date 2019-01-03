import numpy as np


def dummy_user_details():
    details = [{'username': 'Ari', 'city': 'Tel Aviv', 'image': 'placeholder', 'language': 'English', 'hobby': 'Daydreaming', 'age': '1000'},
               {'username': 'Ilona', 'city': 'Tel Aviv', 'image': 'placeholder', 'language': 'French', 'hobby': 'Football', 'age': '25'},
               {'username': 'Jeremy', 'city': 'Tel Aviv', 'image': 'placeholder', 'language': 'French', 'hobby': 'Football', 'age': '25'},
               {'username': 'Remy', 'city': 'Tel Aviv', 'image': 'placeholder', 'language': 'French', 'hobby': 'Piano', 'age': '25'},
               {'username': 'Yair', 'city': 'Tel Aviv', 'image': 'placeholder', 'language': 'French', 'hobby': 'Piano', 'age': '25'}]
    for i in range(len(details)):
        yield details[i]


def dummy_skill_categories():
    details = [{'skill_category': 'Coaching', 'image': 'https://images.unsplash.com/photo-1512291313931-d4291048e7b6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'},
               {'skill_category': 'Builder', 'image': 'https://i.imgur.com/cWnLqV9.jpg'},
               {'skill_category': 'Gardener', 'image': 'https://i.imgur.com/HggIaFy.jpg'},
               {'skill_category': 'Mechanic', 'image': 'https://i.imgur.com/B1AZAge.jpg'},
               {'skill_category': 'Mover', 'image': 'https://i.imgur.com/eBbmkSw.jpg'},
               {'skill_category': 'Beauty Care', 'image': 'https://i.imgur.com/XVbOhsj.jpg'},
               {'skill_category': 'Cooking', 'image': 'https://i.imgur.com/NbjQbsJ.jpg'},
               {'skill_category': 'Computer', 'image': 'https://i.imgur.com/QTWApEe.jpg'},
               {'skill_category': 'Cleaning', 'image': 'https://i.imgur.com/dJPwwln.jpg'},
               {'skill_category': 'Tutoring', 'image': 'https://i.imgur.com/bvYF7QZ.jpg'},
               {'skill_category': 'Plumber', 'image': 'https://i.imgur.com/P6TLN7H.jpg'},
               {'skill_category': 'Electrician', 'image': 'https://i.imgur.com/eshLvdh.jpg'},
               {'skill_category': 'Baby-sitter', 'image': 'https://i.imgur.com/oXbFh6M.jpg'},
               {'skill_category': 'Dog-sitter', 'image': 'https://i.imgur.com/b1V0dO8.jpg'},
               {'skill_category': 'Groceries', 'image': 'https://i.imgur.com/VzE4sCw.jpg'},
               {'skill_category': 'Home Repair', 'image': ''},
               {'skill_category': 'Being Yair', 'image': ''}
               ]
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
               {'status': 'Starting'},
               {'status': 'In Progress'},
               {'status': 'Finishing'},
               {'status': 'Complete'}]
    for i in range(len(details)):
        yield details[i]


def dummy_languages():
    details = [{'language': 'English'},
               {'language': 'French'},
               {'language': 'Hebrew'},
               {'language': 'Spanish'},
               {'language': 'German'},
               {'language': 'Italian'}]
    for i in range(len(details)):
        yield details[i]


def dummy_hobbies():
    details = [{'hobby': 'Daydreaming'},
               {'hobby': 'Football'},
               {'hobby': 'Basketball'},
               {'hobby': 'Tennis'},
               {'hobby': 'Piano'},
               {'hobby': 'Rugby'}]
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


def dummy_jobs_many(num_repeats):
    people = ['Ari', 'Ilona', 'Jeremy', 'Remy', 'Yair']
    people_w = [0.3, 0.2, 0.2, 0.2, 0.1]
    skills = ['Mathematics', 'Physics', 'Electrician', 'Plumber', 'Self-help book provider', 'Is Yair', 'Professional Wizard']
    skills_w = [0.05, 0.05, 0.15, 0.15, 0.1, 0.2, 0.3]

    for i in range(num_repeats):
        yield {'username': np.random.choice(people, size=1, p=people_w)[0], 'skill': np.random.choice(skills, size=1, p=skills_w)[0]}


