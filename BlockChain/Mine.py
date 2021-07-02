import sys
import datetime
import hashlib
import json
from flask.json import jsonify
import requests

class Mine:

    def __init__(self,LastBlock,Transactions):
        self.NewBlock = self.GenerateBlock(BlockNumber = LastBlock['Block Number'], PreviousHash=LastBlock['Previous Hash'],
                                            Transactions = Transactions)
        
    def GenerateBlock(self, BlockNumber, PreviousHash, Transactions):

        Block = {

            'Block Number': BlockNumber+1,
            'Time Stamp': str(datetime.datetime.now()),
            'Nonce': 0,
            'Data': Transactions,
            'Previous Hash': PreviousHash
        }

        return Block

    def GenerateHashOfBlock(self, Block):

        return hashlib.sha512(json.dumps(Block, sort_keys=True).encode()).hexdigest()


    def Mine(self):
        while True:
            Proof = self.GenerateHashOfBlock(self.NewBlock)
            if Proof[0:5] != '0'*5:
                self.NewBlock['Nonce'] += 1
            else:
                self.NewBlock['Hash'] = Proof
                return self.NewBlock


Transactions = requests.get("http://0.0.0.0:9000/GetTransactions").json()
LastBlock = requests.get("http://0.0.0.0:9000/GetLastBlock").json()
Miner = Mine(LastBlock['Last Block'], Transactions['Transactions'])
NewBlock = Miner.Mine()
StatusCode = requests.post('http://0.0.0.0:9000/MinedBlock', json = {'New Block': NewBlock})
print(StatusCode)
