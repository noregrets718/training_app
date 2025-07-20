import json
from typing import List
from app.redis.client import redis_client
from app.exercises.schemas import ExerciseRead

CACHE_KEY = "exercises:list"
CACHE_TTL_SECONDS = 3600  # 1 час

async def get_cached_exercises() -> List[ExerciseRead] | None:
    data = await redis_client.get(CACHE_KEY)
    if data is None:
        return None
    parsed = json.loads(data)
    return [ExerciseRead.model_validate(item) for item in parsed]

async def set_cached_exercises(exercises: List[ExerciseRead]):
    json_data = json.dumps([exercise.model_dump() for exercise in exercises])
    await redis_client.set(CACHE_KEY, json_data, ex=CACHE_TTL_SECONDS)

async def invalidate_cached_exercises():
    await redis_client.delete(CACHE_KEY)