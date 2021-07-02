import sys
import datetime
import hashlib
import json


class GenesisBlock:

    def __init__(self):

        self.Block = {

            'Block Number': 1,
            'Time Stamp': str(datetime.datetime.now()),
            'Nonce': 0,
            'Data': '',
            'Previous Hash': ''
        }

        Hash = self.GenerateHashOfBlock(self.Block)
        self.Block['Hash'] = Hash
   
    
    def GenerateHashOfBlock(self,Block):
        while True:
            Proof = hashlib.sha512(json.dumps(Block, sort_keys=True).encode()).hexdigest()
            if Proof[0:5]=='0'*5:
                return Proof
            else:
                Block['Nonce'] += 1
    
    def GetGenesisBlock(self):

        return [self.Block]



class BlockChain:


    def __init__(self,BlockChainData):
      
        self.Chain = BlockChainData


    def AddBlockToChain(self,Block):

        HashVerification = self.GenerateHashOfBlock({x: Block[x] for x in Block if x != 'Hash'})
        if Block['Hash'] == HashVerification:
            if self.ChainIntegrity():
                self.Chain.append(Block)
                return True
    
    def GetLastBlock(self):

        return self.Chain[-1]

    def GenerateHashOfBlock(self, Block):

        return hashlib.sha512(json.dumps(Block, sort_keys=True).encode()).hexdigest()
       

    def ChainIntegrity(self):

        PreviousBlock = self.Chain[0]
        BlockNumber = 1

        while BlockNumber < len(self.Chain):

            if self.Chain[BlockNumber]['Previous Hash'] != PreviousBlock['Hash']:
                
                return False

            PreviousBlock = self.Chain[BlockNumber]
            BlockNumber += 1
        
        return True

