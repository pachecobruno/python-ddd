import uuid
from core.domain.account import Account


def test_account_model_init():
    code = uuid.uuid4()
    account = Account(code, name='Hubbe', alias='hubbe')

    assert account.uuid == code
    assert account.name == 'Hubbe'
    assert account.alias == 'hubbe'
    assert account.is_active is True
    assert account.settings == {}
    assert account.updated_at is not None
    assert account.created_at is not None

def test_account_model_from_dict():
    code = uuid.uuid4()
    account = Account.from_dict(
        {
            'code': code,
            'size': 200,
            'price': 10,
            'longitude': -0.09998975,
            'latitude': 51.75436293
        }
    )

    assert account.uuid == code
    assert account.name == 'Hubbe'
    assert account.alias == 'hubbe'
    assert account.is_active is True
    assert account.settings == {}
    assert account.updated_at is not None
    assert account.created_at is not None
