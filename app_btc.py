import requests
from datetime import datetime, timedelta

def get_blocks_until_halving():
    # Get the current block height
    response = requests.get("https://api.blockchair.com/bitcoin/stats")
    data = response.json()
    current_block_height = data["data"]["blocks"]
    blocks_day = data["data"]["blocks_24h"]
    transactions_day = data["data"]["transactions_24h"]
    largest_day_usd = data["data"]["largest_transaction_24h"]["value_usd"]
    largest_day_usd = '{:0,.2f}'.format(float(largest_day_usd))
    next_halving_block = ((current_block_height // 210000) +1) * 210000
    
    # Calculate
    blocks_remaining = next_halving_block - current_block_height
    halving_data = [blocks_remaining, next_halving_block, current_block_height, blocks_day, transactions_day, largest_day_usd]

    return halving_data 

def blocks_to_time(halving_data):
    # Blocks to time, assuming 10 minutes per block
    minutes_remaining = halving_data[0] * 10
    time_remaining = str(timedelta(minutes=minutes_remaining))

    return time_remaining

def main():
    
    halving_data = get_blocks_until_halving()
    time_remaining = blocks_to_time(halving_data)

    print(f"Current Block Height: {halving_data[2]}")
    print(f"Next Halving Block: {halving_data[1]}")
    print(f"Blocks Remaining: {halving_data[0]}")
    print(f"Time Remaining: {time_remaining}")
    print('')
    print(f"Blocks 24h: {halving_data[3]}")
    print(f"Transactions 24h: {halving_data[4]}")
    print(f"Largest Transaction 24h: {halving_data[5]} USD")

if __name__ == "__main__":
    main()
