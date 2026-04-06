def test_user_created_in_db(api_client, db_client, user_factory):

    user = user_factory.build()

    created_user = api_client.create_user(user)

    db_user = db_client.get_user_by_email(user.email)

    assert db_user is not None
    assert db_user["email"] == user.email