from tbot_api.enums import StickerType
from tbot_api.types import Sticker


class TestSticker:
    def test_get_profile_photos(self) -> None:
        sticker = Sticker(
            file_id="test",
            file_unique_id="test",
            type=StickerType.REGULAR,
            width=100,
            height=100,
            is_animated=False,
            is_video=False,
        )

        method = sticker.set_position_in_set(position=1)
        assert method.sticker == sticker.file_id

    def test_delete_from_set(self) -> None:
        sticker = Sticker(
            file_id="test",
            file_unique_id="test",
            type=StickerType.REGULAR,
            width=100,
            height=100,
            is_animated=False,
            is_video=False,
        )

        method = sticker.delete_from_set()
        assert method.sticker == sticker.file_id
