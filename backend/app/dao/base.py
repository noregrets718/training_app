
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel
from loguru import logger

class BaseDAO:
    model = None  # Устанавливается в наследниках



    @classmethod
    async def add(cls, session: AsyncSession, values: BaseModel): 
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(f"Добавление записи {cls.model.__name__} с параметрами: {values_dict}")
        instance = cls.model(**values_dict)
        session.add(instance)
        try:
            await session.flush()
            logger.info(f"Запись {cls.model.__name__} успешно добавлена.")
        except SQLAlchemyError as e:
            await session.rollback()
            logger.error(f"Ошибка при добавлении записи: {e}")
            raise e
        return instance
    


    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int, session: AsyncSession):
        # Найти запись по ID
        logger.info(f"Поиск {cls.model.__name__} с ID: {data_id}")
        try:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info(f"Запись с ID {data_id} найдена.")
            else:
                logger.info(f"Запись с ID {data_id} не найдена.")
            return record
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при поиске записи с ID {data_id}: {e}")
            raise



    @classmethod
    async def find_one_or_none(cls, session: AsyncSession, filters: BaseModel):
        # Найти одну запись по фильтрам
        filter_dict = filters.model_dump(exclude_unset=True)
        logger.info(f"Поиск одной записи {cls.model.__name__} по фильтрам: {filter_dict}")
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info(f"Запись найдена по фильтрам: {filter_dict}")
            else:
                logger.info(f"Запись не найдена по фильтрам: {filter_dict}")
            return record
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при поиске записи по фильтрам {filter_dict}: {e}")
            raise



    @classmethod
    async def find_all(cls, session: AsyncSession, filters: BaseModel | None = None):
        # Найти все записи по фильтрам
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(f"Поиск всех записей {cls.model.__name__} по фильтрам: {filter_dict}")
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query)
            records = result.scalars().all()
            logger.info(f"Найдено {len(records)} записей.")
            return records
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при поиске всех записей по фильтрам {filter_dict}: {e}")
            raise


    @classmethod
    async def delete(cls, session: AsyncSession, object_id: int) -> None:
        logger.info(f"Удаление записи {cls.model.__name__} с ID={object_id}")
        try:
            stmt = delete(cls.model).where(cls.model.id == object_id)
            await session.execute(stmt)
            logger.info(f"Запись с ID={object_id} удалена.")
        except SQLAlchemyError as e:
            await session.rollback()
            logger.error(f"Ошибка при удалении записи с ID={object_id}: {e}")
            raise

    
    
    @classmethod
    async def update(
        cls, session: AsyncSession, object_id: int, data: BaseModel
    ):
        update_data = data.model_dump(exclude_unset=True)
        logger.info(f"Обновление {cls.model.__name__} ID={object_id} с данными: {update_data}")
        try:
            stmt = (
                update(cls.model)
                .where(cls.model.id == object_id)
                .values(**update_data)
            )
            await session.execute(stmt)
            logger.info(f"Обновление записи {cls.model.__name__} с ID={object_id} прошло успешно.")
        except SQLAlchemyError as e:
            await session.rollback()
            logger.error(f"Ошибка при обновлении записи с ID={object_id}: {e}")
            raise
