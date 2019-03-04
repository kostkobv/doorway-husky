from linkedinMan import LinkedinMan

def main():
    linkedin_man = get_linkedin()
    linkedin_man.find_profile(first_name='Test1', last_name='Test2')


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
