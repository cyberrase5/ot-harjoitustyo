from UserRepository import user_repository
from initialize_database import initialize_database

def main():
    print("Moi")
    initialize_database()
    db = user_repository
    print(db.users_size())
    


if __name__ == "__main__":
    main()