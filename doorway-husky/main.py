from linkedinMan import LinkedinMan

API_KEY = '77advieyqqgu6l'
API_SECRET = 'juj9gwefJdIjMeD6'


def main():
    linkedin_man = get_linkedin()
    linkedin_man.find_profile(first_name='Bohdan', last_name='Kostko')


def get_linkedin():
    """
    Authenticates and returns the ready for making requests to API LinkedinMan instance

    :return: linkedin app
    """
    linkedin_man = LinkedinMan(api_key=API_KEY, api_secret=API_SECRET)
    linkedin_man.authentication()

    return linkedin_man

if __name__ == '__main__':
    main()
