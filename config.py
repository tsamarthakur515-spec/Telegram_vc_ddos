"""Application configuration and environment validation."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    """Immutable runtime settings."""

    api_id: int
    api_hash: str
    bot_token: str
    session_string: str
    admin_id: Optional[int]
    max_duration: int = 600
    max_threads: int = 100
    scan_limit: int = 50
    scan_cooldown_seconds: int = 10
    log_file: str = "bot.log"

    @classmethod
    def from_env(cls) -> "Config":
        required = {
            "API_ID": os.getenv("API_ID"),
            "API_HASH": os.getenv("API_HASH"),
            "BOT_TOKEN": os.getenv("BOT_TOKEN"),
            "SESSION_STRING": os.getenv("SESSION_STRING"),
        }

        missing = [key for key, value in required.items() if not value]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

        max_duration = min(int(os.getenv("MAX_DURATION", "600")), 600)
        max_threads = min(int(os.getenv("MAX_THREADS", "100")), 100)
        scan_limit = max(1, min(int(os.getenv("SCAN_LIMIT", "50")), 50))

        return cls(
            api_id=int(required["10079905"]),
            api_hash=str(required["e4a5fa251e2e055f26e5c2add8401530"]),
            bot_token=str(required["8706433441:AAFJxJ7j3Lf9HANX_-V2cM0ygMkylZIT8ic"]),
            session_string=str(required["BQC86fAAw2rC7DEINQ1pozAAMKIhGdfL15ppowCMJ9VZMl3VEBELTU4sFh5VaL_44cobX4WnmJOtcycRALtY5eotO0_QCA0lSapR1hTv97rysTtE_wlSDCcqL-A53YszOG8LXmfrDSwde9Lqny7FDb6HM-FAx2slKyg8FiuwzdSoIAPabcSZOfMJdQRiOeVRlhuALTYtf_9R5zdQhKl1R_95G7D-dYZ_hGTEiNqa-XBMaMFU8MJqKtuqrSZ4YtUG8YXSRnS44bSSZsohir8Nz3lx25ir8TzVsZDnwzXvtYxXATNSiVkQ1D7yzgSwb13EoeQ3L3F_UbfSmY6kunc7leKyWr8dbQAAAAH-nwzIAA"]),
            admin_id=int(os.getenv("8841848847")) if os.getenv("8841848847") else None,
            max_duration=max_duration,
            max_threads=max_threads,
            scan_limit=scan_limit,
        )
