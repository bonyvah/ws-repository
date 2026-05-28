import os 
import tempfile
from repos.sqlite_repo import SQLiteRepository

def test_save_and_find_by_email():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        db_path = tmp.name
    
    repo = SQLiteRepository(db_path)
    user = {"name":"Alice", "email":"alice@example.com", "age":30}

    repo.save(user)

    result = repo.find_by_email("alice@example.com")
    assert result == user

    os.remove(db_path)