import generatekey
import VNRcoin
kg = generatekey.KeyGenerator()
kg.seed_input('Stay anonymous pretty much always')
key = kg.generate_key()
address = VNRcoin.VNRcoin.generate_address(key)
print(address)