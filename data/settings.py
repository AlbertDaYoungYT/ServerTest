
LOG_ROTATION_SIZE = "10 MB"

SECRET = "127962c4-fb88-40c7-a065-fa80eb46393a"
STRIPE = ""


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