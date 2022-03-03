from loader import session
from config import api_key


async def get_current(lat: int, lon: int):
    params = {
        'lat': lat,
        'lon': lon,
        'lang': 'ru_RU',
        'extra': 'true'
    }
    headers = {'X-Yandex-API-Key': api_key}
    async with session.get(
            f'https://api.weather.yandex.ru/v2/forecast',
            params=params,
            headers=headers
    ) as response:
        return await response.json()
