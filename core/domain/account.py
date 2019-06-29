from datetime import datetime


class Account:

    def __init__(self, uuid, name, alias, settings=None) -> None:
        super().__init__()

        if settings is None:
            settings = {}

        self.uuid = uuid
        self.name = name
        self.alias = alias
        self.is_active = True
        self.settings = settings
        self.updated_at = datetime.now().astimezone()
        self.created_at = datetime.now().astimezone()
