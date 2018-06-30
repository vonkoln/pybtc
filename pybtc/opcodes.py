OPCODE = dict()

# push opcodes

OPCODE["OP_FALSE"] = 0x00
OPCODE["OP_0"] = 0x00
OPCODE["OP_PUSHDATA1"] = 0x4c
OPCODE["OP_PUSHDATA2"] = 0x4d
OPCODE["OP_PUSHDATA4"] = 0x4e
OPCODE["OP_1NEGATE"] = 0x4f
OPCODE["OP_RESERVED"] = 0x50
OPCODE["OP_TRUE"] = 0x51
OPCODE["OP_1"] = 0x51
OPCODE["OP_2"] = 0x52
OPCODE["OP_3"] = 0x53
OPCODE["OP_4"] = 0x54
OPCODE["OP_5"] = 0x55
OPCODE["OP_6"] = 0x56
OPCODE["OP_7"] = 0x57
OPCODE["OP_8"] = 0x58
OPCODE["OP_9"] = 0x59
OPCODE["OP_10"] = 0x5a
OPCODE["OP_11"] = 0x5b
OPCODE["OP_12"] = 0x5c
OPCODE["OP_13"] = 0x5d
OPCODE["OP_14"] = 0x5e
OPCODE["OP_15"] = 0x5f
OPCODE["OP_16"] = 0x60

# control

OPCODE["OP_NOP"] = 0x61
OPCODE["OP_VER"] = 0x62
OPCODE["OP_IF"] = 0x63
OPCODE["OP_NOTIF"] = 0x64
OPCODE["OP_VERIF"] = 0x65
OPCODE["OP_ELSE"] = 0x67
OPCODE["OP_ENDIF"] = 0x68
OPCODE["OP_VERIFY"] = 0x69
OPCODE["OP_RETURN"] = 0x6a

# stack

OPCODE["OP_TOALTSTACK"] = 0x6b
OPCODE["OP_FROMALTSTACK"] = 0x6c
OPCODE["OP_2DROP"] = 0x6d
OPCODE["OP_2DUP"] = 0x6e
OPCODE["OP_3DUP"] = 0x6f
OPCODE["OP_2OVER"] = 0x70
OPCODE["OP_2ROT"] = 0x71
OPCODE["OP_2SWAP"] = 0x72
OPCODE["OP_IFDUP"] = 0x73
OPCODE["OP_DEPTH"] = 0x74
OPCODE["OP_DROP"] = 0x75
OPCODE["OP_DUP"] = 0x76
OPCODE["OP_NIP"] = 0x77
OPCODE["OP_OVER"] = 0x78
OPCODE["OP_PICK"] = 0x79
OPCODE["OP_ROLL"] = 0x7a
OPCODE["OP_ROT"] = 0x7b
OPCODE["OP_SWAP"] = 0x7c
OPCODE["OP_TUCK"] = 0x7d

# splice

OPCODE["OP_CAT"] = 0x7e
OPCODE["OP_SUBSTR"] = 0x7f
OPCODE["OP_LEFT"] = 0x80
OPCODE["OP_RIGHT"] = 0x81
OPCODE["OP_SIZE"] = 0x82

# bit operations

OPCODE["OP_INVERT"] = 0x83
OPCODE["OP_AND"] = 0x84
OPCODE["OP_OR"] = 0x85
OPCODE["OP_XOR"] = 0x86
OPCODE["OP_EQUAL"] = 0x87
OPCODE["OP_EQUALVERIFY"] = 0x88
OPCODE["OP_RESERVED1"] = 0x89
OPCODE["OP_RESERVED2"] = 0x8a

# math

OPCODE["OP_1ADD"] = 0x8b
OPCODE["OP_1SUB"] = 0x8c
OPCODE["OP_2MUL"] = 0x8d
OPCODE["OP_2DIV"] = 0x8e
OPCODE["OP_NEGATE"] = 0x8f
OPCODE["OP_ABS"] = 0x90
OPCODE["OP_NOT"] = 0x91
OPCODE["OP_0NOTEQUAL"] = 0x92

