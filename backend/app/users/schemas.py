from pydantic import BaseModel, ConfigDict




class TelegramIDModel(BaseModel):
    telegram_id: int

    model_config = ConfigDict(from_attributes=True)



class UserModel(TelegramIDModel):
    username: str | None