import arrow
from dataclasses import dataclass, field
from datetime import datetime, timezone, tzinfo
from typing import List, Dict, Optional
from uuid import uuid4, UUID

# from core.shared.domain_model import DomainModel


@dataclass
class User:
    first_name: str
    last_name: str
    alias: str
    email: str
    account: UUID
    _uuid: UUID = field(default_factory=uuid4)
    _settings: Dict = field(default_factory=dict)
    _is_active: bool = True
    _updated_at: Optional[datetime] = None
    _created_at: datetime = datetime.now().astimezone()

    @property
    def uuid(self) -> str:
        return str(self._uuid)

    @property
    def account(self) -> str:
        return str(self.account)

    @property
    def updated_at(self) -> Optional[str]:
        return self._updated_at.isoformat() or None

    @property
    def created_at(self) -> str:
        return self._created_at.isoformat()

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def from_dict(cls, user_dict):
        user = User(
            _uuid=UUID(user_dict['uuid'], version=4),
            account=UUID(user_dict['account'], version=4),
            first_name=user_dict['first_name'],
            last_name=user_dict['last_name'],
            alias=user_dict['alias'],
            email=user_dict['email'],
            _settings=user_dict['settings'],
            _is_active=user_dict['is_active'],
            _updated_at=user_dict['update_at'],
            _created_at=user_dict['created_at'],
        )
        return user

    def __repr__(self):
        return f'user.uuid: {self.uuid}, user.full_name: {self.full_name}, user.account: {self.account}'

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


# DomainModel.register(Account)