OPCODE["OP_ADD"] = 0x93
OPCODE["OP_SUB"] = 0x94
OPCODE["OP_MUL"] = 0x95
OPCODE["OP_DIV"] = 0x96
OPCODE["OP_MOD"] = 0x97
OPCODE["OP_LSHIFT"] = 0x98
OPCODE["OP_RSHIFT"] = 0x99

OPCODE["OP_BOOLAND"] = 0x9a
OPCODE["OP_BOOLOR"] = 0x9b
OPCODE["OP_NUMEQUAL"] = 0x9c
OPCODE["OP_NUMEQUALVERIFY"] = 0x9d
OPCODE["OP_NUMNOTEQUAL"] = 0x9e
OPCODE["OP_LESSTHAN"] = 0x9f
OPCODE["OP_GREATERTHAN"] = 0xa0
OPCODE["OP_LESSTHANOREQUAL"] = 0xa1
OPCODE["OP_GREATERTHANOREQUAL"] = 0xa2
OPCODE["OP_MIN"] = 0xa3
OPCODE["OP_MAX"] = 0xa4

OPCODE["OP_WITHIN"] = 0xa5

# crypto

OPCODE["OP_RIPEMD160"] = 0xa6
OPCODE["OP_SHA1"] = 0xa7
OPCODE["OP_SHA256"] = 0xa8
OPCODE["OP_HASH160"] = 0xa9
OPCODE["OP_HASH256"] = 0xaa
OPCODE["OP_CODESEPARATOR"] = 0xab
OPCODE["OP_CHECKSIG"] = 0xac
OPCODE["OP_CHECKSIGVERIFY"] = 0xad
OPCODE["OP_CHECKMULTISIG"] = 0xae
OPCODE["OP_CHECKMULTISIGVERIFY"] = 0xaf

# expansion

OPCODE["OP_NOP1"] = 0xb0
OPCODE["OP_CHECKLOCKTIMEVERIFY"] = 0xb1
OPCODE["OP_CHECKSEQUENCEVERIFY"] = 0xb2
OPCODE["OP_NOP4"] = 0xb3
OPCODE["OP_NOP5"] = 0xb4
OPCODE["OP_NOP6"] = 0xb5
OPCODE["OP_NOP7"] = 0xb6
OPCODE["OP_NOP8"] = 0xb7
OPCODE["OP_NOP9"] = 0xb8
OPCODE["OP_NOP10"] = 0xb9

# template matching params

OPCODE["OP_SMALLINTEGER"] = 0xfa
OPCODE["OP_PUBKEYS"] = 0xfb
OPCODE["OP_PUBKEYHASH"] = 0xfd
OPCODE["OP_PUBKEY"] = 0xfe
OPCODE["OP_INVALIDOPCODE"] = 0xff


RAW_OPCODE = dict((OPCODE[i], i) for i in OPCODE)
BYTE_OPCODE = dict((i, bytes([OPCODE[i]])) for i in OPCODE)
HEX_OPCODE = dict((i, bytes([OPCODE[i]]).hex()) for i in OPCODE)

OP_FALSE = BYTE_OPCODE["OP_FALSE"]
OP_0 = BYTE_OPCODE["OP_0"]
OP_PUSHDATA1 = BYTE_OPCODE["OP_PUSHDATA1"]
OP_PUSHDATA2 = BYTE_OPCODE["OP_PUSHDATA2"]
OP_PUSHDATA4 = BYTE_OPCODE["OP_PUSHDATA4"]
OP_1NEGATE = BYTE_OPCODE["OP_1NEGATE"]
OP_RESERVED = BYTE_OPCODE["OP_RESERVED"]
OP_1 = BYTE_OPCODE["OP_1"]
OP_TRUE = BYTE_OPCODE["OP_TRUE"]
OP_2 = BYTE_OPCODE["OP_2"]
OP_3 = BYTE_OPCODE["OP_3"]
OP_4 = BYTE_OPCODE["OP_4"]
OP_5 = BYTE_OPCODE["OP_5"]
OP_6 = BYTE_OPCODE["OP_6"]
OP_7 = BYTE_OPCODE["OP_7"]
OP_8 = BYTE_OPCODE["OP_8"]
OP_9 = BYTE_OPCODE["OP_9"]
OP_10 = BYTE_OPCODE["OP_10"]
OP_11 = BYTE_OPCODE["OP_11"]
OP_12 = BYTE_OPCODE["OP_12"]
OP_13 = BYTE_OPCODE["OP_13"]
OP_14 = BYTE_OPCODE["OP_14"]
OP_15 = BYTE_OPCODE["OP_15"]
OP_16 = BYTE_OPCODE["OP_16"]

