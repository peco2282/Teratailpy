from typing import List, Optional

from . import (
    HTTPClient,
    Route,
    Reply,
    User,
    BaseUser,
    Question,
    InvalidLimitRequested,
    Tag
)



class Client:
    def __init__(self, token: str):
        self.token = token
        self.http = HTTPClient(token=token)

    def get_questions(self, page: int = 1, limit: int = 20) -> Optional[List[Question]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")
        r = Route(method="GET", endpoint=f"questions?limit={limit}&page={page}")
        response = self.http.request(route=r)
        return [Question(question) for question in response.get("questions")]

    def get_question(self, question_id: str) -> Optional[Question]:
        r = Route(method="GET", endpoint=f"questions/{question_id}")
        response = self.http.request(route=r)
        return Question(response.get("question"))

    def get_users(self, page: int = 1, limit: int = 20) -> Optional[List[BaseUser]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")

        r = Route(method="GET", endpoint=f"users?limit={limit}&page={page}")
        response = self.http.request(route=r)
        return [BaseUser(user) for user in response.get("users")]

    def get_user(self, display_name: str) -> Optional[User]:
        r = Route(method="GET", endpoint=f"users/{display_name}")
        response = self.http.request(route=r)
        return User(response.get("user"))

    def search_users(self, query: str, page: int = 1, limit: int = 20) -> Optional[List[BaseUser]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")

        r = Route(method="GET", endpoint=f"users/search?q={query}&page={page}&limit={limit}")
        response = self.http.request(route=r)
        return [BaseUser(base) for base in response.get("users")]

    def get_user_clips(self, display_name: str, page: int = 1, limit: int = 20):
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")

        r = Route(method="GET", endpoint=f"users/{display_name}/clips?page={page}&limit={limit}")
        response = self.http.request(route=r)
        return response.get("clips")

    def get_user_tags(self, display_name: str, page: int = 1, limit: int = 20) -> Optional[List[Tag]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")

        r = Route(method="GET", endpoint=f"users/{display_name}/tags?page={page}&limit={limit}")
        response = self.http.request(route=r)
        return [Tag(tag) for tag in response.get("tags")]

    def get_user_questions(self, display_name: str, page: int = 1, limit: int = 20) -> Optional[List[Question]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")

        r = Route(method="GET", endpoint=f"users/{display_name}/questions?page={page}&limit={limit}")
        response = self.http.request(route=r)
        return [Question(question) for question in response.get("questions")]

    def get_user_replies(self, display_name: str, page: int = 1, limit: int = 20) -> Optional[List[Reply]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")

        r = Route(method="GET", endpoint=f"users/{display_name}/replies?page={page}&limit={limit}")
        response = self.http.request(route=r)
        return [Reply(reply) for reply in response.get("replies")]

    def get_followers(self, display_name: str, page: int = 1, limit: int = 20) -> Optional[List[BaseUser]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")

        r = Route(method="GET", endpoint=f"users/{display_name}/followers?page={page}&limit={limit}")
        response = self.http.request(route=r)
        return [BaseUser(user) for user in response.get("users")]

    def get_followings(self, display_name: str, page: int = 1, limit: int = 20) -> Optional[List[BaseUser]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " and "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")

        r = Route(method="GET", endpoint=f"users/{display_name}/followings?page={page}&limit={limit}")
        response = self.http.request(route=r)
        return [BaseUser(user) for user in response.get("users")]

    def get_tags(self, page: int = 1, limit: int = 20) -> Optional[List[Tag]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " & "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")
        r = Route(method="GET", endpoint=f"tags?limit={limit}&page={page}")
        response = self.http.request(route=r)
        return [Tag(tag) for tag in response.get("tags")]

    def get_tag(self, tag_name: str) -> Optional[List[Tag]]:
        r = Route(method="GET", endpoint=f"tags/{tag_name}")
        response = self.http.request(route=r)
        return Tag(response.get("tag"))

    def get_questions_with_tag(self, tag_name: str, page: int = 1, limit: int = 20) -> Optional[List[Question]]:
        if not (isinstance(page, int) and isinstance(limit, int)):
            raise TypeError(
                "page and limit must be int object, given {}"
                .format(
                    " & "
                    .join(
                        [f"{obj}" for obj in (limit, page)
                         if not isinstance(obj, int)]
                    )
                )
            )
        if not (1 <= limit <= 100):
            raise InvalidLimitRequested("`limit` must be between 1 and 100.")
        r = Route(method="GET", endpoint=f"tags/{tag_name}/questions?page={page}&limit={limit}")
        response = self.http.request(route=r)
        return [Question(questions) for questions in response.get("questions")]
