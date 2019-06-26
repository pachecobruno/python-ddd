from uuid import uuid4, UUID
from datetime import datetime
from core.domain.user import User


first_name = 'Bruno'
last_name = 'Pacheco'
alias = 'brunopacheco'
email = 'bruno@hubbe.co'
password = 'mypass123'
account = uuid4()
date = datetime.utcnow()


def test_user_model_init():

    user = User(
        first_name=first_name,
        last_name=last_name,
        alias=alias,
        email=email,
        password=password,
        account=account
    )

    assert UUID(str(user.uuid), version=4)
    assert user.first_name == first_name
    assert user.last_name == last_name
    assert user.alias == alias
    assert user.email == email
    assert user.password == password
    assert user.account == account
    assert user.public_key.split('.')[1] == user.uuid
    assert user.secret_key.split('.')[0] == 'sk'
    assert user.settings == {}
    assert user.created_at < date
    assert user.updated_at < date


def test_account_model_from_dict():

    user = User.from_dict(
        {
            'first_name': first_name,
            'last_name': last_name,
            'alias': alias,
            'email': email,
            'password': password,
            'account': account,
            # 'settings': {},
        }
    )

    assert UUID(str(user.uuid), version=4)
    assert user.first_name == first_name
    assert user.last_name == last_name
    assert user.alias == alias
    assert user.email == email
    assert user.password == password
    assert user.account == account
    assert user.public_key.split('.')[1] == user.uuid
    assert user.secret_key.split('.')[0] == 'sk'
    assert user.settings == {}
    assert user.created_at < date
    assert user.updated_at < date