# control

OP_NOP = BYTE_OPCODE["OP_NOP"]
OP_VER = BYTE_OPCODE["OP_VER"]
OP_IF = BYTE_OPCODE["OP_IF"]
OP_NOTIF = BYTE_OPCODE["OP_NOTIF"]
OP_VERIF = BYTE_OPCODE["OP_VERIF"]
OP_ELSE = BYTE_OPCODE["OP_ELSE"]
OP_ENDIF = BYTE_OPCODE["OP_ENDIF"]
OP_VERIFY = BYTE_OPCODE["OP_VERIFY"]
OP_RETURN = BYTE_OPCODE["OP_RETURN"]

# stack

OP_TOALTSTACK = BYTE_OPCODE["OP_TOALTSTACK"]
OP_FROMALTSTACK = BYTE_OPCODE["OP_FROMALTSTACK"]
OP_2DROP = BYTE_OPCODE["OP_2DROP"]
OP_2DUP = BYTE_OPCODE["OP_2DUP"]
OP_3DUP = BYTE_OPCODE["OP_3DUP"]
OP_2OVER = BYTE_OPCODE["OP_2OVER"]
OP_2ROT = BYTE_OPCODE["OP_2ROT"]
OP_2SWAP = BYTE_OPCODE["OP_2SWAP"]
OP_IFDUP = BYTE_OPCODE["OP_IFDUP"]
OP_DEPTH = BYTE_OPCODE["OP_DEPTH"]
OP_DROP = BYTE_OPCODE["OP_DROP"]
OP_DUP = BYTE_OPCODE["OP_DUP"]
OP_NIP = BYTE_OPCODE["OP_NIP"]
OP_OVER = BYTE_OPCODE["OP_OVER"]
OP_PICK = BYTE_OPCODE["OP_PICK"]
OP_ROLL = BYTE_OPCODE["OP_ROLL"]
OP_ROT = BYTE_OPCODE["OP_ROT"]
OP_SWAP = BYTE_OPCODE["OP_SWAP"]
OP_TUCK = BYTE_OPCODE["OP_TUCK"]

# splice

OP_CAT = BYTE_OPCODE["OP_CAT"]
OP_SUBSTR = BYTE_OPCODE["OP_SUBSTR"]
OP_LEFT = BYTE_OPCODE["OP_LEFT"]
OP_RIGHT = BYTE_OPCODE["OP_RIGHT"]
OP_SIZE = BYTE_OPCODE["OP_SIZE"]

# bit operations

OP_INVERT = BYTE_OPCODE["OP_INVERT"]
OP_AND = BYTE_OPCODE["OP_AND"]
OP_OR = BYTE_OPCODE["OP_OR"]
OP_XOR = BYTE_OPCODE["OP_XOR"]
OP_EQUAL = BYTE_OPCODE["OP_EQUAL"]
OP_EQUALVERIFY = BYTE_OPCODE["OP_EQUALVERIFY"]
OP_RESERVED1 = BYTE_OPCODE["OP_RESERVED1"]
OP_RESERVED2 = BYTE_OPCODE["OP_RESERVED2"]

# math

OP_1ADD = BYTE_OPCODE["OP_1ADD"]
OP_1SUB = BYTE_OPCODE["OP_1SUB"]
OP_2MUL = BYTE_OPCODE["OP_2MUL"]
OP_2DIV = BYTE_OPCODE["OP_2DIV"]
OP_NEGATE = BYTE_OPCODE["OP_NEGATE"]
OP_ABS = BYTE_OPCODE["OP_ABS"]
OP_NOT = BYTE_OPCODE["OP_NOT"]
OP_0NOTEQUAL = BYTE_OPCODE["OP_0NOTEQUAL"]

