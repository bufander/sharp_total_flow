
##### INPUT VARIABLES #####
# Cairo file name
cairo_program_name=execute_computation.cairo
# Inputs file name
input_json_file=input.json
###########################

cairo_compiled=$(cairo_program_name)_compiled.json
pie_file=$(cairo_program_name).pie


default: compile

all: compile run sharp program_hash

compile:
	cairo-compile $(cairo_program_name) --output $(cairo_compiled)

run: compile
	cairo-run --program=$(cairo_compiled) --program_input=$(input_json_file) --layout=small --cairo_pie_output=$(pie_file) --print_output

sharp:
	cairo-sharp submit --source $(cairo_program_name) --program_input=$(input_json_file)

program_hash: compile
	cairo-hash-program --program $(cairo_compiled)

make status:
	cairo-sharp status $(job_key)

make verify:
	cairo-sharp is_verified $(fact) --node_url=https://goerli.infura.io/v3/f0129bd0022248a881f714027b33e124