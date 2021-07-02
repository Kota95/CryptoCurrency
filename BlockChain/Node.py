import sys
import datetime
import hashlib
import json
import time
import atexit
import requests
from BlockChain import BlockChain, GenesisBlock
from MemPool import MemPool
from Nodes import Nodes
from flask import Flask, jsonify, request


app = Flask(__name__)

BlockChain = BlockChain(GenesisBlock().GetGenesisBlock())
MemPool = MemPool()
Nodes = Nodes()



@app.route('/GetUpdate', methods = ['GET'])
def Update():
    return jsonify({'Chain': BlockChain.Chain,
            'Nodes': Nodes.GetNodes(), 'Length': len(BlockChain.Chain)}), 200

@app.route('/Transaction', methods = ['POST'])
def Transaction():
    Transaction = request.get_json()
    MemPool.NewTransactions(Transaction['Transaction'])
    return 'OK', 200

@app.route('/GetTransactions', methods = ['GET'])
def GetTransactions():
    print(MemPool.GetTransactions())
    return jsonify({'Transactions': MemPool.GetTransactions()}), 200
    

@app.route('/MinedBlock', methods = ['POST'])
def MinedBlock():
    NewBlock = request.get_json()
    if NewBlock['NewBlock']['Data'] != '':
        if MemPool.VerifyTransactions(NewBlock['New Block']['Data'].split('\n')):
            BlockChain.AddBlockToChain(NewBlock['New Block'])
            MemPool.RemoveTransactions(NewBlock['New Block']['Data'].split('\n'))
            return 'OK', 200
    else:
        return 'Error', 500
    
@app.route('/GetLastBlock', methods = ['GET'])
def GetLastBlock():
    return jsonify({'Last Block': BlockChain.GetLastBlock()}), 200


@app.route('/GetChain', methods=['GET'])
def GetBlockChain():
    return jsonify({'Chain': BlockChain.Chain}), 200

@app.route('/ChainIntegrity', methods = ['GET'])
def GetChainIntegrity():
    return jsonify({'Chain Integrity': BlockChain.ChainIntegrity()}), 200


app.run(host='0.0.0.0',port='9000')
