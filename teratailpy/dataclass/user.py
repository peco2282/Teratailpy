from typing import TypedDict, List


class BaseUser(TypedDict):
    display_name: str
    photo: str
    score: int


class Rank(TypedDict):
    rank: int
    score: int


class ScoreRank(TypedDict):
    total: Rank
    weekly: Rank


# class SNS(TypedDict):
#     twitter: str


# class BadgeLevel(TypedDict):
#     level: int
#     aquired_date: str


# class Badge(TypedDict):
#     常連: BadgeLevel
#     hello_world: BadgeLevel


class User(BaseUser):
    created: str
    modified: str
    department: str
    prefecture: str
    self_info: str
    blog: str
    score_ranking: ScoreRank
    tags: List[str]
    sns: str
    badges: str
