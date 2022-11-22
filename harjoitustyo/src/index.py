from UserRepository import user_repository

def main():
    print("Moi")
    db = user_repository
    print(db.users_size())


if __name__ == "__main__":
    main()