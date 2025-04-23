"""OCA Layer types"""

PAINT = 'paintlayer'
VECTOR = 'vectorlayer'
OCA = 'ocalayer'
GROUP = 'grouplayer'
CLONE = 'clonelayer'

# Useful groups to parse/sanitize data

INSTANCE_TYPES = (
    OCA,
    CLONE
)

ALL_TYPES = (
    PAINT,
    VECTOR,
    OCA,
    GROUP,
    CLONE
)
