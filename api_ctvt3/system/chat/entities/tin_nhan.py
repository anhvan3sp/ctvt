from dataclasses import dataclass


@dataclass
class TinNhan:
    id: int
    phong_chat_id: int
    user_id: int
    noi_dung: str
