"""OCA Layer types"""

PAINT = 'paintlayer'
VECTOR = 'vectorlayer'
OCA = 'ocalayer'
GROUP = 'grouplayer'
CLONE = 'clonelayer'

# Useful groups to parse/sanitize data

# These layers are just an instance of another layer
INSTANCE_TYPES = (
    OCA,
    CLONE
)

# These layuers may contain other layers
GROUP_TYPES = (
    GROUP,
    OCA
)

# All layer types
ALL_TYPES = (
    PAINT,
    VECTOR,
    OCA,
    GROUP,
    CLONE
)
