import json
from datetime import datetime

from .dataclass import (
    Rank as RankPayload,
    ScoreRank as ScoreRankPayload,
    BaseUser as BaseUserPayload,
    User as UserPayload
)


def _parse_datetime(_datetime: str):
    return datetime.fromisoformat(_datetime)


class Rank:
    def __init__(self, data: RankPayload):
        self.rank = data.get("rank")
        self.scord = data.get("score")


class ScoreRank:
    def __init__(self, data: ScoreRankPayload):
        self.total = Rank(data.get("total"))
        self.weekly = Rank(data.get("weekly"))


class BaseUser:
    def __init__(self, data: BaseUserPayload):
        self.display_name = data.get("display_name")
        self.photo = data.get("photo")
        self.score = data.get("score")


class User(BaseUser):
    def __init__(self, data: UserPayload):
        super(User, self).__init__(data)
        self.created_at = datetime.fromisoformat(data.get("created"))
        self.modified_at = datetime.fromisoformat(data.get("modified"))
        self.department = data.get("department")
        self.prefecture = data.get("prefecture")
        self.self_info = data.get("self_info")
        self.blog = data.get("blog")
        self.score_ranking = ScoreRank(data.get("score_ranking"))
        self.tags = data.get("tags", [])
        self.__sns = data.get("sns")
        try:
            self.__sns_twitter = json.loads(self.__sns).get("twitter")
            self.sns_twitter_level: int = self.__sns_twitter.get("level")
            self.sns_twitter_aquired_date: datetime = datetime.utcfromtimestamp(self.__sns_twitter.get("aquired_date"))

        except:
            self.sns_twitter_level = self.sns_twitter_aquired_date = None

        self.__badges = data.get("badges")
        try:
            self.__jouren = json.loads(self.__badges).get("常連")
            self.__hello_world = json.loads(self.__badges).get("hello world!")
            self.jouren_level: int = self.__jouren.get("level")
            self.jouren_aquired_date: datetime = datetime.utcfromtimestamp("aquired_date")
            self.hello_world_level: int = self.__hello_world.get("level")
            self.hello_world_aquired_date: datetime = datetime.utcfromtimestamp(self.__hello_world.get("aquired_date"))

        except:
            self.jouren_level = self.jouren_aquired_date = self.hello_world_level = self.hello_world_aquired_date = None
