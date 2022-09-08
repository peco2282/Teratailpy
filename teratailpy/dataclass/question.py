from typing import TypedDict, List

from . import Tag, BaseUser


class Reply(TypedDict):
    body: str
    body_str: str
    created: str
    modified: str
    is_best_answer: bool
    user: BaseUser


class Question(TypedDict):
    id: int
    title: str
    created: str
    modified: str
    count_reply: int
    count_crip: int
    count_pv: int
    is_beginner: bool
    is_accepted: bool
    is_presentation: bool
    tags: List[str]
    user: BaseUser


class DetailQuestion(Question):
    body: str
    body_str: str
    reply: List[Reply]