OP_ADD = BYTE_OPCODE["OP_ADD"]
OP_SUB = BYTE_OPCODE["OP_SUB"]
OP_MUL = BYTE_OPCODE["OP_MUL"]
OP_DIV = BYTE_OPCODE["OP_DIV"]
OP_MOD = BYTE_OPCODE["OP_MOD"]
OP_LSHIFT = BYTE_OPCODE["OP_LSHIFT"]
OP_RSHIFT = BYTE_OPCODE["OP_RSHIFT"]

OP_BOOLAND = BYTE_OPCODE["OP_BOOLAND"]
OP_BOOLOR = BYTE_OPCODE["OP_BOOLOR"]
OP_NUMEQUAL = BYTE_OPCODE["OP_NUMEQUAL"]
OP_NUMEQUALVERIFY = BYTE_OPCODE["OP_NUMEQUALVERIFY"]
OP_NUMNOTEQUAL = BYTE_OPCODE["OP_NUMNOTEQUAL"]
OP_LESSTHAN = BYTE_OPCODE["OP_LESSTHAN"]
OP_GREATERTHAN = BYTE_OPCODE["OP_GREATERTHAN"]
OP_LESSTHANOREQUAL = BYTE_OPCODE["OP_LESSTHANOREQUAL"]
OP_GREATERTHANOREQUAL = BYTE_OPCODE["OP_GREATERTHANOREQUAL"]
OP_MIN = BYTE_OPCODE["OP_MIN"]
OP_MAX = BYTE_OPCODE["OP_MAX"]
OP_WITHIN = BYTE_OPCODE["OP_WITHIN"]

# crypto

OP_RIPEMD160 = BYTE_OPCODE["OP_RIPEMD160"]
OP_SHA1 = BYTE_OPCODE["OP_SHA1"]
OP_SHA256 = BYTE_OPCODE["OP_SHA256"]
OP_HASH160 = BYTE_OPCODE["OP_HASH160"]
OP_HASH256 = BYTE_OPCODE["OP_HASH256"]
OP_CODESEPARATOR = BYTE_OPCODE["OP_CODESEPARATOR"]
OP_CHECKSIG = BYTE_OPCODE["OP_CHECKSIG"]
OP_CHECKSIGVERIFY = BYTE_OPCODE["OP_CHECKSIGVERIFY"]
OP_CHECKMULTISIG = BYTE_OPCODE["OP_CHECKMULTISIG"]
OP_CHECKMULTISIGVERIFY = BYTE_OPCODE["OP_CHECKMULTISIGVERIFY"]

# expansion

OP_NOP1 = BYTE_OPCODE["OP_NOP1"]
OP_CHECKLOCKTIMEVERIFY = BYTE_OPCODE["OP_CHECKLOCKTIMEVERIFY"]
OP_CHECKSEQUENCEVERIFY = BYTE_OPCODE["OP_CHECKSEQUENCEVERIFY"]
OP_NOP4 = BYTE_OPCODE["OP_NOP4"]
OP_NOP5 = BYTE_OPCODE["OP_NOP5"]
OP_NOP6 = BYTE_OPCODE["OP_NOP6"]
OP_NOP7 = BYTE_OPCODE["OP_NOP7"]
OP_NOP8 = BYTE_OPCODE["OP_NOP8"]
OP_NOP9 = BYTE_OPCODE["OP_NOP9"]
OP_NOP10 = BYTE_OPCODE["OP_NOP10"]

# template matching params

OP_SMALLINTEGER = BYTE_OPCODE["OP_SMALLINTEGER"]
OP_PUBKEYS = BYTE_OPCODE["OP_PUBKEYS"]
OP_PUBKEYHASH = BYTE_OPCODE["OP_PUBKEYHASH"]
OP_PUBKEY = BYTE_OPCODE["OP_PUBKEY"]
OP_INVALIDOPCODE = BYTE_OPCODE["OP_INVALIDOPCODE"]