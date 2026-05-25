from __future__ import annotations

import logging
import re

SECRET_PATTERNS = [re.compile(r"(sk-[A-Za-z0-9_-]+)"), re.compile(r"(?i)(jwt_secret|session_secret|api_key)=([^\s]+)")]


class SecretRedactionFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        for pattern in SECRET_PATTERNS:
            message = pattern.sub("[REDACTED]", message)
        record.msg = message
        record.args = ()
        return True


def configure_logging(level: str = "INFO") -> None:
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    logging.getLogger().addFilter(SecretRedactionFilter())
