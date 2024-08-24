from datetime import datetime
import hashlib

MAX_NONCE = 2**32  # 4 billion


class Block:
    """A class representing the block for the blockchain"""

    def __init__(self, index, previous_hash, ts, data, difficulty_bits, nonce, current_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = ts
        self.data = data
        self.difficulty_bits = difficulty_bits
        self.nonce = nonce
        self.hash = current_hash


class Blockchain:
    """A class representing list of blocks"""

    def __init__(self, difficulty_bits=0):
        self._chain = [self._get_genesis_block()]
        self._difficulty_bits = difficulty_bits

    @property
    def chain(self):
        """created a dict containing list of block objects to view"""

        return self._chain

    def reset(self):
        """resets the blockchain blocks except genesis block"""

        self._chain = [self._chain[0]]

    def _get_genesis_block(self):
        """creates first block of the chain"""

        return Block(
            0,
            "0",
            1465154705,
            "my genesis block!!",
            0,
            0,
            "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7",
        )

    def add_block(self, data):
        """appends a new block to the blockchain"""

        self._chain.append(self._create_block(data))

    def _create_block(self, block_data):
        """creates a new block with the given block data"""

        previous_block = self._get_latest_block()
        next_index = previous_block.index + 1
        next_timestamp = int(datetime.now().timestamp())
        next_hash, next_nonce = self._calculate_hash(next_index, previous_block.hash, next_timestamp, block_data)
        return Block(
            next_index, previous_block.hash, next_timestamp, block_data, self._difficulty_bits, next_nonce, next_hash
        )

    def _get_latest_block(self):
        """gets the last block from the blockchain"""

        try:
            return self._chain[-1]
        except IndexError:
            return None

    def _calculate_hash(self, index, previous_hash, timestamp, data):
        """calculates SHA256 hash value"""

        header = str(index) + previous_hash + str(timestamp) + data

        if self._difficulty_bits:
            header += str(self._difficulty_bits)
            hash_value, nonce = self._proof_of_work(header)
        else:
            hash_value = hashlib.sha256(header.encode()).hexdigest()
            nonce = 0

        return hash_value, nonce

    def _proof_of_work(self, header):
        """Calculates nonce for the block based on the difficulty bits set"""

        target = 2 ** (256 - self._difficulty_bits)

        for nonce in range(MAX_NONCE):
            hash_result = hashlib.sha256((str(header) + str(nonce)).encode()).hexdigest()
            if int(hash_result, 16) < target:
                return (hash_result, nonce)

        return nonce


if __name__ == "__main__":
    blockchain = Blockchain(difficulty_bits=21)

    for i in range(5):
        blockchain.add_block(f"block content {i}")

    print("\nBlockchain:\n")
    for block in blockchain.chain:
        print(f"Block {block.index}:")
        print(f"    hash:  {block.hash}")
        print(f"    data:  {block.data}")
        print(f"    nonce: {block.nonce}")
