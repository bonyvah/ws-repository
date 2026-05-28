
class InMemoryRepository:
    def __init__(self):
        self.users = {}

    def save(self, user: dict) -> None:
        if user['email'] in self.users:
            raise ValueError("duplicate email")
        self.users[user['email']] = user

    def find_by_email(self, email: str) -> dict:
        return self.users.get(email, {})
