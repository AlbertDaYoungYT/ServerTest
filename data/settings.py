import logging



LOG_ROTATION_SIZE  = "10 MB"
LOG_RETENTION_TIME = "1 week"
FLASK_LOG_LEVEL = logging.INFO
DISABLE_FLASK_LOG = True

SECRET = open(".flask", "r").read()
STRIPE = open(".stripe", "r").read()


EVENT_TYPES = {
    "MultipleReddem": "MULTIREDEEM",
    "OneTimeRedeem": "ONEREDEEM",
    "Achievement": "ACHIEVEMENT"
}

RARITY_RANKS = {
    "E":    [100,       50],
    "D":    [50,        25],
    "C":    [25,        12.5],
    "B":    [12.5,      6.25],
    "A":    [6.25,      3.125],
    "S":    [3.125,     1.5625],
    "X":    [1.5625,    0.78125],
    "XX":   [0.78125,   0.390625],
    "XXX":  [0.390625,  0]
}