# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _xtract
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


get_descriptor = _xtract.get_descriptor
create_filterbank = _xtract.create_filterbank
destroy_filterbank = _xtract.destroy_filterbank
class floatArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, floatArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, floatArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xtract.new_floatArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_floatArray
    __del__ = lambda self : None;
    def __getitem__(*args): return _xtract.floatArray___getitem__(*args)
    def __setitem__(*args): return _xtract.floatArray___setitem__(*args)
    def cast(*args): return _xtract.floatArray_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _xtract.floatArray_frompointer
    if _newclass:frompointer = staticmethod(_xtract.floatArray_frompointer)
floatArray_swigregister = _xtract.floatArray_swigregister
floatArray_swigregister(floatArray)
floatArray_frompointer = _xtract.floatArray_frompointer

class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xtract.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(*args): return _xtract.intArray___getitem__(*args)
    def __setitem__(*args): return _xtract.intArray___setitem__(*args)
    def cast(*args): return _xtract.intArray_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _xtract.intArray_frompointer
    if _newclass:frompointer = staticmethod(_xtract.intArray_frompointer)
intArray_swigregister = _xtract.intArray_swigregister
intArray_swigregister(intArray)
intArray_frompointer = _xtract.intArray_frompointer

test = _xtract.test
xtract_mean = _xtract.xtract_mean
xtract_variance = _xtract.xtract_variance
xtract_standard_deviation = _xtract.xtract_standard_deviation
xtract_average_deviation = _xtract.xtract_average_deviation
xtract_skewness = _xtract.xtract_skewness
xtract_kurtosis = _xtract.xtract_kurtosis
xtract_spectral_mean = _xtract.xtract_spectral_mean
xtract_spectral_variance = _xtract.xtract_spectral_variance
xtract_spectral_standard_deviation = _xtract.xtract_spectral_standard_deviation
xtract_spectral_average_deviation = _xtract.xtract_spectral_average_deviation
xtract_spectral_skewness = _xtract.xtract_spectral_skewness
xtract_spectral_kurtosis = _xtract.xtract_spectral_kurtosis
xtract_spectral_centroid = _xtract.xtract_spectral_centroid
xtract_irregularity_k = _xtract.xtract_irregularity_k
xtract_irregularity_j = _xtract.xtract_irregularity_j
xtract_tristimulus_1 = _xtract.xtract_tristimulus_1
xtract_tristimulus_2 = _xtract.xtract_tristimulus_2
xtract_tristimulus_3 = _xtract.xtract_tristimulus_3
xtract_smoothness = _xtract.xtract_smoothness
xtract_spread = _xtract.xtract_spread
xtract_zcr = _xtract.xtract_zcr
xtract_rolloff = _xtract.xtract_rolloff
xtract_loudness = _xtract.xtract_loudness
xtract_flatness = _xtract.xtract_flatness
xtract_flatness_db = _xtract.xtract_flatness_db
xtract_tonality = _xtract.xtract_tonality
xtract_noisiness = _xtract.xtract_noisiness
xtract_rms_amplitude = _xtract.xtract_rms_amplitude
xtract_spectral_inharmonicity = _xtract.xtract_spectral_inharmonicity
xtract_crest = _xtract.xtract_crest
xtract_power = _xtract.xtract_power
xtract_odd_even_ratio = _xtract.xtract_odd_even_ratio
xtract_sharpness = _xtract.xtract_sharpness
xtract_spectral_slope = _xtract.xtract_spectral_slope
xtract_lowest_value = _xtract.xtract_lowest_value
xtract_highest_value = _xtract.xtract_highest_value
xtract_sum = _xtract.xtract_sum
xtract_hps = _xtract.xtract_hps
xtract_f0 = _xtract.xtract_f0
xtract_failsafe_f0 = _xtract.xtract_failsafe_f0
xtract_nonzero_count = _xtract.xtract_nonzero_count
xtract_flux = _xtract.xtract_flux
xtract_lnorm = _xtract.xtract_lnorm
xtract_difference_vector = _xtract.xtract_difference_vector
xtract_spectrum = _xtract.xtract_spectrum
xtract_autocorrelation_fft = _xtract.xtract_autocorrelation_fft
xtract_mfcc = _xtract.xtract_mfcc
xtract_dct = _xtract.xtract_dct
xtract_autocorrelation = _xtract.xtract_autocorrelation
xtract_amdf = _xtract.xtract_amdf
xtract_asdf = _xtract.xtract_asdf
xtract_bark_coefficients = _xtract.xtract_bark_coefficients
xtract_peak_spectrum = _xtract.xtract_peak_spectrum
xtract_harmonic_spectrum = _xtract.xtract_harmonic_spectrum
xtract_lpc = _xtract.xtract_lpc
xtract_lpcc = _xtract.xtract_lpcc
xtract_subbands = _xtract.xtract_subbands
xtract_windowed = _xtract.xtract_windowed
xtract_features_from_subframes = _xtract.xtract_features_from_subframes
xtract_is_denormal = _xtract.xtract_is_denormal
XTRACT_BARK_BANDS = _xtract.XTRACT_BARK_BANDS
XTRACT_WINDOW_SIZE = _xtract.XTRACT_WINDOW_SIZE
XTRACT_NONE = _xtract.XTRACT_NONE
XTRACT_ANY = _xtract.XTRACT_ANY
XTRACT_UNKNOWN = _xtract.XTRACT_UNKNOWN
XTRACT_MAXARGS = _xtract.XTRACT_MAXARGS
XTRACT_MAX_NAME_LENGTH = _xtract.XTRACT_MAX_NAME_LENGTH
XTRACT_MAX_AUTHOR_LENGTH = _xtract.XTRACT_MAX_AUTHOR_LENGTH
XTRACT_MAX_DESC_LENGTH = _xtract.XTRACT_MAX_DESC_LENGTH
XTRACT_FEATURES = _xtract.XTRACT_FEATURES
XTRACT_MEAN = _xtract.XTRACT_MEAN
XTRACT_VARIANCE = _xtract.XTRACT_VARIANCE
XTRACT_STANDARD_DEVIATION = _xtract.XTRACT_STANDARD_DEVIATION
XTRACT_AVERAGE_DEVIATION = _xtract.XTRACT_AVERAGE_DEVIATION
XTRACT_SKEWNESS = _xtract.XTRACT_SKEWNESS
XTRACT_KURTOSIS = _xtract.XTRACT_KURTOSIS
XTRACT_SPECTRAL_MEAN = _xtract.XTRACT_SPECTRAL_MEAN
XTRACT_SPECTRAL_VARIANCE = _xtract.XTRACT_SPECTRAL_VARIANCE
XTRACT_SPECTRAL_STANDARD_DEVIATION = _xtract.XTRACT_SPECTRAL_STANDARD_DEVIATION
XTRACT_SPECTRAL_AVERAGE_DEVIATION = _xtract.XTRACT_SPECTRAL_AVERAGE_DEVIATION
XTRACT_SPECTRAL_SKEWNESS = _xtract.XTRACT_SPECTRAL_SKEWNESS
XTRACT_SPECTRAL_KURTOSIS = _xtract.XTRACT_SPECTRAL_KURTOSIS
XTRACT_SPECTRAL_CENTROID = _xtract.XTRACT_SPECTRAL_CENTROID
XTRACT_IRREGULARITY_K = _xtract.XTRACT_IRREGULARITY_K
XTRACT_IRREGULARITY_J = _xtract.XTRACT_IRREGULARITY_J
XTRACT_TRISTIMULUS_1 = _xtract.XTRACT_TRISTIMULUS_1
XTRACT_TRISTIMULUS_2 = _xtract.XTRACT_TRISTIMULUS_2
XTRACT_TRISTIMULUS_3 = _xtract.XTRACT_TRISTIMULUS_3
XTRACT_SMOOTHNESS = _xtract.XTRACT_SMOOTHNESS
XTRACT_SPREAD = _xtract.XTRACT_SPREAD
XTRACT_ZCR = _xtract.XTRACT_ZCR
XTRACT_ROLLOFF = _xtract.XTRACT_ROLLOFF
XTRACT_LOUDNESS = _xtract.XTRACT_LOUDNESS
XTRACT_FLATNESS = _xtract.XTRACT_FLATNESS
XTRACT_FLATNESS_DB = _xtract.XTRACT_FLATNESS_DB
XTRACT_TONALITY = _xtract.XTRACT_TONALITY
XTRACT_CREST = _xtract.XTRACT_CREST
XTRACT_NOISINESS = _xtract.XTRACT_NOISINESS
XTRACT_RMS_AMPLITUDE = _xtract.XTRACT_RMS_AMPLITUDE
XTRACT_SPECTRAL_INHARMONICITY = _xtract.XTRACT_SPECTRAL_INHARMONICITY
XTRACT_POWER = _xtract.XTRACT_POWER
XTRACT_ODD_EVEN_RATIO = _xtract.XTRACT_ODD_EVEN_RATIO
XTRACT_SHARPNESS = _xtract.XTRACT_SHARPNESS
XTRACT_SPECTRAL_SLOPE = _xtract.XTRACT_SPECTRAL_SLOPE
XTRACT_LOWEST_VALUE = _xtract.XTRACT_LOWEST_VALUE
XTRACT_HIGHEST_VALUE = _xtract.XTRACT_HIGHEST_VALUE
XTRACT_SUM = _xtract.XTRACT_SUM
XTRACT_NONZERO_COUNT = _xtract.XTRACT_NONZERO_COUNT
XTRACT_HPS = _xtract.XTRACT_HPS
XTRACT_F0 = _xtract.XTRACT_F0
XTRACT_FAILSAFE_F0 = _xtract.XTRACT_FAILSAFE_F0
XTRACT_LNORM = _xtract.XTRACT_LNORM
XTRACT_FLUX = _xtract.XTRACT_FLUX
XTRACT_ATTACK_TIME = _xtract.XTRACT_ATTACK_TIME
XTRACT_DECAY_TIME = _xtract.XTRACT_DECAY_TIME
XTRACT_DIFFERENCE_VECTOR = _xtract.XTRACT_DIFFERENCE_VECTOR
XTRACT_AUTOCORRELATION = _xtract.XTRACT_AUTOCORRELATION
XTRACT_AMDF = _xtract.XTRACT_AMDF
XTRACT_ASDF = _xtract.XTRACT_ASDF
XTRACT_BARK_COEFFICIENTS = _xtract.XTRACT_BARK_COEFFICIENTS
XTRACT_PEAK_SPECTRUM = _xtract.XTRACT_PEAK_SPECTRUM
XTRACT_SPECTRUM = _xtract.XTRACT_SPECTRUM
XTRACT_AUTOCORRELATION_FFT = _xtract.XTRACT_AUTOCORRELATION_FFT
XTRACT_MFCC = _xtract.XTRACT_MFCC
XTRACT_DCT = _xtract.XTRACT_DCT
XTRACT_HARMONIC_SPECTRUM = _xtract.XTRACT_HARMONIC_SPECTRUM
XTRACT_LPC = _xtract.XTRACT_LPC
XTRACT_LPCC = _xtract.XTRACT_LPCC
XTRACT_SUBBANDS = _xtract.XTRACT_SUBBANDS
XTRACT_WINDOWED = _xtract.XTRACT_WINDOWED
XTRACT_INIT_MFCC = _xtract.XTRACT_INIT_MFCC
XTRACT_INIT_BARK = _xtract.XTRACT_INIT_BARK
XTRACT_INIT_WINDOWED = _xtract.XTRACT_INIT_WINDOWED
XTRACT_SCALAR = _xtract.XTRACT_SCALAR
XTRACT_VECTOR = _xtract.XTRACT_VECTOR
XTRACT_DELTA = _xtract.XTRACT_DELTA
XTRACT_EQUAL_GAIN = _xtract.XTRACT_EQUAL_GAIN
XTRACT_EQUAL_AREA = _xtract.XTRACT_EQUAL_AREA
XTRACT_NO_LNORM_FILTER = _xtract.XTRACT_NO_LNORM_FILTER
XTRACT_POSITIVE_SLOPE = _xtract.XTRACT_POSITIVE_SLOPE
XTRACT_NEGATIVE_SLOPE = _xtract.XTRACT_NEGATIVE_SLOPE
XTRACT_SUCCESS = _xtract.XTRACT_SUCCESS
XTRACT_MALLOC_FAILED = _xtract.XTRACT_MALLOC_FAILED
XTRACT_BAD_ARGV = _xtract.XTRACT_BAD_ARGV
XTRACT_BAD_VECTOR_SIZE = _xtract.XTRACT_BAD_VECTOR_SIZE
XTRACT_DENORMAL_FOUND = _xtract.XTRACT_DENORMAL_FOUND
XTRACT_NO_RESULT = _xtract.XTRACT_NO_RESULT
XTRACT_FEATURE_NOT_IMPLEMENTED = _xtract.XTRACT_FEATURE_NOT_IMPLEMENTED
XTRACT_MAGNITUDE_SPECTRUM = _xtract.XTRACT_MAGNITUDE_SPECTRUM
XTRACT_LOG_MAGNITUDE_SPECTRUM = _xtract.XTRACT_LOG_MAGNITUDE_SPECTRUM
XTRACT_POWER_SPECTRUM = _xtract.XTRACT_POWER_SPECTRUM
XTRACT_LOG_POWER_SPECTRUM = _xtract.XTRACT_LOG_POWER_SPECTRUM
XTRACT_OCTAVE_SUBBANDS = _xtract.XTRACT_OCTAVE_SUBBANDS
XTRACT_LINEAR_SUBBANDS = _xtract.XTRACT_LINEAR_SUBBANDS
XTRACT_FLOAT = _xtract.XTRACT_FLOAT
XTRACT_FLOATARRAY = _xtract.XTRACT_FLOATARRAY
XTRACT_INT = _xtract.XTRACT_INT
XTRACT_MEL_FILTER = _xtract.XTRACT_MEL_FILTER
XTRACT_HERTZ = _xtract.XTRACT_HERTZ
XTRACT_ANY_AMPLITUDE_HERTZ = _xtract.XTRACT_ANY_AMPLITUDE_HERTZ
XTRACT_DBFS = _xtract.XTRACT_DBFS
XTRACT_DBFS_HERTZ = _xtract.XTRACT_DBFS_HERTZ
XTRACT_PERCENT = _xtract.XTRACT_PERCENT
XTRACT_BINS = _xtract.XTRACT_BINS
XTRACT_SONE = _xtract.XTRACT_SONE
XTRACT_FALSE = _xtract.XTRACT_FALSE
XTRACT_TRUE = _xtract.XTRACT_TRUE
XTRACT_GAUSS = _xtract.XTRACT_GAUSS
XTRACT_HAMMING = _xtract.XTRACT_HAMMING
XTRACT_HANN = _xtract.XTRACT_HANN
XTRACT_BARTLETT = _xtract.XTRACT_BARTLETT
XTRACT_TRIANGULAR = _xtract.XTRACT_TRIANGULAR
XTRACT_BARTLETT_HANN = _xtract.XTRACT_BARTLETT_HANN
XTRACT_BLACKMAN = _xtract.XTRACT_BLACKMAN
XTRACT_KAISER = _xtract.XTRACT_KAISER
XTRACT_BLACKMAN_HARRIS = _xtract.XTRACT_BLACKMAN_HARRIS
XTRACT_SPECTRAL = _xtract.XTRACT_SPECTRAL
XTRACT_SPECTRAL_MAGNITUDES = _xtract.XTRACT_SPECTRAL_MAGNITUDES
XTRACT_SPECTRAL_PEAKS = _xtract.XTRACT_SPECTRAL_PEAKS
XTRACT_SPECTRAL_PEAKS_MAGNITUDES = _xtract.XTRACT_SPECTRAL_PEAKS_MAGNITUDES
XTRACT_SPECTRAL_PEAKS_FREQUENCIES = _xtract.XTRACT_SPECTRAL_PEAKS_FREQUENCIES
XTRACT_SPECTRAL_HARMONICS = _xtract.XTRACT_SPECTRAL_HARMONICS
XTRACT_SPECTRAL_HARMONICS_MAGNITUDES = _xtract.XTRACT_SPECTRAL_HARMONICS_MAGNITUDES
XTRACT_SPECTRAL_HARMONICS_FREQUENCIES = _xtract.XTRACT_SPECTRAL_HARMONICS_FREQUENCIES
XTRACT_AUTOCORRELATION_COEFFS = _xtract.XTRACT_AUTOCORRELATION_COEFFS
XTRACT_ARBITRARY_SERIES = _xtract.XTRACT_ARBITRARY_SERIES
XTRACT_AUDIO_SAMPLES = _xtract.XTRACT_AUDIO_SAMPLES
XTRACT_MEL_COEFFS = _xtract.XTRACT_MEL_COEFFS
XTRACT_LPC_COEFFS = _xtract.XTRACT_LPC_COEFFS
XTRACT_LPCC_COEFFS = _xtract.XTRACT_LPCC_COEFFS
XTRACT_BARK_COEFFS = _xtract.XTRACT_BARK_COEFFS
XTRACT_SUBFRAMES = _xtract.XTRACT_SUBFRAMES
XTRACT_NO_DATA = _xtract.XTRACT_NO_DATA
class xtract_function_descriptor_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xtract_function_descriptor_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xtract_function_descriptor_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["id"] = _xtract.xtract_function_descriptor_t_id_set
    __swig_getmethods__["id"] = _xtract.xtract_function_descriptor_t_id_get
    if _newclass:id = _swig_property(_xtract.xtract_function_descriptor_t_id_get, _xtract.xtract_function_descriptor_t_id_set)
    __swig_setmethods__["argc"] = _xtract.xtract_function_descriptor_t_argc_set
    __swig_getmethods__["argc"] = _xtract.xtract_function_descriptor_t_argc_get
    if _newclass:argc = _swig_property(_xtract.xtract_function_descriptor_t_argc_get, _xtract.xtract_function_descriptor_t_argc_set)
    __swig_setmethods__["is_scalar"] = _xtract.xtract_function_descriptor_t_is_scalar_set
    __swig_getmethods__["is_scalar"] = _xtract.xtract_function_descriptor_t_is_scalar_get
    if _newclass:is_scalar = _swig_property(_xtract.xtract_function_descriptor_t_is_scalar_get, _xtract.xtract_function_descriptor_t_is_scalar_set)
    __swig_setmethods__["is_delta"] = _xtract.xtract_function_descriptor_t_is_delta_set
    __swig_getmethods__["is_delta"] = _xtract.xtract_function_descriptor_t_is_delta_get
    if _newclass:is_delta = _swig_property(_xtract.xtract_function_descriptor_t_is_delta_get, _xtract.xtract_function_descriptor_t_is_delta_set)
    __swig_getmethods__["result"] = _xtract.xtract_function_descriptor_t_result_get
    if _newclass:result = _swig_property(_xtract.xtract_function_descriptor_t_result_get)
    __swig_getmethods__["argv"] = _xtract.xtract_function_descriptor_t_argv_get
    if _newclass:argv = _swig_property(_xtract.xtract_function_descriptor_t_argv_get)
    __swig_getmethods__["data"] = _xtract.xtract_function_descriptor_t_data_get
    if _newclass:data = _swig_property(_xtract.xtract_function_descriptor_t_data_get)
    __swig_getmethods__["algo"] = _xtract.xtract_function_descriptor_t_algo_get
    if _newclass:algo = _swig_property(_xtract.xtract_function_descriptor_t_algo_get)
    def __init__(self, *args): 
        this = _xtract.new_xtract_function_descriptor_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_xtract_function_descriptor_t
    __del__ = lambda self : None;
