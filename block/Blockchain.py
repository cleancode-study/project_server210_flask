import datetime
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    # 가장 처음 생성된 블록을 명시하기 위해 proof=1, previous_hash='0' agument 활용
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    # get_previous_block: chain 리스트에 있는 가장 마지막 블록을 리턴
    def get_previous_block(self):
        return self.chain[-1]

    # proof_of_work: 이전 proof 값을 받고 previous_proof와의 연산 해시 값이 특정 조건을 만족하는 new_proof를 찾아 리턴함
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation.startswith('0000'):
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    # hash: 딕셔너리 형태의 block을 받아서 json으로 dump하고 인코딩하여 해시값을 얻어 리턴함
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # 규칙에 맞게 블록체인이 생성되어 있는지 확인
    # 검증 방식은 genesis block의 다음 블록부터 마지막 블록까지 previous_hash 값이 이전 블록의 hash값과 동일한지
    # proof값이 previous_proof 값과 연산 후 해시값 계산시 특정조건('0000'으로 시작)을 만족하는지 체크
    def is_valid_chain(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()

            if not hash_operation.startswith('0000'):
                return False

            previous_block = block
            block_index += 1

        return True


blockchain = Blockchain()
previous_block = blockchain.get_previous_block()
previous_proof = previous_block['proof']
proof = blockchain.proof_of_work(previous_proof)
previous_hash = blockchain.hash(previous_block)
block = blockchain.create_block(proof, previous_hash)
print(blockchain.chain)