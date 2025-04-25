"""Open Cel Animation library"""

# OCA Python Library
# Copyright (c) 2020-2025 - Nicolas Dufresne, RxLaboratorio and contributors
# This script is licensed under the GNU General Public License v3
# https://rxlaboratorio.org
#
# This file is part of OCA.
#   OCA is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    OCA is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with OCA. If not, see <http://www.gnu.org/licenses/>.

# CLASSES
from .document import OCADocument
from .frame import OCAFrame
from .layer import OCALayer
from .source import OCASource
from .object import OCAObject

# UTILS
from . import utils

# ENUMS
from . import blending_modes as BLENDING_MODES
from . import color_depths as COLOR_DEPTHS
from . import labels as LABELS
from . import layer_types as LAYER_TYPES

# CONSTANTS
from .config import VERSION

# DEPRECATED
from . import file
