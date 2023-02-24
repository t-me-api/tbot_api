from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from .base import Request, TelegramMethod

if TYPE_CHECKING:
    from ..bot import Bot


class PinChatMessage(TelegramMethod[bool]):
    __returns__ = bool

    chat_id: Union[int, str]
    message_id: int
    disable_notification: Optional[bool] = None

    def request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="pinChatMessage", data=data)
