"""Agent with RAG search."""

import asyncio

from examples.rag.rag_pipeline import DOC_PATH, QUESTION
from acrionai.logs import logger
from acrionai.rag.engines import SimpleEngine
from acrionai.roles import Sales


async def search():
    """Agent with RAG search."""

    store = SimpleEngine.from_docs(input_files=[DOC_PATH])
    role = Sales(profile="Sales", store=store)
    result = await role.run(QUESTION)
    logger.info(result)


if __name__ == "__main__":
    asyncio.run(search())
