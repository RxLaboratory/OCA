"""OCA Blending modes"""

NORMAL = 'normal'
DARKEN = 'darken'
BURN = 'burn'
COLOR = 'color'
DODGE = 'dodge'
DIVIDE = 'divide'
OVERLAY = 'overlay'
LUMINOSITY = 'luminosity'
SOFT_LIGHT = 'soft_light'
MULTIPLY = 'multiply'
SATURATION = 'saturation'
ERASE = 'erase'
LIGHTEN = 'lighten'
SCREEN = 'screen'
INVERSE_SUBTRACT = 'inverse_subtract'
SUBTRACT = 'subtract'
DARKER_COLOR = 'darker_color'
EASY_BURN = 'easy_burn'
FOG_DARKEN = 'fog_darken'
GAMMA_DARK = 'gamma_dark'
LINEAR_BURN = 'linear_burn'
SHADE = 'shade'
CONVERSE = 'converse'
AND = 'and'
IMPLICATION = 'implication'
NAND = 'nand'
NOR = 'nor'
NOT_CONVERSE = 'not_converse'
NOT_IMPLICATION = 'not_implication'
OR = 'or'
XNOR = 'xnor'
XOR = 'xor'
DISSOLVE = 'dissolve'
INCREASE_LUMINOSITY = 'increase_luminosity'
INCREASE_SATURATION = 'increase_saturation'
DECREASE_LUMINOSITY = 'decrease_luminosity'
DECREASE_SATURATION = 'decrease_saturation'
HUE = 'hue'
DIVISIVE_MODULO = 'divisive_modulo'
ALLANON = 'allanon'
ALPHADARKEN = 'alpha_darken'
STENCIL_ALPHA = 'stencil_alpha'
HARD_OVERLAY = 'hard_overlay'
INTERPOLATION = 'interpolation'
DOUBLE_INTERPOLATION = 'double_interpolation'
HARD_MIX = 'hard_mix'
HARD_MIX_PHOTOSHOP = 'hard_mix_photoshop'
PARALLEL = 'parallel'
PENUMBRA_A = 'penumbra_a'
PENUMBRA_B = 'penumbra_b'
PENUMBRA_C = 'penumbra_c'
PENUMBRA_D = 'penumbra_d'
GREATER = 'greater'
GEOMETRIC_MEAN = 'geometric_mean'
ADDITIVE_SUBTRACTIVE = 'additive_subtractive'
DIFFERENCE = 'difference'
EXCLUSION = 'exclusion'
NEGATION = 'negation'
ARC_TANGENT = 'arc_tangent'
EQUIVALENCE = 'equivalence'
FREEZE_REFLECT = 'FREEZE_REFLECT'
FREEZE = 'freeze'
GLOW_HEAT = 'glow_heat'
HEAT = 'heat'
HEAT_GLOW = 'heat_glow'
HEAT_GLOW_FREEZE_REFLECT = 'heat_glow_freeze_reflect'
GLOW = 'glow'
REFLECT_FREEZE = 'reflect_freeze'
REFLECT = 'reflect'
INCREASE_INTENSITY = 'increase_intensity'
INCREASE_SATURATION_HSI = 'increase_saturation_hsi'
COLOR_HSI = 'color_hsi'
DECREASE_INTENSITY = 'decrease_intensity'
DECREASE_SATURATION_HSI = 'decrease_saturation_hsi'
INTENSITY = 'intensity'
SATURATION_HSI = 'saturation_hsi'
HUE_HSI = 'hue_hsi'
INCREASE_LIGHTNESS = 'increase_lightness'
INCREASE_SATURATION_HSL = 'increase_saturation_hsl'
COLOR_HSL = 'color_hsl'
DECREASE_LIGHTNESS = 'decrease_lightness'
DECREASE_SATURATION_HSL = 'decrease_saturation_hsl'
LIGHTNESS = 'lightness'
SATURATION_HSL = 'saturation_hsl'
HUE_HSL = 'hue_hsl'
INCREASE_SATURATION_HSV = 'increase_saturation_hsv'
INCREASE_VALUE = 'increase_value'
COLOR_HSV = 'color_hsv'
DECREASE_SATURATION_HSV = 'decrease_saturation_hsv'
DECREASE_VALUE = 'decrease_value'
SATURATION_HSV = 'saturation_hsv'
VALUE = 'value'
LIGHTER_COLOR = 'lighter_color'
EASY_DODGE = 'easy_dodge'
FLAT_LIGHT = 'flat_light'
FOG_LIGHTEN = 'fog_lighten'
LINEAR_LIGHT = 'linear_light'
GAMMA_ILLUMINATION = 'gamma_illumination'
LUMINOSITY_SAI = 'luminosity_sai'
GAMMA_LIGHT = 'gamma_light'
SOFT_LIGHT = 'soft_light'
HARD_LIGHT = 'hard_light'
PIN_LIGHT = 'pin_light'
VIVID_LIGHT = 'vivid_light'
PNORM_A = 'pnorm_a'
PNORM_B = 'pnorm_b'
SOFT_LIGHT_IFS = 'soft_light_ifs'
SOFT_LIGHT_PEGTOP_DELPHI = 'soft_light_pegtop_delphi'
SUPER_LIGHT = 'super_light'
TINT = 'tint'
LINEAR_DODGE = 'linear_dodge'
ADD = 'add'

