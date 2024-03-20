from enum import Enum


class Environments(str, Enum):
    LOCAL = "LOCAL"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"
