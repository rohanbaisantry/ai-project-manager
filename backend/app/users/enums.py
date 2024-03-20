from enum import Enum


class UserChatSentBy(str, Enum):
    USER = "USER"
    SYSTEM = "SYSTEM"


class UserRoles(str, Enum):
    ADMIN = "ADMIN"
    TEAM_MEMBER = "TEAM_MEMBER"
