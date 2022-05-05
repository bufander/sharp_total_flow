pragma solidity 0.8.13;


interface ICairoVerifier {
    function isValid(bytes32) external view returns (bool);
}

struct Input {
    bytes32 input_hash;
    uint256 timestamp;
}

contract L1Action
{   
    // SHARP - Cairo verifier contract
    //TODO: update to mainnet address
    address constant GOERLY_SHARP_VERIFIER = 0xAB43bA48c9edF4C2C4bB01237348D1D7B28ef168;
    ICairoVerifier public cairoVerifier = ICairoVerifier(GOERLY_SHARP_VERIFIER);


    // Cairo version/hash
    uint256  public cairoProgramHash=0x0; 


    // user to givenInput mapping
    mapping(address => Input) public givenInputs;

    // hours to execute Cairo program and send results
    uint256 public stalePeriod = 3600*3;


    // Event confirming proper execution
    event ActionExecuted(uint256 cairoProgramHash, uint256[] cairoProgramOutput);

    // TODO: add Owner as only Admins should be able to change Cairo program hash
    function updateCairoProgramHash(uint256 _cairoProgramHash) external {
        cairoProgramHash = _cairoProgramHash;
    }

    function get_inputs() external returns (uint256[2] memory input){

        // get account
        address account = msg.sender;

        // compute inputs
        input = [uint256(1),uint256(40)];

        //update mapping and return input values
        bytes32 input_hash = keccak256(abi.encodePacked(input));
        givenInputs[account]=Input(input_hash, block.timestamp);
        return input;

    }

    function execute_action(uint256[] memory cairoProgramOutput) external {

        uint256[] memory user_input = new uint256[](2);
        user_input[0] = cairoProgramOutput[0];
        user_input[1] = cairoProgramOutput[1];


        address account = msg.sender;
        Input memory givenInput = givenInputs[account];

        // User should have asked for the inputs, inputs should be the same and not much time should have passed
        bytes32 user_input_hash = keccak256(abi.encodePacked(user_input));
        require(givenInput.input_hash==user_input_hash, "Wrong inputs");

        // Check that not much time has passed since we asked for input
        require(givenInput.timestamp + stalePeriod >=block.timestamp, "Too much time since inputs given");


        // Check with SHARP if execution was done
        bytes32 cairoProgramOutputHash = keccak256(abi.encodePacked(cairoProgramOutput));
        bytes32 fact = keccak256(abi.encodePacked(cairoProgramHash, cairoProgramOutputHash));
        require(cairoVerifier.isValid(fact), "Wrong proof");

        // Simulating whatever action
        emit ActionExecuted(cairoProgramHash, cairoProgramOutput);

    }
}