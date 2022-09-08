from datetime import datetime

from . import BaseUser
from .dataclass import (
    Question as QuestionPayload,
    DetailQuestion as DetailQuestionPayload,
    Reply as ReplyPayload
)


class Question:
    def __init__(self, data: QuestionPayload):
        self.id = data.get("id")
        self.title = data.get("title")
        self.created = datetime.fromisoformat(data.get("created"))
        self.modified = datetime.fromisoformat(data.get("modified"))
        self.reply_count = data.get("count_reply")
        self.clip_count = data.get("count_crip")
        self.pv_count = data.get("count_pv")
        self.is_beginner = data.get("is_beginner")
        self.is_accepted = data.get("is_accepted")
        self.is_presentation = data.get("is_presentation")
        self.tags = data.get("tags", [])
        self.user = BaseUser(data.get("user"))


class DetailQuestion(Question):
    def __init__(self, data: DetailQuestionPayload):
        super().__init__(data)
        self.body = data.get("body")
        self.body_str = data.get("body_str")
        self.reply = Reply(data.get("reply"))


class Reply:
    def __init__(self, data: ReplyPayload):
        self.body = data.get("body")
        self.body_str = data.get("body_str")
        self.created = datetime.fromisoformat(data.get("created"))
        self.modified = datetime.fromisoformat(data.get("modified"))
        self.is_best_answer = data.get("is_best_answer")