# Useful groups to parse/sanitize data

ALL_MODES = (
    NORMAL,
    DARKEN,
    BURN,
    COLOR,
    DODGE,
    DIVIDE,
    OVERLAY,
    LUMINOSITY,
    SOFT_LIGHT,
    MULTIPLY,
    SATURATION,
    ERASE,
    LIGHTEN,
    SCREEN,
    INVERSE_SUBTRACT,
    SUBTRACT,
    DARKER_COLOR,
    EASY_BURN,
    FOG_DARKEN,
    GAMMA_DARK,
    LINEAR_BURN,
    SHADE,
    CONVERSE,
    AND,
    IMPLICATION,
    NAND,
    NOR,
    NOT_CONVERSE,
    NOT_IMPLICATION,
    OR,
    XNOR,
    XOR,
    DISSOLVE,
    INCREASE_LUMINOSITY,
    INCREASE_SATURATION,
    DECREASE_LUMINOSITY,
    DECREASE_SATURATION,
    HUE,
    DIVISIVE_MODULO,
    ALLANON,
    ALPHADARKEN,
    STENCIL_ALPHA,
    HARD_OVERLAY,
    INTERPOLATION,
    DOUBLE_INTERPOLATION,
    HARD_MIX,
    HARD_MIX_PHOTOSHOP,
    PARALLEL,
    PENUMBRA_A,
    PENUMBRA_B,
    PENUMBRA_C,
    PENUMBRA_D,
    GREATER,
    GEOMETRIC_MEAN,
    ADDITIVE_SUBTRACTIVE,
    DIFFERENCE,
    EXCLUSION,
    NEGATION,
    ARC_TANGENT,
    EQUIVALENCE,
    FREEZE_REFLECT,
    FREEZE,
    GLOW_HEAT,
    HEAT,
    HEAT_GLOW,
    HEAT_GLOW_FREEZE_REFLECT,
    GLOW,
    REFLECT_FREEZE,
    REFLECT,
    INCREASE_INTENSITY,
    INCREASE_SATURATION_HSI,
    COLOR_HSI,
    DECREASE_INTENSITY,
    DECREASE_SATURATION_HSI,
    INTENSITY,
    SATURATION_HSI,
    HUE_HSI,
    INCREASE_LIGHTNESS,
    INCREASE_SATURATION_HSL,
    COLOR_HSL,
    DECREASE_LIGHTNESS,
    DECREASE_SATURATION_HSL,
    LIGHTNESS,
    SATURATION_HSL,
    HUE_HSL,
    INCREASE_SATURATION_HSV,
    INCREASE_VALUE,
    COLOR_HSV,
    DECREASE_SATURATION_HSV,
    DECREASE_VALUE,
    SATURATION_HSV,
    VALUE,
    LIGHTER_COLOR,
    EASY_DODGE,
    FLAT_LIGHT,
    FOG_LIGHTEN,
    LINEAR_LIGHT,
    GAMMA_ILLUMINATION,
    LUMINOSITY_SAI,
    GAMMA_LIGHT,
    SOFT_LIGHT,
    HARD_LIGHT,
    PIN_LIGHT,
    VIVID_LIGHT,
    PNORM_A,
    PNORM_B,
    SOFT_LIGHT_IFS,
    SOFT_LIGHT_PEGTOP_DELPHI,
    SUPER_LIGHT,
    TINT,
    LINEAR_DODGE,
    ADD,
)