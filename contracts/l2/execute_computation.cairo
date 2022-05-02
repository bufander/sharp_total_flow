%builtins output

from starkware.cairo.common.serialize import serialize_word

func main{output_ptr: felt*}() -> ():
    alloc_locals

    local input_a: felt
    local input_b: felt


    # Read input vars
    %{  
        # We create simple result and input variables
        ids.input_a = program_input["input_a"]
        ids.input_b = program_input["input_b"]

        assert ids.input_a>0
        assert ids.input_b>0
    %}

    # Compute logic and test results and variable
    local result = input_a + input_b

    # Output inputs and program computation

    serialize_word(input_a)
    serialize_word(input_b)
    serialize_word(result)

    ret

end
