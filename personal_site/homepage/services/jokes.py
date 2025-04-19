import httpx

JOKES_API_URL = "https://v2.jokeapi.dev/joke/Programming?type=single"


async def get_single_joke() -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(JOKES_API_URL)
    return response.json()["joke"]
