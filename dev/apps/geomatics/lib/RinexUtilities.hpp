#pragma ident "$Id: $"

//============================================================================
//
//  This file is part of GPSTk, the GPS Toolkit.
//
//  The GPSTk is free software; you can redistribute it and/or modify
//  it under the terms of the GNU Lesser General Public License as published
//  by the Free Software Foundation; either version 2.1 of the License, or
//  any later version.
//
//  The GPSTk is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU Lesser General Public License for more details.
//
//  You should have received a copy of the GNU Lesser General Public
//  License along with GPSTk; if not, write to the Free Software Foundation,
//  Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//  
//  Copyright 2004, The University of Texas at Austin
//
//============================================================================

//============================================================================
//
//This software developed by Applied Research Laboratories at the University of
//Texas at Austin, under contract to an agency or agencies within the U.S. 
//Department of Defense. The U.S. Government retains all rights to use,
//duplicate, distribute, disclose, or release this software. 
//
//Pursuant to DoD Directive 523024 
//
// DISTRIBUTION STATEMENT A: This software has been approved for public 
//                           release, distribution is unlimited.
//
//=============================================================================

/**
 * @file RinexUtilities.hpp
 * Miscellaneous RINEX-related utilities for use with geomatics lib.
 */

#ifndef GPSTK_RINEX_UTILITIES_INCLUDE
#define GPSTK_RINEX_UTILITIES_INCLUDE

//------------------------------------------------------------------------------------
// system includes
#include <string>
#include <vector>

// GPSTk
#include "BCEphemerisStore.hpp"
#include "SP3EphemerisStore.hpp"

//------------------------------------------------------------------------------------
/** @defgroup rinexutils Rinex Utilities */
//@{
   /** Register commonly used extended Rinex observation types.
    * @return 0 ok, or the return value of RegisterExtendedRinexObsType().
    */
int RegisterARLUTExtendedTypes(void);

   /** Determine if the given file is an SP3 format file.
    * @param file the filename
    * @return true if the file is SP3 format.
    */
bool isSP3File(const std::string& file);

   /** Determine if the given file is a Rinex navigation file.
    * @param file the filename
    * @return true if the file is a Rinex navigation file.
    */
bool isRinexNavFile(const std::string& file);

   /** Determine if the given file is a Rinex observation file.
    * @param file the filename
    * @return true if the file is a Rinex observation file.
    */
bool isRinexObsFile(const std::string& file);

   /** Open the files and add to the appropriate EphemerisStore.
    * @param files vector of the filenames.
    * @param PE an SP3EphemerisStore into which to put SP3 ephemeris data.
    * @param BCE a BCEphemerisStore into which to put broadcast
    *    (Rinex Nav) ephemeris data.
    * @return the number of files successfully read.
    * Throws on errors.
    */
int FillEphemerisStore(const std::vector<std::string>& files,
      gpstk::SP3EphemerisStore& PE,
      gpstk::BCEphemerisStore& BCE);

//@}

#endif
//------------------------------------------------------------------------------------