xtract_function_descriptor_t_swigregister = _xtract.xtract_function_descriptor_t_swigregister
xtract_function_descriptor_t_swigregister(xtract_function_descriptor_t)

class xtract_function_descriptor_t_result(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xtract_function_descriptor_t_result, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xtract_function_descriptor_t_result, name)
    __repr__ = _swig_repr
    __swig_getmethods__["vector"] = _xtract.xtract_function_descriptor_t_result_vector_get
    if _newclass:vector = _swig_property(_xtract.xtract_function_descriptor_t_result_vector_get)
    __swig_getmethods__["scalar"] = _xtract.xtract_function_descriptor_t_result_scalar_get
    if _newclass:scalar = _swig_property(_xtract.xtract_function_descriptor_t_result_scalar_get)
    def __init__(self, *args): 
        this = _xtract.new_xtract_function_descriptor_t_result(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_xtract_function_descriptor_t_result
    __del__ = lambda self : None;
xtract_function_descriptor_t_result_swigregister = _xtract.xtract_function_descriptor_t_result_swigregister
xtract_function_descriptor_t_result_swigregister(xtract_function_descriptor_t_result)

class xtract_function_descriptor_t_result_vector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xtract_function_descriptor_t_result_vector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xtract_function_descriptor_t_result_vector, name)
    __repr__ = _swig_repr
    __swig_setmethods__["format"] = _xtract.xtract_function_descriptor_t_result_vector_format_set
    __swig_getmethods__["format"] = _xtract.xtract_function_descriptor_t_result_vector_format_get
    if _newclass:format = _swig_property(_xtract.xtract_function_descriptor_t_result_vector_format_get, _xtract.xtract_function_descriptor_t_result_vector_format_set)
    __swig_setmethods__["unit"] = _xtract.xtract_function_descriptor_t_result_vector_unit_set
    __swig_getmethods__["unit"] = _xtract.xtract_function_descriptor_t_result_vector_unit_get
    if _newclass:unit = _swig_property(_xtract.xtract_function_descriptor_t_result_vector_unit_get, _xtract.xtract_function_descriptor_t_result_vector_unit_set)
    def __init__(self, *args): 
        this = _xtract.new_xtract_function_descriptor_t_result_vector(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_xtract_function_descriptor_t_result_vector
    __del__ = lambda self : None;
xtract_function_descriptor_t_result_vector_swigregister = _xtract.xtract_function_descriptor_t_result_vector_swigregister
xtract_function_descriptor_t_result_vector_swigregister(xtract_function_descriptor_t_result_vector)

class xtract_function_descriptor_t_result_scalar(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xtract_function_descriptor_t_result_scalar, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xtract_function_descriptor_t_result_scalar, name)
    __repr__ = _swig_repr
    __swig_setmethods__["min"] = _xtract.xtract_function_descriptor_t_result_scalar_min_set
    __swig_getmethods__["min"] = _xtract.xtract_function_descriptor_t_result_scalar_min_get
    if _newclass:min = _swig_property(_xtract.xtract_function_descriptor_t_result_scalar_min_get, _xtract.xtract_function_descriptor_t_result_scalar_min_set)
    __swig_setmethods__["max"] = _xtract.xtract_function_descriptor_t_result_scalar_max_set
    __swig_getmethods__["max"] = _xtract.xtract_function_descriptor_t_result_scalar_max_get
    if _newclass:max = _swig_property(_xtract.xtract_function_descriptor_t_result_scalar_max_get, _xtract.xtract_function_descriptor_t_result_scalar_max_set)
    __swig_setmethods__["unit"] = _xtract.xtract_function_descriptor_t_result_scalar_unit_set
    __swig_getmethods__["unit"] = _xtract.xtract_function_descriptor_t_result_scalar_unit_get
    if _newclass:unit = _swig_property(_xtract.xtract_function_descriptor_t_result_scalar_unit_get, _xtract.xtract_function_descriptor_t_result_scalar_unit_set)
    def __init__(self, *args): 
        this = _xtract.new_xtract_function_descriptor_t_result_scalar(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_xtract_function_descriptor_t_result_scalar
    __del__ = lambda self : None;
xtract_function_descriptor_t_result_scalar_swigregister = _xtract.xtract_function_descriptor_t_result_scalar_swigregister
xtract_function_descriptor_t_result_scalar_swigregister(xtract_function_descriptor_t_result_scalar)

class xtract_function_descriptor_t_argv(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xtract_function_descriptor_t_argv, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xtract_function_descriptor_t_argv, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _xtract.xtract_function_descriptor_t_argv_type_set
    __swig_getmethods__["type"] = _xtract.xtract_function_descriptor_t_argv_type_get
    if _newclass:type = _swig_property(_xtract.xtract_function_descriptor_t_argv_type_get, _xtract.xtract_function_descriptor_t_argv_type_set)
    __swig_setmethods__["min"] = _xtract.xtract_function_descriptor_t_argv_min_set
    __swig_getmethods__["min"] = _xtract.xtract_function_descriptor_t_argv_min_get
    if _newclass:min = _swig_property(_xtract.xtract_function_descriptor_t_argv_min_get, _xtract.xtract_function_descriptor_t_argv_min_set)
    __swig_setmethods__["max"] = _xtract.xtract_function_descriptor_t_argv_max_set
    __swig_getmethods__["max"] = _xtract.xtract_function_descriptor_t_argv_max_get
    if _newclass:max = _swig_property(_xtract.xtract_function_descriptor_t_argv_max_get, _xtract.xtract_function_descriptor_t_argv_max_set)
    __swig_setmethods__["_def"] = _xtract.xtract_function_descriptor_t_argv__def_set
    __swig_getmethods__["_def"] = _xtract.xtract_function_descriptor_t_argv__def_get
    if _newclass:_def = _swig_property(_xtract.xtract_function_descriptor_t_argv__def_get, _xtract.xtract_function_descriptor_t_argv__def_set)
    __swig_setmethods__["unit"] = _xtract.xtract_function_descriptor_t_argv_unit_set
    __swig_getmethods__["unit"] = _xtract.xtract_function_descriptor_t_argv_unit_get
    if _newclass:unit = _swig_property(_xtract.xtract_function_descriptor_t_argv_unit_get, _xtract.xtract_function_descriptor_t_argv_unit_set)
    __swig_setmethods__["donor"] = _xtract.xtract_function_descriptor_t_argv_donor_set
    __swig_getmethods__["donor"] = _xtract.xtract_function_descriptor_t_argv_donor_get
    if _newclass:donor = _swig_property(_xtract.xtract_function_descriptor_t_argv_donor_get, _xtract.xtract_function_descriptor_t_argv_donor_set)
    def __init__(self, *args): 
        this = _xtract.new_xtract_function_descriptor_t_argv(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_xtract_function_descriptor_t_argv
    __del__ = lambda self : None;
xtract_function_descriptor_t_argv_swigregister = _xtract.xtract_function_descriptor_t_argv_swigregister
xtract_function_descriptor_t_argv_swigregister(xtract_function_descriptor_t_argv)

class xtract_function_descriptor_t_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xtract_function_descriptor_t_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xtract_function_descriptor_t_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["format"] = _xtract.xtract_function_descriptor_t_data_format_set
    __swig_getmethods__["format"] = _xtract.xtract_function_descriptor_t_data_format_get
    if _newclass:format = _swig_property(_xtract.xtract_function_descriptor_t_data_format_get, _xtract.xtract_function_descriptor_t_data_format_set)
    __swig_setmethods__["unit"] = _xtract.xtract_function_descriptor_t_data_unit_set
    __swig_getmethods__["unit"] = _xtract.xtract_function_descriptor_t_data_unit_get
    if _newclass:unit = _swig_property(_xtract.xtract_function_descriptor_t_data_unit_get, _xtract.xtract_function_descriptor_t_data_unit_set)
    def __init__(self, *args): 
        this = _xtract.new_xtract_function_descriptor_t_data(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_xtract_function_descriptor_t_data
    __del__ = lambda self : None;
xtract_function_descriptor_t_data_swigregister = _xtract.xtract_function_descriptor_t_data_swigregister
xtract_function_descriptor_t_data_swigregister(xtract_function_descriptor_t_data)

class xtract_function_descriptor_t_algo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xtract_function_descriptor_t_algo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xtract_function_descriptor_t_algo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _xtract.xtract_function_descriptor_t_algo_name_set
    __swig_getmethods__["name"] = _xtract.xtract_function_descriptor_t_algo_name_get
    if _newclass:name = _swig_property(_xtract.xtract_function_descriptor_t_algo_name_get, _xtract.xtract_function_descriptor_t_algo_name_set)
    __swig_setmethods__["p_name"] = _xtract.xtract_function_descriptor_t_algo_p_name_set
    __swig_getmethods__["p_name"] = _xtract.xtract_function_descriptor_t_algo_p_name_get
    if _newclass:p_name = _swig_property(_xtract.xtract_function_descriptor_t_algo_p_name_get, _xtract.xtract_function_descriptor_t_algo_p_name_set)
    __swig_setmethods__["desc"] = _xtract.xtract_function_descriptor_t_algo_desc_set
    __swig_getmethods__["desc"] = _xtract.xtract_function_descriptor_t_algo_desc_get
    if _newclass:desc = _swig_property(_xtract.xtract_function_descriptor_t_algo_desc_get, _xtract.xtract_function_descriptor_t_algo_desc_set)
    __swig_setmethods__["p_desc"] = _xtract.xtract_function_descriptor_t_algo_p_desc_set
    __swig_getmethods__["p_desc"] = _xtract.xtract_function_descriptor_t_algo_p_desc_get
    if _newclass:p_desc = _swig_property(_xtract.xtract_function_descriptor_t_algo_p_desc_get, _xtract.xtract_function_descriptor_t_algo_p_desc_set)
    __swig_setmethods__["author"] = _xtract.xtract_function_descriptor_t_algo_author_set
    __swig_getmethods__["author"] = _xtract.xtract_function_descriptor_t_algo_author_get
    if _newclass:author = _swig_property(_xtract.xtract_function_descriptor_t_algo_author_get, _xtract.xtract_function_descriptor_t_algo_author_set)
    __swig_setmethods__["year"] = _xtract.xtract_function_descriptor_t_algo_year_set
    __swig_getmethods__["year"] = _xtract.xtract_function_descriptor_t_algo_year_get
    if _newclass:year = _swig_property(_xtract.xtract_function_descriptor_t_algo_year_get, _xtract.xtract_function_descriptor_t_algo_year_set)
    def __init__(self, *args): 
        this = _xtract.new_xtract_function_descriptor_t_algo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_xtract_function_descriptor_t_algo
    __del__ = lambda self : None;
xtract_function_descriptor_t_algo_swigregister = _xtract.xtract_function_descriptor_t_algo_swigregister
xtract_function_descriptor_t_algo_swigregister(xtract_function_descriptor_t_algo)

class xtract_mel_filter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xtract_mel_filter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xtract_mel_filter, name)
    __repr__ = _swig_repr
    __swig_setmethods__["n_filters"] = _xtract.xtract_mel_filter_n_filters_set
    __swig_getmethods__["n_filters"] = _xtract.xtract_mel_filter_n_filters_get
    if _newclass:n_filters = _swig_property(_xtract.xtract_mel_filter_n_filters_get, _xtract.xtract_mel_filter_n_filters_set)
    __swig_setmethods__["filters"] = _xtract.xtract_mel_filter_filters_set
    __swig_getmethods__["filters"] = _xtract.xtract_mel_filter_filters_get
    if _newclass:filters = _swig_property(_xtract.xtract_mel_filter_filters_get, _xtract.xtract_mel_filter_filters_set)
    def __init__(self, *args): 
        this = _xtract.new_xtract_mel_filter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xtract.delete_xtract_mel_filter
    __del__ = lambda self : None;
xtract_mel_filter_swigregister = _xtract.xtract_mel_filter_swigregister
xtract_mel_filter_swigregister(xtract_mel_filter)

xtract_init_mfcc = _xtract.xtract_init_mfcc
xtract_init_bark = _xtract.xtract_init_bark
xtract_init_fft = _xtract.xtract_init_fft
xtract_free_fft = _xtract.xtract_free_fft
xtract_init_window = _xtract.xtract_init_window
xtract_free_window = _xtract.xtract_free_window
xtract_make_descriptors = _xtract.xtract_make_descriptors
xtract_free_descriptors = _xtract.xtract_free_descriptors


