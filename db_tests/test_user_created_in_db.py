

def test_user_created_in_db(db_client, user_email):
    try:
        db_client.create_user(user_email)

        db_user = db_client.get_user_by_email(user_email)

        assert db_user is not None
        assert db_user["email"] == user_email
        assert "id" in db_user

    finally:
        db_client.delete_user(user_email)


def test_user_not_found(db_client, user_email):
    db_user = db_client.get_user_by_email(user_email)
    assert db_user is None