Simulates whole flow of SHARP program


L2. 

Use make all to compile run deploy and get status value of Cairo program

        $ make all
        Makefile:33: warning: overriding recipe for target 'make'
        Makefile:30: warning: ignoring old recipe for target 'make'
        cairo-compile execute_computation.cairo --output execute_computation.cairo_compiled.json
        cairo-run --program=execute_computation.cairo_compiled.json --program_input=input.json --layout=small --cairo_pie_output=execute_computation.cairo.pie --print_output
        Program output:
        1
        40
        41

        cairo-sharp submit --source execute_computation.cairo --program_input=input.json
        Compiling...
        Running...
        Submitting to SHARP...
        Job sent.
        Job key: 9a8e7d16-3e9e-4616-8908-2509e875123d
        Fact: 0xfb7915ff90710a578708774188ed578e31c023e7a23853f17d6443b49ba4ad7e
        cairo-hash-program --program execute_computation.cairo_compiled.json
        0xc31e4da4b646e6661e98d893161cb4341f37403e48840c90ef4b76952f50d4


L1. 

Run tests with a fork of goerli

    brownie test --network goerli-fork