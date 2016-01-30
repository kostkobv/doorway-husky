from linkedinMan import LinkedinMan

API_KEY = '77advieyqqgu6l'
API_SECRET = 'juj9gwefJdIjMeD6'


def main():
    linked = LinkedinMan(api_key=API_KEY, api_secret=API_SECRET)
    linked.authentication()

    app = linked.get_app()


if __name__ == '__main__':
    main()
