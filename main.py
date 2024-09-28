"""Module that contains main application logic."""

import asyncio

from dotenv import load_dotenv

from logger.logger import logger
from spider.spider import run_search


def load_env() -> (str, str, str, int):
    """
    Load ENV variables.
    :return: postgres_user, postgres_password, postgres_db
    """
    load_dotenv()
    # return postgres_user, postgres_password, postgres_db


async def main():
    """
    Main function.
    :return:
    """
    logger.info("Application started.")

    # Load env variables.
    # postgres_user, postgres_password, postgres_db = load_env()

    # Run the spider.
    await run_search()

    logger.info("Application finished.")


if __name__ == "__main__":
    asyncio.run(main())
