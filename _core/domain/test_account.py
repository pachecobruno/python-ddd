from uuid import uuid4, UUID
from datetime import datetime
from account import Account

accounts = {
    'simple_init': {
        'name': 'Hubbe',
        'alias': 'hubbe'
    },
    'account1': {
        'uuid': '150beb26-361d-4a20-b029-58b6b081e6f1',
        'name': 'Core Account',
        'alias': 'core-account',
        'domains': ['core-accounts.com', 'core-accounts.net'],
        'setting': {},
        'is_active': True,
        'updated_at': None,
        'created_at': datetime.utcnow()
    },
    'account2': {
        'uuid': '10edaeb8-1fbe-49d0-aedf-1865c20e84de',
        'name': 'Hubbe Corp',
        'alias': 'hubbe-corp',
        'domains': ['hubbe.co'],
        'setting': {
            'logo_url': 'http://statiuc.hubbe.co/12345678.png'
        },
        'is_active': True,
        'updated_at': datetime.utcnow(),
        'created_at': datetime.utcnow()
    },
    'error_account1': {
        'name': 'Hubbe Corp',
        'alias': 'hubbe-corp',
        'domains': 'hubbe.co',
        'setting': True,
        'is_active': None,
        'updated_at': datetime.utcnow(),
        'created_at': datetime.utcnow()
    },
    'error_account2': {},
    'error_account3': {},
}


def test_account_model_init():

    account = Account(
        name=accounts['simple_init']['name'],
        alias=accounts['simple_init']['alias'],
    )

    assert UUID(str(account.uuid), version=4)
    assert account.name == accounts['simple_init']['name']
    assert account.alias == accounts['simple_init']['alias']
    assert account.domains == []
    assert account.settings == {}

    # isodate_format_str = '%Y-%m-%dT%H:%M:%S.%f%z'
    # created_at = datetime.strptime(account.created_at, isodate_format_str)
    # updated_at = datetime.strptime(account.updated_at, isodate_format_str) if account.updated_at is not None else None
    #
    # assert account.created_at == created_at.isoformat()
    # assert account.updated_at == updated_at.isoformat() or None


def test_account_model_from_dict():
    """
    account = Account.from_dict(
        {
            'name': name,
            'slug': slug,
            'domain': domain,
            'settings': None
        }
    )

    assert UUID(str(account.uuid), version=4)
    assert account.name == name
    assert account.slug == slug
    assert account.domains == [domain]
    assert account.created_at < date
    assert account.updated_at < date
    """
