from datetime import datetime

from .dataclass import Tag as TagPayload


class Tag:
    def __init__(self, data: TagPayload):
        self.tag_name: str = data.get("tag_name")
        self.explain: str = data.get("explain")
        self.created: datetime = datetime.fromisoformat(data.get("created"))
