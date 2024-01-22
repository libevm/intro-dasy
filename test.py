import json
import boa

from dasy import compiler
from dasy.parser.output import get_external_interface

source_code = 'random.dasy'

with open(f'./{source_code}') as f:
    src = f.read()
    compiler_data = compiler.compile(src, name=source_code.split('.')[0])

contract_addr = boa.env.deploy_code(bytecode=compiler_data.bytecode)[0]
contract_factory = boa.loads_abi(json.dumps(compiler_data.abi))
contract = contract_factory.at(contract_addr)

# Gets the random number
print(contract.num())