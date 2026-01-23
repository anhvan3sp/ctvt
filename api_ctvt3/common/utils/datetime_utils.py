from datetime import datetime, date
from common.constants.datetime_constants import DATETIME_FORMAT, DATE_FORMAT


def now() -> datetime:
    return datetime.now()


def format_datetime(dt: datetime) -> str:
    return dt.strftime(DATETIME_FORMAT)


def parse_date(value: str) -> date:
    return datetime.strptime(value, DATE_FORMAT).date()
