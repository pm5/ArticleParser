from typing import *
import pugsql
from datetime import datetime
from uuid import UUID
import json


def module(module_path):
    return pugsql.module("queries")


def to_uuid(u: str = None, default=None) -> UUID:
    if u is None:
        return default
    else:
        return UUID(u)


def of_uuid(u: UUID) -> str:
    return str(u).replace("-", "")


def to_datetime(ts: int = None, default=None) -> datetime:
    if ts is None:
        return default
    else:
        return datetime.fromtimestamp(ts)


def of_datetime(d: datetime) -> int:
    return int(d.timestamp())


def to_json(j: str = None, default=None) -> Any:
    if j is None:
        return default
    else:
        return json.loads(j)


def of_json(j: Any) -> str:
    return json.dumps(j)


def to_producer(row):
    return {
        "producer_id": to_uuid(row["producer_id"]),
        **{
            k: row[k]
            for k in ["name", "classification", "url", "scraper_id", "site_id"]
        },
        "first_seen_at": to_datetime(row["first_seen_at"], default=""),
        "last_updated_at": to_datetime(row["last_updated_at"], default=""),
        "data": to_json(row["data"], default={}),
    }


def to_producers(rows):
    for row in rows:
        yield to_producer(row)
