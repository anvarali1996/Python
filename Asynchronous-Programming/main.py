import asyncio
import random

# Simulate an asynchronous network request
async def fetch_data(user_id):
    print(f"Fetching data for user {user_id}...")
    await asyncio.sleep(random.uniform(0.5, 1.5))  # simulate network delay
    print(f"Finished fetching data for user {user_id}")
    return {"user_id": user_id, "data": f"Sample data for {user_id}"}

# Gather all requests concurrently
async def main():
    user_ids = [1, 2, 3, 4, 5]
    tasks = [fetch_data(uid) for uid in user_ids]
    results = await asyncio.gather(*tasks)
    print("\nAll data fetched:")
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
