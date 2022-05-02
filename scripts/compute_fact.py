from web3 import Web3

# Add Cairo program hash: cairo-hash-program --program <cairo_compiled>.json
program_hash = 0xc31e4da4b646e6661e98d893161cb4341f37403e48840c90ef4b76952f50d4

# Add program output
program_output = [0x1, 0x28, 0x29]

# Fact returned by submitting job to SHARP
fact = 0xfb7915ff90710a578708774188ed578e31c023e7a23853f17d6443b49ba4ad7e


calculated_fact = Web3.solidityKeccak(
    ["uint256", "bytes32"],
    [program_hash, Web3.solidityKeccak(["uint256[]"], [program_output])],
).hex()

try:
    assert hex(fact)==calculated_fact
    print("Fact is right!")
except:
    print("Wrong values")
