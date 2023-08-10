![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# Blending Modes

Blending modes are named after the ones used in [*Krita*](http://krita.org).

Depending on the application, a blending mode with the same name may have different results. When a blending mode is set in *OCA*, its result should be the same as the blending mode with the same name in *Krita*. This choice was made because *Krita* is a free and open source software, so anyone can have a look at how these blending modes are implemented, to be sure about what they do, and because *Krita* uses one of the biggest list of blending modes.

The implementation of these blending modes is described in details in the [Krita Reference Manual](https://docs.krita.org/en/reference_manual/blending_modes.html){target="_blank"}.

To know the correspondance of the blending mode names and implementations between *Krita/OCA* and the most common other applications, we're building correspondance tables (see below).

## Krita Blending Modes

This table lists the correspondance between OCA Blending Modes and Krita Blending Modes.

As OCA Blending modes are based on those of Krita, all of these are exact matches and should be considered the reference implementation of them. See [Krita.org](http://krita.org){target="_blank"} and the [Krita Reference Manual](https://docs.krita.org/en/reference_manual/blending_modes.html){target="_blank"} for more information about them.

If a blending mode is not listed in this table, that means it is not supported by OCA (yet).

| Krita | OCA |
|---|---|
| normal | normal |
| darken | darken |
| burn | burn |
| color | color |
| dodge | dodge |
| divide | divide |
| overlay | overlay |
| luminize | luminosity |
| soft_light_svg | soft_light |
| multiply | multiply |
| saturation | saturation |
| erase | erase |
| lighten | lighten |
| screen | screen |
| inverse_subtract | inverse_subtract |
| subtract | subtract |
| darker color | darker_color |
| easy burn | easy_burn |
| fog_darken_ifs_illusions | fog_darken |
| gamma_dark | gamma_dark |
| linear_burn | linear_burn |
| shade_ifs_illusions | shade |
| converse | converse |
| and | and |
| implication | implication |
| nand | nand |
| nor | nor |
| not_converse | not_converse |
| not_implication | not_implication |
| or | or |
| xnor | xnor |
| xor | xor |
| dissolve | dissolve |
| inc_luminosity | increase_luminosity |
| inc_saturation | increase_saturation |
| dec_luminosity | decrease_luminosity |
| dec_saturation | decrease_saturation |
| hue | hue |
| divisive_modulo | divisive_modulo |
| allanon | allanon |
| alphadarken | alpha_darken |
| destination-in | stencil_alpha |
| hard overlay | hard_overlay |
| interpolation | interpolation |
| interpolation 2x | double_interpolation |
| hard mix | hard_mix |
| hard_mix_photoshop | hard_mix_photoshop |
| parallel | parallel |
| penumbra a | penumbra_a |
| penumbra a | penumbra_b |
| penumbra a | penumbra_c |
| penumbra a | penumbra_d |
| greater | greater |
| geometric_mean | geometric_mean |
| additive_subtractive | additive_subtractive |
| diff | difference |
| exclusion | exclusion |
| negation | negation |
| arc_tangent | arc_tangent |
| equivalence | equivalence |
| freeze_reflect | freeze_reflect |
| freeze | freeze |
| glow_heat | glow_heat |
| heat | heat |
| heat_glow | heat_glow |
| heat_glow_freeze_reflect_hybrid | heat_glow_freeze_reflect |
| glow | glow |
| reflect_freeze | reflect_freeze |
| reflect | reflect |
| inc_intensity | increase_intensity |
| inc_saturation_hsi | increase_saturation_hsi |
| color_hsi | color_hsi |
| dec_intensity | decrease_intensity |
| dec_saturation_hsi | decrease_saturation_hsi |
| intensity | intensity |
| saturation_hsi | saturation_hsi |
| hue_hsi | hue_hsi |
| inc_lightness | increase_lightness |
| inc_saturation_hsl | increase_saturation_hsl |
| color_hsl | color_hsl |
| dec_lightness | decrease_lightness |
| dec_saturation_hsl | decrease_saturation_hsl |
| lightness | lightness |
| saturation_hsl | saturation_hsl |
| hue_hsl | hue_hsl |
| inc_saturation_hsv | increase_saturation_hsv |
| inc_value | increase_value |
| color_hsv | color_hsv |
| dec_saturation_hsv | decrease_saturation_hsv |
| dec_value | decrease_value |
| saturation_hsv | saturation_hsv |
| value | value |
| lighter color | lighter_color |
| easy dodge | easy_dodge |
| flat_light | flat_light |
| fog_lighten_ifs_illusions | fog_lighten |
| linear light | linear_light |
| gamma_illumination | gamma_illumination |
| luminosity_sai | luminosity_sai |
| gamma_light | gamma_light |
| soft_light | soft_light |
| hard_light | hard_light |
| pin_light | pin_light |
| vivid_light | vivid_light |
| pnorm_a | pnorm_a |
| pnorm_b | pnorm_b |
| soft_light_ifs_illusions | soft_light_ifs |
| soft_light_pegtop_delphi | soft_light_pegtop_delphi |
| super_light | super_light |
| tint_ifs_illusions | tint |
| linear_dodge | linear_dodge |
| add | add |

## Adobe After Effects Blending Modes

This table lists the correspondance between OCA Blending Modes and Adobe After Effects Blending Modes.

If a blending mode is not listed in this table, that means it is not supported by After Effects and there is no approximation close enough.

Legend:  
✔️: Exact correspondance  
❗: Approximation

| OCA | After Effects | Note |
|---|---|---|
| normal | NORMAL | ✔️ |
| darken | DARKEN | ✔️ |
| burn | COLOR_BURN | ✔️ |
| color | COLOR | ✔️ |
| dodge | CLASSIC_COLOR_DODGE | ✔️ |
| divide | DIVIDE | ✔️ |
| overlay | OVERLAY | ✔️ |
| luminosity | LUMINOSITY | ✔️ |
| soft_light_svg | SOFT_LIGHT | ✔️ |
| multiply | MULTIPLY | ✔️ |
| saturation | SATURATION | ✔️ |
| erase | SILHOUETE_ALPHA | ✔️ |
| lighten | LIGHTEN | ✔️ |
| screen | SCREEN | ✔️ |
| inverse_subtract | LINEAR_BURN | ✔️ |
| subtract | SUBTRACT | ✔️ |
| darker_color | DARKER_COLOR | ✔️ |
| easy_burn | MULTIPLY | ❗ |
| fog_darken | DARKEN | ✔️ |
| gamma_dark | VIVID_LIGHT | ❗ |
| linear_burn | LINEAR_BURN | ✔️ |
| shade | LINEAR_BURN | ❗ |
| and | LINEAR_BURN | ❗ |
| or | ADD | ❗ |
| dissolve | DISSOLVE | ✔️ |
| increase_luminosity | ADD | ❗ |
| increase_saturation | OVERLAY | ❗ |
| hue | HUE | ✔️ |
| alpha_darken | LUMINESCENT_PREMUL | ✔️ |
| stencil_alpha | STENCIL_ALPHA | ✔️ |
| hard_overlay | VIVID_LIGHT | ❗ |
| hard_mix | HARD_MIX | ❗ |
| hard_mix_photoshop | CLASSIC_COLOR_BURN | ❗ |
| parallel | DARKEN | ✔️ |
| geometric_mean | MULTIPLY | ✔️ |
| additive_subtractive | DIFFERENCE | ❗ |
| difference | DIFFERENCE | ✔️ |
| exclusion | EXCLUSION | ✔️ |
| equivalence | DIFFERENCE | ✔️ |
| freeze_reflect | OVERLAY | ✔️ |
| heat_glow | HARD_LIGHT | ❗ |
| color_hsi | COLOR | ❗ |
| intensity | LUMINOSITY | ❗ |
| saturation_hsi | SATURATION | ❗ |
| hue_hsi | HUE | ❗ |
| lighter_color | LIGHTER_COLOR | ✔️ |
| flat_light | VIVID_LIGHT | ❗ |
| fog_lighten | LIGHTEN | ❗ |
| linear_light | LINEAR_LIGHT | ✔️ |
| luminosity_sai | ADD | ✔️ |
| soft_light | SOFT_LIGHT | ✔️ |
| hard_light | HARD_LIGHT | ✔️ |
| pin_light | PIN_LIGHT | ✔️ |
| vivid_light | COLOR_BURN | ❗ |
| soft_light_ifs | SOFT_LIGHT | ✔️ |
| soft_light_pegtop_delphi | SOFT_LIGHT | ❗ |
| super_light | PIN_LIGHT | ❗ |
| linear_dodge | LINEAR_DODGE | ✔️ |
| add | ADD | ✔️ |
