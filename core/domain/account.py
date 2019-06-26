

"""
TODO:   * Os conceitos abaixo deverão ser utilizados em todo o projeto:
        ** Remover regras de validação do construtor (se houver)
        ** Disponibilizar um método factory para os objetos
        ** Validações devem ocorrer no método factory
        ** Priorizar o uso de classes imutáveis (sem esterações no estado interno)
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional
from uuid import uuid4, UUID

"""
import mashumaro
import eventsourcing
"""

# from core.shared.domain_model import DomainModel


@dataclass
class Account:
    name: str
    alias: str
    _uuid: UUID = field(default_factory=uuid4)
    domains: List[str] = field(default_factory=list)
    settings: Dict = field(default_factory=dict)
    is_active: bool = Truex
    _updated_at: Optional[datetime] = None
    _created_at: datetime = datetime.now().astimezone()

    @property
    def uuid(self) -> str:
        return str(self._uuid)

    @property
    def updated_at(self) -> Optional[str]:
        return self._updated_at.isoformat() or None

    @property
    def created_at(self) -> str:
        return self._created_at.isoformat()

    @classmethod
    def from_dict(cls, account_dict):
        account = Account(
            _uuid=UUID(account_dict['uuid'], version=4),
            name=account_dict['name'],
            alias=account_dict['alias'],  # Unique. Space/namespace/tenantId
            domains=account_dict['domains'],
            settings=account_dict['settings'],
            is_active=account_dict['is_active'],
            _updated_at=account_dict['updated_at'],
            _created_at=account_dict['created_at'],
        )

        return account

    def __repr__(self):
        return f'account.uuid: {self.uuid}, account.name: {self.name}'

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


# DomainModel.register(Account)

