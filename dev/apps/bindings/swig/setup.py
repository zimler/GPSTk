import sys
import doc
import os
from distutils.core import setup, Extension


core_lib =  ['gpstk.i',
            '../../../src/AlmOrbit.cpp',
            '../../../src/ANSITime.cpp',
            '../../../src/BinUtils.cpp',
            '../../../src/BrcClockCorrection.cpp',
            '../../../src/BrcKeplerOrbit.cpp',
            '../../../src/CivilTime.cpp',
            '../../../src/ClockSatStore.cpp',
            '../../../src/CommonTime.cpp',
            '../../../src/convhelp.hpp',
            '../../../src/EllipsoidModel.hpp',
            '../../../src/EngAlmanac.cpp',
            '../../../src/EngEphemeris.cpp',
            '../../../src/EngNav.cpp',
            '../../../src/Exception.cpp',
            '../../../src/FFData.cpp',
            '../../../src/FFStream.cpp',
            '../../../src/FFStreamError.hpp',
            '../../../src/FFTextStream.hpp',
            '../../../src/FileStore.hpp',
            '../../../src/GalEphemeris.cpp',
            '../../../src/GalEphemerisStore.cpp',
            '../../../src/geometry.hpp',
            '../../../src/GNSSconstants.hpp',
            '../../../src/gps_constants.hpp',
            '../../../src/GPS_URA.hpp',
            '../../../src/GPSAlmanacStore.cpp',
            '../../../src/GPSEphemerisStore.cpp',
            '../../../src/gpstkplatform.h',
            '../../../src/GPSWeek.cpp',
            '../../../src/GPSWeekZcount.cpp',
            '../../../src/GPSWeekSecond.cpp',
            '../../../src/GPSZcount.cpp',
            '../../../src/JulianDate.cpp',
            '../../../src/MathBase.hpp',
            '../../../src/MJD.cpp',
            '../../../src/ObsID.cpp',
            '../../../src/ObsID.hpp',
            '../../../src/ObsIDInitializer.cpp',
            '../../../src/OrbElemStore.hpp',
            '../../../src/Position.cpp',
            '../../../src/PositionSatStore.cpp',
            '../../../src/PZ90Ellipsoid.hpp',
            '../../../src/ReferenceFrame.cpp',
            '../../../src/Rinex3ClockBase.hpp',
            '../../../src/Rinex3ClockData.cpp',
            '../../../src/Rinex3ClockHeader.cpp',
            '../../../src/Rinex3ObsHeader.cpp',
            '../../../src/Rinex3ObsHeader.hpp',
            '../../../src/Rinex3ObsStream.hpp',
            '../../../src/RinexClockBase.hpp',
            '../../../src/RinexClockData.cpp',
            '../../../src/RinexClockHeader.cpp',
            '../../../src/RinexObsHeader.cpp',
            '../../../src/RinexObsHeader.hpp',
            '../../../src/RinexObsID.cpp',
            '../../../src/RinexObsStream.hpp',
            '../../../src/RinexSatID.cpp',
            '../../../src/SatID.hpp',
            '../../../src/SatID.hpp',
            '../../../src/SP3Base.hpp',
            '../../../src/SP3Data.cpp',
            '../../../src/SP3EphemerisStore.cpp',
            '../../../src/SP3Header.cpp',
            '../../../src/SP3SatID.cpp',
            '../../../src/StringUtils.hpp',
            '../../../src/SVNumXRef.cpp',
            '../../../src/SystemTime.cpp',
            '../../../src/TabularSatStore.hpp',
            '../../../src/TimeConstants.hpp',
            '../../../src/TimeConverters.cpp',
            '../../../src/TimeString.cpp',
            '../../../src/TimeSystem.cpp',
            '../../../src/TimeTag.cpp',
            '../../../src/TimeTag.hpp',
            '../../../src/Triple.cpp',
            '../../../src/UnixTime.cpp',
            '../../../src/Vector.hpp',
            '../../../src/VectorBase.hpp',
            '../../../src/WGS84Ellipsoid.hpp',
            '../../../src/Xv.hpp',
            '../../../src/Xvt.cpp',
            '../../../src/XvtStore.hpp',
            '../../../src/YDSTime.cpp',
            '../../../src/YumaAlmanacStore.cpp',
            '../../../src/YumaData.cpp',
            '../../../src/YumaHeader.hpp']


def is_header(f):
    return ('.hpp' in f) or ('.h' in f)
files_to_compile = filter(lambda f: not is_header(f), core_lib)

cpp_flags = ['-std=c++11', '-w']
swig_flags = ['-c++', '-I../include', '-w362,383,384,503']


if not os.path.exists('doc/doc.i'):
      os.makedirs('doc')
      file = open('doc/doc.i', 'w+')
doc.generate_docs()


setup(name='GPSTk',
      version='2.1',
      description='The GPS Toolkit',
      author='Applied Research Laboratories at the University of Texas at Austin',
      author_email='gpstk@arlut.utexas.edu',
      url='http://www.gpstk.org/',
      ext_modules=[Extension(name='_gpstk',
                             sources=files_to_compile,
                             include_dirs=['../../../src/'],
                             extra_compile_args=cpp_flags,
                             swig_opts=swig_flags,
                             language='c++')],
      py_modules=['gpstk', 'timeconvert'])
