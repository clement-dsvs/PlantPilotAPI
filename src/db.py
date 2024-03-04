from motor.motor_asyncio import AsyncIOMotorClient

mongo_uri = "mongodb+srv://cdesavis:ZnGa4pkR9L0YJt1t@cluster0.wdhqpjz.mongodb.net/?retryWrites=true&w=majority"
client = AsyncIOMotorClient(mongo_uri)
database = client["EPlantCare"]
