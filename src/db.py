from motor.motor_asyncio import AsyncIOMotorClient

mongo_uri = ""
client = AsyncIOMotorClient(mongo_uri)
database = client["EPlantCare"]
