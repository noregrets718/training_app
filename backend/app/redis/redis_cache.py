from app.redis.client import redis_client
import json

def get_key(user_id: int) -> str:
    return f"unfinished_workout:{user_id}"

async def save_unfinished_workout(user_id: int, data: dict):
    key = get_key(user_id)
    await redis_client.set(key, json.dumps(data))

async def get_unfinished_workout(user_id: int) -> dict | None:
    key = get_key(user_id)
    data = await redis_client.get(key)
    return json.loads(data) if data else None

async def delete_unfinished_workout(user_id: int):
    key = get_key(user_id)
    await redis_client.delete(key)