""":mod:`libraw.structs` --- LibRaw struct definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from ctypes import *  # noqa


class ph1_t(Structure):

    """Contains color data read by Phase One cameras."""
    _fields_ = [
        ('format', c_int),
        ('key_off', c_int),
        ('tag_21a', c_int),
        ('t_black', c_int),
        ('split_col', c_int),
        ('black_col', c_int),
        ('split_row', c_int),
        ('black_row', c_int),
        ('tag_210', c_float),
    ]


class libraw_iparams_t(Structure):

    """The primary parameters of the image."""
    _fields_ = [
        ('make', c_char * 64),
        ('model', c_char * 64),
        ('software', c_char * 64),
        ('raw_count', c_uint),
        ('dng_version', c_uint),
        ('is_foveon', c_uint),
        ('colors', c_int),
        ('filters', c_uint),
        ('xtrans', c_char * 6 * 6),
        ('xtrans_abs', c_char * 6 * 6),
        ('cdesc', c_char * 5),
        ('xmplen', c_uint),
        ('xmpdata', POINTER(c_char)),
    ]


class libraw_image_sizes_t(Structure):

    """Describes the size of the image."""
    _fields_ = [
        ('raw_height', c_ushort),
        ('raw_width', c_ushort),
        ('height', c_ushort),
        ('width', c_ushort),
        ('top_margin', c_ushort),
        ('left_margin', c_ushort),
        ('iheight', c_ushort),
        ('iwidth', c_ushort),
        ('raw_pitch', c_uint),
        ('pixel_aspect', c_double),
        ('flip', c_int),
        ('mask', c_int * 8 * 4),
    ]


class libraw_dng_color_t(Structure):

    _fields_ = [
        ('illuminant', c_ushort),
        ('calibration', c_float * 4 * 4),
        ('colormatrix', c_float * 4 * 3),
    ]


class libraw_canon_makernotes_t(Structure):

    _fields_ = [
        ('CanonColorDataVer', c_int),
        ('CanonColorDataSubVer', c_int),
        ('SpecularWhiteLevel', c_int),
        ('AverageBlackLevel', c_int),
    ]


class libraw_colordata_t(Structure):

    """Describes all color data of the image."""
    _fields_ = [
        ('curve', c_ushort * 0x10000),
        ('cblack', c_uint * 4102),
        ('black', c_uint),
        ('data_maximum', c_uint),
        ('maximum', c_uint),
        ('white', c_ushort * 8 * 8),
        ('cam_mul', c_float * 4),
        ('pre_mul', c_float * 4),
        ('cmatrix', c_float * 3 * 4),
        ('rgb_cam', c_float * 3 * 4),
        ('cam_xyz', c_float * 4 * 3),
        ('phase_one_data', ph1_t),
        ('flash_used', c_float),
        ('canon_ev', c_float),
        ('model2', c_char * 64),
        ('profile', c_void_p),
        ('profile_length', c_uint),
        ('black_stat', c_uint * 8),
        ('dng_color', libraw_dng_color_t * 2),
        ('canon_makernotes', libraw_canon_makernotes_t),
        ('baseline_exposure', c_float),
        ('OlympusSensorCalibration', c_int * 2),
        ('FujiExpoMidPointShift', c_float),
        ('digitalBack_color', c_int),
    ]


class libraw_gps_info_t(Structure):

    """GPS data for the image."""
    _fields_ = [
        ('latitude', c_float * 3),
        ('longitude', c_float * 3),
        ('gpstimestamp', c_float * 3),
        ('altitude', c_float),
        ('altref', c_char),
        ('latref', c_char),
        ('longref', c_char),
        ('gpsstatus', c_char),
        ('gpsparsed', c_char),
    ]


class libraw_imgother_t(Structure):

    """
    Information read from the raw file that is unnecessary for raw processing.
    """
    _fields_ = [
        ('iso_speed', c_float),
        ('shutter', c_float),
        ('aperture', c_float),
        ('focal_len', c_float),
        ('timestamp', c_uint),  # time_t
        ('shot_order', c_uint),
        ('gpsdata', c_uint * 32),
        ('parsed_gps', libraw_gps_info_t),
        ('desc', c_char * 512),
        ('artist', c_char * 64),
    ]


class libraw_thumbnail_t(Structure):

    """Describes the thumbnail image embedded in the raw file."""
    _fields_ = [
        ('tformat', c_uint),  # LibRaw_thumbnail_formats
        ('twidth', c_ushort),
        ('theight', c_ushort),
        ('tlength', c_uint),
        ('tcolors', c_int),
        ('thumb', POINTER(c_char)),
    ]


class libraw_internal_output_params_t(Structure):

    _fields_ = [
        ('mix_green', c_uint),
        ('raw_color', c_uint),
        ('zero_is_bad', c_uint),
        ('shrink', c_ushort),
        ('fuji_width', c_ushort),
    ]


class libraw_rawdata_t(Structure):

    """
    Raw image data (after it has been unpacked) and a backup copy of color info
    used during post processing.
    """
    _fields_ = [
        ('raw_alloc', c_void_p),
        ('raw_image', POINTER(c_ushort)),
        ('color4_image', POINTER(c_ushort * 4)),
        ('color3_image', POINTER(c_ushort * 3)),
        ('ph1_cblack', POINTER(c_short * 2)),
        ('ph1_rblack', POINTER(c_short * 2)),
        ('iparams', libraw_iparams_t),
        ('sizes', libraw_image_sizes_t),
        ('ioparams', libraw_internal_output_params_t),
        ('color', libraw_colordata_t),
    ]


class libraw_output_params_t(Structure):

    """Output parameters for processing the image with dcraw."""
    _fields_ = [
        ('greybox', c_uint * 4),
        ('cropbox', c_uint * 4),
        ('aber', c_double * 4),
        ('gamm', c_double * 6),
        ('user_mul', c_float * 4),
        ('shot_select', c_uint),
        ('bright', c_float),
        ('threshold', c_float),
        ('half_size', c_int),
        ('four_color_rgb', c_int),
        ('highlight', c_int),
        ('use_auto_wb', c_int),
        ('use_camera_wb', c_int),
        ('use_camera_matrix', c_int),
        ('output_color', c_int),
        ('output_profile', c_char_p),
        ('camera_profile', c_char_p),
        ('bad_pixels', c_char_p),
        ('dark_frame', c_char_p),
        ('output_bps', c_int),
        ('output_tiff', c_int),
        ('user_flip', c_int),
        ('user_qual', c_int),
        ('user_black', c_int),
        ('user_cblack', c_int * 4),
        ('user_sat', c_int),
        ('med_passes', c_int),
        ('auto_bright_thr', c_float),
        ('adjust_maximum_thr', c_float),
        ('no_auto_bright', c_int),
        ('use_fuji_rotate', c_int),
        ('green_matching', c_int),
        ('dcb_iterations', c_int),
        ('dcb_enhance_fl', c_int),
        ('fbdd_noiserd', c_int),
        ('eeci_refine', c_int),
        ('es_med_passes', c_int),
        ('ca_correc', c_int),
        ('cared', c_float),
        ('cablue', c_float),
        ('cfaline', c_int),
        ('linenoise', c_float),
        ('cfa_clean', c_int),
        ('lclean', c_float),
        ('cclean', c_float),
        ('cfa_green', c_int),
        ('green_thresh', c_float),
        ('exp_correc', c_int),
        ('exp_shift', c_float),
        ('exp_preser', c_float),
        ('wf_debanding', c_int),
        ('wf_deband_treshold', c_float * 4),
        ('use_rawspeed', c_int),
        ('no_auto_scale', c_int),
        ('no_interpolation', c_int),
        ('straw_ycc', c_int),
        ('force_foveon_x3f', c_int),
        ('x3f_flags', c_int),
        ('sony_arw2_options', c_int),
        ('sony_arw2_posterization_thr', c_int),
        ('coolscan_nef_gamma', c_float),
    ]


class libraw_nikonlens_t(Structure):

    _fields_ = [
        ('NikonEffectiveMaxAp', c_float),
        ('NikonLensIDNumber', c_ubyte),
        ('NikonLensFStops', c_ubyte),
        ('NikonMCUVersion', c_ubyte),
        ('NikonLensType', c_ubyte),
    ]


class libraw_dnglens_t(Structure):

    _fields_ = [
        ('MinFocal', c_float),
        ('MaxFocal', c_float),
        ('MaxAp4MinFocal', c_float),
        ('MaxAp4MaxFocal', c_float),
    ]


class libraw_makernotes_lens_t(Structure):

    _fields_ = [
        ('LensID', c_ulonglong),
        ('Lens', c_char * 128),
        ('LensFormat', c_ushort),
        ('LensMount', c_ushort),
        ('CamID', c_ulonglong),
        ('CameraFormat', c_ushort),
        ('CameraMount', c_ushort),
        ('body', c_char * 64),
        ('FocalType', c_short),
        ('LensFeatures_pre', c_char * 16),
        ('LensFeatures_suf', c_char * 16),
        ('MinFocal', c_float),
        ('MaxFocal', c_float),
        ('MaxAp4MinFocal', c_float),
        ('MaxAp4MaxFocal', c_float),
        ('MinAp4MinFocal', c_float),
        ('MinAp4MaxFocal', c_float),
        ('MaxAp', c_float),
        ('MinAp', c_float),
        ('CurFocal', c_float),
        ('CurAp', c_float),
        ('MaxAp4CurFocal', c_float),
        ('MinAp4CurFocal', c_float),
        ('LensFStops', c_float),
        ('TeleconverterID', c_ulonglong),
        ('Teleconverter', c_char * 128),
        ('AdapterID', c_ulonglong),
        ('Adapter', c_char * 128),
        ('AttachmentID', c_ulonglong),
        ('Attachment', c_char * 128),
        ('CanonFocalUnits', c_short),
        ('FocalLengthIn35mmFormat', c_float),
    ]


class libraw_lensinfo_t(Structure):

    _fields_ = [
        ('MinFocal', c_float),
        ('MaxFocal', c_float),
        ('MaxAp4MinFocal', c_float),
        ('MaxAp4MaxFocal', c_float),
        ('EXIF_MaxAp', c_float),
        ('LensMake', c_char * 128),
        ('Lens', c_char * 128),
        ('FocalLengthIn35mmFormat', c_ushort),
        ('nikon', libraw_nikonlens_t),
        ('dng', libraw_dnglens_t),
        ('makernotes', libraw_makernotes_lens_t),
    ]


class libraw_data_t(Structure):

    """
    A container which comprises the data structures that make up libraw's
    representation of a raw file.
    """
    _fields_ = [
        ('image', POINTER(c_ushort * 4)),
        ('sizes', libraw_image_sizes_t),
        ('idata', libraw_iparams_t),
        ('lens', libraw_lensinfo_t),
        ('params', libraw_output_params_t),
        ('progress_flags', c_uint),
        ('process_warnings', c_uint),
        ('color', libraw_colordata_t),
        ('other', libraw_imgother_t),
        ('thumbnail', libraw_thumbnail_t),
        ('rawdata', libraw_rawdata_t),
        ('parent_class', c_void_p),
    ]


class libraw_processed_image_t(Structure):

    """A container for processed image data."""
    _fields_ = [
        ('type', c_uint),
        ('height', c_ushort),
        ('width', c_ushort),
        ('colors', c_ushort),
        ('bits', c_ushort),
        ('data_size', c_uint),
        ('data', c_byte * 1),
    ]


class libraw_decoder_info_t(Structure):

    """Describes a raw format decoder name and format."""
    _fields_ = [
        ('decoder_name', c_char_p),
        ('decoder_flags', c_uint),
    ]
