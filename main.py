import asyncio
import logging

from db.main_db import create_tables
from bot_config import dp,database
from handlers import (
    start,
    myinfo,
    random_names,
    complaint_dialog,
    store_fsm,
    send_products

)

async def main():


    start.register_handlers(dp)
    myinfo.register_handlers(dp)
    random_names.register_handlers(dp)
    complaint_dialog.register_handlers(dp)
    store_fsm.register_handlers(dp)
    # database.create_tables()
    # запуск бота
    await create_tables()
    await dp.start_polling()



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
