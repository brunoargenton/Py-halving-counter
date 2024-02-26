from flask import Flask, render_template
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


@app.route('/')
def index():
    halving_data = get_blocks_until_halving()
    time_remaining = blocks_to_time(halving_data)
    # Passing data to render on the template
    return render_template('index.html', halving_data=halving_data, time_remaining=time_remaining)



if __name__ == "__main__":
    main()
