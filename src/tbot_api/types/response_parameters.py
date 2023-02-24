from __future__ import annotations

from typing import Optional

from .base import TelegramObject


class ResponseParameters(TelegramObject):
    migrate_to_chat_id: Optional[int] = None
    retry_after: Optional[int] = None
