import asyncio
import logging

from bot_config import dp,database
from handlers import (
    start,
    myinfo,
    random_names,
    complaint_dialog,

)

async def main():
    start.register_handlers(dp)
    myinfo.register_handlers(dp)
    random_names.register_handlers(dp)
    complaint_dialog.register_handlers(dp)
    database.create_tables()
    # запуск бота
    await dp.start_polling()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

