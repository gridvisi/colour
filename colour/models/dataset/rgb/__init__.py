from __future__ import absolute_import

from .aces_rgb import ACES_RGB_COLOURSPACE, ACES_RGB_LOG_COLOURSPACE
from .aces_rgb import ACES_RGB_PROXY_10_COLOURSPACE, ACES_RGB_PROXY_12_COLOURSPACE
from .adobe_rgb_1998 import ADOBE_RGB_1998_COLOURSPACE
from .adobe_wide_gamut_rgb import ADOBE_WIDE_GAMUT_RGB_COLOURSPACE
from .alexa_wide_gamut_rgb import ALEXA_WIDE_GAMUT_RGB_COLOURSPACE
from .apple_rgb import APPLE_RGB_COLOURSPACE
from .best_rgb import BEST_RGB_COLOURSPACE
from .best_rgb import BEST_RGB_COLOURSPACE
from .beta_rgb import BETA_RGB_COLOURSPACE
from .c_log import C_LOG_COLOURSPACE
from .cie_rgb import CIE_RGB_COLOURSPACE
from .color_match_rgb import COLOR_MATCH_RGB_COLOURSPACE
from .dci_p3 import DCI_P3_COLOURSPACE
from .don_rgb_4 import DON_RGB_4_COLOURSPACE
from .eci_rgb_v2 import ECI_RGB_V2_COLOURSPACE
from .ekta_space_ps5 import EKTA_SPACE_PS_5_COLOURSPACE
from .max_rgb import MAX_RGB_COLOURSPACE
from .ntsc_rgb import NTSC_RGB_COLOURSPACE
from .pal_secam_rgb import PAL_SECAM_RGB_COLOURSPACE
from .pointer_gamut import POINTER_GAMUT_DATA
from .prophoto_rgb import PROPHOTO_RGB_COLOURSPACE
from .rec_709 import REC_709_COLOURSPACE
from .rec_2020 import REC_2020_COLOURSPACE
from .russell_rgb import RUSSELL_RGB_COLOURSPACE
from .s_log import S_LOG_COLOURSPACE
from .smptec_rgb import SMPTE_C_RGB_COLOURSPACE
from .srgb import sRGB_COLOURSPACE
from .xtreme_rgb import XTREME_RGB_COLOURSPACE

RGB_COLOURSPACES = {ACES_RGB_COLOURSPACE.name: ACES_RGB_COLOURSPACE,
                    ACES_RGB_LOG_COLOURSPACE.name: ACES_RGB_LOG_COLOURSPACE,
                    ACES_RGB_PROXY_10_COLOURSPACE.name: ACES_RGB_PROXY_10_COLOURSPACE,
                    ACES_RGB_PROXY_12_COLOURSPACE.name: ACES_RGB_PROXY_12_COLOURSPACE,
                    ADOBE_RGB_1998_COLOURSPACE.name: ADOBE_RGB_1998_COLOURSPACE,
                    ADOBE_WIDE_GAMUT_RGB_COLOURSPACE.name: ADOBE_WIDE_GAMUT_RGB_COLOURSPACE,
                    ALEXA_WIDE_GAMUT_RGB_COLOURSPACE.name: ALEXA_WIDE_GAMUT_RGB_COLOURSPACE,
                    APPLE_RGB_COLOURSPACE.name: APPLE_RGB_COLOURSPACE,
                    BEST_RGB_COLOURSPACE.name: BEST_RGB_COLOURSPACE,
                    BETA_RGB_COLOURSPACE.name: BETA_RGB_COLOURSPACE,
                    CIE_RGB_COLOURSPACE.name: CIE_RGB_COLOURSPACE,
                    C_LOG_COLOURSPACE.name: C_LOG_COLOURSPACE,
                    COLOR_MATCH_RGB_COLOURSPACE.name: COLOR_MATCH_RGB_COLOURSPACE,
                    DCI_P3_COLOURSPACE.name: DCI_P3_COLOURSPACE,
                    DON_RGB_4_COLOURSPACE.name: DON_RGB_4_COLOURSPACE,
                    ECI_RGB_V2_COLOURSPACE.name: ECI_RGB_V2_COLOURSPACE,
                    EKTA_SPACE_PS_5_COLOURSPACE.name: EKTA_SPACE_PS_5_COLOURSPACE,
                    MAX_RGB_COLOURSPACE.name: MAX_RGB_COLOURSPACE,
                    NTSC_RGB_COLOURSPACE.name: NTSC_RGB_COLOURSPACE,
                    PAL_SECAM_RGB_COLOURSPACE.name: PAL_SECAM_RGB_COLOURSPACE,
                    PROPHOTO_RGB_COLOURSPACE.name: PROPHOTO_RGB_COLOURSPACE,
                    REC_709_COLOURSPACE.name: REC_709_COLOURSPACE,
                    REC_2020_COLOURSPACE.name: REC_2020_COLOURSPACE,
                    RUSSELL_RGB_COLOURSPACE.name: RUSSELL_RGB_COLOURSPACE,
                    S_LOG_COLOURSPACE.name: S_LOG_COLOURSPACE,
                    SMPTE_C_RGB_COLOURSPACE.name: SMPTE_C_RGB_COLOURSPACE,
                    sRGB_COLOURSPACE.name: sRGB_COLOURSPACE,
                    XTREME_RGB_COLOURSPACE.name: XTREME_RGB_COLOURSPACE}

__all__ = ["RGB_COLOURSPACES"]
__all__ += sorted(RGB_COLOURSPACES.keys())
__all__ = ["POINTER_GAMUT_DATA"]
