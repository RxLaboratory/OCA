"""Open Cel Animation library for Krita"""

# OCA Python Library
# Copyright (c) 2020-2023 - Nicolas Dufresne, RxLaboratory and contributors
# This script is licensed under the GNU General Public License v3
# https://rxlaboratory.org
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

from .blending_modes import BLENDING_MODES as KRITA_BLENDING_MODES
from . import document as kritaDocument
from . import tags as kritaTags
from . import metadata as kritaMetadata
from ..oca_core import *
