from scripts.deploy import deploy_contract
from brownie import L1Action
from brownie import network, exceptions, chain
import pytest
import time



def test_program_hash():

    account, contract = deploy_contract()

    # Check that program hash is empty
    assert contract.cairoProgramHash()==hex(0)


    # Check that we can change program hash value
    tx = contract.updateCairoProgramHash(hex(0x1234),{"from": account})
    tx.wait(1)
    assert contract.cairoProgramHash() == hex(0x1234)

def test_is_valid():

    if network.show_active() in ["goerli", "goerli-fork"]:

        account, contract = deploy_contract()

        # Using and old deployed cairo program
        program_hash=hex(0xc31e4da4b646e6661e98d893161cb4341f37403e48840c90ef4b76952f50d4)
        tx = contract.updateCairoProgramHash(program_hash,{"from": account})
        tx.wait(1)

        # Ask for inputs
        tx = contract.get_inputs({"from": account})
        tx.wait(1)
        inputs = tx.return_value
        assert inputs==[1,40]

        # Execute action by verifying
        program_output = [1,40,41]
        tx = contract.execute_action(program_output)
        tx.wait(1)

        assert tx.events[0]["cairoProgramHash"] == program_hash
        assert tx.events[0]["cairoProgramOutput"] == program_output

        # Ensure a wrong input does not work
        program_output = [1,40,40]
        with pytest.raises(exceptions.VirtualMachineError):
            contract.execute_action(program_output)
    
        

def test_get_inputs():
    account, contract = deploy_contract()

    # Using and old deployed cairo program
    program_hash=hex(0xc31e4da4b646e6661e98d893161cb4341f37403e48840c90ef4b76952f50d4)
    tx = contract.updateCairoProgramHash(program_hash,{"from": account})
    tx.wait(1)

    # Ask for inputs
    tx = contract.get_inputs({"from": account})
    tx.wait(1)

    inputs = tx.return_value

    assert inputs==[1,40]
