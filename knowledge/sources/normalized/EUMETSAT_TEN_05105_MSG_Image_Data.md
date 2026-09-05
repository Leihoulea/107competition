# MSG Level 1.5 Image Data Format Description

## Document metadata

- Publisher: EUMETSAT
- Document ID: EUM/MSG/ICD/105
- Version: v8 e-signed
- Document date: 2017-09-26
- Original file: eumetsat_ten_05105_msg_image_data.pdf
- Raw SHA-256: b70c47c67b7961d1f9a9741cacb6313241f163a39dd4518b7f5e83296739f8c1

<!-- source_page: 1 -->

© EUMETSAT
The copyright of this document is the property of EUMETSAT.
































Doc.No. : EUM/MSG/ICD/105
Issue : v8 e-signed
Date : 26 September 2017
WBS/DBS :
MSG Level 1.5 Image Data Format
Description


EUMETSAT
Eumetsat-Allee 1, D-64295 Darmstadt, Germany
Tel: +49 6151 807-7
Fax: +49 6151 807 555
http://www.eumetsat.int

<!-- source_page: 2 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 2 of 129

Page intentionally blank

<!-- source_page: 3 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 3 of 129

Document Change Record
Issue /
Revision
DCN.
No
Changed Pages / Paragraphs
1 New
2 Author changed from Y. Buhler and J. Flewin to C. Rogers.
Sections 1, 2 and 7 updated.
3 Author changed from C. Rogers to K. Dammann and J. Mueller
Section 2.2 rewritten.
Section 3.1.5 on the alignment of the HRV and non-HRV images and their
datums inserted.
Note 3 in Section 3.1.7 deleted.
Section on PSF deleted.
Section 4.1 updated.
General information in Section 5.2 deleted (now covered by Section 2.2).
Information on temperature encoding included for "FCU tempera tures" in
Section 7.
Instrument ground characterisation moved from Section 2 into Appendix
A
Table and text on the stability of interchannel spatial registration updated.
v4 Author changed from K. Dammann and J. Mueller to G. Fowler.
Data in Appendix A transferred to separate Technical Note
Section 7.1.3 addition of star ID table
V5 Update following the ECP 833, change to effective radiance:
Author changed from G. Fowler to Johannes Müller
- Section1.2 Document Structure:
Reference to section 3.1 deleted.
- Section 1.4 Reference Documents
Reference to “internal” ICDs removed
Reference to [OGC] removed, because the document is not available
Introduced reference to spectral and PSF characterisation TEN/0005-10
- Section 3.1 Receiving Level 1.5 Data:

<!-- source_page: 4 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 4 of 129

Issue /
Revision
DCN.
No
Changed Pages / Paragraphs
Deleted, because outdated.
- Section 3.2.7 Pixel Value Representation:
Explains the difference between effective and spectral radiance.
-Section 5.6 Where to Find Pixel and Data Representation Information?
Reference to section 3.1 deleted.
-Section 6.1 Level 1.5 Header Summary: “Header Version” parameter
explained differently
-Section 6.1.4 Image Description Record Summary:
“Level1_5ImageProduction” parameter explanation updated.
-Section 6.1.7 IMPF Configuration Record Summary:
Added note that this is not disseminated.
-Section 7.1 15HEADER Record Structure:
Pointed out that 15HeaderVersion is not disseminated.
-Section 7.1.4 Image Description Record:
Change of PlannedChanProcessing from Boolean byte to enumerated
byte.
-Section: 7.1.7 IMPFConfiguration Record:
Pointed out that IMPF configuration record is not disseminated
Added recommendation not to use this record.
Added information on “maxIncidentRadiance”
Corrected information on “IncidenceRadiance”
Appendix A: Fully removed
V5A Corrected editorial error in 7.1.4
V6 Improved description on straylight processing:
- 3.1.11 Udated for clarity
- 7.2.5 Improved description of StraylightCorrectionFlag and
StraylightCorrection
- Appendix A, B, C added to illustrate the use of straylight
information.

<!-- source_page: 5 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 5 of 129

Issue /
Revision
DCN.
No
Changed Pages / Paragraphs
v7 Sections 6.1.5 and 7.2.5 updated to reflect the addition of GSICS
information to:
Radiometric Processing Record
MPEFCalFeedback
IMPF_CAL_Data
This change consists of replacing:
 CalMonBias by GSICSCalCoeff
 CalMonRms by GSICSCalError
 OffsetCount by GSICSOffsetCount

N.B.: The first two of those three fields were not filled in the past, and the
third one was statically set to 51.
Sections 6.1.7 and 7.2.7 updated to include reprocessing version.
Section 7.2: Description of NominalLongitude and LongitudeOfSSP
updated, following misunderstandings by users.
V8 Sections 3.1.4 and 7.2.6 updated to reflect the fix of the geometric offset
problem in 2017.

<!-- source_page: 6 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 6 of 129

Table of Contents
1 Introduction ................................................................................................................................. 8
1.1 Purpose and Scope – Intended Readership ...................................................................... 8
1.2 Document Structure ............................................................................................................ 8
1.3 Applicable Documents ........................................................................................................ 9
1.4 Reference Documents ...................................................................................................... 10
2 Overview of Level 1.0 Data Acquisition .................................................................................. 11
2.1 SEVIRI Description ........................................................................................................... 11
2.1.1 Image Acquisition Principle.................................................................................. 11
2.1.2 Focal Plane Arrangement .................................................................................... 12
2.1.3 Channel Characteristics ....................................................................................... 13
2.1.4 Detection Chain Scheme ..................................................................................... 13
2.2 On-board Calibration Principle ......................................................................................... 15
3 Overview of Level 1.5 Data ...................................................................................................... 19
3.1 Characteristics of Level 1.5 Image Data .......................................................................... 19
3.1.1 Spectral Bands .................................................................................................... 19
3.1.2 Level 1.5 Image Coverage, Repeat Cycle Duration ............................................ 20
3.1.3 Image Size ........................................................................................................... 21
3.1.4 Image Projection and Relation to Geographical Coordinates ............................. 21
3.1.5 Geographical Alignment of the Non-HRV and HRV images ............................... 23
3.1.6 On-Ground Resolution of Level 1.5 Images ........................................................ 24
3.1.7 Pixel Value Representation ................................................................................. 27
3.1.8 Radiometric Quality ............................................................................................. 28
3.1.9 Geometric Quality ................................................................................................ 28
3.1.10 Interchannel Registration ..................................................................................... 31
3.1.11 Straylight Compensation Characteristics ............................................................. 32
3.1.12 Timeliness and Availability of Level 1.5 Image Data ........................................... 32
4 Structure of the Level 1.5 Data ................................................................................................ 33
4.1 Data Formats .................................................................................................................... 33
4.2 Detailed Level 1.5 Data Structure..................................................................................... 33
4.3 Rationale for the Level 1.5 Data Content and Structure .................................................. 36
5 Locating Information in Level 1.5 Data ................................................................................... 38
5.1 Where to Find Image Size and Projection Information? ................................................... 38
5.2 Where to Find Image Calibration Information? ................................................................. 38
5.3 Where to Find Image Radiometry Information? ............................................................... 39
5.4 Where to Find Image Geometrical Accuracy Information? .............................................. 39
5.5 Where to Find Inter-channel Registration Information?.................................................... 40
5.6 Where to Find Pixel and Data Representation Information? ............................................ 40
5.7 Where to Find Image Quality and Validity Information? ................................................... 40
5.8 Where to Find Image Acquisition & Scanning Conditions? .............................................. 41
5.9 Where to Find Navigation Information? ............................................................................ 41
5.10 Where to Find Satellite and Celestial Body Positions? .................................................... 42
6 Data Content Summary per Record ........................................................................................ 43
6.1 Level 1.5 Header Summary .............................................................................................. 43
6.1.1 Satellite Status Record Summary ........................................................................ 44
6.1.2 Image Acquisition Record Summary ................................................................... 49
6.1.3 Celestial Events Record Summary ...................................................................... 53
6.1.4 Image Description Record Summary ................................................................... 55
6.1.5 Radiometric Processing Record Summary .......................................................... 59
6.1.6 Geometric Processing Record Summary ............................................................ 64
6.1.7 IMPF Configuration Record Summary ................................................................. 67
6.2 Level 1.5 Image Data Summary ....................................................................................... 70
6.2.1 15VIS/IR Image Line Record Summary .............................................................. 71
6.2.2 15HRV Image Line Record Summary ................................................................. 72
6.3 Level 1.5 Trailer Summary ............................................................................................... 73
6.3.1 Image Production Stats Record Summary .......................................................... 74

<!-- source_page: 7 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 7 of 129

6.3.2 Navigation Extraction Results Record Summary................................................. 76
6.3.3 Radiometric Quality Record Summary ................................................................ 78
6.3.4 Geometric Quality Record Summary ................................................................... 79
6.3.5 Timeliness and Completeness Record Summary ............................................... 81
7 Detailed Data Content – Application Data Units .................................................................... 82
7.1.1 GP_SC_NAME: Spacecraft name ....................................................................... 83
7.2 15HEADER Record Structure .......................................................................................... 85
7.2.1 SatelliteStatus Record ......................................................................................... 85
7.2.2 Image Acquisition Record .................................................................................... 88
7.2.3 Celestial Events Record ...................................................................................... 93
7.2.4 Image Description Record ................................................................................... 95
7.2.5 Radiometric Processing Record .......................................................................... 98
7.2.6 GeometricProcessing Record ............................................................................ 103
7.2.7 IMPFConfiguration Record ................................................................................ 104
7.3 1.5 VIS/IR Line Record Structure ................................................................................... 109
7.4 1.5 HRV Line Record Structure ...................................................................................... 111
7.5 15TRAILER Record Structure ........................................................................................ 112
7.5.1 Image Production Stats Record ......................................................................... 112
7.5.2 Navigation Extraction Results Record ............................................................... 115
7.5.3 Radiometric Quality Record ............................................................................... 116
7.5.4 Geometric Quality Record ................................................................................. 120
7.5.5 TimelinessAndCompleteness Record ............................................................... 123
Appendix A Decoding of a Function in Terms of Chebyshev Coefficicients. ................ 125
Appendix B Decoding of 2 Dimensional Straylight Fields ............................................... 127
Appendix C Level 1.0 Co-ordinate Frame (10CF) .............................................................. 129

<!-- source_page: 8 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 8 of 129

1 INTRODUCTION
1.1 Purpose and Scope – Intended Readership
Level 1.5 image data is the result of the processing of the satellite raw data (designated as Level
1.0 data) and constitutes one of the main products of the Meteosat Second Generation (MSG)
system. The designation ‘Level 1.5’ corresponds to image data that has been corrected for all
unwanted radiometric and geometric effects, has been geolocated using a standardised
projection, and has been calibrated and radiance -linearised. The Level 1.5 data is suitable for
the derivation of meteorological products and further meteorological processing.

Ancillary information is also available for Level 1.5 dat a in the form of a ‘Header’ and an
‘Trailer’ to the imagery data. These components provide valuable side -information necessary
to allow full interpretation, validation and calibration of the imagery data to be made.

The purpose of this document is to:
 Provide an introduction to the MSG system to new users who wish to familiarise with the
MSG imagery data.
 Act as a reference document for routine MSG data users who are considering to optimise
the usage of the ancillary data, the extraction of new meteorologi cal products from Level
1.5 data, or the generation of new applications based on it.
 Provide detailed explanatory text on the ancillary information to expert users with
particular areas of specialisation such as image navigation, image radiometric & geometric
quality, calibration, etc.

In short, the goal of the document is to ease the access to the information and therefore to
promote the usage of Level 1.5 image data and its ancillary information.

The reader should be aware that this document describes t he ‘native format’ of the Level 1.5
data, as explained further in the section on applicable documents. Depending on the type of
data service and data product, the user may or may not have access to all the data described.

1.2 Document Structure
The document is structured as follows:
 This introduction details the purpose and scope of this document and explains its relation
to the other documents concerning the MSG System.
 Section 2 presents an overview of the Level 1.0 image acquisition process by the instrument
and provides an introduction to the SEVIRI instrument characteristics (acquisition, On -
Board Calibration principle).
 Section 3 presents the detailed overview of the Level 1.5 data. The most recent information
on the basic characteristics and performance figures for the Level 1.5 image data are
provided.
 Section 4 defines the structure of the Level 1.5 dataset. A synoptic diagram shows the toplevel organisation of the dataset in Records, and can be used as a navigation aid to the more

<!-- source_page: 9 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 9 of 129

detailed Record information. The section also presents the rationale for defining the Level
1.5 dataset structure as it is.
 Section 5 has the goal to provide the reader with a help to locate desired information in the
numerous Records of the Level 1.5 dataset. It is organised by major topics and areas of
expertise that can be of interest to the users (like “Where to find information on Calibration,
Radiometry, Image Quality, etc…”). For each of these topics, the Records of the Level 1.5
dataset containing the relevant information are clearly identified.
 Section 6 contains the list of Data Content Sum mary for all the Records of the Level 1.5
dataset. For each Record, the actual meaning and background of the information, its
dynamics and its relation to the image data is presented.
 Section 7 finally provides the most detailed information on the Level 1.5 Records, down to
the format of the single variables and arrays. This section corresponds to the Detailed Data
Content of the Level 1.5 dataset (at Interface Control Document Level). It is advisable to
read also Section 5 and/o r Section 6 before using this information to ensure correct
understanding of the background and actual meaning of the data.

1.3 Applicable Documents
The following MSG documents are applicable to this document. They take precedence in case
of conflict:

[EURD] End Users Requirements Document, Issue 2.2, EUM/MSG/SPE/013.
[GS] LRIT/HRIT Global Specification, Issue 2.6, August 1999.
[MSI] MSG Ground Segment LRIT/HRIT Mission Specific Implementation, Issue
5, EUM/MSG/SPE/057.
[GSDS] Ground Segment Design Specification, Volume F: Data Types and Encoding
Rules. Issue 1.3, January 1999, EUM/MSG/SPE/055.

The [EURD] is a top-level document summarising the requirements on the MSG system, and
in particular, the image quality requirements.

The [GS] is the basic document defining the transmission scheme used for the dissemination
of the Level 1.5 data (for the users receiving the Level 1.5 data via the dissemination service).

The [MSI] is based on the previous document but provides the MSG-specific extensions to this
transmission scheme.

The [GSDS] volume F contains the detailed information related to the representation of binary
values for the different data types (INTEGER, REAL, TIME).

<!-- source_page: 10 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 10 of 129

1.4 Reference Documents

The following documents provide additional information about ground characterisation data:

[MET8PSF] MSG-1 SEVIRI Modulation Transfer Function Characterisation,
EUM/MSG/TEN/06/0005, Issue 1, 19 January 2006.
[MET9PSF] MSG-2 SEVIRI Modulation Transfer Function Characterisation,
EUM/MSG/TEN/06/0006, Issue 1, 19 January 2006.
[MSG3PSF] MSG-3 SEVIRI Modulation Transfer Function Characterisation,
EUM/MSG/TEN/06/0007, Issue 1, 19 January 2006.
[MSGSRC] MSG SEVIRI Spectral Response Characterisation,
EUM/MSG/TEN/06/0010, Issue 1, 19 January 2006.

<!-- source_page: 11 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 11 of 129

2 OVERVIEW OF LEVEL 1.0 DATA ACQUISITION
The Level 1.0 data correspond to the image data as acquired by the MSG satellite before any
ground processing has taken place. The Level 1.0 image data are acquired by the Spinning
Enhanced Visible and IR Imager (SEVIRI) of the MSG satellites.

2.1 SEVIRI Description
2.1.1 Image Acquisition Principle
The SEVIRI instrument is designed to produce the image of the Earth full disk from a spinning
geostationary satellite.

The scanning of the Earth disk is obtained by using the satellite spi n (100 rpm +/- 1%) in the
East-West direction and by stepping a flat scan mirror in the South -North direction after each
East-West line, to set up the instrument for acquiring the scan of image data.

Figure 1 shows the Earth imaging principle used by SEVIRI.


Figure 1 – Earth imaging principle
One complete revolution of the satellite lasts 0.6 seconds of which only about 30 milliseconds
are available over the Earth disk to acquire one scan. After the 30ms spent imaging the Earth,
the remaining 570ms are used mainly for scan mirror stepping, data transmission and deep
space data acquisition for Direct Current Removal (DCR).

The image nominal repeat cycle is 15 minutes, including on-board radiometric calibration and
scan mirror retrace. Shorter repeat cycles are programmable if an image of a reduced area of
Earth is required (see also Section 3.1.2).

<!-- source_page: 12 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 12 of 129

2.1.2 Focal Plane Arrangement
The instrument generates images of the Earth in 12 different spectral channels, from visible to
infrared, with a sampling distance corresponding nominally to 3 km at Sub Satellite Point (1
km for High Resolution Visible channel on a reduced Earth area).

These channels are known as either 'cold' channels (IR3.9, IR6.2, IR7.3, IR8.7, IR9.7, IR10.8,
IR12.0, IR13.4) or 'warm' or 'solar' channels: HRV, VIS0.6, VIS0.8, NIR1.6.

For each spectral channel there are three detectors, hence in one revolution of the satellite, three
lines of image are acquired simultaneously. For the HRV channel there are 9 detectors and 9
lines are obtained per revolution.

The SEVIRI focal plane arrangement is shown in Figure 2.

Figure 2 – SEVIRI focal plane arrangement
The East -West alignment of the detectors in each channel is obtained by delaying the
acquisition of the detectors according to their position in the focal plane. The East -West
alignment of the channels is obtained by re -addressing the image rows (done by on -ground
processing). The South-North alignment is obtained by re -addressing the image rows (this is
also done by on-ground processing).

Note that for Level 1.0 (raw) data only, the ‘1’ next to each set of detectors in the diagram
indicates the order in which the data from the 3 (9 for HRV) detectors appears in the Level 1.0
data. Detector marked ‘1’ appears first, followed by the centre detector of the group, then the
detector furthest from the marked ‘1’. For HRV the detector marked ‘1’ is first, followed by
the other 8 up to the one marked ‘9’.

Y Im
X Im
Telescope Focal Plane (mm)
SSP (km)
Time Delay
(Microseconds)
T elescope
Focal point
8,10 mm 8,10 mm
8,10 mm
4.05 mm 4.05 mm
54 km 54 km
54 km
27 km27 km
144 micros. 144 micros.72 micros. 72 micros.
3.6 s
E-W Scan
S-N Scan
1
NIR 1.6
1
VIS 0.6
1
VIS 0.8
1
9HRV
1
1
IR 13.4
IR 7.3
1
1
IR 9.7
IR 6.2
1
1
IR 12.0IR 8.7
11
IR 10.8
IR 3.9

<!-- source_page: 13 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 13 of 129

2.1.3 Channel Characteristics

Channel ID Absorption Band
Channel Type
Nominal
Centre
Wavelength
(m)

Spectral
Bandwidth
(m)


Spectral
Bandwidth
As % of energy
actually detected
within spectral
band
HRV Visible
High Resolution
Nominally 0.75 0.6 to 0.9 Precise spectral
characteristics not
critical
VIS 0.6 VNIR
Core Imager
0.635 0.56 to 0.71 98.0 %
VIS 0.8 VNIR
Core Imager
0.81 0.74 to 0.88 99.0 %
IR 1.6 VNIR
Core Imager
1.64 1.50 to 1.78 99.0 %
IR 3.9 IR / Window
Core Imager
3.92 3.48 to 4.36 98.6 % (1)
IR 6.2 Water Vapour
Core Imager
6.25 5.35 to 7.15 99.0 %
IR 7.3 Water Vapour
Pseudo-Sounding
7.35 6.85 to 7.85 98.0 %
IR 8.7 IR / Window
Core Imager
8.70 8.30 to 9.10 98.0 %
IR 9.7 IR / Ozone
Pseudo-Sounding
9.66 9.38 to 9.94 99.0 %
IR 10.8 IR / Window
Core Imager
10.80 9.80 to 11.80 98.0 %
IR 12.0 IR / Window
Core Imager
12.00 11.00 to 13.00 98.0 %
IR 13.4 IR / Carbon Dioxide
Pseudo-Sounding
13.40 12.40 to 14.40 96.0 %

2.1.4 Detection Chain Scheme
The amplification of the detector signal is done in two stages:
 a preamplifier unit (PU)
 and a main detection unit (MDU)

Each stage applies several amplification factors and offsets to the signal. The block diagram of
the SEVIRI detection chain is shown in the following Figure:

<!-- source_page: 14 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 14 of 129


Figure 3 – SEVIRI detection chain
The sequence of operations performed by the detection chain on the detector signal is described
by the following equation.

C is the Counts at the instrument output
EL is the signal coming from the detectors (it includes the dark signal ED)
GPU is the parameter called PUGain in the 1.5 header. There is one value of PUGain
per detector (42 values). It is programmable by TC.
OPU is the parameter called PUOffset in the 1.5 header. The PUOffset is programmable
per detector except HRV, VIS0.6 and VIS0.8 (27 values). This offset is used to
remove most of the dark current and the instrument self -emitted radiance in order
to fully exploit the dynamic range for the Earth signal
I0 is a fixed current that is set to the appropriate value. It is not included in the 1.5
Header
GMDU-c is the parameter called MDUCoarseGain in the 1.5 header. There is one value of
MDUCoarseGain per detector (42 values). It is programmable by TC.
GMDU-0 is a fixed gain that is set to the appropriate value. It is not included in the 1.5 Header
DO is the parameter called DCRValues in the record “RadiometricProcessing” of the
1.5 header. There is one value of DCRValues per detector (42 values). Each value
is obtained by averaging 2048 values acquired during Deep Space View.
GMDU-f is the parameter called MDUFineGain in the 1.5 header. There is one value of
MDUFineGain per detector (42 values). It is programmable by TC.
GMDU-Out is the parameter ca lled MDUOutGain in the 1.5 header. There is one value of
MDUOutGain per detector (42 values). It is programmable by TC.

Note: all these parameters are calibrated out by the calibration procedure. A few parameters
are not provided in the 1.5 level header because they are fixed. The variable ones are provided
in the 1.5 header (see Sections 3, 4 and 5).

Detector
PU
(GPU, OPU, Io)
Anti-aliasing
filter
Coarse
gain
Signal
adaptation
Sample/Hold
and AD
Converter
DOC
-
Star sensing
data
Fine
gain Numerical
offset (O MDU)
+
Numerical
filter
Output data
to S/C
GMDU-c
GMDU-o
GMDU-f GMDU-Out
PU MDU
     MDUoPULPUcMDUMDUfMDUOutMDUL ODOIOEGGGGGEC   0

<!-- source_page: 15 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 15 of 129

2.2 On-board Calibration Principle
In the SEVIRI 3 -mirror telescope, the incoming Earth radiance is reflected on the primary
telescope mirror M1 by a flat scan mirror that is used to adjust the line of sight in North-South
direction for scanning. The primary mirror transfers the light through the central hole of the
scan mirror onto the secondary and tertiary mirrors, M2 and M3, from where the light is
focussed onto the detectors via a relay optic. A black baffle on the centre of the M1 mirror
reduces the stray light that enters the telescope. The large size of the entrance aperture makes
it impossible to put a calibration source there. However, a small black body source can be
placed near the field stop in the intermediate focal plane between primary and secondary
mirror. The "front optics" (scan mirror, mirror M1, M1 baffle) cannot be seen from the detector
when the blackbody source is in place, whereas the "back optics" (M2, M3 and following relay
optics) is the one behind the blackbody calibration source.

During each satellite rotation, deep space measurements are taken corresponding to zero input
radiance. The irradiance at detector level now corresponds to the self -radiation of the
instrument only.

The signal of the deep space measurements is subtracted on-board automatically from the Earth
measurements after digitisation and sent as digital counts to the ground. When the blackbody
is in place, the deep space measurements from the image line prior to the blackbody
measurement are used. Hence, on the one hand, in all cases the contribution of thermal radiation
of the full optical path is subtracted. On the other hand, the counts received during black body
measurement contain information from the front optics obtained during the deep space
measurements (Figure 4). With SEVIRI, the effect of the front optics on the Earth measurement
and the black body measurement needs to be considered in a calibration model.


Back-Optics Front-Optics
Difference
=
Earth
Measurement
Difference
=
Black Body
Measurement
Earth
Space
Black Body
Space

<!-- source_page: 16 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 16 of 129

Figure 4 – Measurements and Direct Offset Correction

Level 1.5 data are representing a fixed radiometric scale. This scale is provided to the user via
two linear scaling parameters in the image header ("Cal_Slope" and "Cal_Offset",). From here,
the user can reproduce the radiance for each spectral band by the relation:

Physical Units = Cal_Offset + (Cal_Slope x Level 1.5 Pixel Count) (expre ssed in mWm -2 sr -
1 (cm -1) -1)

The user must note that "Cal_Slope" and "Cal_Offset" are fixed scaling factors that will
normally not change. They are not related to the calibration process performed to correct the
image radiometrically.

The radiometric processing from Level 1.0 (raw data) to Level 1.5 is performed in four main
steps:
1. Linearisation. The non -linearity of the detection chains has been established on ground.
This information is used to remove the effects of non-linearity from the measurement.
2. Conversion into radiances. A preliminary conversion is performed to go from counts into
radiances.
3. Calibration. The calibration allows correcting the preliminary estimate of the radiance into
accurate numbers.
4. Scaling. To store the radiance values in the foreseen 10-bit integer format, a linear scaling
is performed using "Cal_Slope" and "Cal_Offset". These are chosen so that the necessary
dynamic range falls into the available interval [0, 1023]

The consequence of this approach is illustrated in Figure 5.

<!-- source_page: 17 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 17 of 129


Figure 5 – Schematic of the scaling of Level 1.5 counts

Figure 5 shows the Level 1.0 count and the Level 1.5 count of an idealised stable target. The
raw Level 1.0 count degrades in time as contamination increases. At some point, a gain change
is performed to maintain image quality. During all this time, the Level 1.5 count remains stable
as the instrument calibration is used to remove degradation effects from the Level 1.5 image.
Also, a gain change is transparent to the user. "Cal_Slope" represents a pure scaling constant
for target radiances to Level 1.5 pixel counts, which is not affected by instrument degradation
or gain changes.


Time
Count
L15 Count
L10 Count
Signal
Degradation
Gain
Change
“Cal_slope”
G0
(normalised)

<!-- source_page: 18 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 18 of 129

Black Body Calibration

The signal irradiance as received at the detector level is the product of three factors:

1. The target radiance, either from Earth or black body.
2. The total optical loss accrued during passage through the instrument.
3. The solid angle under which the detector collects the radiation. The opening cone for the
incoming radiation is determined by the diameter and the focal length of the optical system.

The Calibration is performed in two steps: at ambient temperature plus a measurement with the
blackbody heated to about 20K above ambient. The pair allows for the calibration of the "back
optics" in a classic two -point measurement. Knowing the gain of the back optics, the self -
radiation of the front optics can be measured when viewing cold space (= zero input). In fact,
this needs only a single measurement with the blackbody at ambient because the space count
is always subtracted. The assumption that the reflectance of the mirrors plus their emissivity
equals 1 allows estimating the front optics transmittance from its temperature and its self -
radiation. With the back optics responsivity and the front optics transmit tance the full
instrument gain can be calculated.

<!-- source_page: 19 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 19 of 129

3 OVERVIEW OF LEVEL 1.5 DATA
Level 1.5 data is derived from the Level 1.0 data that is acquired by the MSG satellite and
received by EUMETSAT’s ground segment. EUMETSAT corrects in real -time each received
Level 1.0 image for all radiometric and geometric effects and geolocates it using a standardised
projection. The resulting Level 1.5 image consists of Earth -located, calibrated and radiance -
linearised information that is suitable for the derivation of meteorological products and other
further meteorological processing.

3.1 Characteristics of Level 1.5 Image Data
This section introduces the reader to the basic characteristics of the Level 1.5 image,
considering only the imagery-related aspects.

Important Note: The information given herein is provided with the goal to make available to a
wide community of potential users the latest status of the knowledge within EUMETSAT. This
knowledge will evolve over time when the characteristics of the satellite or the actual accuracy
of the involved processing become more and more accurately known. It has to be stressed that
this information does in no way represent formal requirements on the MSG System, as these
formal requirements are documented in the [EURD]. In case of contradiction or inconsistency
the [EURD] takes precedence.

3.1.1 Spectral Bands
The 12 SEVIRI images channel correspond to the following spectral bands. The following table
presents the spectral characteristics, the dynamic range, the operating temperature of the
detectors, the number of detectors simultaneously acquiring image informatio n during each
satellite revolution and the sampling distance of the Level 1.0 image data:

<!-- source_page: 20 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 20 of 129

Channel Bands Centre
Wavel..
Spectral Band
(99% energy limits)
Dynamic Range Operating
Temp.
Detectors
per
channel
Sample
distance
at SSP
m m K km
HRV Visible

&
(0.75) broadband (peak
within 0.6 - 0.9)
0 - 459 W/m2 sr m
(scaled at centre
frequency)
300 9 1
VIS0.6 0.635 0.56 - 0.71 0 - 533 W/m2 sr m 3 3
VIS0.8 Near 0.81 0.74 - 0.88 0 - 357 W/m2 sr m
IR1.6 IR 1.64 1.50 - 1.78 0 - 75 W/m2 sr m
IR3.9 3.92 3.48 - 4.36
(98% energy limits)
0 - 335 K 85-95


IR8.7 Window 8.70 8.30 - 9.10
(98% energy limits)
0 - 300 K
IR10.8 10.80 9.80 - 11.80
(98% energy limits)
0 - 335 K
IR12.0 12.00 11.00 - 13.00
(98% energy limits)
0 - 335 K
IR6.2 Water
Vapour
6.25 5.35 - 7.15 0 - 300 K
IR7.3 7.35 6.85 - 7.85
(98% energy limits)
0 - 300 K
IR9.7 Ozone 9.66 9.38 - 9.94 0 - 310 K
IR13.4 Carbondioxide
13.40 12.40 - 14.40
(96% energy limits)
0 - 300 K

Table 1 – MSG SEVIRI spectral channel definition


3.1.2 Level 1.5 Image Coverage, Repeat Cycle Duration
Nominally the full Earth disk is covered for all image channels except HRV. For HRV only
half Earth coverage in E-W is provided. The nominal repeat cycle duration providing this Earth
coverage is 15 minutes. Below a visual representation of the full coverage of the Level 1.5 data:

All Channels except HRV HRV (nominal and alternative coverage)

Figure 6 – Nominal Earth coverage of MSG image channels

Note 1: Shorter repeat cycles with a correspondingly reduced coverage in North-South are
technically possible and are supported by the image processing on ground, but are currently
not considered for operational usage.

<!-- source_page: 21 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 21 of 129

Note 2: The space area of the Level 1.5 image is set to a predefined binary value called the
space mask. Further, any missing Level 1.5 image information will also be replaced by this
predefined value (called “masked” in the following). In particul ar in the case of HRV, there
will be masked pixels near the vertical edges: these account for the pixels that cannot
mathematically be generated (due to the required Orbit and Attitude correction, the projection
applied and the processing filter length).

Note 3: In the case of the HRV channel, the nominal coverage is only the central half of
the full Earth disk in E -W. However, alternative coverages can be operated, with a southern
and a northern part of the HRV image having different positions in E-W. The details about the
planned HRV coverage in the Level 1.5 data can be found in the Header Record Image
Description. Note also that some lines around the “break line” between the southern and
northern parts might be masked out in the Level 1.5 data, the reasons being the possibility of
loss/corruption of the Level 1.0 data during acquisition by the SEVIRI and/or the mathematical
impossibility to derive correct values (due to the required Orbit and Attitude correction, the
projection applied and the processing filter length).

3.1.3 Image Size
For all channels except HRV, the nominal Level 1.5 image size is 3712 lines by 3712 columns
(N-S by E-W), the sampling distance defined to be exactly 3 km by 3 km at the sub -satellite
point.

For the HRV channel, the image size is 11136 lines by 5568 columns (N -S by E -W) with a
sampling distance defined to be exactly 1 km by 1 km at the sub-satellite point.

Note: As mentioned earlier, it is technically possible to acquire and process shorter Repeat
Cycles. Then the image size will be reduced. Full information about the image size can be
found in the Record Image Description (see Section 7.2.4).

3.1.4 Image Projection and Relation to Geographical Coordinates
3.1.4.1 The GEOS Projection
The level 1.5 image is provided in a geostationary projection (GEOS P rojection), fully
described in [GS]. For the 0 Degree Full Disk service, this is normally centred on 0° longitude,
for Rapid Scan Service at 9.5 degrees East , and for the Indian Ocean Data Coverage, at 41.5
degrees East as this introduces the least distortions in the Level 1.5 image. Other projections
are currently not foreseen. The actual longitude used is described by the parameter
LongitudeOfSSP being part of the ProjectionDescription record (see Section 7.2.4).

The formulae providing the relation between a given pixel position (i, j) within the Level 1.5
image and the corresponding geographical coordinates (Longitude, Latitude) as well as t he
inverse relation, are fully described in [GS].

3.1.4.2 Erroneous Georeferencing Offset
Until 2017, the Level 1.5 image low resolution and HRV images of the MSG satellites were
shifted by 1.5 km SSP North and West against the nominal GEOS projection. This was due to
various small errors in the ground processor. This shift is still within the requirement of the

<!-- source_page: 22 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 22 of 129

geometrical accuracy of 3.0 km. All MSG missions (0-Deg FES, RSS, and IODC) are affected.
This problem was apparently present since the beginning of the MSG operations.

The problem is a constant shift of the image by 0.5 low resolution pixels North plus 0.5 low
resolution pixels West. The HRV channel appears shifted by 1.5 HRV pixels North plus 1.5
HRV pixels West . A correction has been introduced in December 2017 to correct this error.
After introduction of the correction, the disseminated images as well as the images in the data
centre do not have this offset anymore. (Note that the correction has no effect of th e natural
variation in image quality, which are normally low but measurable.) The presence of the
correction can be evaluated by inspecting the parameter TypeOfEarthModel, being parameter
of the EarthModel record in the GeometricProcessing record (see Section 7.2.6). The
interpretation is as follows:

TypeOfEarthModel:= 1 georeferencing offset present (i.e. image shifted wrt GEOS
projection)
TypeOfEarthModel:=2 corrected data

<!-- source_page: 23 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 23 of 129

3.1.5 Geographical Alignment of the Non-HRV and HRV images
For the non -HRV images, the nominal geostationary projection centre (0° longitude, 0°
latitude) coincides with the middle of the pixel that has the line and column number
(1856,1856), where the pixel numbering starts in the South -Eastern corner of the image with
line and column number (1,1), see Figure 7.

Figure 7 – Alignment and numbering of the non-HRV pixels

For the HRV image, the nominal geostationary position is the middle of the HRV -pixel with
the line and column number (5566,5566), referenced to the HRV Reference Grid as shown in
Figure 8. Note that nine HRV -pixels (3 by 3) cover one non -HRV pixel such that both non -
HRV and HRV images are perfectly aligned with respect to the nominal geostationary position.
However, the choice of image centres for the non-HRV and HRV images means that the datum
pixel of the non-HRV image is not fully covered with HRV pixels as it is shown in Figure 8.

Note that the HRV Reference Grid normally consists of 11136 x 11136 pixels and is given in
the Image Description Record as ReferenceGridHRV (see 7.2.4). Within the HRV
Reference Grid the current HRV image (as shown i.e. in Figure 6) is given in the Image
Production Stats Record (see Section 7.5.1) by the values o f LowerSouthLineActual,
LowerNorthLineActual, LowerEastColumnActual, LowerWestColumnActual,
UpperSouthLineActual, UpperNorthLineActual, UpperEastColumnActual and
UpperWestColumnActual, which are given the boundaries lines and columns of the HRV
image referring to the Reference Grid and the datum of the image as shown in Figure 8 and
Figure 9.


( 1857,
1859)
( 1857,
1858)
( 1857,
1857)
( 1857,
1856)
( 1857,
1855)
( 1857,
1854)
( 1856,
1859)
( 1856,
1858)
( 1856,
1857)
( 1856,
1856)
( 1856,
1855)
( 1856,
1854)
( 1855,
1859)
( 1855,
1858)
( 1855,
1857)
( 1855,
1856)
( 1855,
1855)
( 1855,
1854)
0° East of Greenwich
Equator
(1, 1)
0° East of Greenwich
Equator
( 5567,
5568)
( 5567,
5567)
( 5567,
5566)
( 5567,
5565)
( 5567,
5564)
( 5566,
5568)
( 5566,
5567)
( 5566,
5566)
( 5566,
5565)
( 5566,
5564)
( 5565,
5568)
( 5565,
5567)
( 5565,
5566)
( 5565,
5565)
( 5565,
5564)
Low Res Pixel
(1, 1)
(2, 1)(2, 2)
(1,2)
(1856, 1856)
(1,1)

<!-- source_page: 24 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 24 of 129


Figure 8 – Alignment and numbering of the HRV-pixels with respect to non-HRV pixels
and the HRV reference grid

Figure 9 – Example of the HRV alignment and numbering of the HRV offset scanning
format with respect to the HRV reference grid

3.1.6 On-Ground Resolution of Level 1.5 Images
The following figures provide the map of the on -ground pixel resolution function of the
geographical coordinates. This is a direct consequence of the image acquisition process by the
MSG satellite based on constant angular steps seen from the geostationary orbit.

Lower
Area
Upper
Area
LowerNorthLineActual
(8064)
LowerSouthLineActual
(1)
LowerEastColumnActual
(1)
UpperNorthLineActual
(11136)
UpperEastColumnActual
(2064)
UpperWestColumnActual
(7631)
UpperSouthLineActual
(8065)
LowerWestColumnActual
(5568)

<!-- source_page: 25 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 25 of 129

Legend: Darkest grey correspond to 3.1 km, lighter grey to 4 km, 5 km, 6 km, 8 km and
11km respectively
Figure 10 – MSG Level 1.5 ground resolution map (N-S direction)

<!-- source_page: 26 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 26 of 129

Figure 11 – MSG Level 1.5 ground resolution map (E-W direction)

Figure 12 – MSG Level 1.5 ground resolution (equivalent surface)

<!-- source_page: 27 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 27 of 129

3.1.7 Pixel Value Representation
The Level 1.5 pixel binary representation is 10 -bit (8 -bit for LRUS -received data), this
corresponding to linearised and equalised image information (correcting for differences in
response between the contributing detectors).

Note 1: As mentioned in the previous section, space pixels are “masked out”, i.e. set to a
predefined value.

Note 2: The relation between the binary pixel value (the pixel count) and the physical
radiance units (expressed in mWm -2sr-1(cm-1)-1) is fully defined for each spe ctral band by the
relation:
Physical Units = Cal_Offset + (Cal_Slope . Pixel Count)

More details can be found in the Level1_5ImageCalibration Record. Concerning the accuracy
of this calibration information, please refer to [EURD] for the specified figures.

Originally, the Level 1.5 image data were produced in terms of spectral radiance so that Level
1.5 product radiance
~
15L can be used to determine brightness temperatures T L15 using the
following formula:

 
0
410
,










~
15
13
215
1ln
L
c
cT L



With 0 the centre wavelength specified in Table 1,  wavenumber in cm -1, and C1=1.19104
10-5 mW(cm-1)-4m-2sr-1, C2=1.43877 K cm.

Following an update to the processing software, the Level 1.5 image data were produced in
terms of effective radiance, defined by the following formula:







dr
drL
L15


With L target spectral radiance. In any case the unit would be mWm-2sr-1(cm-1)-1. Whether
spectral or effective radiance is used, is indicated in the PlannedChanProcessing array in the
Level 1_5 ImageProduction record, being part of Image Description Record.

Note: The Level 1.5 pixels are the results of the resampling of Level 1.0 image data being
acquired by several detectors (3 for all channels, except HRV where 9 detectors are used). For
this reason, in order to apply a mathematically correct processi ng, the Level 1.0 detector
information are first pre -processed for equalisation/linearisation of the detectors response
before resampling to Level 1.5 is applied. The relative “weighting” put on the individual
detectors is fully defined in the Record RadTransform.

<!-- source_page: 28 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 28 of 129

3.1.8 Radiometric Quality
The radiometric quality presented in the table below corresponds to the Level 1.0 radiometric
quality. For more details on the Level 1.0 radiometric quality, please refer to [EURD] or to
§5.3 of this document.

The additional radiometric errors introduced by the processing to the Level 1.5 (due to the
inaccuracies in the implementation of the operation pe rformed on the pixels) can be
characterised as follows:
 The radiometric errors due to the implementation of the processing functions that transform
the Level 1.0 into Level 1.5 data in real-time are generally small to negligible. This is due
to the fact that all operations that modify the pixel values are implemented in floating point
with the resampling function (windowed function of size up to 9x9) providing an accuracy
that is very close to the ideal resampler.
 The final rounding from this internal floating-point representation to the 10 -bit
representation of the Level 1.5 data is by far the largest contributor. The error characteristic
is evenly distributed between –0.5 and +0.5 digital count (out of 1024).
 The radiometric errors related to the inac curacies in the knowledge of the linearisation,
equalisation, etc… corrections are covered by the absolute calibration accuracy figure
[EURD] and are therefore not repeated here.
 The inaccuracies in the geolocation of the data will obviously as a side effect introduce also
radiometric errors with respect to the expected radiance for a given location. These errors
are however strongly scene-dependent. It is considered more appropriate to separate clearly
these contributions and define them as the geometric quality figures.

CHANNEL NOISE MEDIUM-TERM DRIFT
HRV Visible S/N >4.3 for target of 0.1% dynamic range <0.1% of Dyn. Range/Day (outside eclipse days &
gain changes)
VIS0.6 & SNR>10.1 for target of 1% dynamic range <0.1% of Dyn. Range/Day (outside eclipse days &
gain changes)
VIS0.8 Near SNR>7.28 for target of 1% dynamic range
IR1.6 IR SNR>3 for target of 1% dynamic range
IR3.8
(IR3.9)
0.35 K @ 300 K <10% of the long-term drift between two on -board
calibration.
IR8.7 Window 0.28 K @ 300 K
IR10.8 0.25 K @ 300 K
IR12.0 0.37 K @ 300 K
WV6.2 Water
Vapour
0.75 K @ 250 K
WV7.3 0.75 K @ 250 K
IR9.7 Ozone 1.50 K @ 255 K
IR13.4 Carbondioxide
1.80 K @ 270 K

Table 2 – MSG SEVIRI radiometric quality

3.1.9 Geometric Quality
The geometric quality budgets and estimated values are shown in the following figures. These
values might be updated when the actual behaviour of the MSG satellite in orbit are better
known (distances are in equivalent sub-satellite point (SSP) distances):

<!-- source_page: 29 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 29 of 129


The geometric accuracy applies to the image after ground processing. The values given in this
section are obtained with the Image Quality Ground Support Equipment (IQGSE) that has been
developed by Alcatel Space to verify the MSG image geometry performan ces after ground
processing. They are formulated in a statistical sense, either over 1 day (absolute error, error
over 500 lines and error over 6 lines) or in a relative sense between two consecutive images.

The verification is based on the usage of IQGSE coupled with the knowledge of the satellite
parameters as measured during the test campaign.

<!-- source_page: 30 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 30 of 129

NS EW
Performance
(km)
Specification
(km) (SSP)
Performance
(km)
Specification
(km) (SSP)
Absolute
Error within
One Image
1.32 3.0 0.15 3.0
Relative
Accuracy
(consecutive
Images)
0.33 1.2 0.12 1.2
Relative
Accuracy (500
Samples NS)
0.42 3.0 0.09 3.0
Relative
Accuracy (500
Samples EW)
0.42 3.0 0.09 3.0

Error on 16 samples
Requirement: 0.75km total error

N/S error
on N/S
samples
E/W
error on
E/W
samples
E/W
error on
N/S
samples
N/S error
on E/W
samples
Channel Budget Budget Budget Budget
All
Channels
223m 76m 236m 146m

The tables actually refer to the data before re -sampling. Estimates provided by the Image
Processing Facility (IMPF) assume a contribution in terms of interpolation error in the order
of .29 km at SSP.

Note 1: The Absolute accuracy corresponds to the RMS value (over one image) of the error
between the actual position of a pixel in the image and its ideal position. It is verified using
landmark deviation measurements with respect to the ideal position (defined by a high -
accuracy digital map).

Note 2: The relative accuracy from image to image corresponds to the variation in the
geographical location of a pixel from one repeat cycl e to the next. It is a measure of the
“stability” of the image navigation and this criterion is especially important when tracking
displacement of features (like clouds) rather than geolocating them in the absolute sense. This
error is measured by tracking the displacement of landmarks from one image to the next.

<!-- source_page: 31 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 31 of 129

Note 3: The relative accuracy within an image (over 500 resp. 16 pixels) gives the variation
in the location error between two pixels that are separated by up to 500 (resp. 16) sampling
distances. This criterion can be considered as a measure of the local deformation within the
image. Currently, no direct methods for regular verification of these criteria are validated,
although functionality is foreseen.

Note 4: The specification figures (worst case for nominal image) given above will be
replaced with figures that correspond to nominally achieved quality once the S/C and SEVIRI
are better known and the image processing function is operational.

3.1.10 Interchannel Registration
The specified and expected registration errors for the same pixel positions in different spectral
channels are shown in the following figures. Here also, the figures might need to be updated
once the actual behaviour of the MSG S/C in orbit is better characterised. All channels are
registered to a common grid with the following accuracy:

Channel Groups Residual
Misregistration
Requirement (km)
Residual Misregistration
Budget (km)*
VNIR 0.6 0.45
Warm

(HRV +VNIR)
0.6 0.45
Window

(IR3.9/IR8.7/IR10.2/IR12.0)
0.6 0.45
Cold

(All except HRV and VNIR)
0.75 0.45
ALL 1.5 0.45

*This is comprised of two summed errors, arising from 1) error in the interpolation methods
used (0.27km) and 2) an error in the SEVIRI focal plane model (0.18km)

Note 1: Distances are at sub-satellite point (SSP).

Note 2: The grid of HRV images is such that 3x3 pixels of the HRV image are registered
to 1 pixel of the VIS/IR channels.

Note 3: The phenomenon of misregistration is mainly due to the thermo -elastic variations
within the SEVIRI (both between the cold & warm focal planes and to a lesser extent between
channels within a given focal plane). The misregistrations characterised on ground are of
limited value after the launch, due to its thermal and mechanical influences. Therefore, the onground processing is an auto-adaptive method that continuously re -estimates and corrects the
focal plane misregistration based on the newest observations taken from the image. It has a
typical integration time of one day, but shorter periods are considered following ecl ipse or
manoeuvre situations.

<!-- source_page: 32 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 32 of 129

3.1.11 Straylight Compensation Characteristics
The stray light performance of the SEVIRI instrument is generally speaking very good. Only
the solar channels (VIS06, VIS08, NIR16 and HRV) and the IR 3.9 channel are affected when
the Sun is close to the Field of View of the instrument. This is only the case for a few hours
around midnight during or close to eclipse season. Although the effect is largest for the solar
channels, the illuminated part of the Earth is minimal and hence the usefulness of the solar
channel data collected during this period is low. Since, the stray light dominates the image for
the solar channels and is complex in nature, no correction can be applied. In the IR 3.9 channel,
the effect is smaller and the Earth s ignal larger, a correction is normally applied based on the
angular distance between the image pixel direction and the direction towards the Sun.

3.1.12 Timeliness and Availability of Level 1.5 Image Data
Via the Dissemination Service, Level 1.5 image data of a given geographical area are available
to the users within 5 minutes from the time of acquisition by the satellite of this area (for users
having HRUS stations, 15 minutes in the case of users having LRUS stations). For users
accessing Level 1.5 data via ot her services, the timeliness is defined by the service (refer to
[EURD]).

Image of nominal quality, completeness, timeliness are provided by the Dissemination Service
with an availability of better than 95% [See EURD].

<!-- source_page: 33 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 33 of 129

4 STRUCTURE OF THE LEVEL 1.5 DATA
This section presents the general structure of the Level 1.5 data, showing graphically how the
data content is organised in ‘Records’. Please note that if information is searched on specific
areas of interest, but there is no familiarity with the Record conte nt, the help provided in
Chapter 5 may be more adequate.

4.1 Data Formats
Before the Structure of the Level 1.5 data is presented, it is important to note the following
aspects:

The native Level 1.5 data, as produced and distribut ed within the MSG Ground Segment, is
distributed as MSG Ground Segment packets. The actual data content of the Ground Segment
packets is either:
1. Level 1.5 Data Header, holding the ancillary data that is known at the start of the repeat
cycle.
2. Level 1.5 Image Line, comprising groups of image lines, with each group holding the scanlines for the 12 spectral channels (3 for HRV, and one for each of the other 11 channels).
This group is repeated (nominally) 3712 times.
3. Level 1.5 Data Trailer, holding the ancillary data that has been generated or only became
known during the repeat cycle.

Note: Depending on the capabilities of the service used to access the information, the user
may receive the image part of the Level 1.5 data in a structure that does not directly correspond
the ‘native format’ (i.e. the one presented in this document), but which is a derived one, such
as a continuous image array of a single spectral channel. The format of the Header and Trailer
information is however fixed.

Example: For the users receiving the data via the Dissemination Service, the image information
is grouped by 464 image lines in the so -called HRIT/LRIT Image Segment Files. The Level
1.5 Header and the Level 1.5 Trailer are disseminated as separate HRIT/LRIT files [MSI] called
"Prologue" (Level 1.5 Header) and "Epilogue" (Level 1.5 Trailer).

4.2 Detailed Level 1.5 Data Structure
The following figures present the structure of the Level 1.5 Data Header, the Level 1.5 Image
Lines, and the Level 1.5 Data Trailer.

Note that the following figures have been prepared using ‘hyperlinks’. To use these to their
full extent on the electronic version of this document, enable the Web Toolbar in MS -Word
(offered with version 7 onwards). Any underlined text which causes the cursor to change into
a ‘pointing finger’ is a hyperlink that can be used to navigate to more detailed descriptions.
When the cursor is positioned over a Record name of interest, click the left mouse -button to
jump to the document section where the Record is described in detail. The ‘Back’ and
‘Forward’ arrows on the Web Toolbar allow the user to move between hyperlinks and
associated texts.

<!-- source_page: 34 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 34 of 129




LEVEL 1.5 DATA HEADER 15HEADERVersion no further decomposition

SATELLITE STATUS Satellite Definition
Satellite Operations
Orbit
Attitude
SpinRateatRCStart
UTCCorrelation

IMAGE ACQUISITION PlannedAcquisitionTime
RadiometerStatus
RadiometerSettings
RadiometerOperations

CELESTIAL EVENTS CelestialBodiesPosition
RelationToImage

IMAGE DESCRIPTION ProjectionDescription
ReferenceGridVIS_IR
ReferenceGridHRV
PlannedCoverageVIS_IR
PlannedCoverageHRV
Level1_5ImageProduction

RADIOMETRIC PROCESSING RPSummary
Level1_5ImageCalibration
BlackBodyDataUsed
MPEFCalFeedback
RadTransform
RadProcMTFAdaptation
StraylightCorrection

GEOMETRIC PROCESSING OptAxisDistances
EarthModel
AtmosphericModel
ResamplingFunctions

IMPF CONFIGURATION OverallConfiguration
SUDetails
WarmStartParms


Figure 13 – Structure of Level 1.5 Header

<!-- source_page: 35 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 35 of 129





15VIS/IRLINE LineSideInfo no further decomposition
LineData no further decomposition

15HRVLINE LineSideInfo no further decomposition
LineData no further decomposition

Figure 14 – Structure of Level 1.5 Image Lines






LEVEL 1.5 DATA TRAILER 15TRAILERVersion Not further decomposed

IMAGE PRODUCTION STATS SatelliteId
ActualScanningSummary
RadiometerBehaviour
ReceptionSummaryStats
L15ImageValidity
ActualL15CoverageVIS_IR
ActualL15CoverageHRV

NAVIGATION EXTRACTION
RESULTS
ExtractedHorizons
ExtractedStars
ExtractedLandmarks

RADIOMETRIC QUALITY L10RadQuality
L15RadQuality

GEOMETRIC QUALITY AbsoluteAccuracy
RelativeAccuracy
500PixelsrelativeAccuracy
16PixelsRelativeAccuracy
MisregistrationResiduals
GeometricQualityStatus

TIMELINESS AND COMPLETENESS Timeliness
Completeness


Figure 15 – Structure of Level 1.5 Trailer

<!-- source_page: 36 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 36 of 129

4.3 Rationale for the Level 1.5 Data Content and Structure
The definition of the Level 1.5 data, both from structural and content points of view, was driven
by a number of requirements or constraints but also by the goal to satisfy a large variety of
users and potential ap plications. The rationale for the data structure/data content is presented
here.

Stringent Timeliness Requirements & Real -time Product Extraction . The Level 1.5 data
structure was adapted to the real-time extraction of meteorological products and to the stringent
timeliness requirements. This resulted in the following:
 The selected structure with Header / Image Data / Trailer.
 A spectral channel -interleaved format allowing parallel transmission of all 12 spectral
channels.
 The Header data content is fully describing the characteristics of the image data to follow,
allowing to prepare the real-time meteorological processing.
 A line-by-line validity information is provided together with the image data, allowing realtime data acceptance by the subsequent meteorological processing.
 The Trailer data content corresponds to all the side -information that can only be derived
after the completion of the image (e.g. actual Level 1.5 image quality, summary statistics).

Standardised Projection . In order to comply with the internationally accepted LRIT/HRIT
Global Specification [GS], the projection used for the Level 1.5 data is the geostationary
projection defined therein, allowing minimum distortion of the image data.

Full Calibration Information . With a high -accuracy imaging system, the accuracy and
completeness of the calibration information plays a fundamental role. The Level 1.5 data
provides the users of the data with complete calibration information.

Ancillary Information to support/allow/promote Product Extraction. The future MSG system
will be the basis for the generation of an entire set of new meteorological products. The Level
1.5 data plays a central role in this system, and it is important that the image data is provided
with sufficient ancillary information to promote its widespread use for product extraction. As
an example, the following information is provided (see following sections for more details):
Sun and Satellite exact positions during image acquisition, full calibration information, detail
of all transformations actually applied to the pixel values, complete quality and validity
information etc. Note that this amount of very detailed side information can be distributed to
the users without noticeable impact on the transmission channel usag e, as its volume is very
small compared to the size of the complete image data.

Operational Flexibility. The structure of the Level 1.5 data includes many ‘self -describing’
features and this, coupled with the composition of the Header data, allows flexibi lity in the
execution of operations (like e.g. reduced scanning with faster Repeat Cycles, scanning
start/stop absolute time, etc…).

Historical Reprocessing Capability. This is due a EUMETSAT-internal constraint, allowing to
reprocess the image data (from Level 1.0 to 1.5) during operations if, for example, real -time

<!-- source_page: 37 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 37 of 129

image processing failed or if subsequent system improvements are desired to be applied to
older datasets. To facilitate reprocessing, the initial conditions for the processing are forming
part of the Level 1.5 Header.

Visibility of Actual Image Quality . Full details on the actual image quality (both radiometric
and geometric) derived by the EUMETSAT real -time image quality assessment function is
provided together with the Level 1.5 data, allow ing the data user to characterise the image
information used for the derivation of products.

<!-- source_page: 38 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 38 of 129

5 LOCATING INFORMATION IN LEVEL 1.5 DATA
The purpose of this section is to provide the user with a fast guide for finding information in
this document related to the most relevant areas of interest. High-level information for each of
these areas of interest is provided below together with a pointer to the subsequent chapters
where the details can be found.

5.1 Where to Find Image Size and Projection Information?
The Header of the Level 1.5 data provides all necessary data defining the size and projection
of the Level 1.5 image. This information is provided in the Image Description Record (Section
6.1.4) of the Header. This information applies only to the corresponding image data and is
updated for every image. This provides self -description of the image data in e.g. the case of
reduced Earth scanning with shorter than nominal repeat cycles.

Related information. the Header Record Image Acquisition (Section 6.1.2) provides the full
details of the commanded acquisition of the corresponding Level 1.0 data. The Trailer Records
Image Production Stats (Section 6.3.1) provides the statistics on the actually performed Level
1.0 image acquisition and Level 1.5 generation.

5.2 Where to Find Image Calibration Information?
Providing accurate and unambiguous calibration information to the data users is one of the
main objectives of the development and operation of the MSG system. For this reason a
sophisticated calibration approach has been defined and the results are made available to the
users in an unambiguous manner.

The Level 1.5 image data being provided to the users are corrected for non -linearity in the
detector response, for differences in the detector response within a given channel, and are
represented as 10 bit data with the linear (slope, offset) relation between binary counts and
physical radiance bei ng unambiguously defined in the Header Record
Level_15ImageCalibration (Section 6.1.5).

Related Information. For users wi shing full visibility of the way the provided calibration
information is derived within the MSG System, the following additional information is
provided:
 All data acquired by the instrument during blackbody viewing that are used by the
processing are provided in the Header Record BlackBody Data Used (Section 6.1.5).
 The calibration feedback resulting from either vicarious methods or from the calibration
monitoring function are provided in the Header Record MPEFCalfeedback (Section 6.1.5).
 The details of the look -up table used for transforming the Level 1.0 counts into the Level
1.5 radiometric data representation are provided for each detector in the Header Record
RadTransform (Section 6.1.5). This information allows to fully relate the Level 1.5 data to
the Level 1.0 data.

<!-- source_page: 39 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 39 of 129

5.3 Where to Find Image Radiometry Information?
The radiometric quality of the image data has clearly been given careful attention during the
definition of the MSG System. For this reason the Level 1.5 data includes numerous
information on this aspect:
 The H eader Record Image Acquisition (Section 6.1.2) provides all details about the
radiometer settings (Gains, offset, etc.) actually u sed for the acquisition of the Level 1.0
data. In addition, the radiometer status information is provided, identifying any potential
abnormalities in the acquisition process.
 The Header Record Radiometric Processing (Section 6.1.5) provides all the details of the
transformations performed between the Level 1.0 and the Level 1.5 data from a radiometric
point of view. This include s the calibration information (see above) the MTF adaptation
that was performed and the straylight compensation that might have been applied.
 The Image Records 15VIS/IR Line (Section 6.2.1) and 15HRV Line (Section 6.2.2) are
providing for every spectral channel an d per line of the Level 1.5 data, the information
about the radiometric validity of this line. This allows the Level 1.5 data users who intend
to perform data acceptance on a line-per-line basis to implement such a mechanism.
 The Trailer Record Radiometric Quality (Section 6.3.3) provides all extracted Radiometric
quality information for both the Level 1.0 (at detector level) and L evel 1.5 (on a channel
basis). This includes typical measures like Signal Noise ratios, histograms, entropy, etc.).

5.4 Where to Find Image Geometrical Accuracy Information?
The geometrical accuracy of the processed image is clearly an important aspect of the Level
1.5 data. The following information is provided:
 The Trailer Record Geometric Quality (Section 6.3.4) provides the summary results of the
Geometric Quality Assessment function, for the different types of image accuracies that are
considered (Absolute, Relative image to image, Relative within an image). This Geometric
Quality Assessment function is based on the recognition and correlation of numerous
landmarks and has the purpose to indicate the quality of the Level 1.5 image data being
produced. This is also the tool used by EUMETSAT to optimi se the image quality during
the operational lifetime of the mission.
 The Header Record Geometric Processing (Section 6.1.6) describes the values used within
the processing models (distances of detectors to the optical axis, The parameters of the
Earth model, the parameters of the atmospheric model, and the resampling function being
used.
 The Image Record 15VIS/IR Line (Section 6.2.1) and 15HRV Line (Section 6.2.2) are
providing for every spectral channel and per line of the Level 1.5 data, information about
the geometric validity of this line. This allows the Level 1.5 data users who intend to
perform data acceptance on a line-per-line basis to implement such a mechanism.

<!-- source_page: 40 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 40 of 129

5.5 Where to Find Inter-channel Registration Information?
A frequently expressed concern of the users is the quality/accuracy of the registration of image
information between the different spe ctral channels. Information is provided in the Level 1.5
data in two manners:
 The Header Record OptAxisDistances (Section 6.1.6) g ives the most up -to-date and
accurate knowledge of the relative positions of the detectors in the focal plane of the
instrument (“focal plane layout”). This is a useful information for a user wishing to know
what are the differences in Line Of sight betwee n any two channels / detector during the
acquisition of the Level 1.0 data (if e.g. he/she wishes to relate Level 1.0 data acquired by
different channels). In it important to note that these figures are the result of a constant reestimation of the actual focal plane positions and are more accurate and relevant than on -
ground characterised values.
 The Trailer Record MisregistrationResiduals (Section 6.3.4) provides the results of the
Geometric Quality Assessment function with respect to the residual misregistration
between channels in the Level 1.5 data. Note that the uncertainty radius on these
measurements is much higher th an the uncertainty on the focal plane layout for the
following reason: the focal plane layout is derived for the accumulation of many
measurements over a situation -adaptive period of time, whereas the misregistration
residuals are only measured on the current image!

5.6 Where to Find Pixel and Data Representation Information?
The Level 1.5 image pixels are represented as 10 bit data, the relation between the digital value
and physical units being as defined in the above section on calibration. Note that depending on
the data service, the user might receive image data that are rounded to 8 bits. All the other
information remains the same.

The representations used for the other types of data (Integers, Reals, Time codes, etc.) are all
described in detail in [GSDS].

5.7 Where to Find Image Quality and Validity Information?
This area covers the following:
 Geometric Quality: please see “Where to find Image Geometrical Accuracy Information?”
(Section 5.4).
 Radiometric Quality: please see “Where to find Image Radiometry Information?“ (Section
5.3).
 Line-by Line Validity of the image data. For each line of the Level 1.5 data, validity
information is provided within the Records LineSideInfo (VIS/IR) (Section 6.2.1) and Line
Side Info (HRV) (Section 6.2.2). This information can be used as a criterion for the data
acceptance within a meteorological product processing function.
 Timeliness and Completeness statistics can be found in the Trailer Record
TimelinessAndCompleteness (Section 6.3.5).

<!-- source_page: 41 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 41 of 129

5.8 Where to Find Image Acquisition & Scanning Conditions?
For Users wishing to know the exact conditions of the acquisition of the Level 1.0 image (on
which the processing to Level 1.5 is based upon) by the instrument, there are two major sources
of information:
 The Header Record Image Acquisition (Section 6.1.2) provides all the Radiometer settings
and parameters that were active for the acquisition of the Level 1.0 image by the instrument
and considered by the Image Processing function. In particular the scanning information is
available there. Note that if one is interested in the coverage used for the Level 1.5 image
the Header Record PlannedCoverage VIS_IR (Section 6.1.4) and PlannedCoverage HRV
(Section 6.1.4) are the best source of information.
 For the specific information related to the acquisition of the BlackBody data during the onboard calibration, this information can be found in the Header Record BlackBodyDataUsed
(Section 6.1.5).

5.9 Where to Find Navigation Information?
Image navigation can be understood in several ways. We identify here where to find the related
information for the different meanings of this term:
 If Navigation is understood as the way the image processing implements the geometrical
transformation from Level 1.0 data to the Level 1.5 data, the following information is
provided in the Level 1.5 data:
1. In the Header Records Orbit /Attitude / SpinRateatRCStart (Section 6.1.1) the Flight
Dynamics and satellite information used for the processing are provided.
2. In the Header Record ProjectionDescription (Section 6.1.4) the projection applied by
the resampling function is defined.
3. In the Header Record Geometric Processing (Section 6.1.6) all the parameters / state
of the mai n models used within the Image Processing function to derive the
deformation to be applied to the Level 1.0 data in order to derive the Level 1.5 data are
provided.
 If Navigation is meant as the information required to relate any Level 1.5 image data to the
geographical coordinates, then this information can be found in Section 3 of this document
and in [GS].
 Finally, the following information is also made available th at can be useful in the context
of navigation:
1. The Trailer Record Navigation Extraction Results (Section 6.3.2) is prov iding all the
image-based measurements (horizons, landmarks, and stars) that are performed by
IMPF in order to support the estimation of Orbit & Attitude.
2. Refer to Section 3 of this document for all aspects related to the accuracy of the
navigation, i.e. to the geometric image accuracy.

<!-- source_page: 42 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 42 of 129

5.10 Where to Find Satellite and Celestial Body Positions?
It was generally found important to document within the Level 1.5 both the actual position of
the satellite but also of relevant celestial bodies during the image acquisition. The reasons are
twofold: the position of Sun relative to the S/C for a given geographical position ca n be
important for the subsequent processing, e.g. involving bi-directional reflectance. Further, the
presence of celestial bodies close to or within the field of view of the Level 1.0 image might
have an impact on the image quality that is analysed by the Image Processing function.

The Header component record Satellite Status (Section 6.1.1) provides all the information on
the position of the S/C with respect to the Earth at the moment of image acquisition.

The Header component record Celestial Events (Section 6.1.3) provides all the information on
the position of Sun, Moon, Stars and provides the expected impact on the image data.

<!-- source_page: 43 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 43 of 129

6 DATA CONTENT SUMMARY PER RECORD
Note that the headings for the following subsections correspond to the names of the highest -
level component Records in the structure detailed in Section 7 of this document.

6.1 Level 1.5 Header Summary
The purpose of the Level 1.5 header which accompanies Level 1.5 imagery data is to supply
ancillary information which is needed by the end -user for interpreting the image data and
processing it further.
There is one header for each repeat cycle and it is produced, as its name implies, before the
image data in each repeat cycle. The information it provides is that which is known at the time
of the start of the repeat cycle. Information which becomes available at a later time during the
repeat cycle is provided in the complementary Record, the Level 1.5 trailer, which is generated
following the image data. This complementary Record is described later in the present chapter
in Section 6.3 ‘Level 1.5 Trailer’.
The header comprises a number of component items which hold information relevant to the
topics indicated below:

Topic Component
Type
Details of Component
Header Version Field This field identifies the version of the
header
Satellite Status Record See corresponding subsection
Image Acquisition Record See corresponding subsection
Celestial Events Record See corresponding subsection
Image Description Record See corresponding subsection
Radiometric Processing Record See corresponding subsection
Geometric Processing Record See corresponding subsection
IMPF Configuration Record See corresponding subsection
These topics are presented in the sub -sections below, in terms of the general data content and
the relation that the information has to the image data.
Throughout these sub -sections, the data is described as though the users are receiving Level
1.5 image data via dissemination (in near real-time). The header, for example, is described in
terms of it being received in advance of the imagery data which is yet to be acquired, processed
and disseminated. Users who receive Level 1.5 data ‘after the event’, f or example via offline
Data Services such as retrieval from the EUMETSAT archive, should remember this when
reading the text.

<!-- source_page: 44 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 44 of 129

6.1.1 Satellite Status Record Summary
This first record of the Header provides the user with information on the status of the satellite
which is producing the image. Along with the satellite’s identification, information is given
concerning the position of the satellite, its operational status, the last operation executed, the
next operation planned for it, and the satellite’s on-board time.

The satellite’s ‘onboard time’ can be correlated with ‘Universal Time’ by using the UTC -
correlation information provided, in order to match the satellite timestamps with the absolute
time on the ground.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.2.1 Satellite Status Record.

Component Record Description
SatelliteDefinition Constituent Data. Provides the identification of the satellite
which produced the image, the longitude at which it is
nominally stationed (this being the reference point from
which the Orbit deviation is computed), and its operational
status. Note that the longitude of the S/C should not be
confused with the one used for the projection of the Level
1.5 data.

Usage. To identify the imaging satellite and to learn its
current status.

Data Constancy. If the satellite is moved to a different
geostationary location, or if its operational status changes,
information in this Record will change. Examples of the
latter are when a satellite enters operational use after
commissioning is completed, or when a d econtamination is
performed.

If there is a change in the imaging satellite used (e.g. if a
switch to a spare satellite is effected for the prime imaging
mission), this will also be reflected here.

<!-- source_page: 45 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 45 of 129

Component Record Description
SatelliteOperations Constituent Data. Information concerning the last and next
manoeuvres of the satellite which are likely to have an
impact on image quality.

Usage. Image quality impact is to be expected in the 3 -hour
period following a manoeuvre. Advance notice of the next
manoeuvre allows the user to take this into account when
planning his usage of the images. Knowledge that a
manoeuvre took place in the recent past can help explaining
deviations in the geometrical image quality (that will be
reflected in the measured geometrical quality figures: see
Geometric Quality).

Data Constancy. Manoeuvres that have taken place (or will
take place) in the last (next) 48 hours are presented in this
component Record. Attitude manoeuvres are conducted
approximately every 2 months, as the need arises. Other
manoeuvres (station keeping, spin -up) are generally
performed as infrequently as possible to make best use of the
available propellant and optimise the S/C lifetime.

<!-- source_page: 46 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 46 of 129

Component Record Description
Orbit Constituent Data. Provides the orbit offset of the satelli te
relative to its nominal position (as defined by the nominal
longitude on the geostationary orbit). This is expressed as (X,
Y, Z) plus velocities in an Earth -fixed frame. The
information provided covers a defined period of time from
past to future and c onsists of a set of polynomials which
allow to obtain the position at any moment in time. Cartesian
coordinates are obtained in a frame as defined in Section 7.
The information is the most accurate available in the MSG
Ground Segment, and is exactly the information used by the
processing to generate the Level 1.5 image data. The
accuracy figures are currently specified to be:

Better than 2000m/2000m/500m in the
longitude/latitude/Altitude directions for the absolute
accuracy.

Better than 300m/300m/100m in the
longitude/latitude/Altitude directions for the maximum
difference between two successive orbit determinations.

Note: As the orbit accuracy is of high importance for the
image navigation, efforts are spent to get the best possible
accuracy: In operations, the above figures (although
sufficient to achieve nominal image quality) will need to be
updated with the actually achieved accuracies.

Usage. Allows to define the position of the imaging satellite
relative to it s nominal position as a function of UTC time
with the highest possible accuracy. The usage could be for
GERB processing, accurate bi -directional reflectance
calculations (in combination with Sun position), etc.

Data Constancy. Updated in case new orbit in formation is
received and (after validation) used by the image processing
function. This can be as frequently as every repeat cycle, but
in practice it is influenced by the frequency of update in
operations.

<!-- source_page: 47 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 47 of 129

Component Record Description
Attitude Constituent Data. Provides the attitude of the MSG imaging
satellite. The information covers a defined period of time
extending from past to future. After interpolation, (X, Y, Z)
coordinates of the spin axis in an Earth -fixed frame are
obtained that give the actual satellite attitude at any UTC
time within this period. The information is the most accurate
available and is exactly the information used by the
processing to generate the Level 1.5 image data. The
accuracy of the Attitude information is specified to be:

Better than 0.0005 degrees in absolute sense.

Better than 0.0002 degrees for the difference between two
successive attitude determinations.

As for the Orbit, efforts are spent to optimise the accuracy.
In operations, the above figures are to be replaced by the
achieved accuracy.

Usage. All applications requiring the satellite attitude
information, either for investigations or for processing
purpose. GERB processing can be an example.

Data Constancy. Updated as frequently as every repeat
cycle. The update rate is higher than the one for the orbit
information. However, only one attitude dataset is used per
repeat cycle, and this is the one included in this record.

<!-- source_page: 48 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 48 of 129

Component Record Description
SpinRateatRCStart Constituent Data. Provides the spin -rate of the MSG
imaging satellite at the start of the repeat cycle with a high
accuracy. The accuracy is expected to be better than 2 in
100,000 (at the moment of the Repeat Cycle start). Note that
during the Repeat Cycle, the spin rate w ill deviate from this
figure due to the mirror motion and in case of eclipse, due to
the thermal effects. The amplitude of the deviation to be
expected will be provided after commissioning of the S/C
and behaviour characterisation in actual eclipses.

Usage. The exact spin-rate can be computed at any moment
from the 1.0 data by processing the Start -Of-Line datations.
It was nevertheless found useful to provide the spin -rate at
one characteristic moment in time for the information of the
users. Usage of this information should take into account the
operational situation, as spin -up manoeuvres or eclipse
situations can affect the representativity of the value for the
remainder of the Repeat Cycle.

Data Constancy. Updated every repeat cycle.

UTCCorrelation Constituent Data. Are all information required to relate the
On-Board Time to the Universal Time Coordinated (UTC).
The information covers a defined time period from past to
future and is defined as polynomial coefficients of UTC =
f(On-Board time).

Usage. All applications that need to relate On -Board Time
information provided by the MSG Satellite to UTC. An
example is processing of GERB data that might require
accurate conversion of Start -Of-Line Datation to UTC
transformation. Other examples are investiga tions or
historical reprocessing, where the information is critical.

Data Constancy. Can be updated once per repeat cycle. The
actual rate can be less frequent and depends on operational
aspects. The information is exactly the one that is used for
the processing of the Level 1.5 image of this repeat cycle.

<!-- source_page: 49 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 49 of 129

6.1.2 Image Acquisition Record Summary
This component record of the header holds information that has been used by EUMETSAT’s
image-processing system for the processing of the image data which the header precedes.

The information includes time delimiters for the start, end -of-forward-scan and end of the
repeat cycle, and states and settings of the SEVIRI radiometer instrument. The majority of the
values have been extracted from the satellite’s housekeepin g telemetry prior to the start of
processing.

The status of the radiometer channels is given, along with various settings related to previous
operations of the instrument such as gain changes, decontamination and blackbody calibration.

The following tab le gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.2.2 Image Acquisition Record.

Component Record Description
PlannedAcquisitionTime Constituent Data. These are the actual start-time of the
repeat cycle, the planned time of forward scan end, and the
planned Repeat Cycle end-time. Note: this is due to the fact
that the actual end-times are not known (did not occur) at the
moment the Header was created. – the actual times will only
be known when real-time processing has completed, and thus
they are held in the trailer. The planned information is
generally so accurate (to less than 0.6 seconds) that it is
sufficient for the Image Processing and therefore is probably
sufficient for all derived applications.

Usage. To relate image data to the time & date of
observation. In the case of reduced scans, allows to identify
the duration of the repeat cycle.

Data Constancy. Changes with each image.

<!-- source_page: 50 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 50 of 129

Component Record Description
RadiometerStatus Constituent Data. Status indicators for all channels and all
detectors of the radiometer, showing which are switched
on/off within the SEVIRI instrument.

Usage. In determining the status of the radiometer during
image acquisition.

Note 1: Users will normally not receive images which have
been scanned by the radiometer operating in ‘test mode’
(unless specifically requested) – this information is generally
for EUMETSAT’s reference only.

Note 2: The information only relates to the SEVIRI status
during Level 1.0 image acquisition This status information
should not be confused with the presence o r not of given
image channels within the Level 1.5 data. For Level 1.5
channel information, the User should consider first the
Record Level 1_5 Image Production.

Data Constancy. The status of each of the radiomet er
channels is nominally ‘on’, but during operations it might
happen (e.g. during decontamination) that channels are
switched “off”. Similarly for the status of each of the
detectors. The status applies to the complete Repeat Cycle
and can be updated each Repeat Cycle.

<!-- source_page: 51 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 51 of 129

Component Record Description
RadiometerSettings Constituent Data. Provides the basic parameters of the
radiometer that apply for the acquisition of the repeat cycle
and are used for the processing of the image. Of particular
interest are the radiometric gains and offset settings used for
Level 1.0 acquisition that will be used in the on -ground
processing to derive (and calibrate) the Level 1.5 data.

Also contained in this Record is the group of ‘Operation
Parameters’ which shows the commanding of the radiometer
just prior to the start of the repeat cycle (these commanded
values are applicable to the Repeat cycle the Header belongs
to).

Usage. Not only for internal operations of the Ground
Segment, but also for system calibration activities that
require the exact know ledge of the actual
gains/offsets/temperature that were applicable during the
acquisition of the image. Required also for EUMETSAT -
internal activities like historical reprocessing.

Data Constancy. Detector gains are set according to
radiometer channel to make best use of the dynamic range.
In theory, gains can change from one repeat cycle to the next,
but nevertheless stay constant for the duration of a repeat
cycle.

Operation parameters can also change for each repeat cycle,
but many of them will be con stant in operation (unless
reduced scans are exercised for example).

<!-- source_page: 52 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 52 of 129

Component Record Description
RadiometerOperations Constituent Data. Information to show the time / duration /
scope of the last gain -change, the last (or current)
decontamination and the last blackbody calibration.
Temperatures of the cold and warm focal planes are also
given.

Usage. Activities such as decontamination and blackbody
calibration, which affect the operation of the radiometer,
have an influence on the image quality. The information here
can help the u nderstanding of variations in the image. In
addition, the information is important for the monitoring of
the calibration.

Data Constancy. The data provided here is the latest form
of the information available within the MSG Ground
Segment, and is updated as soon as newer information
becomes available.

<!-- source_page: 53 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 53 of 129

6.1.3 Celestial Events Record Summary
This component record of the header holds information related to the position of the pertinent
celestial bodies (i.e. the Earth, moon, sun and stars) and to the events which have effected the
image, such as eclipses and appearances of bodies in the satellite’s Field Of View (FOV).

Ephemeris information is mainly organised as time delimiters for the period concerned, and a
set of coefficients for the Chebychev polynomials which describe the positions of the Earth,
moon, sun and stars. For details on the coordinate frame and the polynomial com putation see
Section 7.2.3 Celestial Events Record.

The information concerning possible effect on an image includes the start and end times of
eclipses, the type of eclipse, indicators for bodies either visible in the image or close to the
satellite’s FOV and an indication of the impact that might occur on image quality (e.g. horizons
made indistinct by low illumination or stray light altering the radiometric quality within the
Earth disc).

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.2.3 Celestial Events Record.

Component Record Description
CelestialBodiesPosition Constituent Data. Defines the position of the main celestial
bodies as a function of time over a specified period of
validity (covering past to future) including the current
Repeat Cycle. The celestial bodies are the sun, the moon and
an identified small set of bright stars. The positions of stars
are primarily used for EUMETSAT -internal purposes, as a
support for navigation.

Usage. The information is of interest to any user trying to
relate the observation to the actual position of the sun / moon.

The position of the sun is useful in defining the illumination
situation for bi -directional reflectance computations (in
conjunction with satellite longitude and orbit data), but also
in defining whether flare and stray-light may affect the image
(also see the next Component Record).

The position of the moon is used to define whether or not the
moon is within the field of view for the Level 1.0 image. The
moon image will be masked out by the space -mask applied
to the Level 1.5 image data, but if desired, it can be extracted
(via a suitable data service) from the corresponding Level 1.0
data, e.g. for visible-channel calibration purposes.

Data Constancy. The data can be updated as frequently as
once per repeat cycle. In practice, a lower rate of update will
occur, depending on operational needs. The information is

<!-- source_page: 54 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 54 of 129

Component Record Description
the latest available and is the one used for the image
processing function.

RelationToImage Constituent Data. Provides the result of the analysis
performed by the image-processing function on the positions
of the celestial bodies. This covers the occurrences of
eclipse, pre-eclipse, moon or sun in (or close to) the field of
view w.r.t. the Level 1.0 data and the expected effect on the
image data.

Usage. Mainly to determine whether the image data may be
impacted or not by an eclipse or similar event. It also
provides information on the type of expected impact. This
information is useful for e.g. users wishing to find images
that include the sun or the moon.

Note 1: only Level 1.0 data contains such image data,
however – as Level 1.5 normally has the space area masked
out.

Note 2: Celestial bodies that are identified as “close” to the
Field Of View (FOV) are not actually visible in the Level 1.0
image but are sufficiently close to potentially impact
radiometry, e.g. via straylight.

Note 3: the type of impact is only estimated in the He ader
based on calculated positions. Please consider that the
actually measured image quality (radiometry & geometry) is
only provided in the Trailer.

Data Constancy. Eclipses are frequent phenomena that
affect the satellite every night (for a period of up to 80
minutes around midnight) during several weeks in spring and
in autumn. The information here is updated every repeat
cycle to indicate the conditions for the coming image
acquisition.

<!-- source_page: 55 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 55 of 129

6.1.4 Image Description Record Summary
This component record of the header holds information which describes the image in terms of
its projection, reference grids (one for HRV channel data, another for all other channels),
planned-coverage mapping (one set of parameters for HRV channel data, another for all other
channels), and an indication of the spectral channels for which it was foreseen to receive and
process the image data. The information can be used to geographically locate the observed
image. Please refer to Section 3.1.4.

The reference grids are defined in terms of numbers of lines and columns, grid -step sizes (in
km equivalent Sub-Satellite Point) in the directions of lines of columns, and an ind ication of
the position of the grid origin. One grid is present for VIS and IR data, another for HRV. The
two grids are defined such that 3x3 HRV pixels are aligned with one VIS/IR pixel.

The planned -coverage mapping parameters include values for the plan ned southern and
northern lines, the planned eastern and western columns. One set of parameters are present for
VIS and IR data, another set for HRV. Note that for HRV, due to the capability to split the
image in two parts (a Southern and a Northern) with different E-W positions (see Section 3.1.2),
the planned coverage description is more complex.

The information about the planned production of the Level 1.5 data in cludes the indication if
the processing is configured to generate or not the Level 1.5 image for any given channel.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.2.4 Image Description Record.

<!-- source_page: 56 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 56 of 129

Component Record Description
ProjectionDescription Constituent Data. Indicates the mathematical projection
which will be used to generate the Level 1.5 data, and the
longitude of the Sub-Satellite Point (SSP) that is used for the
projection. Note: it is not foreseen currently to use other
projections than the Geostationary one (see Section 3.1.4)
The technical/mathematical details of the projection are fully
defined in [GS].

Note: The longitude of SSP defines from which point the
projection is applied and should not be confused with the
nominal satellite position (the longitude which is held in the
Record ‘ Satellite Status ’). The ground processing is
theoretically able to receive images acquired by a satellite
located at any longitude and to process these to Level 1.5
using any (different) longitude for the projection. It is
however of limited interest if the difference between the two
longitudes is too high (e.g. above 10 degrees), as distortions
appear and the actually useful Level 1.5 image surface is
reduced.

Usage. This information, combined with the grid
information, is used for relating pixels of Level 1.5 data to
Earth coordinates (longitude and latitude).

Data Constancy. The information is un likely to be
modified, but it is foreseen that the longitude at SSP may be
changed (infrequently) if the imaging satellite is moved to a
position far away from the nominal 0° longitude in order to
cover a different area of the globe.

ReferenceGridVIS_IR Constituent Data. Defines the grid used for the 11 VIS and
IR channels which have 3-km pixel spacing. The size of the
nominal Level 1.5 image area (in lines and columns), the
origin of the grid and the actual pixel spacing (in line and
column directions) are provided.

Usage. Facilitates the relating of pixel positions to Earth
locations for the VIS and IR channels when combined with
the projection information.

Data Constancy. Unlikely to change.

<!-- source_page: 57 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 57 of 129

Component Record Description
ReferenceGridHRV Constituent Data. Defines the grid used for the High
Resolution Visible channel which has 1 -km pixel -spacing.
The size of the nominal Level 1.5 image area (in lines and
columns), the origin of the grid and the actual pixel spacing
(in line and column directions) are provided.

Usage. Same as for ReferenceGridVIS_IR, except for the
HRV channel.

Data Constancy. Unlikely to change.

PlannedCoverageVIS_IR Constituent Data. Defines the coverage that is planned for
the VIS and IR channels of the Level 1.5 image to come,
w.r.t. the reference grid for those channels. For a nominal
image, the coverage will be identical to the grid. For reduced
scans, the information defines which subset of the Level 1.5
grid is actually generated. Note that the actual coverage is
given in the Level 1.5 trailer. See also Section 3.1.2.

Usage. For advance knowledge of the intended Level 1.5
coverage for the VIS and IR channels - particularly of value
in the case of reduced scanning.

Data Constancy. Can change from one repeat cycle to the
next, but in practice should remain constant unless reduced
scans are exercised.

PlannedCoverageHRV Constituent Data. HRV-specific data is similar to that for
‘PlannedCoverageVIS_IR’, but the number of parameters is
extended to define the bounds of the two possible areas of
coverage (northern part and Southern part) which may result
from the alternative HRV coverage mode being operated
(see also Section 3.1.2). Note that the actual coverage is
given in the Level 1.5 trailer.

Usage. For advance knowledge of the intended Level 1.5
coverage for the HRV channel - particularly of value in the
case of HRV alternative coverage mode.

Data Constancy. Can change from one repeat cycle to the
next, but in practice should remain constant unless different
than nominal scans are exercised (reduced scans or HRV
alternative coverage).

<!-- source_page: 58 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 58 of 129

Component Record Description
Level1_5ImageProduction Constituent Data. Gives the directions of line - and pixelgeneration of the Level 1.5 image data, and also identifies
the channels for which Level 1.5 data will be generated
(nominally all 12 channels).

Usage. To allow the user of the data (or more probably, the
automated system receiving the data) to handle it in an
appropriate manner. Storage, display and possibly
processing functions will need to take account of the
production information i n order to perform their actions
correctly.

Data Constancy. It is expected that the line - and pixel -
generation directions will be set to ‘South-North’ and ‘East-
West’ respectively, and will remain so permanently. It is also
expected that Level 1.5 data wi ll be produced for all 12
radiometer channels, except for when special operations
(such as a radiometer decontamination) is performed. In the
event of a malfunction of one or more of the channels, then
it may be planned not to derive Level 1.5 data for par ticular
channel(s) and the relevant indicators will then reflect this.
Moreover, it is indicated whether the image is representing
effective or spectral radiance.

<!-- source_page: 59 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 59 of 129

6.1.5 Radiometric Processing Record Summary
This component record of the header provides information related to the radiometric data
processing applied to the Level 1.0 data but also information related to the calibration of the
radiometer. This latter involves consideration of the self -emitted radiance of radiometer
elements which affect the radiometer’s infra-red measurements.

The information includes all ‘Black Body’ data last acquired (extracted from the SEVIRI Level
1.0 image data, and the housekeeping telemetry) that are used in the calibration process, the
data which has been derived fr om it, and calibration feedback from EUMETSAT’s
meteorological product extraction facility. Data for the Modulation Transfer Function and
‘stray-light’ corrections is also included.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.2.5 Radiometric Processing Record.

Component Record Description
RPSummary Constituent Data. Summarised details of radiometric
processing per radiometer channel, indicating whether or not
various aspects of radiometric processing have been applied
or not to the data for each of the channels.

Usage. The sum mary indicators will show which of the
detailed data following ‘RPSummary’ is valid to be used,
depending on whether the relevant functions of radiometric
processing have been applied (this per spectral channel). As
can be seen from the component Records described below in
this table, a large amount of detailed information is provided
to allow the user to determine the scope of radiometric
processing.

Data Constancy. Nominally, the summary indicators will
always show that all radiometric processing functi ons have
been applied for all channels for this Repeat cycle. The
indicators may vary from one Repeat cycle to the next, as a
function of the operational situation (e.g. if a BlackBody
calibration provided or not new values, if the Calibration
feedback was received or not, etc.).

<!-- source_page: 60 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 60 of 129

Component Record Description
Level1_5ImageCalibration Constituent Data. Calibration information for Level 1.5
data, for each of the 12 radiometric channels, comprising
‘slope’ coefficients and ‘offset’ constants which have been
extracted from either on-board calibration data or from other
sources such as MPEF calibration feed back data. It is the
most accurate/up to date calibration information available
within the MSG Ground Segment.

Important Note: This information is the primary calibration
information that should be used when relating the Level 1.5
pixel count values to the physical radiance units.

Note: the provision of one set of Slope/Offset coefficients
per channel is sufficient for accurate calibration as the Level
1.5 data is produced after linearisation and equalisation of
the radiance response of the single detecto rs (see Section
3.1.7).

Usage. To relate the Level 1.5 image pixel count values to
physical radiance units.

Data Constancy. The data is (as all fundamental processing
aspects) kept constant for an image but is likely to be updated
from one image to the next (although it is expected to vary
only slowly).

<!-- source_page: 61 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 61 of 129

Component Record Description
BlackBodyDataUsed Constituent Data. This record holds the values associated
with the last blackbody calibration performed. This includes
MDU and PU gains for each of the radiometer’s detectors,
and the temperatures of the focal planes (warm and cold),
scan mirror and the various sensors, such as these located on
the baffle, the other mirrors and the black -body. Extracted
black-body data (i.e. extracted from the image data acquired
during black-body viewing) for each of the 12 radiometer
channels is also included in this record, describing the set of
pixels used in each case.

Usage. The purpose of the data is to provide full visibility of
all data used as input to the blackbody processing in IMPF.
This can be used for investigation, for historical reprocessing
or for research/analysis purpose in order to optimise the
processing.

Data Constancy. Blackbody calibration may be performed
up to once per Repeat Cycle, although lower frequency of
calibration may be applied when the instrument is known to
be stable from a radiometric standpoint. The information
presented is always the latest one, updated up to once per
Repeat Cycle.

<!-- source_page: 62 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 62 of 129

Component Record Description
MPEFCalFeedback Constituent Data. This Record contains two types of information,
the calibration feedback information from vicarious calibration
against forecast and radiosondes and the cross-calibration against
IASI according to the GSICS standards. The vicarious calibration
information from MPEF is used for internal purposes as a
feedback for the image-processing function. Flags for each of the
12 radiometer channels are provided, indicating whether or not
MPEF considers that calibration performed by IMPF is of good
quality, and if not, whether MPEF-supplied absolute calibration
coefficients should be used by the automated image processing
function. The absolute calibration data itself follows the quality
flags in this Record, and includes details of the type of data, along
with values for coefficients and biases.

Important note: this information is normally already taken into
account for the derivation of the Level1_5ImageCalibration, so
that the normal Level 1.5 data user does not need to an alyse the
present Record. In particular, differences between the information
within the Level1_5ImageCalibration and this one might have
valid operational reasons, so that the information has to be used
with extreme care.

The GSICS cross -calibration part of the Record provides the
results of the Near Real-Time (NRT) IASI-MSG cross-calibration
to users. These data are updated usually once per day.

Usage. The vicarious calibration information is mainly for use
within the MSG Ground Segment and should only be used for
specific purposes by users external to the Ground Segment. It
presents the insight on the MPEF feedback and can be used for
specific investigations or research on calibration. The normal data
user should always use the Level1_5ImageCalibration, as this is
the most accurate information available at the moment of
processing within the Ground Segment.

Users can optionally apply the GSICS cross -calibration
coefficients instead of the Level1_5ImageCalibration to ensure
SEVIRI's calibration is consistent with that of the GSICS
reference, and to correct for known radiometric biases, where
these may affect their products.

Data Constancy. Indicators are included in the Record to show
whether the calibration values have changed since the last repeat
cycle. It is expected that MPEF will perform calibration cross -
checking once every repeat cycle, and so variation may occur as
frequently as that.

<!-- source_page: 63 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 63 of 129

Component Record Description
RadTransform Constituent Data. Holds the values of the Look -Up Tables
(in steps of 64 counts) for each of the 42 detectors which are
used for mapping the Level 1.0 digital counts to the floating
point representation used for image -processing. For more
details on these aspects see also Section 3.1.7 and Section
3.1.8.

Usage. The primary use is for the expert Users who desire to
trace back very accurately all radiometric transformations
applied to the Level 1.0 data. This is the case for example in
the cas e of investigations on the end -to-end system
calibration activities/campaigns.

Data Constancy. The look -up table values are likely to
change from one repeat cycle to another as a result of
dynamic calibration, equalisation, linearisation, etc.

RadProcMTFAdaptation Constituent Data. This Record contains the FIR filter sets
of coefficients used for the MTF adaptation in N-S and E-W
directions for each of the 42 detectors. The Level 1.5 impulse
response (the inverse Fourier transform of the Level 1.5
MTF) is the result of the convolution of the initial Level 1.0
impulse response with the provided data.

Usage. To provide full trace of all applied transformation in
the processing from Level 1.0 to Level 1.5. The usage is
limited to expert users for specific investigations/research.

Data Constancy. The data is in practice constant over longer
periods of time, but might be updated from one Repeat cycle
to the next when a new set of MTF adaptation FIR is entering
into operations (e.g. as a result of better characterisation).

StraylightCorrection Constituent Data. This Record holds Chebyshev
coefficients of the st raylight compensation which is a
function of radiometer position and E -W Level 1.0 pixel
location, and that can be applied in the production of the
Level 1.5 image data (see also Section 3.1.11).

Usage. To provide full trace of the transformations applied
to the Image data in order to derive the Level 1.5 image data.

Data Constancy. The data is by nature quasi -constant over
time but can be updated from one Repeat Cyc le to the next
when more accurate information is provided.

<!-- source_page: 64 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 64 of 129

6.1.6 Geometric Processing Record Summary
This component record of the header provides information for east-west and north-south focal
plane layouts, the scanning law, the Earth and atmosphere models a nd the resampling
functions.

Scanning law data consists of the angles corresponding to the steps of the radiometer which
the latter takes in the course of its excursion between the lower and upper thresholds of the
scanning.

The Earth model corresponds to the Earth Model used for the Horizons and Landmark
processing as well as for the derivation of the relation of a given observation in the Level 1.0
image to physical geographical coordinates.

Note: This Earth Model is not the same than the one underlyi ng the Level 1.5 Projection (that
only defines the way the Level 1.5 data is projected on a surface, function of the geographical
coordinates).

The atmospheric model gives values indicating the apparent limits of the atmosphere.

The resampling function defines what resampling kernel was used for the processing to Level
1.5.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.2.6 Geometric Processing Record.

<!-- source_page: 65 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 65 of 129

Component Record Description
OptAxisDistances Constituent Data. This is also sometimes referred to as the
“Focal Plane layout”. It defines the latest and most accurate
knowledge of the estimated relative locations of the detectors
in the focal plane. The distances from the optical axis in both
E-W and N -S directions are expressed for each of the
detectors in terms of kilometres from SSP.

Usage. Provides expert users the knowledge of what was the
focal plane misregistration that was corrected for in the
processing to the Level 1.5. As the pre -launch
characterisation of the Focal Plane is of limited value once
in operations, the dete ctor positions are regularly re -
estimated (using horizons and landmarks measurements) by
the automated processing. The information is therefore
useful because it provides the most accurate knowledge
available on the true misregistration in the Level 1.0 im age
data. It is used also in the case of historical reprocessing.

Data Constancy. The misregistration is accurately tracked
and compensated for: the data is updated every Repeat Cycle
(although only minor/slow modifications are expected). The
values are used for the processing of the full Repeat Cycle.

EarthModel Constituent Data. Details of the earth model used by IMPF
for navigation, and the sizes of the equatorial, northern polar
and southern polar radii in kilometres, used by IMPF for the
navigation of Level 1.0 to Level 1.5.

Usage. For EUMETSAT internal usage only. Note: this is
only indicating how observations in the Level 1.0 image are
related to geographical positions, it is not the way the Level
1.5 image pixels are related to geographical positions (for
this see ProjectionDescription).

Data Constancy. Foreseen to be constant over long periods
of time. Can however change from one image to the next as
a result of an update of the corresponding database (e.g. for
improved accuracy).

<!-- source_page: 66 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 66 of 129

Component Record Description
AtmosphericModel Constituent Data. An array with elem ents for each of the
channels and 360 elements per channel corresponding to the
apparent atmosphere limit, sampled from South to North.

Usage. For EUMETSAT -internal purposes (e.g. historical
reprocessing).

Data Constancy. Will change every Repeat Cycle.

ResamplingFunctions Constituent Data. Defines for each channel the type of
Resampling used for the processing. The default (baseline)
resampling function used in IMPF is a 9x9 FIR Shannon
interpolation with a Kaiser window. Other resampling
functions (Bicubic Splines 4x4 and Nearest Neighbour) are
possible for specific use / reference.

Usage. Information on the applied interpolator for expert
users. Used for historical reprocessing and f or tracing the
exact configuration of the applied processing.

Data Constancy. Likely to stay constant. However changes
from one Repeat Cycle to the next can occur as a
consequence of an upgrade or an improvement.

<!-- source_page: 67 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 67 of 129

6.1.7 IMPF Configuration Record Summary
This component record of the header provides information on the active configuration of the
image processing function within the EUMETSAT MSG Ground Segment.

Information is also contained within this Record that facilitates the resumption of image -
processing during a ‘warm-start’ of EUMETSAT’s image-processing system. The availability
of such information means that image -processing can resume in a seamless manner after a
restart/switch of the computer hosting the software system or in case of controlled histor ical
reprocessing. The principle of this warm -start data is to save at a controlled breakpoint in the
processing, the state of all basic internal variables/models that are required for the processing
of the next Repeat Cycle.

As the information is really only of interest for the internal operations within EUMETSAT .
Note: This record is not disseminated and externally only available via the UMARF.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.2.7 IMPF Configuration Record.

Component Record Description
OverallConfiguration Constituent Data. Gives the overall identification of
processing history (in terms of real time processing and
offline reprocessing of archived data).

Usage. To identify the real time processed and reprocessed
data.

Data Constancy. The overall identifica tion will change
when data is re-processed offline.

<!-- source_page: 68 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 68 of 129

Component Record Description
SUDetails Constituent Data. Provides details of all ‘Software Units’
(SUs) and their associated ‘Information Bases’ that are in use
on the EUMETSAT MSG computer system that processed
the image.

Each SU is identified uniquely within IMPF and according
to its instantiation. Details of the processing modes and
states of the (SUs) that were in use on the EUMETSAT MSG
computer system that processed the image.

Possible SU modes are OFF, ON/Non-Processing, ON/Real-
Time Processing and ON/Analysis.

The possible SU states are ERROR, NOMINAL and
DEGRADED.

Usage. For EUMETSAT’s own use – the data is unlikely to
be of value to users. EUMETSAT might require it in the
case of image-data reprocessing being necessary, or possibly
for problem diagnosis.

It is not foreseen that this component Record will be
disseminated with the other Records constituting the header
via LRIT/HRIT, but it will be supplied with retrievals made
from U-MARF.

Data Constancy. A SU will change when a new version of
software is made operational. It is not expected that new
versions would be introduced more than a few times in the
course of a year. An ‘Information Base’ may also change at
these times in accordance with the software, but may also
change when special operational activities require it. The
latter may occur from several times a year upwards to
potentially several times on certain days.

SU mode and state information is a snapshot at the start of
image resampling. It is expected that, for images distributed
to external users, the information will be constant for all SUs,
each taking the nominal value. It should be noted that the
snapshot information can become out of date in the course of
the repeat cycle.

<!-- source_page: 69 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 69 of 129

Component Record Description
WarmStartParms Constituent Data. The states of all the models required for
a warm start or the historical reprocessing of the image data.

Usage. Purely for EUMETSAT purposes like historical
reprocessing, troubleshooting or on-going optimisation.

Data Constancy. Updated (in part at least) with each repeat
cycle.

<!-- source_page: 70 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 70 of 129

6.2 Level 1.5 Image Data Summary
For each scan of the earth disc by the MSG satellite, image data for 12 different spectral
channels is produced in nominal operations. Each channel’s line data is held in one of two
different Record structures, depending on which spectral type it is.

One type of Record structure is designed to hold the data of the nominal line-size of 3712 pixels
(i.e. the 11 types of visible (VIS) / infra -red (IR) data), and the other to hold the greater linesize of 5568 pixels (i.e. that of the high-resolution visible (HRV) channel).

The channel ordering of the image data constituting one scan line is as follows:

VIS 0.6
VIS 0.8
NIR 1.6 (Near-Infra-Red)
IR 3.9
IR 6.2 (WV)
IR 7.3 (WV)
IR 8.7
IR 9.7 (Ozone)
IR 10.8
IR 12.0
IR 13.4 (CO2)
HRV

<!-- source_page: 71 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 71 of 129

6.2.1 15VIS/IR Image Line Record Summary
This record structure is the one used for holding data for any of the 11 VIS / IR image lines.

The following table gives details of the likely usage of the data a nd its main characteristics.
For full details on the Data Content see Section 7.3 1.5 VIS/IR Line Record.

Component Record Description
LineSideInfo Constituent Data. The specification of the satellite which
produced the data originally, the image -line and spectral
channel context of the data, the acquisition time of that line,
and various validity / quality indicators.

Usage. The side-information for the line allows the user to
determine to which repeat cycle (and spectral channel
thereof) the data belongs, and whether the data for the
particular line is usable or not. The user is informed if the
data present is non -nominal due to having been ‘missed’,
‘corrupted’, ‘replaced’, or ‘interpolated’, and a classification
of ‘nominal’, ‘usable’, ‘suspect’ or ‘do not use’ is provided
for both radiometric and geometric quality.

Data Constancy. While it is expected that the sate llite id.
and validity / quality indicators will normally stay constant,
the remaining information will vary on a line-by-line basis.

LineData Constituent Data. The Level 1.5 pixel data for the spectral
channel and line is indicated in ‘ LineSideInfo’ above. For
the number of pixels held in this component Record, and the
number of these Records which together constitute an image,
please refer to the Section 3.1.3.

Usage. The pixel data contained in this field is nominally
used to build an image (for the indicated spectral -channel)
corresponding to one scan of the earth.

Data Constancy. This is Image data, so no constancy. The
only exception might be the lines of masked space that occur
close to the South Pole or the North Pole.

<!-- source_page: 72 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 72 of 129

6.2.2 15HRV Image Line Record Summary
This record structure is that used for holding data for the HRV image line.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.4 1.5 HRV Line Record.

Component Record Description
LineSideInfo Constituent Data. Same applies as for the field
‘LineSideInfo’ of the Record structure ‘VIS / IR Image Line’.

Usage. Same applies as for the field ‘LineSideInfo’ of the
Record structure ‘VIS / IR Image Line’.

Data Constancy. Same applies as for the field
‘LineSideInfo’ of the Record structure ‘VIS / IR Image Line’.

LineData Constituent Data. The Level 1.5 pixel data for the HRV line
is indicated in ‘ LineSideInfo’ above. For the number of
pixels held in this component Record, and the number of
these Records which together constitute an image, please
refer to the Section 3.1.3.

Usage. The pixel data contained in this field is nominally
used to build an HRV image corresponding to one scan of
the earth.

Data Constancy. This is Image data, so no constancy. The
only exception might be the lines of masked space that occur
close to the South Pole or the North Pole.

<!-- source_page: 73 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 73 of 129

6.3 Level 1.5 Trailer Summary
The purpose of the trailer which accompanies each Level 1.5 image is also to supply ancillary
information needed by the end -user for interpreting the data and / or further processing the
image.
In contrast to the header, the trailer contains information which is either accumulated during
the processing of the image, or at its completion, and is generated at the end of the image repeat
cycle, following the image data.
The trailer comprises a n umber of component items which hold information relevant to the
topics indicated below:

Topic Component
Type
Details of Component
Trailer Version Field This field identifies the version of
the trailer – important when its
format may have been upgraded
Image Production Stats Record See corresponding subsection
Navigation Extraction Results Record See corresponding subsection
Radiometric Quality Record See corresponding subsection
Geometric Quality Record See corresponding subsection
Timeliness and Completeness Record See corresponding subsection

These topics are described in the sub-sections that follow, in terms of both the data content and
the relation the information has to the image data.

<!-- source_page: 74 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 74 of 129

6.3.1 Image Production Stats Record Summary
This component record of the trailer holds information on the actual image produced, providing
details of its dimensions.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.5.1 Image Production Stats Record.

Component Record Description
SatelliteId Constituent Data. Indicator to show which of the satellites
in the MSG series scanned the image.

Usage. Unambiguous relation of the present trailer to the
image taking satellite.

Data Constancy. Might change as a consequence of a
change in the imaging satellite. Note thi s can occur even if
the disseminating satellite stays the same.

ActualScanningSummary Constituent Data. Summary details of image-taking for this
repeat cycle, which include an indication of whether image -
taking was performed in the nominal manner during the
whole repeat cycle, whether it was a reduced scan, and the
times of the first and last lines of forward scan.

Usage. Information about the actual image acquisition cycle
(start and end of forward scan)

Data Constancy. Updated every Repeat Cycle.

RadiometerBehaviour Constituent Data. Details of radiometer behaviour for this
repeat cycle, which include indicators for nominal behaviour
of the radiometer instrument during the whole of this repeat
cycle, and whether any scan irregularity, radiometer
stoppage or any other radiometer event has occurred which
is considered abnormal behaviour.

Usage. Accurate information on the actual status at the end
of the image acquisition for this Repeat Cycle.

Data Constancy. Updated for every Repeat Cycle.
Hopefully always nominal!

<!-- source_page: 75 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 75 of 129

Component Record Description
ReceptionSummaryStats Constituent Data. Statistics on a radiometer channel basis
which give the number of corrupted Level 1.0 lines for this
repeat cycle, the number of missing lines, the number of
corrupt lines and the number of replaced lines.

Usage. Information on the actual status at the end of the
Repeat Cycle.

Data Constancy. Updated every repeat cycle.

L15ImageValidity Constituent Data. A component sub-Record per radiometer
channel which indicates the validity of the Level 1.5 image
in terms of completeness, radiometric quality, geometric
quality and timeliness.

Usage. Updated information on the actual status at the end
of the Repeat Cycle.

Data Constancy. Updated every Repeat Cycle.

ActualL15CoverageVIS/IR Constituent Data. The line numbers of the actual bounds of
this Level 1.5 image (i.e. the northern -, southern-, eastern-
and western-most lines). These line numbers are within the
limit of the planned -coverage information which was
presented in the Level 1.5 header.

Usage. Updated information on the actual status at the end
of the Repeat Cycle.

Data Constancy. Updated every Repeat Cycle.

ActualL15CoverageHRV Constituent Data. Similar to ‘ ActualL15CoverageVIS/IR’
above, except that there are two line numbers given for the
eastern and western bounds – these cater for the ‘upper’ and
‘lower’ areas of a alternative coverage HRV image. For an
example of such an HRV image, please see the Section 3.1.2.

Usage. Updated information on the actual status at the end
of the Repeat Cycle.

Data Constancy. Updated every Repeat Cycle.

<!-- source_page: 76 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 76 of 129

6.3.2 Navigation Extraction Results Record Summary
This com ponent record of the trailer holds information containing all the image -based
measurements (i.e. horizons, landmarks and stars) which have been made by IMPF to support
navigation, and in particular the estimation of Orbit & Attitude.

The following table g ives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.5.2 Navigation Extraction Results Record.

Component Record Description
ExtractedHorizons Constituent Data. Alpha and beta angle measurements (in
radians), accompanied by respective confidence intervals,
the time of observation and the satellite spin -rate (in rpm.)
for each of the 4 horizons (south, north, east & west) for the
present Repeat Cycle. For more det ails on the angles
definition, see section Navigation Extraction Results Record.
Note: in case of miniscans, there might be only 2 horizons
(East & West) or none extracted.

Usage. Provides expert users the infor mation about the
observed, refined horizons extracted from the Level 1.0
image for the purpose of being used to derive the attitude/
(these data are passed together with other observations to the
Flight Dynamics function of the Ground Segment for
Attitude & Orbit derivation).

Data Constancy. Updated every Repeat Cycle and
containing the information extracted during the Repeat
Cycle.

ExtractedStars Constituent Data. The same information as for each of the
‘ExtractedHorizons’, but this time for each of the stars for
which navigation information has been generated. Note that
a unique EUMETSAT star identifier is held within the data
for each star.

Usage. Same as for ‘ ExtractedHorizons’, but this time for
each of the stars used for navigation.

Data Constancy. Updated every Repeat Cycle and
containing the information extracted during the Repeat
Cycle.

<!-- source_page: 77 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 77 of 129

Component Record Description
ExtractedLandmarks Constituent Data. The same information as for each of the
‘ExtractedHorizons’, but this time for each of the landmarks
for which navigation information has been generated. Note
that a unique EUMETSAT landmark identifier is held within
the data for each landmark, along with the landm ark’s
latitude and longitude.

Usage. of the ‘ExtractedHorizons’, but this time for each of
the landmarks used for navigation.

Data Constancy. Updated every Repeat Cycle and
containing the information extracted during the Repeat
Cycle.

<!-- source_page: 78 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 78 of 129

6.3.3 Radiometric Quality Record Summary
This component record of the trailer holds information.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.5.3 Radiometric Quality Record.

Component Record Description
L10RadQuality Constituent Data. Details of the radiometric quality for each
of the 42 detectors, in the form of a variety of statistical
measures for the full image data, and al so the Earth -disc,
moon and space-region component data. S ampled versions
of the accumulated Power Spectral Density (PSD) over all
applicable E-W rows and over all applicable N -S columns
are also included.

Usage. Full information on the actual radiometri c image
quality per detector of the Level 1.0 data

Data Constancy. Updated every Repeat Cycle.

L15RadQuality Constituent Data. Details of the radiometric quality for each
of the 12 channels, which includes a subset of the fields
contained in ‘ L10RadQuality’ (but – note! – only per
channels, not detectors, as the signal from the detectors of a
given spectral channel has been combined during the
production of the Level 1.5 data). Additional fields to those
for Level 1.0 also provide the RMS and mean values
respectively for the space corners of the Level 1.5 data (i.e.
equivalent to the area that would have been produced had a
space mask not been applied).

Usage. The values can be compared with the same
information for Level 1.0 to assess the impact on the noise
due to IMPF processing from Level 1.0 to Level 1.5.

Data Constancy. Updated every Repeat Cycle.

<!-- source_page: 79 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 79 of 129

6.3.4 Geometric Quality Record Summary
This component record of the trailer holds 4 sets of statistical information which describes the
absolute accuracy of the image, the relative accuracy from image to image, and the relative
accuracy within the image over 500 -pixel and 16 -pixel ranges, and this for each of the 12
radiometer channels. It also holds misregistr ation residual and geometric quality status
information, again, on a radiometer channel basis.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.5.4 Geometric Quality Record.

Component Record Description
AbsoluteAccuracy Constituent Data. If derived, statistical information related
to the overall absolute accuracy of the image data for each of
the 12 radiometer channels, in both north -south and east -
west directions. The metrics provided include magnitudes
and uncertainties of accumulated RMS, deviations in image
accuracy and maximum uncertainty factors in both.

Usage. Provides the data users with the actually measure
absolute accuracy of the Level 1.5 image.

Data Constancy. Measured every Repeat Cycle.

RelativeAccuracy Constituent Data. Similar statistical information to that for
‘AbsoluteAccuracy’, but this time related to the relative
accuracy from image to image.

Usage. Provides the data users with the actually measured
relative accuracy (a criterion of the “stability” over time of
the image correction)

Data Constancy. Computed every Repeat Cycle, by
comparing with the previous Level 1.5 image.

RelativeAccuracy500Pixels Constituent Data. Similar statistical information to that for
‘RelativeAccuracy’, but this time related to the relative
accuracy within an image over the range of 500 pixels.

Usage. Provides data users with the actually measured
accuracy within 500 pixels (gives a measure of the
“distortion” between pixels that are separated by up to 500
pixels).

Data Constancy. Updated every Repeat Cycle.

<!-- source_page: 80 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 80 of 129

Component Record Description
RelativeAccuracy16Pixels Constituent Data. Similar statistical information to that for
‘RelativeAccuracy500Pixels’, but this time for the relative
accuracy within the image over the range of 16 pixels.

Usage. Currently, it is TBC if it is possible to measure these
deviations in a reliable manner. If this is the case, the figures
would be provided here.

Data Constancy. Updated every repeat Cycle.

MisregistrationResiduals Constituent Data. If derived, statistical information related
to the misregistration residuals of the image data for each of
the 12 radiometer channels, in both north -south and east -
west directions. The metrics indicate magnitudes,
uncertainty factors therein, and the RMS of misregistration.

Usage. Provides the actually measured residual
misregistration once the OptAxisDistance has been
compensated for. Note that the process of estimating the true
focal plane distances is an extremely accurate one, based on
the accumulation of hundreds of measurements from many
Repeat cycles, whereas these measurements are only done
within this Repeat cycle and therefore have a much higher
uncertainty. Therefore it is advisable to consider the
provided u ncertainty radii for any work based on these
values. For the most accurate knowledge related to the actual
Focal Plane Layout, the information provided within the
OptAxisDistance should be considered.

Data Constancy. Updated every Repeat Cycle.

GeometricQualityStatus Constituent Data. Geometric quality status information for
each of the 12 radiometer channels, indicating whether
overall quality is nominal, whether absolute image accuracy
is nominal, whether relative im age-to-image accuracy is
nominal, whether relative accuracy within the image (for 16-
and 500-pixel ranges) is nominal, and finally, whether image
registration between spectral bands is nominal.

Usage. Provides a summary indicating to the Data Users if
the image geometric quality is within specifications for the
completed Repeat Cycle.

Data Constancy. Updated every Repeat Cycle.

<!-- source_page: 81 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 81 of 129

6.3.5 Timeliness and Completeness Record Summary
This component record of the trailer holds information.

The following table gives details of the likely usage of the data and its main characteristics.
For full details on the Data Content see Section 7.5.5 Timeliness and Completeness Record.

Component Record Description
Timeliness Constituent Data. Minimum, maximum and mean delays in
seconds for the whole image, between the Level 1.0 mean
acquisition time and the time of the corresponding 1.5 image
data output by EUMETSAT’s image-processing facility.

Usage. Arguably of importance to EUMETSAT only, to
provide a basis for statistics which will show the operational
performance of its image -processing facility in terms of
speed of the production of the Level 1.5 image.

Data Constancy. Updated every Repeat Cycle.

Completeness Constituent Data. Information showing the variation
between the planned and the actual coverage of the Level 1.5
image (for each radiometer channel) in terms of the number
of lines within each coverage, the number of Level 1.5
invalid lines, the number of dummy Level 1.5 i mage lines
that were produced without corresponding Level 1.0 data
(e.g. due to missing data) and the number of Level 1.5 image
lines that were generated using corrupted Level 1.0 data.

Usage. Also of importance to EUMETSAT, to provide a
basis for statist ics which will show the operational
performance of its image -processing facility in terms of its
production of acceptable quality Level 1.5 image data.

Data Constancy. Updated every Repeat Cycle.

<!-- source_page: 82 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 82 of 129

7 DETAILED DATA CONTENT – APPLICATION DATA UNITS

Terms Used in the Level 1.5 Data Content definition:

1.0 mean acquisition time: the average acquisition time of the Level 1.0 data from which the
1.5 data item is derived (data from several scan lines is used to
derive a 1.5 data item).

Centre square: the square area of pixels measuring 1024 by 1024 pixels located
in the centre of the image square, as characterised by the
coordinates (1344, 1344) and (2368, 2368) in the Level 1.5
reference grid.

Earth disk: the Earth disk part of the image for a particular spectral channel.

Full image: the full image array (including space) of the corresponding
spectral channel.

Lower area: refers to the area of HRV image data that is scanned prior to the
occurrence of a ‘break line’, i.e. the point in forward scan where
the East-West offset is altered.

Upper area: refers to the area of HRV image data that is scanned subsequent
to the occurrence of a ‘break line’, i.e. the point in forward scan
where the East-West offset is altered.

Space corner: the square area of pixels measuring up to 500 by 500 pixels in
either the SE, SW, NE or NW corner of the image square (the
relevant 2 -letter prefix used to identify which one). The
expression “four space corners” is used to refer to the data from
all four of the space corners.


Basic Data Structures

To be completed

The following data structures are used and not further detailed:

GP_SC_ID Spacecraft identification. The spacecraft addressed through the
MSGGS shall be uniquely identified. They concern the MSG
spacecraft and simulators as well as spacecraft controlled by
external ground segments interfaced to the MSGGS.


Title: Spacecraft Identification Id: GP_SC_ID Area: general purpose

GP_SC_ID ::= ENUMERATED SHORT

<!-- source_page: 83 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 83 of 129

{NoSpacecraft (0), -- No specific satellite
METEOSAT-3 (16), -- MOP spacecraft, ESA assigned ID
METEOSAT-4 (19),
METEOSAT-5 (20),
METEOSAT-6 (21),
MTP-1 (150), -- MTP spacecraft, ESA assigned ID
MTP-2 (151),
MSG-1 (321), -- MSG spacecraft, CCSDS assigned ID
MSG-2 (322),
MSG-3 (323),
MSG-4 (324),
METOP-1 (11), -- EPS, CCSDS assigned ID
METOP-2 (12),
METOP-3 (13),
NOAA-12 (17012), -- NOAA polar, MSG GS assigned ID
NOAA-13 (17013),
NOAA-14 (17014),
NOAA-15 (17015),
NOAA-16 (17016),
NOAA-17 (17017),
GOES-7 (18007), -- GOES, MSG GS assigned ID
GOES-8 (18008),
GOES-9 (18009),
GOES-10 (18010),
GOES-11 (18011),
GOES-12 (18012),
GOMS-1 (19001), -- GOMS, MSG GS assigned ID
GOMS-2 (19002),
GOMS-3 (19003),
GMS-4 (20004), -- GMS, MSG GS assigned ID
GMS-5 (20005),
GMS-6 (20006),
MTSAT-1 (21001), -- MTSAT, MSG GS assigned ID
MTSAT-1R (21003),
MTSAT-2 (21002),
UnknownSpacecraft (OTHERS)}

7.1.1 GP_SC_NAME: Spacecraft name

The spacecraft addressed through the MSGGS shall be assigned unique names.

Title: Spacecraft name Id: GP_SC_NAME Area: general purpose
GP_SC_NAME ::= CHARACTERSTRING SIZE (12)
(“NoSpacecraft” | -- No specific satellite
“METEOSAT3 ” | -- MOP spacecraft
“METEOSAT4 ” |
“METEOSAT5 ” |

<!-- source_page: 84 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 84 of 129

“METEOSAT6 ” |
“MTP1 ” | -- MTP spacecraft
“MTP2 ” |
“MSG1 ” | -- MSG spacecraft
“MSG2 ” |
“MSG3 ” |
“METOP1 ” | -- EPS
“METOP2 ” |
“NOAA12 ” | -- NOAA polar
“NOAA13 ” |
“NOAA14 ” |
“NOAA15 ” |
“NOAA16 ” |
“NOAA17 ” |
“GOES7 ” | -- GOES
“GOES8 ” |
“GOES9 ” |
“GOES10 ” |
“GOES11 ” |
“GOES12 ” | “GOMS1 ” | -- GOMS
“GOMS2 ” |
“GOMS3 ” |
“GMS4 ” | -- GMS
“GMS5 ” |
“GMS6 ” |
“MTSAT1 ” | -- MTSAT
“MTSAT1R ” |
“MTSAT2 ” |
“Unknown ”) -- Other


TIME CDS SHORT CCSDS Day Segmented time in its SHORT (6 bytes, day since
epoch + number of milliseconds in day) format. For the CDS
time, the epoch is 1958 January 1st starting with 0. The CDS time
is UTC-based and takes into account leap second corrections.

Day Milliseconds of day
UNSIGNED SHORT
2 bytes
UNSIGNED
4 bytes
Table 3 - Short CDS time

<!-- source_page: 85 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 85 of 129

7.2 15HEADER Record Structure
The packet body assigned to the 15Header service subtype is defined as follows:
15HEADER ::= RECORD
{15HEADERVersion UNSIGNED BYTE (0),
SatelliteStatus_Record SatelliteStatus, -- See below for definition
ImageAcquisition_Record ImageAcquisition, -- See below for definition
CelestialEvents_Record CelestialEvents, -- See below for definition
ImageDescription_Record ImageDescription, -- See below for definition
RadiometricProcessing_Record RadiometricProcessing, -- See below for definition
GeometricProcessing_Record GeometricProcessing, -- See below for definition
IMPFConfiguration_Record IMPFConfiguration} -- See below for definition

15HEADERVersion is used to identify the header version. Note: This parameter is not disseminated and
externally only available via the UMARF.

7.2.1 SatelliteStatus Record
This is defined as follows:
SatelliteStatus ::= RECORD
{SatelliteDefinition RECORD
{SatelliteId GP_SC_ID,
NominalLongitude REAL,
SatelliteStatus ENUMERATED BYTE
{operational (1),
standby (2),
commissioning/test (3),
manoeuvre (4),
decontamination (5),
safe mode (6),
dissemination only (7)}},
SatelliteOperations RECORD
{LastManoeuvreFlag BOOLEAN BYTE,
LastManoeuvreStartTime TIME CDS SHORT,
LastManoeuvreEndTime TIME CDS SHORT,
LastManoeuvreType ENUMERATED BYTE
{Spin-Up (0),
Spin-Down (1),
Attitude Slew (2),
N-S Station-Keeping (3),
E-W Station-Keeping (4),
Station Relocation (5)},
NextManoeuvreFlag BOOLEAN BYTE,
NextManoeuvreStartTime TIME CDS SHORT,
NextManoeuvreEndTime TIME CDS SHORT,
NextManoeuvreType ENUMERATED BYTE
{Spin-Up (0),
Spin-Down (1),
Attitude Slew (2),
N-S Station-Keeping (3),
E-W Station-Keeping (4),
Station Relocation (5)}},
Orbit ORBIT, -- See below for definition
Attitude ATTITUDE, -- See below for definition
SpinRateatRCStart REAL DOUBLE,
UTCCorrelation UTCCORRELATION} -- See below for definition

<!-- source_page: 86 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 86 of 129

SatelliteDefinition:

SatelliteId gives the satellite’s identification. It is the ID received by IMPF in the GS packet sub -header of the
1.0 data used to produce the 1.5 data.

NominalLongitude gives the satellite nominal longitude in degrees.
It is important to understand that there is a difference between the satellite position and the L1.5 Image projection.
The first is where the satellite physically is at any one time, whereas the latter is the projection (=map) to which
the Level 1.5 image is rectified. In practise, if the user needs (e.g.) to find a loca tion of a pixel on the Earth
ellipsoid, he/she needs to refer to the image projection. If one needs to refer to (e.g) the satellite viewing angles,
one needs to refer to the satellite position. The satellite is not exactly stationary on the geostationary ring. The true
position of the satellite varies slightly with time because all the satellites are drifting from their nominal position.
The station keeping is maintained actively by manoeuvres such that the satellite moves only in a confined area,
the "station keeping box". The NominalLongitude is the position of the centre of satellite station keeping box on
the geostationary ring. (Provided in degrees from the Greenwich Meridian and a positive value corresponds to a
position East of it, a negative value to the West.) This is not to be confused with the real satellite position, which
is described in the Orbit record, nor with the notional longitude used for image projection, which described in
Projection Description record.

SatelliteStatus gives the status of the satellite.

SatelliteOperations:

LastManoeuvreFlag is a flag that indicates if there has been a manoeuvre in the recent past (maximum 48 hours).
A value of true indicates that there was a manoeuvre.

LastManoeuvreStartTime gives the start-time of the last manoeuvre.

LastManoeuvreEndTime gives the end-time of the last manoeuvre.

LastManoeuvreType gives the type of the last manoeuvre performed.

NextManoeuvreFlag indicates if a manoeuvre is planned for the near future (i.e. within 48 hours). ‘TRUE’
indicates that a manoeuvre is planned.

NextManoeuvreStartTime gives the foreseen start-time of the next planned manoeuvre.

NextManoeuvreEndTime gives the foreseen end-time of the next planned manoeuvre.

NextManoeuvreType gives the next planned manoeuvre type.

SpinRateatRCStart gives the spin rate in RPM at the start of the current repeat cycle.

ORBIT is defined as follows:
ORBIT ::= RECORD
{PeriodStartTime TIME CDS SHORT,
PeriodEndTime TIME CDS SHORT,
OrbitPolynomial ARRAY SIZE (1..100) OF ORBITCOEF}

PeriodStartTime gives the start time of the coverage period.

PeriodEndTime gives the end time of the coverage period.

OrbitPolynomial is a fixed size array containing orbit coefficient sets. Unused array elements are filled with
zeros.

<!-- source_page: 87 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 87 of 129

ORBITCOEF is defined as follows:
ORBITCOEF ::= RECORD
{StartTime TIME CDS SHORT,
EndTime TIME CDS SHORT,
X ARRAY SIZE (8) OF REAL DOUBLE,
Y ARRAY SIZE (8) OF REAL DOUBLE,
Z ARRAY SIZE (8) OF REAL DOUBLE,
VX ARRAY SIZE (8) OF REAL DOUBLE,
VY ARRAY SIZE (8) OF REAL DOUBLE,
VZ ARRAY SIZE (8) OF REAL DOUBLE}

StartTime gives the start time for the coefficient set validity. StartTime of set N is always greater than StartTime
of set N-1.

EndTime gives the end time for the coefficient set validity. EndTime of set N is always greater than EndTime of
set N-1).

X, Y, Z and VX, VY and VZ represent the spacecraft position and velocity in an Earth fixed coordinate frame.
The relation between the spacecraft position or velocity and time is provided by a Chebychev polynomial. For
each of the arrays, the index 0 coefficient contains the degree 0 coefficient of the Chebychev polynomial, the
index 1 coefficient contains the degree 1 coefficient of the Chebychev polynomial, etc…

ATTITUDE is defined as follows:
ATTITUDE ::= RECORD
{PeriodStartTime TIME CDS SHORT,
PeriodEndTime TIME CDS SHORT,
PrincipleAxisOffsetAngle REAL DOUBLE
AttitudePolynomial ARRAY SIZE (1..100) OF ATTITUDECOEF}

PeriodStartTime gives the start time of the coverage period.

PeriodEndTime gives the end time of the coverage period.

PrincipleAxisOffsetAngle represents the angle, in radians, between the S/C principle axis and th e geometrical
axis perpendicular to the baseplate. It is derived from a model that predicts this angle based on the actual fuel
status. This is valid for any time within the period covered by the file.

AttitudePolynomial is a fixed size array containing a ttitude coefficient sets. Unused array elements are filled
with zeros.

ATTITUDECOEF is defined as follows:
ATTITUDECOEF ::= RECORD
{StartTime TIME CDS SHORT,
EndTime TIME CDS SHORT
XofSpinAxis ARRAY SIZE (8) OF REAL DOUBLE,
YofSpinAxis ARRAY SIZE (8) OF REAL DOUBLE,
ZofSpinAxis ARRAY SIZE (8) OF REAL DOUBLE}

StartTime gives the start time for the coefficient set validity. StartTime of set N is always greater than StartTime
of set N-1.

EndTime gives the end time for the coefficient set validity. EndTime of set N is always greater than EndTime of
set N-1).

XOfSpinAxis, YOfSpinAxis and ZOfSpinAxis represent the spacecraft spin axis in an Earth fixed coordinate
frame. The relation between the spacecraft spin axis and time is provided by a Che bychev polynomial. For each

<!-- source_page: 88 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 88 of 129

of the arrays, the index 0 coefficient contains the degree 0 coefficient of the Chebychev polynomial, the index 1
coefficient contains the degree 1 coefficient of the Chebychev polynomial, etc…

UTCCORRELATION is defined as follows:
UTCCORRELATION ::= RECORD
{PeriodStartTime TIME CDS SHORT,
PeriodEndTime TIME CDS SHORT,
OnBoardTimeStart CUC SIZE (4,3),
VarOnBoardTimeStart REAL DOUBLE,
A1 REAL DOUBLE,
VarA1 REAL DOUBLE,
A2 REAL DOUBLE,
VarA2 REAL DOUBLE}

PeriodStartTime represents the time from which on the correlation becomes valid.

PeriodEndTime represents the time from which point onwards the accuracy of the correlation cannot be
guaranteed.

OnBoardTimeStart is equivalent to PeriodStartTime, but from spacecraft epoch.

VarOnBoardTimeStart, VarA1 and VarA2 represent the variance (“the uncertainty”) of the coefficients
OnBoardTimeStart, A1 and A2 respectively.

OnBoardTimeStart, A1 and A2 are the coefficients of the function:

UTC = OnBoardTimeStart + (1+A1) x (OBT - OnBoardTimeStart) + A2 x (OBT - OnBoardTimeStart)2
OBT represents the On-board time as it is received from the S/C while the resulting UTC represents a corrected
on-board time. It is a continuous an d uniform time, but does not include leap second as UTC times expressed in
CDS time format.

7.2.2 Image Acquisition Record
This is defined as follows:
ImageAcquisition ::= RECORD
{PlannedAcquisitionTime RECORD
{TrueRepeatCycleStart TIME CDS EXPANDED,
PlannedForwardScanEnd TIME CDS EXPANDED,
PlannedRepeatCycleEnd TIME CDS EXPANDED},
RadiometerStatus RECORD
{ChannelStatus ARRAY SIZE (1..12) of ENUMERATED BYTE
{OFF (0),
ON (1)},
DetectorStatus ARRAY SIZE (1..42) of ENUMERATED BYTE
{OFF (0),
ON (1)}},
RadiometerSettings RECORD
{MDUSamplingDelays ARRAY SIZE (1..42) OF UNSIGNED SHORT,
HRVFrameOffsets RECORD
{MDUNomHRVDelay1 UNSIGNED SHORT,
MDUNomHRVDelay2 UNSIGNED SHORT,
Spare BITSTRING SIZE(16), -- Set to 0x0000
MDUNomHRVBreakline UNSIGNED SHORT},
DHSSSynchSelection ENUMERATED BYTE
{SUN (0),
EARTH-NORTH (1),
EARTH-SOUTH (2)},

<!-- source_page: 89 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 89 of 129

MDUOutGain ARRAY SIZE (1..42) OF UNSIGNED SHORT,
MDUCourseGain ARRAY SIZE (1..42) OF BYTE,
MDUFineGain ARRAY SIZE (1..42) OF UNSIGNED SHORT,
MDUNumericalOffset ARRAY SIZE (1..42) OF UNSIGNED SHORT,
PUGain ARRAY SIZE (1..42) OF UNSIGNED SHORT,
PUOffset ARRAY SIZE (1..27) OF UNSIGNED SHORT,
PUBias ARRAY SIZE (1..15) OF UNSIGNED SHORT,
OperationParameters RECORD
{L0_LineCounter UNSIGNED SHORT,
K1_RetraceLines UNSIGNED SHORT,
K2_PauseDeciseconds UNSIGNED SHORT,
K3_RetraceLines UNSIGNED SHORT,
K4_PauseDeciseconds UNSIGNED SHORT,
K5_RetraceLines UNSIGNED SHORT,
X_DeepSpaceWindowPosition ENUMERATED BYTE
{no delay (0),
predefined delay no. 1 (1),
predefined delay no. 2 (2),
predefined delay no. 3 (3)}},
RefocusingLines UNSIGNED SHORT
RefocusingDirection ENUMERATED BYTE
{Up (0),
Down (1)},
RefocusingPosition UNSIGNED SHORT,
ScanRefPosFlag BOOLEAN BYTE,
ScanRefPosNumber UNSIGNED SHORT,
ScanRefPotVal REAL,
ScanFirstLine UNSIGNED SHORT,
ScanLastLine UNSIGNED SHORT,
RetraceStartLine UNSIGNED SHORT},
RadiometerOperations RECORD
{LastGainChangeFlag BOOLEAN BYTE,
LastGainChangeTime TIME CDS SHORT,
Decontamination RECORD
{DecontaminationNow BOOLEAN BYTE,
DecontaminationStart TIME CDS SHORT,
DecontaminationEnd TIME CDS SHORT},
BBCalScheduled BOOLEAN BYTE,
BBCalibrationType ENUMERATED BYTE
{Hot (1),
Ambient (2),
Indeterminate (3)},
BBFirstLine UNSIGNED SHORT,
BBLastLine UNSIGNED SHORT,
ColdFocalPlaneOpTemp UNSIGNED SHORT,
WarmFocalPlaneOpTemp UNSIGNED SHORT}

<!-- source_page: 90 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 90 of 129



PlannedAcquisitionTime:

TrueRepeatCycleStart is the start time of the current repeat cycle, accurate to within 10-6seconds.

PlannedForwardScanEnd is the planned start time of the current repeat cycle, accurate to within 0.1 second.

PlannedRepeatCycleEnd is the planned end time of the current repeat cycle, accurate to within 0.1 second.

RadiometerStatus:

ChannelStatus is an array with one element per channel that gives the status of each radiometer channel: OFF,
ON.

DetectorStatus is an array with one element per detector that gives the status of each radiometer detector: OFF,
ON.


RadiometerSettings:

MDUSamplingDelays are the adjustment delays applied to each detection chain of the S/C in East-West to align
the raw image pixels within a channel. It should be noted that these delays do not allow channel -to-channel
alignment in the raw image. Units of 2 clock-pulses, as in the telemetry.

MDUNomHRVDelay1 is the delay applied by the spacecraft to the southern part of the HRV raw image (i.e. the
part of the image before the field MDUNomHRVBreakline). Units of 512 clock-pulses, as in the telemetry.

MDUNomHRVDelay2 is the delay applied by the spacecraft to the northern part of the HRV raw image (i.e. the
part of the image after the field MDUNomHRVBreakline). Units of 512 clock-pulses, as in the telemetry.

Spare is a spare field.

MDUNomHRVBreakline is the line in the HRV raw image at which the ‘upper area’ of the image begins (i.e.
the image line at which the new East-West delay MDUNomHRVDelay2 is applied).

DHSSSynchSelection indicates whether the synchronisation signal for the line events has be en derived from the
sun sensor unit (0), or the earth sensor unit (ESU). For the latter case the synchronisation pulse is either derived
from the northern IR telescope (1) or the southern one (2) which are both part of the ESU (note that North and
South refers to the ESU telescopes under nominal flight conditions).

The definition of the detection parameters can be understood from the following relationship:


C are the Counts at the instrument output

EL is the signal coming from the detectors (it includes the dark signal ED)

GPU is the parameter called PUGain in the 1.5 header. There is one value of PUGain per detector
(42 values)

OPU is the parameter called PUOffset in the 1.5 header. There is one value of PUOffset per detector
except HRV, VIS0.6 and VIS0.8 (27 values)
     MDUoPULPUcMDUMDUfMDUOutMDUL ODOIOEGGGGGEC   0

<!-- source_page: 91 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 91 of 129


I0 is a fixed current. It is not part of the 1.5 Header

GMDU-c is the parameter called MDUCoarseGain in the 1.5 header. There is one value of
MDUCoarseGain per detector (42 values)

GMDU-0 is a fixed gain. It is not part of the 1.5 Header

DO is the parameter called DCRValues in the record “RadiometricProcessing” of the 1.5 header.
There is one value of DCRValues per detector (42 values). Each value is obtained by averaging
2048 values acquired during Deep Space View.

GMDU-f is the parameter called MDUFineGain in the 1.5 header. There is one value of MDUFineGain
per detector (42 values)

GMDU-Out is the parameter called MDUOutGain in the 1.5 header. There is one value of MDUOutGain
per detector (42 values).

MDUNumericalOffset is the parameter OMDU in the above equation. There is one such value per detector.

Note that all gains, bias and offset values take the same units as in the housekeeping telemetry.

PUBias is the bias current that is applied to the PhotoConductive detectors. It modifies their dark signal E D
according to a fixed relationship.

L0_LineCounter gives the line counter value at which the forward scan will stop if CONFIGURATION mode is
entered. It is not used in NOMINAL mode.

K1_RetraceLines gives the first ‘retrace parameter’. The radiometer retraced ‘K1’ lines, at a rate of 1 line every
100msec.

K2_PauseDeciseconds gives the second ‘retrace parameter’. The radiometer paused for ‘K2*100’ msec,
subsequent to the K1 retrace.

K3_RetraceLines gives the third ‘retrace parameter’. The radiometer retraced ‘K3’ lines, at a rate of 1 line every
100msec.

K4_PauseDeciseconds gives the fourth ‘retrace parameter’. The radiometer paused ‘K4*100’ msec, subsequent
to the K3 retrace.

K5_RetraceLines gives the fifth ‘retrace parameter’. The radiometer retraced ‘K5’ lines, at a rate of 1 line every
100msec.

X_DeepSpaceWindowPosition is the position in the backscan where the DCR values have been acquired. There
are three possible windows which can be selected in order to avoid Sun or Moon interference; the positions of
these three windows are defined as delays w.r.t. the Start-Of-Line.

RefocusingLines is the number of image lines during which one step of the refocusing mechanism is performed.

RefocusingDirection is the direction of the step performed by the refocusing mechanism.

RefocusingPosition is the absolute position of the refocusing mechanism at the start of the repeat cycle. Units
are step counts.

ScanRefPosFlag indicates whether the radiometer went to the reference position before starting forward scan.

<!-- source_page: 92 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 92 of 129

ScanRefPosNumber is the readout of the scan line counter value at the moment of the scan mirror being at
reference position.

ScanRefPotVal is the potentiometer readout at the moment of the scan mirror being at reference position (as
supplied by SEVIRI auxiliary data).

ScanFirstLine is the line counter value of the first line of the image.

ScanLastLine is the line counter value of the last line of the image.

RetraceStartLine is the line counter value at which the scan mechanism will start the retrace. Not to be confused
with ScanLastLine.

Radiometer Operations:

LastGainChangeFlag indicates if there has been a Gain Change in the recent past (i.e. within the last 48 hours).
‘True’ indicates that there has been a change.

LastGainChangeTime gives the time of the last gain change. Accuracy is to 64 seconds.

DecontaminationNow indicates whether a decontamination operation is currently taking place (true/false). Note
that the operation is defined as the time from when the focal plane heater is first switched on until the point where
the focal plane has cooled down to its nominal imaging temperature after the heater has been switched -off.

DecontaminationStart gives the start-time of the last decontamination operation, or of the current operation if
one is currently taking place. Accuracy is of the order of 30 seconds.

DecontaminationEnd gives the end -time of the last decontamination operation that has been conducted.
Accuracy is of the order of 30 seconds. Note that if a decontamination operation is currently taking place, this
value will be undefined. If no decontamination operation is taking place, and the start - and end-time values are
the same, then the system has no record of a decontamination operation having taken place.

BBCalScheduled indicates if BB Calibration foreseen in the coming repeat cycle (true/false).

BBCalibrationType gives the type of calibration planned.

BBFirstLine gives the line counter value of the first line of the image for which BB calibration is performed.

BBLastLine gives the line counter value of the last line of the image for which BB calibration is performed.

ColdFocalPlaneOpTemp is the temperature of the cold focal plane (i.e. also the temperature of the cold
detectors). It is one of the fields FCUNominalColdFocalPlaneTemp or FCURedundantColdFocalPlaneTemp
of the record “RadiometricProcessing”, depending on whether the Nominal or Redundant electronics unit is
selected.

WarmFocalPlaneOpTemp is the temperature of the warm focal plane (i.e. also the temperature of the warm
detectors. It i s either FCUNominalWarmFocalPlaneVHROTemp or
FCURedundantWarmFocalPlaneVHROTemp (of the record “RadiometricProcessing”), depending whether
the Nominal or Redundant electronics unit is selected.

<!-- source_page: 93 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 93 of 129

7.2.3 Celestial Events Record
This is defined as follows:
CelestialEvents ::= RECORD
{CelestialBodiesPosition EPHEMERIS -- See below for definition
RelationToImage RECORD
{TypeofEclipse ENUMERATED BYTE
{None (0),
Sun (1),
Moon (2)},
EclipseStartTime TIME CDS SHORT,
EclipseEndTime TIME CDS SHORT,
VisibleBodiesInImage ENUMERATED BYTE
{None (0),
Sun (1),
Moon (2),
Sun and Moon (3)},
BodiesClosetoFOV ENUMERATED BYTE
{None (0),
Sun (1),
Moon (2),
Sun and Moon (3)},
ImpactOnImageQuality ENUMERATED BYTE
{None (0),
Radiometric (1),
Geometric (2)}}}

TypeofEclipse indicates if there has been or will be an Eclipse in the near past or the future (+/-12 Hours) and the
type of eclipse if relevant (‘Sun’ or ‘Moon’). If ‘None’, then the contents of the fields

EclipseStartTime and EclipseEndTime will be undefined.

EclipseStartTime gives the start time of the eclipse. If the eclipse was in the past then this will be the actual start
time of the eclipse, and if in the future then it will be the predicted time. Time is accurate to better than 1 second.

EclipseEndTime gives the start time of the eclipse. If the eclipse was in the past then this will be the actual start
time of the eclipse, and if in the future then it will be the predicted time. Time is accurate to better than 1 second.

VisibleBodiesInImage indicates which celestial bodies are visible in the image.

BodiesClosetoFOV indicates what bodies are close to the field of view.

ImpactOnImageQuality indicates possible impact on the image.

EPHEMERIS is defined as follows:
EPHEMERIS::=RECORD
{PeriodStartTime TIME CDS SHORT,
PeriodEndTime TIME CDS SHORT,
RelatedOrbitFileTime TIME GENERALIZED,
RelatedAttitudeFileTime TIME GENERALIZED,
EarthEphemeris ARRAY SIZE (1..100) OF EARTHMOONSUNCOEF
MoonEphemeris ARRAY SIZE (1..100) OF EARTHMOONSUNCOEF
SunEphemeris ARRAY SIZE (1..100) OF EARTHMOONSUNCOEF
StarEphemeris ARRAY SIZE (1..100) OF STARCOEF}

PeriodStartTime gives the start time of the coverage for data in this record.

<!-- source_page: 94 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 94 of 129

PeriodEndTime gives the end time of the coverage for data in this record.

RelatedOrbitFileTime gives the time of creation of corresponding orbit file.

RelatedAttitudeFileTime gives the time of creation of corresponding attitude file.

EarthEphemeris is a fixed length array containing Earth ephemeris data. Unused array elements are filled with
zeros.

MoonEphemeris is a fixed length array containing Moon ephemeris data. Unused array elements are filled with
zeros.

SunEphemeris is a fixed length array containing Sun ephemeris data. Unused array elements are filled with zeros.

StarEphemeris is a fixed length array containing Star ephemeris data. Unused array elements are filled with
zeros.

EARTHMOONSUNCOEF is defined as follows:
EARTHMOONSUNCOEF ::= RECORD
{StartTime TIME CDS SHORT,
EndTime TIME CDS SHORT,
AlphaCoef ARRAY SIZE (8) OF REAL DOUBLE,
BetaCoef ARRAY SIZE (8) OF REAL DOUBLE}

StartTime gives the start time for the coefficient set validity. StartTime of set N is always greater than StartTime
of set N-1.

EndTime gives the end time for the coefficient set validity. EndTime of set N is always greater than EndTime of
set N-1).

AlphaCoef and BetaCoef are the Chebychev polynomial coefficients that give the position of the Earth, Moon
or Sun in the Spacecraft Frame. The relation between the Earth, Moon or Sun position and time is provided by a
Chebychev polynomial. For each of the arrays, the in dex 0 coefficient contains the degree 0 coefficient of the
Chebychev polynomial, the index 1 coefficient contains the degree 1 coefficient of the Chebychev polynomial,
etc…

The alpha and beta coordinates of Earth and Moon are given relative to the spacecr aft frame at the time of the
predicted position.

The position of the Sun will be provided in a slightly modified alpha and beta format. The beta will be the
declination in the satellite based coordinate frame as above. However, the alpha value given for t he Sun position
will, in this case, be the angle of rotation about the satellite spin axis (Z axis) from the Earth centre to the Sun
centre.

STARCOEF is defined as follows:
STARCOEF ::= ARRAY SIZE (1..20) OF RECORD
{StarId UNSIGNED SHORT
StartTime TIME CDS SHORT,
EndTime TIME CDS SHORT,
AlphaCoef ARRAY SIZE (8) OF REAL DOUBLE,
BetaCoef ARRAY SIZE (8) OF REAL DOUBLE}

StarId gives the ID of the star to which this record corresponds. The details of mapping this ID to a specific star
are given in Table 4.

ID Star
1 Rigel

<!-- source_page: 95 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 95 of 129

2 Procyon
3 Betelgeuse
4 Alphard
5 Altair
6 Bellatrix
7 Alnilam
8 Alnitak
9 Yed Prior
10 Mintaka
11 53KapOri
12 Zubeneschamali
13 Sadalsuud
14 67BetEri
15 Porrima
16 Sadalmelik
17 Menkar
18 Cebelrai
19 Unukalhai
20 Enif

Table 4 - Star Identifier Conversion
StartTime gives the start time for the coefficient set validity. StartTime of set N is always greater than StartTime
of set N-1

EndTime gives the end time for the coefficient set validity. EndTime of set N is always greater than EndTime of
set N-1)

AlphaCoef and BetaCoef are the Chebychev polynomial coefficients that give the position of the stars in the
Spacecraft Frame at the time of the predicted position. The relation between the stars position and time is provided
by a Chebychev polynomial. For each of the arrays, the index 0 coefficient contains the degree 0 coefficient of
the Chebychev polynomial, the index 1 coefficient contains the degree 1 coefficient of the Chebychev polynomial,
etc…

7.2.4 Image Description Record
This is defined as follows:
ImageDescription ::= RECORD
{ProjectionDescription RECORD
{TypeOfProjection ENUMERATED BYTE
{Geostationary, Earth centred in grid (1)},
LongitudeOfSSP REAL},
ReferenceGridVIS_IR RECORD
{NumberOfLines INTEGER,
NumberOfColumns INTEGER,
LineDirGridStep REAL,
ColumnDirGridStep REAL,
GridOrigin ENUMERATED BYTE
{North-West corner (0),
South-West corner (1),
South-East corner (2),
North-East corner (3)}},
ReferenceGridHRV RECORD
{NumberofLines INTEGER,
NumberOfColumns INTEGER,
LineDirGridStep REAL,
ColumnDirGridStep REAL,
GridOrigin ENUMERATED BYTE

<!-- source_page: 96 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 96 of 129

{North-West corner (0),
South-West corner (1),
South-East corner (2),
North-East corner (3)}},
PlannedCoverageVIS_IR RECORD
{SouthernLinePlanned INTEGER,
NorthernLinePlanned INTEGER,
EasternColumnPlanned INTEGER,
WesternColumnPlanned INTEGER},
PlannedCoverageHRV RECORD
{LowerSouthLinePlanned INTEGER,
LowerNorthLinePlanned INTEGER,
LowerEastColumnPlanned INTEGER,
LowerWestColumnPlanned INTEGER,
UpperSouthLinePlanned INTEGER,
UpperNorthLinePlanned INTEGER,
UpperEastColumnPlanned INTEGER,
UpperWestColumnPlanned INTEGER},
Level 1_5 ImageProduction RECORD
{ImageProcDirection ENUMERATED BYTE
{North-South (0),
South-North (1)},
PixelGenDirection ENUMERATED BYTE
{East-West (0),
West-East (1)},
PlannedChanProcessing ARRAY SIZE (1..12) OF ENUMERATED BYTE
{Channel not processed (0),
Channel processed in spectral radiance (1),
Channel processed in effective radiance (2)},

}

ProjectionDescription:

TypeOfProjection gives the type of projection used for the Level 1.5 image generation. The type ‘Enumerated
Byte’ has been used to allow future upgrades.

LongitudeOfSSP is notional longitude used for image projection. (Provided in degrees from the Greenwich
Meridian and a positive value corresponds to a position East of it, a negative value to the West.). This is not to be
confused with the real satellite position, nor with the position of the satellite station keeping box on the
geostationary ring, both provided in the SatelliteStatus Record. Note, that LongitudeOfSSP indeed c an be
different from the nominal satellite longitude (e.g. a spare satellite located nominally at +3.5° might be used to
generate the Level 1.5 image for the main mission, but the image would be pro jected to 0° longitude).
LongitudeOfSSP field is only relevant to certain projection types (identified by TypeOfProjection).

ReferenceGridVIS_IR:

This record gives details of the reference grid for the VIS and IR channels.

NumberOfLines gives the number of lines in the reference grid for VIS and IR. Maximum possible value for
VIS and IR is 3712.

NumberOfColumns gives the number of columns in the reference grid for VIS and IR. The NumberOfColumns
has a fixed value of 3712.

<!-- source_page: 97 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 97 of 129

LineDirGridStep gives the grid step size in km SSP in the line direction. Default value is 3km for VIS and IR,
and 1km for HRV. The on-ground grid step size of 3 km at the SSP represents an instrument scan step of 251.53
microrad divided by 3.

ColumnDirGridStep gives the grid step si ze in km SSP in the column direction. Default value as for
‘LineDirGridStep’.

GridOrigin gives the reference grid origin: North -West corner, South -West corner, South -East corner, North -
East corner. Operations default is the South-East corner. The origin has the coordinates (1,1).

ReferenceGridHRV:

This record gives details of the reference grid for the HRV channel. The individual fields in this record are the
same as those in the ReferenceGridVIS_IR record defined above.

PlannedCoverageVIS_IR:

This record gives details of the planned Level 1.5 coverage with respect to the grid definition for the VIS and IR
channels. The details of each field are given below.

SouthernLinePlanned is the planned southern line number, taking a value in the range 1 to 37 12.

NorthernLinePlanned is the planned northern line number, taking a value in the range 1 to 3712.

EasternColumnPlanned is the planned eastern column number, always taking the value 1.

WesternColumnPlanned is the planned western column number, always taking the value 3712.

Note that the number of column pixel per line for the VIS and IR channels is always 3712.

PlannedCoverageHRV:

This record gives details of the planned coverage Level 1.5 coverage for the HRV channel. The component fields
are the same as those for the record PlannedCoverageVIS_IR, with the difference that the line and column
bounds are given for each of the two areas constituting the scan, i.e. the lower and the upper areas. The terms
‘lower’ and ‘upper’ refer to the line numbering in respect to the reference grid, i.e. ‘lower’ means the area with
the lower line numbers, ‘upper’ the one with higher line numbers.

LowerSouthernLinePlanned is the planned southern line number, taking a value in the range 1 to 11136.

LowerNorthernLinePlanned is the planned northern line number, taking a value in the range 1 to 11136.

LowerEasternColumnPlanned is the planned eastern column number, taking a value in the range 1 to 5569.

LowerWesternColumnPlanned is the planned western column number, taking a value in the range 5568 to
11136.

UpperSouthernLinePlanned is the planned southern line number, taking a value in the range 1 to 11136.

UpperNorthernLinePlanned is the planned northern line number, taking a value in the range 1 to 11136.

UpperEasternColumnPlanned is the planned eastern column number, taking a value in the range 1 to 5569.

UpperWesternColumnPlanned is the planned western column number, taking a value in the range 5568 to
11136.

Note, that the number of column pixel per line for the HRV channel is always 5568.

<!-- source_page: 98 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 98 of 129


Level 1_5 ImageProduction:

ImageProcDirection defines the direction of the production of the Level 1.5 image in real -time, this
corresponding to the actual scanning direction by the Radiometer.

PixelGenDirection defines the direction of the generation of the pixels, therefore indicating if the first pixel in a
line in the most Eastern or Western one. The default is the most Eastern pixel.

PlannedChanProcessing is an array whose elements indicate for each channel if it is planned to derive 1.5 data
from the received data and what the representation of the data is. If a channel is not processed, this is indicated
by a 0, if it is processed, but in spectral radiance, then it is set to 1, in effective radiance to 2. Users are reminded
that information on r adiometric processing is also provided in the RPSummary record of the Radiametric
Processing record.

7.2.5 Radiometric Processing Record
This is defined as follows:
RadiometricProcessing ::= RECORD
{RPSummary RECORD
{RadianceLinearization ARRAY SIZE (1..12) OF BOOLEAN BYTE,
DetectorEqualization ARRAY SIZE (1..12) OF BOOLEAN BYTE,
OnboardCalibrationResult ARRAY SIZE (1..12) OF BOOLEAN BYTE,
MPEFCalFeedback ARRAY SIZE (1..12) OF BOOLEAN BYTE,
MTFAdaptation ARRAY SIZE (1..12) OF BOOLEAN BYTE,
StraylightCorrectionFlag ARRAY SIZE (1..12) OF BOOLEAN BYTE},
Level1_5ImageCalibration ARRAY SIZE (1..12) OF RECORD
{Cal_Slope REAL DOUBLE,
Cal_Offset REAL DOUBLE},
BlackBodyDataUsed RECORD
{BBObservationUTC TIME CDS EXPANDED,
BBRelatedData RECORD
{OnBoardBBTime TIME CUC SIZE (4,3),
MDUOutGain ARRAY SIZE (1..42) OF UNSIGNED SHORT
MDUCoarseGain ARRAY SIZE (1..42) OF BYTE,
MDUFineGain ARRAY SIZE (1..42) OF UNSIGNED SHORT,
MDUNumericalOffset ARRAY SIZE (1..42) OF UNSIGNED SHORT,
PUGain ARRAY SIZE (1..42) OF UNSIGNED SHORT,
PUOffset ARRAY SIZE (1..27) OF UNSIGNED SHORT,
PUBias ARRAY SIZE (1..15) OF UNSIGNED SHORT,
DCRValues ARRAY SIZE (1..42) OF BITSTRING SIZE (12),
X_DeepSpaceWindowPosition ENUMERATED BYTE
{no delay (0),
predefined delay no. 1 (1),
predefined delay no. 2 (2),
predefined delay no. 3 (3)},
ColdFPTemperature RECORD
{FCUNominalColdFocalPlaneTemp UNSIGNED SHORT,
FCURedundantColdFocalPlaneTemp UNSIGNED SHORT},
WarmFPTemperature RECORD
{FCUNominalWarmFocalPlaneVHROTemp UNSIGNED SHORT,
FCURedundantWarmFocalPlaneVHROTemp UNSIGNED SHORT},
ScanMirrorTemperature RECORD
{FCUNominalScanMirrorSensor1Temp UNSIGNED SHORT,
FCURedundantScanMirrorSensor1Temp UNSIGNED SHORT,
FCUNominalScanMirrorSensor2Temp UNSIGNED SHORT,
FCURedundantScanMirrorSensor2Temp UNSIGNED SHORT},

<!-- source_page: 99 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 99 of 129

M1M2M3Temperature RECORD
{FCUNominalM1MirrorSensor1Temp UNSIGNED SHORT,
FCURedundantM1MirrorSensor1Temp UNSIGNED SHORT,
FCUNominalM1MirrorSensor2Temp UNSIGNED SHORT,
FCURedundantM1MirrorSensor2Temp UNSIGNED SHORT,
FCUNominalM23AssemblySensor1Temp BYTE,
FCURedundantM23AssemblySensor1Temp BYTE,
FCUNominalM23AssemblySensor2Temp BYTE,
FCURedundantM23AssemblySensor2Temp BYTE},
BaffleTemperature RECORD
{FCUNominalM1BaffleTemp UNSIGNED SHORT,
FCURedundantM1BaffleTemp UNSIGNED SHORT},
BlackBodyTemperature RECORD
{FCUNominalBlackBodySensorTemp UNSIGNED SHORT,
FCURedundantBlackBodySensorTemp UNSIGNED SHORT},
FCUMode RECORD
{FCUNominalSMMStatus BITSTRING SIZE (16),
FCURedundantSMMStatus BITSTRING SIZE (16)},
ExtractedBBData ARRAY SIZE (1..12) of RECORD
{NumberOfPixelsUsed UNSIGNED,
MeanCount REAL,
RMS REAL,
MaxCount UNSIGNED SHORT,
MinCount UNSIGNED SHORT,
BB_Processing_Slope REAL DOUBLE,
BB_Processing_Offset REAL DOUBLE}},
MPEFCalFeedback IMPF_CAL_Data, -- See below for definition
RadTransform ARRAY SIZE (1..42) of ARRAY SIZE (1..64) of REAL,
RadProcMTFAdaptation RECORD
{VIS_IRMTFCorrectionE_W ARRAY SIZE (1..33) OF
ARRAY SIZE (1..16) of REAL,
VIS_IRMTFCorrectionN_S ARRAY SIZE (1..33) OF
ARRAY SIZE (1..16) of REAL,
HRVMTFCorrectionE_W ARRAY SIZE (34..42) OF
ARRAY SIZE (1..16) of REAL,
HRVMTFCorrectionN_S ARRAY SIZE (34..42) OF
ARRAY SIZE (1..16) of REAL,
StraylightCorrection ARRAY SIZE (1..12) OF
ARRAY SIZE (1..8) OF
ARRAY SIZE (1..8) of REAL}

RPSummary:

RadianceLinearization is an array with one element per channel indicating if the linearization of the radiance
response has been applied to the channel. ‘True’ indicates it has been applied.

DetectorEqualization is an array with one element per channel indicating if the equalization of the detector
responses within the channel has been applied to the channel. ‘True’ indicates it has been applied.

OnboardCalibrationResult is an array with one element per channel indicating if the results of the on -board
black-body calibration have been applied to the channel. ‘True’ indicates it has been applied.

MPEFCalFeedback is an array with one element per channel indicating if the calibration feedback information
provided by MPEF has been applied to the channel. ‘True’ indicates it has been applied.

MTFAdaptation is an array with one element per channel indicating if MTF adaptation has been applied to the
channel. ‘True’ indicates it has been applied.

<!-- source_page: 100 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 100 of 129


StraylightCorrectionFlag is an array with one element per channel indicating whether the straylight correction
algorithm is activated for this channel. i.e. whether the image processing system has been configured to make an
attempt at correcting for straylight in that channel. Since the straylight correction is usually permanently activated
for the 3.9 channel this flag is normally set to TRUE for this channel and to FALSE for all the other channels. To
find out whether a straylight correction has actually be applied for the cu rrent image, the StraylightCorrection
array in the RadProcMTFAdaptation record (see below) should be checked,

Level1_5ImageCalibration:

An array of records providing calibration information for the Level 1.5 image data, one record per channel.

Cal_Slope is the derived linear calibration coefficient extracted either from the on -board calibration (for IR
channels) or from other sources (e.g. MPEF feedback or external data). The units are mWm-2sr-1(cm-1)-1count-
1.

Cal_Offset is the offset constant between the pixel count and physical radiance extracted either from the on-board
calibration (for IR channels) or from other sources (e.g. MPEF feedback or external data). The units are mWm -
2sr-1(cm-1)-1.

(Physical_Unit = Cal_Offset + Cal_Slope x pixel c ount). Units are spectral radiance i.e. the units are mWm -2sr-
1(cm-1)-1.

BlackbodyDataUsed:

This record defines all parameters used for the blackbody calibration.

OnBoardBBTime gives the on-board time at which blackbody calibration was started. Accuracy is 0.6 seconds.

BBObservationUTC is the UTC time at which calibration was started. Accuracy is 0.6 seconds.

The definition of the detection parameters can be understood from the following relationship:

C is the Counts at the instrument output

EL is the signal coming from the detectors (it includes the dark signal ED)

GPU is the parameter called PUGain in the 1.5 header. There is one value of PUGain per detector (42
values)

OPU is the parameter called PUOffset in the 1.5 header. There is one value of PUOffset per detector
except HRV, VIS0.6 and VIS0.8 (27 values)

I0 is a fixed current.

GMDU-c is the parameter called MDUCoarseGain in the 1.5 header. There is one value of
MDUCoarseGain per detector (42 values)

GMDU-0 is a fixed gain.

     MDUoPULPUcMDUMDUfMDUOutMDUL ODOIOEGGGGGEC   0

<!-- source_page: 101 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 101 of 129

DO is the parameter called DCRValues in the 1.5 header. There is one value of DCRValues per
detector (42 values). Each value is obtained by averaging 2048 values acquired during Deep
Space View.

GMDU-f is the parameter called MDUFineGain in the 1.5 header. There is one value of MDUFineGain
per detector (42 values)

GMDU-Out is the parameter called MDUOutGain in the 1.5 header. There is one value of MDUOutGain per
detector (42 values).

MDUNumericalOffset is the parameter OMDU in the above equation. There is one such value per detector.

PUBias is the bias current that is applied to the Photo Conductive detectors. It modifies their dark signal E D
according to a fixed relationship.

X_DeepSpaceWindow Position is the position in the backscan where the DCRValues have been acquired.
There are three possible positions available, from which one can be selected in order to avoid Sun or Moon
interference; these three windows are defined as delays w.r.t. Start-Of-Line.

FCU temperatures: field names are self-explanatory, and the temperatures are encoded as follows:
ColdFocalPlaneTemp =(float_Temp_in_K) *100)
WarmFocalPlaneVHROTemp =(float_Temp_in_K - 250.0K) *100)
ScanMirrorSensor1Temp =(float_Temp_in_K - 250.0K) *100)
ScanMirrorSensor2Temp =(float_Temp_in_K - 250.0K) *100)
M1MirrorSensor1Temp =(float_Temp_in_K - 250.0K) *100)
M1MirrorSensor2Temp =(float_Temp_in_K - 250.0K) *100)
M1BaffleTemp =(float_Temp_in_K - 250.0K) *100)
M23AssemblySensor1Temp =(float_Temp_in_K - 265.0K) *4)
M23AssemblySensor2Temp =(float_Temp_in_K - 265.0K) *4)
BlackBodySensorTemp =(float_Temp_in_K - 250.0K) *100)

FCUNominalSMMStatus is the SEVIRI general stat us word related to the nominal electronics. It gives the
evidence if during the blackbody calibration and the related image data acquisition there was an event affecting
the image validity or quality. It is generated by IMPF using the TM and the SEVIRI status word contained in the
SEVIRI AUX data at the start of the Repeat Cycle (first line of forward scan).

FCURedundantSMMStatus is the same as FCUNominalSMMStatus, but it applies to the redundant
electronics.

ExtractedBBData:

NumberOfPixelsUsed is the number of the pixels used to calculate the calibration mean counts.

MeanCount is the average fractional counts over the number of pixels used.

RMS is the RMS of the set of pixels used.

MaxCount is the maximum pixel count of the set of pixels used.

MinCount is the minimum pixel count of the set of pixels used.

BB_Processing_Slope is the “raw” linear calibration coefficient derived from the processing of the data acquired
during BB viewing, without any further adaptations or inclusion of feedback. Units are the same as for Cal_Slope.

BB_Processing_Offset is the “raw” offset constant between the pixel count and physical radiance, which results
from the execution of the BB processing, without any further adaptation or inclusion of feedback. Units are the
same as for Cal_Offset.

<!-- source_page: 102 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 102 of 129


MPEFCalFeedback:

This record holds calibration information provided by MPEF for image-processing purposes. The structure of the
record and the definition of individual fields can be found below.

RadTransform is an array of elements, each of which holds 64 equally spaced steps for each of the 42 detectors,
mapping the Level 1.0 digital counts (0-1023) to the REAL (4-byte) representation of the pixel used for the online
processing.

RadProcMTFAdaptation:

VIS_IRMTFCorrectionE_Wis the FIR filter set of coefficients used for MTF adaptation in E-W for each VIS/IR
detector.

VIS_IRMTFCorrectionN_S is the FIR filter set of coefficients used for MTF adaptation in N-S for each VIS/IR
detector.

HRVMTFCorrectionE_W is the FIR filter set of coefficients used for MTF adaptation in E -W for each HRV
detector.

HRVMTFCorrectionN_S is the FIR filter set of coefficients used for MTF adaptation in N -S for each HRV
detector.

StraylightCorrection is an 8x8 array of Chebyshev coefficients
l
kc that define a 2D Chebyshev polynomial for
the stray light correction as a function of the radiometer position and the E -W Level 1.0 pixel location (so called
Level 1.0 Coordinate Frame, see Appendix C). The array describes the correction that is actually applied. Hence,
if the image processing system is not configured to perform a correction for the channel or if the channel is
believed to be free of straylight the n, the coefficients are zero. To just find out whether any straylight correction
is actually is applied; it is sufficient check whether the fist Chebyshev is different from zero. For details on the
decoding, refer to the Appendix.

IMPF_CAL_Data is defined as follows:
IMPF_CAL_Data ::= ARRAY SIZE (1..12) OF RECORD
{ImageQualityFlag ENUMERATED BYTE
{IMPF Cal OK (0),
Dubious IMPF Cal (1),
Use MPEF Cal (2)},
ReferenceDataFlag ENUMERATED BYTE
{Not calculated (0),
Met data (1),
FSD (2),
Mixed MET and FSD (3)},
AbsCalMethod ENUMERATED BYTE
{Not changed (0),
External (1),
Vicarious (2),
Cross-satellite (3),
Mixed vic & xsat (4)},
Pad1 CHARACTERSTRING SIZE(1),
AbsCalWeightVic REAL,
AbsCalWeightXsat REAL,
AbsCalCoeff REAL,
AbsCalError REAL,
GSICSCalCoeff REAL,
GSICSCalError REAL,

<!-- source_page: 103 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 103 of 129

GSICSOffsetCount REAL}

Unused array elements of IMPF_CAL_Data are filled with zeros.

ImageQualityFlag indicates whether or not the calibration of the Level 1.5 Data is considered good, i.e. whether
the MPEF supplied absolute calibration coefficients should be substituted for those being used by the IMPF.

ReferenceDataFlag indicates the data source for th e absolute calibration e.g. meteorological forecast (for the
window channels) or observation (non -windows) data, foreign satellite data, or a mixture of meteorological and
FSD data.

AbsCalWeightVic and AbsCalWeightXsat are normalised coefficients.

AbsCalMethod defines the method used for instantaneous absolute calibration. When absolute calibration has
not been performed for a specific channel during the repeat cycle the AbsCalMethod will be set to (Not changed)
and AbsCalCoeff will retain its most recently derived value. If VIS/NIR/HRVIS coefficients have been manually
input to the system at the start of the repeat cycle the AbsCalMethod will be set to (External).
AbsCalCoeff represents the absolute calibration coefficient determined by MPEF. The units are mWm-2sr-1(cm-
1)-1count-1.

AbsCalError represents the accuracy of the absolute calibration coefficient determined by MPEF. The units are
mWm-2sr-1(cm-1)-1count-1.

GSICSCalCoeff represents the calibration derived from the cross -calibration according to t he GSICS NRT
requirements. The units are mWm-2sr-1(cm-1)-1.

GSICSCalError represents the RMSE of the GSICS cross calibration coefficient in units of mWm-2sr-1(cm-1)-1.

GSICSOffsetCount is equivalent to the calibration offset derived from the GSICS cross -calibration, converted
to counts. The sign convention is so that GSICSOffsetCount is equal to the NEGATIVE value of the level 1.5
count corresponding to zero radiance.


7.2.6 GeometricProcessing Record
This is defined as follows:
GeometricProcessing ::= RECORD
{OptAxisDistances RECORD
{E-WFocalPlane ARRAY SIZE (1..42) OF REAL,
N-SfocalPlane ARRAY SIZE (1..42) OF REAL},
EarthModel RECORD
{TypeOfEarthModel ENUMERATED BYTE
{Ellipsoid with Rpn Rps Req (1)},
EquatorialRadius REAL DOUBLE,
NorthPolarRadius REAL DOUBLE,
SouthPolarRadius REAL DOUBLE},
AtmosphericModel ARRAY SIZE (1..12) of ARRAY SIZE (1..360) of REAL,
ResamplingFunctions ARRAY SIZE (1..12) of ENUMERATED BYTE
{Windowed Shannon (1),
Bicubic Splines (2),
Nearest Neighbour (3)}}

OptAxisDistances:

E-WFocalPlane gives the distance of the detectors from the optical axis in the East -West direction in km from
the SSP.

<!-- source_page: 104 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 104 of 129


N-SFocalPlane gives the distance of the detectors from the optical axis in the North -South direction in km from
the SSP.

EarthModel:

TypeOfEarthModel gives details of the earth model used by IMPF for navigation. The parameter was only
changed once to indicate the removal of the georeferencing offset (see Section 3.1.4.2).
TypeOfEarthModel:=1 georeferencing offset present (i.e. image shifted wrt GEOS projection)
TypeOfEarthModel:=2 corrected data



EquatorialRadius gives the size of the equatorial radius used by IMPF for the navigation of Level 1.0 to Level
1.5. Units are km.

NorthPolarRadius gives the size of the northern polar radius used by IMPF for the na vigation of Level 1.0 to
Level 1.5.. Units are km.

SouthPolarRadius gives the size of the southern polar radius used by IMPF for the navigation of Level 1.0 to
Level 1.5.. Units are km.

AtmosphericModel:

This is a two dimensional array with elements for each of the channels and 360 elements per channel
corresponding to the apparent atmospheric variation relative to the Earth model, sampled every 10 detector line.

ResamplingFunctions:

This is an array with one element per channel giving the type of Resampling used for the processing. The default
(baseline) resampling function used in IMPF is a 9x9 FIR Shannon interpolation with a Kaiser window. Other
resampling functions (Bicubic Splines 4x4 and Nearest Neighbour) are available for specific use / refe rence.

7.2.7 IMPFConfiguration Record
Note: This record is not disseminated and externally only available via the UMARF. It is
defined as follows:
IMPFConfiguration::=RECORD
{OverallConfiguration RECORD
{Issue UNSIGNED SHORT
Revision UNSIGNED SHORT},
SUDetails ARRAY SIZE (1..50) OF RECORD
{SUId GP_SU_ID,
SUIdInstance BYTE,
SUMode ENUMERATED BYTE
{OFF (0),
ON/Non-Processing (1),
ON/Real-Time Processing (2),
ON/Analysis Mode (3)},
SUState ENUMERATED BYTE
{Error (0),
Nominal (1),
Degraded (2)},
SUConfiguration RECORD
{SWVersion RECORD
{Issue UNSIGNED SHORT
Revision UNSIGNED SHORT},

<!-- source_page: 105 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 105 of 129

InfoBaseVersions ARRAY SIZE (1..10) OF RECORD
{Issue UNSIGNED SHORT
Revision UNSIGNED SHORT}}},
WarmStartParms RECORD
{ScanningLaw ARRAY SIZE (1..1527) OF REAL DOUBLE,
RadFramesAlignment ARRAY SIZE (1..3) OF REAL DOUBLE,
ScanningLawVariation ARRAY SIZE (1..2) OF REAL,
EqualisationParms ARRAY SIZE (1..42) OF RECORD
{ConstCoef REAL,
LinearCoef REAL,
QuadraticCoef REAL},
BlackBodyDataForWarmStart RECORD
{GTotalForMethod1 ARRAY SIZE (1..12) REAL DOUBLE,
GTotalForMethod2 ARRAY SIZE (1..12) REAL DOUBLE,
GTotalForMethod3 ARRAY SIZE (1..12) REAL DOUBLE,
GBackForMethod1 ARRAY SIZE (1..12) REAL DOUBLE,
GBackForMethod2 ARRAY SIZE (1..12) REAL DOUBLE,
GBackForMethod3 ARRAY SIZE (1..12) REAL DOUBLE,
RatioGTotalToGBack ARRAY SIZE (1..12) REAL DOUBLE,
GainInFrontOpticsCont ARRAY SIZE (1..12) REAL DOUBLE,
CalibrationConstants ARRAY SIZE (1..12) OF REAL,
maxIncidentRadiance ARRAY SIZE (1..12) REAL DOUBLE,
TimeOfColdObsSeconds REAL DOUBLE,
TimeOfColdObsNanoSecs REAL DOUBLE,
IncidenceRadiance ARRAY SIZE (1..12) REAL DOUBLE,
TempCal REAL DOUBLE,
TempM1 REAL DOUBLE,
TempScan REAL DOUBLE,
TempM1Baf REAL DOUBLE,
TempCalSurround REAL DOUBLE},
MirrorParameters RECORD
{MaxFeedbackVoltage REAL DOUBLE,
MinFeedbackVoltage REAL DOUBLE,
MirrorSlipEstimate REAL DOUBLE},
LastSpinPeriod REAL DOUBLE,
HKTMParameters RECORD
{TimeS0Packet TIME CDS SHORT,
TimeS1Packet TIME CDS SHORT,
TimeS2Packet TIME CDS SHORT,
TimeS3Packet TIME CDS SHORT,
TimeS4Packet TIME CDS SHORT,
TimeS5Packet TIME CDS SHORT,
TimeS6Packet TIME CDS SHORT,
TimeS7Packet TIME CDS SHORT,
TimeS8Packet TIME CDS SHORT,
TimeS9Packet TIME CDS SHORT,
TimeSYPacket TIME CDS SHORT,
TimePSPacket TIME CDS SHORT},
WSPReserved OCTETSTRING SIZE (3408)}}

This record is intended to hold all data pertinent to the production and internal use of Level 1.5 data.

OverallConfiguration

OverallConfiguration is the overall configuration number of IMPF. The following values are used:
Issue 1 = real-time date; 2 = reprocessed data
Revision 0 for real-time data; >0 corresponds to reprocessing run number

<!-- source_page: 106 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 106 of 129



SUDetails:

A fixed length array with one element for each SU/SUInstance in the IMPF processing instance which performed
the processing of the image. The table below provides the mapping between the array indices and the SUs. The
unused array elements are filled with zeros.

Index SU Name
1 SW_Instance_M&C_SU
2 Accept_Data_SEVIRI_SU
3 Accept_Data_HKTM_SU
4 Accept_Data_GERB_SU
5 Accept_Data_FTP_Server_SU
6 RCal_GCal_SU
7 RQA_SU
8 GQA_SU
9 Requantize_Resample_VIS06_SU
10 Requantize_Resample_VIS08_SU
11 Requantize_Resample_IR16_SU
12 Requantize_Resample_IR38_SU
13 Requantize_Resample_WV62_SU
14 Requantize_Resample_WV73_SU
15 Requantize_Resample_IR87_SU
16 Requantize_Resample_IR97_SU
17 Requantize_Resample_IR108_SU
18 Requantize_Resample_IR120_SU
19 Requantize_Resample_IR134_SU
20 Requantize_Resample_HRV_SU
21 Produce_Quicklook_Data_SU
22 Send_Data_SEVIRI_1pt0_SU
23 Send_Data_SEVIRI_1pt5_SU
24 Send_Data_HKTM_SU
25 Send_Data_Raw_GERB_SU
26 Send_Data_Validated_GERB_SU
27 Send_Data_Generated_FD_SU
28 Send_Data_FTP_Client_Put_SU
29 Object_Store_Server_SU

SUId is a unique id used to identify an SU within the IMPF.

SUIdInstance allows to identify uniquely an instantiation of an SU within IMPF.

SUMode gives the mode of the SU at the start of image resampling.

SUState gives the state of the SU at the start of image resampling.

SWVersion gives the software version number of the SU identified by the SUId/SuIdInstance which was
running during this repeat cycle. Note that it is possible to change the versions of SUs during a repeat cycle (by
stopping/starting) the SU so this version may not be the one running at the end of the repeat cycle.

InfoBaseVersions is a fixed length array giving the version numbers for each information base used by the

SUId/ SuIdInstance. If an SU uses less information bases than allowed by the size of this array then, the unused
elements will be filled with zeros

<!-- source_page: 107 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 107 of 129

WarmStartParms:

Contains the state of all the models required for a warm start or the historical reprocessing of the image data. This
is purly internal for image processing facility and is not recommended to be used.

ScanningLaw is an array with one element per number of steps giving the angle of the instrument absolute step.
Units are radians, and possible values are –0.192 to +0.192.

RadFramesAlignment is an array of three elements giving the alignment of the SEVIRI axis to the spin axis.

ScanningLawVariation is an array of two elements, the linear and quadratic coefficients of the Radiometer Scan
Law.

EqualisationParms is an array of 42 records, one per detector.

ConstCoef is the constant coefficient used for equalisation

LinearCoef is the linear coefficient used for equalisation

QuadraticCoef is the quadratic coefficient used for equalisation

BlackBodyDataForWarmStart is an array of 12 records, one for each channel

GTotalForMethod1 is the overall SEVIRI instrument gain for Method1 calibration, G total.

GTotalForMethod2 is the overall SEVIRI instrument gain for Method2 calibration, G total.

GTotalForMethod3 is the overall SEVIRI instrument gain for Method3 calibration, G total.

GBackForMethod1 is the instrument and processing gain as seen by the Black Body for Method 1, G back.

GBackForMethod2 is the instrument and processing gain as seen by the Black Body for Method 2, G back

GBackForMethod3 is the instrument and processing gain as seen by the Black Body for Method 3, Gback.

RatioGTotalToGBack is the ratio of Gtotal to Gback used for Method 3.

GainInFrontOpticsCont is the current estimate of the front optics contribution (g f) used in Method 2.

CalibrationConstants are the value of Kcal used, Kcal = 1/Gtotal for the selected Method.

MaxIncidenceRadiance is an array of 12 elements, the mean linearised channel output corresponding to the
maximum temperature.

TimeOfColdObsSeconds is the start time of the preceding cold Black Body observation.

TimeOfColdObsNanoSecs is nano-second portion of the start time.

IncidenceRadiance is the mean linearised channel output for Black Body cold reading, R cal(Tcold).

TempCal is the temperature of Black Body for cold reading, T cold.

TempM1 is the temperature of the primary mirror for Black Body cold reading, T M1.

TempScan is the temperature of the scan mirror for Black Body cold reading, T scan.

TempM1Baf is the temperature of the primary mirror baffle for Black Body cold reading, T M1baf.

<!-- source_page: 108 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 108 of 129

TempCalSurround is the temperature is the temperature of the black body surroundings for Black Body cold
reading, T*cal.

MaxFeedbackVoltage is the initial value of the mirror potentiometer maximum feedback voltage.

MinFeedbackVoltage is the initial value of the mirror potentiometer minimum feedback voltage.

MirrorSlipEstimate is the initial value of the mirror slip.

LastSpinPeriod is the initial value of spin period.

TimeS0Packet is the time of first S0 packet received for this repeat cycle.

TimeS1Packet is the time of first S1 packet received for this repeat cycle.

TimeS2Packet is the time of first S2 packet received for this repeat cycle.

TimeS3Packet is the time of first S3 packet received for this repeat cycle.

TimeS4Packet is the time of first S4 packet received for this repeat cycle.

TimeS5Packet is the time of first S5 packet received for this repeat cycle.

TimeS6Packet is the time of first S6 packet received for this repeat cycle.

TimeS7Packet is the time of first S7 packet received for this repeat cycle.

TimeS8Packet is the time of first S8 packet received for this repeat cycle.

TimeS9Packet is the time of first S9 packet received for this repeat cycle.

TimeSYPacket is the time of first SY packet received for this repeat cycle.

TimePSPacket is the time of first PS packet received for this repeat cycle.

WSPReserved is reserved space for further Warm-Start Parameters.

<!-- source_page: 109 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 109 of 129

7.3 1.5 VIS/IR Line Record Structure
The packet body assigned to the 15VIS/IRLine service subtype is defined as follows:
15VIS/IRLINE::=RECORD
{15VIS/IRLINEVersion UNSIGNED BYTE (0),
LineSideInfo RECORD
{SatelliteId GP_SC_ID,
TrueRepeatCycleStart TIME CDS EXPANDED,
LineNumberInVIS_IRGrid INTEGER,
ChannelId GP_SC_CHAN_ID,
L10LineMeanAcquisitionTime TIME CDS SHORT,
LineValidity ENUMERATED BYTE
{Not Derived (0),
Nominal (1),
Based on missing data (2),
Based on corrupted data (3),
Based on replaced or interpolated data (4)},
LineRadiometricQuality ENUMERATED BYTE
{Not Derived (0),
Nominal (1),
Usable (2),
Suspect (3),
Do not use (4)},
LineGeometricQuality ENUMERATED BYTE
{Not Derived (0),
Nominal (1),
Usable (2),
Suspect (3),
Do not use (4)}},
LineData ARRAY SIZE (1..3712) OF UNSIGNED (10)}

15VIS/IRLINEVersion is set to zero initially and is used to identify possible future upgrades of this record.

LineSideInfo:

SatelliteId gives the identification of the satellite whose 1.0 data was used to produce this 1.5 data. This ID is
copied by IMPF from the packet sub header of the 1.0 data. Therefore its reliability depends on the configuration
of the PGS when the data was acquired.

TrueRepeatCycleStart is the start time of the current repeat cycle, accurate to within 10 -6seconds.

LineNumberInVIS_IRGrid gives the line number in the VIS/IR grid. Possible value lies in the range 1 to
planned number of lines constituting the planned coverage.

ChannelId gives the channel id to which this line belongs. Possible value lies in the range 1..11 for VIS and IR.

L10LineMeanAcquisitionTime gives the acquisition time of the Level 1.0 image line used to construct this Level
1.5 line. This field contains the mean time of constituent lines when more than one Level 1.0 line was used.

LineValidity indicates the validity of the Level 1.5 line. ‘Based on missing data’ means that a block of missing
data at Level 1.0 intersects this Level 1.5 line and has not been replaced. ‘Based on corrupt data’ means similar,
but the data was corrupt. ‘Based on replaced or interpolate d data’ means that a block of missing or corrupt data
at Level 1.0 intersects this Level 1.5 line and has been replaced by interpolation between data from adjacent Level
1.0 lines.

LineRadiometricQuality indicates the radiometric quality of the line. ‘Useable’ means corrupt or missing data
contributes slightly to some of this line. ‘ Suspect’ means corrupt or missing data is a dominant contribution to
some pixels in this line, but has been successfully replaced by interpolation. ‘Do not use’ means corrupt or missing

<!-- source_page: 110 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 110 of 129

data is a dominant contribution to some pixels in this line and has not been replaced by interpolation since adjacent
data is also suspect.

LineGeometricQuality indicates the geometric quality of the line. The indication values have meanings si milar
to those for LineRadiometricQuality.

LineData:

An array of elements holding the pixels constituting the line data for the specified channel. Each element holds
one pixel value in the range offered by the 10-bit size (i.e. 0..1023).

<!-- source_page: 111 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 111 of 129

7.4 1.5 HRV Line Record Structure
The packet body assigned to the 15HRVLine service subtype is defined as follows:
15HRVLINE::= RECORD
{15HRVLINEVersion UNSIGNED BYTE (0),
LineSideInfo RECORD
{SatelliteId GP_SC_ID,
TrueRepeatCycleStart TIME CDS EXPANDED,
LineNumberInHRVGrid INTEGER,
ChannelId GP_SC_CHAN_ID,
L10LineMeanAcquisitionTime TIME CDS SHORT,
LineValidity ENUMERATED BYTE
{Not derived (0),
Nominal (1),
Based on missing data (2),
Based on corrupted data (3),
Based on replaced or interpolated data (4)},
LineRadiometricQuality ENUMERATED BYTE
{Not derived (0),
Nominal (1),
Usable (2),
Suspect (3),
Do not use (4)},
LineGeometricQuality ENUMERATED BYTE
{Not derived (0),
Nominal (1),
Usable (2),
Suspect (3),
Do not use (4)}},
LineData ARRAY SIZE (1..5568) OF UNSIGNED (10)}

15HRVLINEVersion is set to zero initially and is used to identify possible future upgrades of this record.

The other field names and definitions for 15HRVLINE are the same as those for the 15VIS/IRLINE record
structure, with the following exceptions:

LineNumberInHRVGrid is the field name used instead of LineNumberInVIS_IRGrid.

ChannelId will take the value 12 for HRV.

LineData has 5568 elements instead of 3712, in order to accommodate the HRV data.

<!-- source_page: 112 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 112 of 129

7.5 15TRAILER Record Structure
The packet body assigned to the 15Trailer service subtype is defined as follows:
15TRAILER::=RECORD
{15TRAILERVersion UNSIGNED BYTE (0),
ImageProductionStats_Record ImageProductionStats, -- See below
NavigationExtractionResults_Record NavigationExtractionResults, -- See below
RadiometricQuality_Record RadiometricQuality, -- See below
GeometricQuality_Record GeometricQuality, -- See below
TimelinessAndCompleteness_Record TimelinessAndCompleteness} -- See below

15TRAILERVersion is used to identify possible future upgrades of this record.

7.5.1 Image Production Stats Record
This is defined as follows:
ImageProductionStats ::= RECORD
{SatelliteId GP_SC_ID,
ActualScanningSummary RECORD
{NominalImageScanning BOOLEAN BYTE,
ReducedScan BOOLEAN BYTE,
ForwardScanStart TIME CDS SHORT,
ForwardScanEnd TIME CDS SHORT},
RadiometerBehaviour RECORD
{NominalBehaviour BOOLEAN BYTE,
RadScanIrregularity BOOLEAN BYTE,
RadStoppage BOOLEAN BYTE,
RepeatCycleNotCompleted BOOLEAN BYTE,
GainChangeTookPlace BOOLEAN BYTE,
DecontaminationTookPlace BOOLEAN BYTE,
NoBBCalibrationAchieved BOOLEAN BYTE,
IncorrectTemperature BOOLEAN BYTE,
InvalidBBData BOOLEAN BYTE,
InvalidAuxOrHKTMData BOOLEAN BYTE,
RefocusingMechanismActuated BOOLEAN BYTE,
MirrorBackToReferencePos BOOLEAN BYTE},
ReceptionSummaryStats RECORD
{PlannedNumberOfL10Lines ARRAY SIZE (1..12) OF UNSIGNED,
NumberOfMissingL10Lines ARRAY SIZE (1..12) OF UNSIGNED,
NumberOfCorruptedL10Lines ARRAY SIZE (1..12) OF UNSIGNED,
NumberOfReplacedL10Lines ARRAY SIZE (1..12) OF UNSIGNED},
L15ImageValidity ARRAY SIZE (1..12) OF RECORD
{NominalImage BOOLEAN BYTE,
NonNominalBecauseIncomplete BOOLEAN BYTE,
NonNominalRadiometricQuality BOOLEAN BYTE,
NonNominalGeometricQuality BOOLEAN BYTE,
NonNominalTimeliness BOOLEAN BYTE,
IncompleteL15 BOOLEAN BYTE},
ActualL15CoverageVIS_IR RECORD
{SouthernLineActual INTEGER,
NorthernLineActual INTEGER,
EasternColumnActual INTEGER,
WesternColumnActual INTEGER},
Actual L15CoverageHRV RECORD
{LowerSouthLineActual INTEGER,
LowerNorthLineActual INTEGER,
LowerEastColumnActual INTEGER,
LowerWestColumnActual INTEGER,

<!-- source_page: 113 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 113 of 129

UpperSouthLineActual INTEGER,
UpperNorthLineActual INTEGER,
UpperEastColumnActual INTEGER,
UpperWestColumnActual INTEGER}}

ActualScanningSummary:

This is a record giving summary details of image-taking for this repeat cycle.

NominalImageScanning is a flag that indicates if image-taking was performed in the nominal manner during the
whole repeat cycle. A value of true indicates nominal.

ReducedScan is a flag that indicates if the repeat cycle was a reduced scan. ‘TRUE’ indicates a reduced scan.

ForwardScanStart is the time of the first line of forward scan.

ForwardScanEnd is the time of the last line of forward scan.

RadiometerBehaviour:

This is a record giving details of the behaviour of the radiometer instrument.

NominalBehaviour is a flag indicating if the behaviour of the RADIOMETER instrument was nominal during
the whole of this repeat cycle. A value of true indicates nominal behaviour.

RadScanIrregularity is a flag that indicates if there was a scan irregularity during this repeat cycle. A value of
true indicates that an irregularity occurred.

RadStoppage is a flag that indicates if there was a radiometer stoppage during this repeat cycle. A value of true
indicates that there was a stoppage.

RepeatCycleNotCompleted is a flag that indicates that the repeat cycle was not completed. A value of true
indicates that it was not complete

GainChangeTookPlace is a flag that indicates if a gain change took place during this repeat cycle. A value of
true indicates that it took place.

DecontaminationTookPlace is a flag that indicates if a decontamination took place during this repeat cycle. A
value of true indicates that it took place.

NoBBCalibrationAchieved is a flag that indicates that no BB calibration took place even though it was planned.
A value of true indicates that BB calibration did not take place

IncorrectTemperature is a flag that indicates if the radiometer exhibited an incorrect temperature during this
repeat cycle. A value of true indicates an incorrect temperature.

InvalidBBData is a flag t hat indicates that Blackbody sample data was corrupt and/or inconsistent. A value of
true indicates corrupt/inconsistent.

InvalidAuxorHKTMData is a flag that indicates that AUX and / or HK telemetry data are corrupt and/or
inconsistent. A value of true indicates corrupt/inconsistent.

RefocusingMechanismActuated is a flag that indicates that the refocusing mechanism was activated during this
repeat cycle. A value of true indicates that it was activated.

MirrorBackToReferencePos is a flag that indicates if the scan mirror was moved back to the reference position
during this repeat cycle. A value of true indicates it was moved.

<!-- source_page: 114 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 114 of 129


ReceptionSummaryStats:

PlannedNumberOfL10Lines is an array with one element per channel giving the pla nned number of Level 1.0
lines for this repeat cycle.

NumberOfMissingL10Lines is an array with one element per channel giving the number of missing Level 1.0
lines for this repeat cycle.

NumberOfCorruptedL10Lines is an array with one element per channel giving the number of corrupted Level
1.0 lines for this repeat cycle.

NumberOfReplacedL10Lines is an array with one element per channel giving the number of replaced Level 1.0
lines for this repeat cycle.

L15ImageValidity:

This is an array with one element per channel. Each element is a record giving details of the image validity for
the channel.

NominalImage is a flag that indicates if the Level 1.5 image produced for this repeat cycle is of nominal quality.
‘TRUE’ indicates nominal.

NonNominalBecauseIncomplete is a flag that indicates if the image quality is non nominal due to it being
incomplete. ‘True’ indicates non-nominal.

NonNominalRadiometricQuality is a flag that indicates if the image quality is non n ominal due to bad
radiometric quality. ‘True’ indicates non-nominal.

NonNominalGeometricQuality is a flag that indicates if the image quality is non nominal due to bad geometric
quality. ‘True’ indicates non-nominal.

NonNominalTimeliness is a flag that indicates if the image quality is non nominal due to late arrival of data.
‘TRUE’ indicates non-nominal.

IncompleteL15 is a flag that indicates that not all of the Level 1.5 data was produced.

Actual L15CoverageVIS_IR:

This is a record giving details of the actual coverage for the VIS and IR channels.

SouthernLineActual gives the line number of the southern most line in this Level 1.5 image. Possible values are
within the limit of the planned coverage (info present in the Level 1.5 header).

NorthernLineActual gives the line number of the northern most line in this Level 1.5 image. Possible values are
within the limit of the planned coverage (info present in the Level 1.5 header).

EasternColumnActual gives the column nu mber of the easternmost column in this Level 1.5 image. Possible
values are within the limit of the planned coverage (info present in the Level 1.5 header).

WesternColumnActual gives the column number of the western most column in this Level 1.5 image. Po ssible
values are within the limit of the planned coverage (info present in the Level 1.5 header).

Actual L15CoverageHRV:

<!-- source_page: 115 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 115 of 129

This is a record giving details of the actual coverage for the Level 1.5 HRV channel. The component fields are
the same as those for th record Actual L15CoverageVIS_IR, with the difference that the line and column bounds
are given for each of the two areas constituting the scan, i.e. the Lower and the Upper areas.

7.5.2 Navigation Extraction Results Record
This is defined as follows:
NavigationExtractionResults ::= RECORD
{ExtractedHorizons ARRAY SIZE (1..4) OF HORIZONOBSERVATION, -- See below
ExtractedStars ARRAY SIZE (1..20) OF STAROBSERVATION, -- See below
ExtractedLandmarks ARRAY SIZE (1..50) OF LANDMARKOBSERVATION} -- See below

HORIZONOBSERVATION is defined as follows:
HORIZONOBSERVATION ::= RECORD
{HorizonId ENUMERATED BYTE
{South (0),
North (1),
East (2),
West (3)},
Alpha REAL DOUBLE, -- in Radians
AlphaConfidence REAL DOUBLE, -- confidence interval
Beta REAL DOUBLE, -- in Radians
BetaConfidence REAL DOUBLE, -- confidence interval
ObservationTime TIME CDS, -- time of observation
SpinRate REAL DOUBLE -- at time of observation, in RPM
AlphaDeviation REAL DOUBLE, -- in Radians
BetaDeviation REAL DOUBLE} -- in Radians

Alpha and Beta are the alpha and beta coefficients of the observed horizon position in the Spacecraft Frame as it
exists at the observation time given in ObservationTime. The North and South horizons, as points, lie in the plane
containing the spacecraft, the centre of the Earth reference ellipsoid and the Earth spin axis and are at the points
where a line in this plane passing through the spacecraft are tangential to the Earth ellipsoid . The East and West
horizons are similarly defined but lie in a plane containing the spacecraft and the ellipsoid centre and perpendicular
to the spin axis.

AlphaDeviation and BetaDeviation represent the horizon position error, i.e. the difference between the predicted
and actual observed position, expressed in terms of right ascension and declination in the spacecraft frame.

STAROBSERVATION is defined as follows:
STAROBSERVATION ::= RECORD
{StarId UNSIGNED SHORT,
Alpha REAL DOUBLE, -- in Radians
AlphaConfidence REAL DOUBLE, -- confidence interval
Beta REAL DOUBLE, -- in Radians
BetaConfidence REAL DOUBLE, -- confidence interval
ObservationTime TIME CDS, -- time of observation
SpinRate REAL DOUBLE -- at time of observation, in RPM
AlphaDeviation REAL DOUBLE, -- in Radians
BetaDeviation REAL DOUBLE} -- in Radians

Alpha and Beta are the alpha and beta coefficients of the observed star position in the Spacecraft Frame as it
exists at the observation time given in ObservationTime.

AlphaDeviation and BetaDeviation represent the star position error, i.e. the difference between the predicted
and actual observed position, expressed in terms of right ascension and declination in the spacecraft frame.

<!-- source_page: 116 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 116 of 129

LANDMARKOBSERVATION is defined as follows:
LANDMARKOBSERVATION ::= RECORD
{LandmarkId UNSIGNED SHORT,
LandmarkLongitude REAL DOUBLE, -- in Radians
LandmarkLatitude REAL DOUBLE, -- in Radians
Alpha REAL DOUBLE, -- in Radians
AlphaConfidence REAL DOUBLE, -- confidence interval
Beta REAL DOUBLE, -- in Radians
BetaConfidence REAL DOUBLE, -- confidence interval
ObservationTime TIME CDS, -- time of observation
SpinRate REAL DOUBLE -- at time of observation, in RPM
AlphaDeviation REAL DOUBLE, -- in Radians
BetaDeviation REAL DOUBLE} -- in Radians

Alpha and Beta are the alpha and beta coefficients of the observed landmark position in the Spacecraft Frame as
it exists at the observation time given in ObservationTime. The landmark point whose position is given is the
landmark centre as defined in the reference landmark definition.

AlphaDeviation and BetaDeviation represent the landmark matching error, i.e. the difference between the
predicted and actual observed position, expresse d in terms of right ascension and declination in the spacecraft
frame.

7.5.3 Radiometric Quality Record
This is defined as follows:
RadiometricQuality ::= RECORD
{L10RadQuality ARRAY SIZE (1..42) OF RECORD
{FullImageMinimumCount UNSIGNED SHORT,
FullImageMaximumCount UNSIGNED SHORT,
EarthDiskMinimumCount UNSIGNED SHORT,
EarthDiskMaximumCount UNSIGNED SHORT,
MoonMinimumCount UNSIGNED SHORT,
MoonMaximumCount UNSIGNED SHORT,
FullImageMeanCount REAL,
FullImageStandardDeviation REAL,
EarthDiskMeanCount REAL,
EarthDiskStandardDeviation REAL,
MoonMeanCount REAL,
MoonStandardDeviation REAL,
SpaceMeanCount REAL,
SpaceStandardDeviation REAL,
SESpaceCornerMeanCount REAL,
SESpaceCornerStandardDeviation REAL,
SWSpaceCornerMeanCount REAL,
SWSpaceCornerStandardDeviation REAL,
NESpaceCornerMeanCount REAL,
NESpaceCornerStandardDeviation REAL,
NWSpaceCornerMeanCount REAL,
NWSpaceCornerStandardDeviation REAL,
4SpaceCornersMeanCount REAL,
4SpaceCornersStandardDeviation REAL,
FullImageHistogram ARRAY SIZE (0..255) of UNSIGNED,
EarthDiskHistogram ARRAY SIZE (0..255) of UNSIGNED,
ImageCentreSquareHistogram ARRAY SIZE (0..255) of UNSIGNED,
SESpaceCornerHistogram ARRAY SIZE (0..127) of UNSIGNED,
SWSpaceCornerHistogram ARRAY SIZE (0..127) of UNSIGNED,
NESpaceCornerHistogram ARRAY SIZE (0..127) of UNSIGNED,

<!-- source_page: 117 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 117 of 129

NWSpaceCornerHistogram ARRAY SIZE (0..127) of UNSIGNED,
FullImageEntropy ARRAY SIZE (0..2) of REAL,
EarthDiskEntropy ARRAY SIZE (0..2) of REAL,
ImageCentreSquareEntropy ARRAY SIZE (0..2) of REAL,
SESpaceCornerEntropy ARRAY SIZE (0..2) of REAL,
SWSpaceCornerEntropy ARRAY SIZE (0..2) of REAL,
NESpaceCornerEntropy ARRAY SIZE (0..2) of REAL,
NWSpaceCornerEntropy ARRAY SIZE (0..2) of REAL,
4SpaceCornersEntropy ARRAY SIZE (0..2) of REAL,
ImageCentreSquarePSD_EW ARRAY SIZE (0..127) of REAL,
FullImagePSD_EW ARRAY SIZE (0..127) of REAL,
ImageCentreSquarePSD_NS ARRAY SIZE (0..127) of REAL,
FullImagePSD_NS ARRAY SIZE (0..127) of REAL},
L15RadQuality ARRAY SIZE (1..12) OF RECORD
{FullImageMinimumCount UNSIGNED SHORT,
FullImageMaximumCount UNSIGNED SHORT,
EarthDiskMinimumCount UNSIGNED SHORT,
EarthDiskMaximumCount UNSIGNED SHORT,
FullImageMeanCount REAL,
FullImageStandardDeviation REAL,
EarthDiskMeanCount REAL,
EarthDiskStandardDeviation REAL,
SpaceMeanCount REAL,
SpaceStandardDeviation REAL,
FullImageHistogram ARRAY SIZE (0..255) of UNSIGNED,
EarthDiskHistogram ARRAY SIZE (0..255) of UNSIGNED,
ImageCentreSquareHistogram ARRAY SIZE (0..255) of UNSIGNED,
FullImageEntropy ARRAY SIZE (0..2) of REAL,
EarthDiskEntropy ARRAY SIZE (0..2) of REAL,
ImageCentreSquareEntropy ARRAY SIZE (0..2) of REAL,
ImageCentreSquarePSD_EW ARRAY SIZE (0..127) of REAL,
FullImagePSD_EW ARRAY SIZE (0..127) of REAL,
ImageCentreSquarePSD_NS ARRAY SIZE (0..127) of REAL,
FullImagePSD_NS ARRAY SIZE (0..127) of REAL,
SESpaceCornerL15_RMS REAL,
SESpaceCornerL15_Mean REAL,
SWSpaceCornerL15_RMS REAL,
SWSpaceCornerL15_Mean REAL,
NESpaceCornerL15_RMS REAL,
NESpaceCornerL15_Mean REAL,
NWSpaceCornerL15_RMS REAL,
NWSpaceCornerL15_Mean REAL}}

L10RadQuality:

This is an array containing one record for each detector giving details of radiometric quality for the detector.

FullImageMinimumCount gives the minimum pixel value for the whole image for this channel/detector.

FullImageMaximumCount gives the maximum pixel value for the whole image for this channel/detector.

EarthDiskMinimumCount gives the minimum pixel value within the earth disk for this channel/detector.

EarthDiskMaximumCount gives the maximum pixel value within the earth disk for this channel/detector.

MoonMinimumCount gives the minimum pixel count for the moon image area (0 indicates no statistics
extracted).

<!-- source_page: 118 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 118 of 129


MoonMaximumCount gives the maximum pixel count for the moon image area (0 indicates no statistics
extracted).

FullImageMeanCount gives the mean image count for the full image.

FullImageStandardDeviation gives the standard deviation for the full image.

EarthDiskMeanCount gives the mean image count for the Earth disk.

EarthDiskStandardDeviation gives the standard deviation for the Earth disk.

MoonMeanCount gives the mean count for the moon image area.

MoonStandardDeviation gives the standard deviation for the moon image area.

SpaceMeanCount gives the mean count for the complete space image area.

SpaceStandardDeviation gives the standard deviation for the complete space image area.

SESpaceCornerMeanCount gives the mean count for the SE space corner.

SESpaceCornerStandardDeviation gives the standard deviation for the SE space corner.

SWSpaceCornerMeanCount gives the mean count for the SW space corner.

SWSpaceCornerStandardDeviation gives the standard deviation for the SW space corner.

NESpaceCornerMeanCount gives the mean count for the NE space corner.

NESpaceCornerStandardDeviation gives the standard deviation for the NE space corner.

NWSpaceCornerMeanCount gives the mean count for the NW space corner.

NWSpaceCornerStandardDeviation gives the standard deviation for the NW space corner.

4SpaceCornersMeanCount gives the mean count for all four space corners.

4SpaceCornersStandardDeviation gives the standard deviation for all four space corners.

FullImageHistogram is an array with one element for every f our adjacent count value. Each element contains a
count of the pixels in the full image having the value corresponding to the index for that element.

EarthDiskHistogram is an array with one element for every four adjacent count value. Each element contain s a
count of the pixels in the earth disk having the value corresponding to the index for that element.

ImageCentreSquareHistogram is an array with one element for every four adjacent count value. Each element
contains a count of the pixels in the image c entre square having the value corresponding to the index for that
element.

SESpaceCornerHistogram is an array with one element for every four adjacent count value. Each element
contains a count of the pixels in the SE space corner having the value corresponding to the index for that element.

SWSpaceCornerHistogram is an array with one element for every four adjacent count value. Each element
contains a count of the pixels in the SW space corner having the value corresponding to the index for that element.

NESpaceCornerHistogram is an array with one element for every four adjacent count value. Each element
contains a count of the pixels in the NE space corner having the value corresponding to the index for that element.

<!-- source_page: 119 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 119 of 129


NWSpaceCornerHistogram is an array with one element for every four adjacent count value. Each element
contains a count of the pixels in the NW space corner having the value corresponding to the index for that element.

FullImageEntropy is an array with elements corresponding to entropy of the 0th, 1st and 2nd order containing the
entropy for the full image. The entropy is computed per channel (not per detector) and is then repeated for each
detector composing one channel.

EarthDiskEntropy is an array with elements corresponding to entropy of the 0th, 1st and 2nd order containing the
entropy for the earth disk. The entropy is computed per channel (not per detector) and is then repeated for each
detector composing one channel.

ImageCentreSquareEntropy is an array with elements c orresponding to entropy of the 0 th, 1 st and 2 nd order
containing the entropy for the image centre square. The entropy is computed per channel (not per detector) and is
then repeated for each detector composing one channel.

SESpaceCornerEntropy is an array with elements corresponding to entropy of the 0th, 1st and 2nd order containing
the entropy for the SE space corner. The entropy is computed per channel (not per detector) and is then repeated
for each detector composing one channel.

SWSpaceCornerEntropy is an array with elements corresponding to entropy of the 0 th, 1 st and 2 nd order
containing the entropy for the SW space corner. The entropy is computed per channel (not per detector) and is
then repeated for each detector composing one channel.

NESpaceCornerEntropy is an array with elements corresponding to entropy of the 0 th, 1 st and 2 nd order
containing the entropy for the NE space corner. The entropy is computed per channel (not per detector) and is
then repeated for each detector composing one channel.

NWSpaceCornerEntropy is an array with elements corresponding to entropy of the 0 th, 1 st and 2 nd order
containing the entropy for the NW space corner. The entropy is computed per channel (not per detector) and is
then repeated for each detector composing one channel.

4SpaceCornersEntropy is an array with elements corresponding to entropy of the 0th, 1st and 2nd order containing
the entropy for all four space corners. The entropy is computed per channel (not per detector) and is then repeated
for each detector composing one channel.

ImageCentreSquarePSD_EW gives a sub-sampled version of the accumulated Power Spectral Density (PSD)
over all applicable E-W rows. The PSD is calculated from the sum of the moduli of the Fourier Transform of all
applicable rows. The zeroth element represents the zero spatial frequency component, the next element the
component with spatial wavelength 128 pixels, etc.

FullImagePSD_EW gives the same as for ‘ImageCentreSquarePSD_EW’, but over all EW rows.

ImageCentreSquarePSD_NS gives the same as for ‘ImageCentreSquarePSD_EW’, but for all applicable N -S
columns.

FullImagePSD_NS gives the same as for ‘ImageCentreSquarePSD_NS’, but over all N-S columns.

L15RadQuality:

This is an array containing one record per channel giving details of the radiometric quality for that channel. The
array contains a subset of the fields contained in the array of records ‘10RadQuality’ with the exception of the
following:

The fields xxSpaceCornerL15_RMS and xxSpaceCornerL15_Mean (where xx is SE, SW, NE or NW) provide
the RMS and mean values respectively for the space corners in the Level 1.5 image (equivalent to the area that
would have been pr oduced had a space mask not been applied). The values can be compared with the same
information for Level 1.0 to assess the impact on the noise due to IMPF processing from Level 1.0 to 1.5.

<!-- source_page: 120 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 120 of 129


7.5.4 Geometric Quality Record
This is defined as follows:
GeometricQuality ::= RECORD
{AbsoluteAccuracy ARRAY SIZE (1..12) OF RECORD
{QualityInfoValidity ENUMERATED BYTE
{Not derived (0),
Derived and valid (1),
Derived and invalid (2),
Estimated (3)},
EastWestAccuracyRMS REAL,
NorthSouthAccuracyRMS REAL,
MagnitudeRMS REAL,
EastWestUncertaintyRMS REAL,
NorthSouthUncertaintyRMS REAL,
MagnitudeUncertaintyRMS REAL,
EastWestMaxDeviation REAL,
NorthSouthMaxDeviation REAL,
MagnitudeMaxDeviation REAL,
EastWestUncertaintyMax REAL,
NorthSouthUncertaintyMax REAL,
MagnitudeUncertaintyMax REAL},
RelativeAccuracy ARRAY SIZE (1..12) OF RECORD
{QualityInfoValidity ENUMERATED BYTE
{Not derived (0),
Derived and valid (1),
Derived and invalid (2),
Estimated (3)},
EastWestAccuracyRMS REAL,
NorthSouthAccuracyRMS REAL,
MagnitudeRMS REAL,
EastWestUncertaintyRMS REAL,
NorthSouthUncertaintyRMS REAL,
MagnitudeUncertaintyRMS REAL,
EastWestMaxDeviation REAL,
NorthSouthMaxDeviation REAL,
MagnitudeMaxDeviation REAL,
EastWestUncertaintyMax REAL,
NorthSouthUncertaintyMax REAL,
MagnitudeUncertaintyMax REAL},
500PixelsRelativeAccuracy ARRAY SIZE (1..12) OF RECORD
{QualityInfoValidity ENUMERATED BYTE
{Not derived (0),
Derived and valid (1),
Derived and invalid (2),
Estimated (3)},
EastWestAccuracyRMS REAL,
NorthSouthAccuracyRMS REAL,
MagnitudeRMS REAL,
EastWestUncertaintyRMS REAL,
NorthSouthUncertaintyRMS REAL,
MagnitudeUncertaintyRMS REAL,
EastWestMaxDeviation REAL,
NorthSouthMaxDeviation REAL,
MagnitudeMaxDeviation REAL,
EastWestUncertaintyMax REAL,
NorthSouthUncertaintyMax REAL,

<!-- source_page: 121 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 121 of 129

MagnitudeUncertaintyMax REAL},
16PixelsRelativeAccuracy ARRAY SIZE (1..12) OF RECORD
{QualityInfoValidity ENUMERATED BYTE
{Not derived (0),
Derived and valid (1),
Derived and invalid (2),
Estimated (3)},
EastWestAccuracyRMS REAL,
NorthSouthAccuracyRMS REAL,
MagnitudeRMS REAL,
EastWestUncertaintyRMS REAL,
NorthSouthUncertaintyRMS REAL,
MagnitudeUncertaintyRMS REAL,
EastWestMaxDeviation REAL,
NorthSouthMaxDeviation REAL,
MagnitudeMaxDeviation REAL,
EastWestUncertaintyMax REAL,
NorthSouthUncertaintyMax REAL,
MagnitudeUncertaintyMax REAL},
MisregistrationResiduals ARRAY SIZE (1..12) OF RECORD
{QualityInfoValidity ENUMERATED BYTE
{Not derived (0),
Derived and valid (1),
Derived and invalid (2),
Estimated (3)},
EastWestResidual REAL,
NorthSouthResidual REAL,
EastWestUncertainty REAL,
NorthSouthUncertainty REAL,
EastWestRMS REAL,
NorthSouthRMS REAL,
EastWestMagnitude REAL,
NorthSouthMagnitude REAL,
EastWestMagnitudeUncertainty REAL,
NorthSouthMagnitudeUncertainty REAL},
GeometricQualityStatus ARRAY SIZE (1..12) OF RECORD
{QualityNominal BOOLEAN BYTE,
NominalAbsolute BOOLEAN BYTE,
NominalRelativeToPreviousImage BOOLEAN BYTE,
NominalForREL500 BOOLEAN BYTE,
NominalForREL16 BOOLEAN BYTE,
NominalForResMisreg BOOLEAN BYTE}}

The above structure ‘GeometricQuality’ contains the 4 following top-level arrays:

AbsoluteAccuracy: An array with one record per channel giving the absolute accuracy of the image.

RelativeAccuracy: An array with one record per channel giving the relative accuracy from image to image.

500PixelsRelativeAccuracy: An array with one record per channel giving the relative accuracy within the image
over 500 pixels.

16PixelsRelativeAccuracy: An array with one record per channel giving the relative accuracy within the image
over 16 pixels.

Each of the records in the above arrays contains the following identical fields (note that units are the Level 1.5
grid units, i.e. pixels):

<!-- source_page: 122 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 122 of 129

QualityInfoValidity indicates the whole channel record’s validity. This parameter sho uld be checked before
using the values of any other fields in the record.

EastWestAccuracyRMS gives the E-W component of the image accuracy in RMS terms.

NorthSouthAccuracyRMS gives the N-S component of the image accuracy in RMS terms.

MagnitudeRMS gives the magnitude of the accumulated RMS.

EastWestUncertaintyRMS gives the E-W uncertainty in the accumulated RMS.

NorthSouthUncertaintyRMS gives the N-S uncertainty in the accumulated RMS.

MagnitudeUncertaintyRMS gives the magnitude uncertainty in the accumulated RMS.

EastWestMaxDeviation gives the maximum E-W deviation in the image accuracy.

NorthSouthMaxDeviation gives the maximum N-S deviation in the image accuracy.

MagnitudeMaxDeviation gives the magnitude of the maximum deviation in the image accuracy.

EastWestUncertaintyMax gives the maximum E-W uncertainty factor.

NorthSouthUncertaintyMax gives the maximum N-S uncertainty factor.

MagnitudeUncertaintyMax gives the maximum magnitude uncertainty factor.

The remainder of the structure ‘GeometricQuality’ contains the arrays described below:

MisregistrationResiduals:

This is an array with one record per channel giving misregistration residual information. It contains the following
fields:

QualityInfoValidity indicates the whole channel record’s validity. This parameter should be checked before
using the values of any other fields in the record.

EastWestResidual gives the residual value of the misregistration in the East-West direction.

NorthSouthResidual gives the residual value of the misregistration in the North-South direction.

EastWestUncertainty gives the uncertainty E-W of the misregistration.

NorthSouthUncertainty gives the uncertainty N-S of the misregistration.

EastWestRMS gives the RMS E-W of the misregistration.

NorthSouthRMS gives the RMS N-S of the misregistration.

EastWestMagnitude gives the magnitude E-W of the misregistration.

NorthSouthMagnitude gives the magnitude N-S of the misregistration.

EastWestMagnitudeUncertainty gives the uncertainty factor in the magnitude E-W of the misregistration.

NorthSouthMagnitudeUncertainty gives the uncertainty factor in the magnitude N-S of the misregistration.

GeometricQualityStatus:

<!-- source_page: 123 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 123 of 129


This is an array giving geometric quality status information for each radiometer channel. It contains the following
fields:

QualityNominal is a flag indicating if the quality is nominal. ‘True’ indicates nominal.

NominalAbsolute is a flag indicating if the absolute image accuracy is nominal. ‘True’ indicates nominal.

NominalRelativeToPreviousImage is a flag indicating if the relative (image to image) accuracy is nominal.
‘True’ indicates nominal.

NominalForREL500 is a flag indicating if the relative (500 pixels) image accuracy is nominal. ‘True’ indicates
nominal.

NominalForREL16 is a flag indicating if the relative (16 pixels) image accuracy is nominal. ‘True’ indicates
nominal.

NominalForResMisreg is a flag indicating if the image registration (between spectral bands) is nominal. ‘True’
indicates nominal.

7.5.5 TimelinessAndCompleteness Record
This is defined as follows:
TimelinessAndCompleteness ::= RECORD
{Timeliness RECORD
{MaxDelay REAL,
MinDelay REAL,
MeanDelay REAL},
Completeness RECORD of ARRAY SIZE (1..12) OF RECORD
{PlannedL15ImageLines UNSIGNED SHORT,
GeneratedL15ImageLines UNSIGNED SHORT,
ValidL15ImageLines UNSIGNED SHORT,
DummyL15ImageLines UNSIGNED SHORT,
CorruptedL15ImageLines UNSIGNED SHORT}}

Timeliness:

This is a record presenting the following information concerning delay in output of the Level 1.5 image:

MaxDelay gives the maximum delay, for the whole image, between 1.5 image output and corresponding 1.0 mean
acquisition time in seconds for the whole image.

MinDelay gives the minimum delay, for the whole image, between 1.5 image output and corresponding 1.0 mean
acquisition time in seconds.

MeanDelay gives the mean delay between 1.5 image output and corresponding 1.0 mean acquisition time in
seconds.

Completeness:

This is an array with one element for each channel. For each channel details of the number of missing information
between the planned and the actual coverage of Level 1.5 image and number of missing lines within the actual
coverage are given.

PlannedL15ImageLines gives the planned number of 1.5 image lines for the channel.

<!-- source_page: 124 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 124 of 129

GeneratedL15ImageLines gives the number of generated 1.5 lines for the channel, i.e. the lines that have actually
been produced.

ValidL15ImageLines gives the number of 1.5 lines that are indicated as being valid. A line is valid if the
LineValidity field in the line record indicates nominal.

DummyL15ImageLines gives the number of dummy 1.5 image lines that were produced without corresponding
Level 1.0 data (e.g. due to the data being missing), in order to fill the Level 1.5 format.

CorruptedL15ImageLines gives the number of 1. 5 lines generated using corrupted 1.0 data. A 1.5 line will be
considered as corrupt if any of the 1.0 lines used to construct it are corrupted.

<!-- source_page: 125 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 125 of 129

APPENDIX A DECODING OF A FUNCTI ON IN TERMS OF CHEBY SHEV
COEFFICICIENTS.

Within the L15 Header stricter, many fields are encoded in terms of Chebyshev coefficients.
To reconstruct the function, the following formula can be used.



 
n
k
kks ctTcxf
1
11
2
1)()(

where c1 to c8 are the supplied coefficients, Tk-1(t) is the Chebyshev polynomial for order k-1

Tk(t) is defined by

T0(t) = 1
T1(t) = t
T2(t) = 2t2 - 1
T3(t) = 4t3 -3t

Tn+1(t) = 2tTn(t) - Tn-1(t) n1

and

 
 xstartxend
xstartxendx
t
__2
1
__2
1





where start_x and end_x define the validity interval for the set of Chebyshev coefficients. This
can be a date or something else. In fact, the parameter t only projects the validity interval (time
or other) within the real number interval [-1,1].

; INPUT:
; A, B: [A,B] defines the interval on wich the chebyshev polynomial is defined
; C: A vector containing the chebychech polynomial coefficients
; X: The argument;;




d = 0.0d0
dd = 0.0d0
save = 0.0d0
t = 0.0d0
t2 = 0.0d0
;
M=N_elements(C) ; find the number of coefficients
; ;= the dgree of the polynomial
; calculate the position of the argument x within the interval [A,B]
;
t=X-0.5*(A+B)/(0.5*(B-A))
t2=2*t
;
FOR j=m-1 ,1L,-1L DO BEGIN
save= d

<!-- source_page: 126 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 126 of 129

d = t2 * d - dd + C[j]
dd = save
ENDFOR
RETURN, t * d -dd + 0.5 * C[0]

<!-- source_page: 127 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 127 of 129

APPENDIX B DECODING OF 2 DIMENSIONAL STRAYLIGHT FIELDS

In case of the straylight distribution, the straylight affecting a single image line i is expressed
in terms of 8 Chebyshev coefficients C 1i … C 8i. As the straylight distribution is two
dimensional, these coefficients vary from line to line. To describe the variation of the
coefficients, each of the 8 coefficients is encoded by a second, nested level Chebyshev
approximation. Hence,

Given the 8 x 8 matrix for a specific channel from the level 1.5 header Radiometric Processing
Record:
l
kc . To obtain the straylight correction for the image line i, it is first necessary to derive
the Chebychev coefficients
l
iC for line i, by the nested Chebychev interpolation:




 
8
1
1
11
11
2
1)(
k
kki ctTcC

…


 
8
1
8
11
88
2
1)(
k
kki ctTcC


And

 
 linefirstlinelast
linefirstlinelasti
t
__2
1
__2
1





To calculate the straylight SL on line i ( i.e. for each pixel j on line i), Chebyshev coefficients
C1i … C8i., as calculated above, are used:




 
8
1
1
1
2
1)(),(
l
il
l
i CsTCjiSL

using
 
 pixfirstpixlast
pixfirstpixlastj
s
__2
1
__2
1






For the encoding of the data, the following parameters are used:

first_pix :1
last_pix :3834
first_line :
l15header.IMAGEACQUISITION.RADIOMETERSETTING.SCANFirstLINE * 3 -3

<!-- source_page: 128 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 128 of 129

last_line :
l15header.IMAGEACQUISITION.RADIOMETERSETTING.SCANLastLINE * 3 -3

(For IR39 channel, where currently straylight correction is applied)

The following pseudo code illustrates the decoding:

;
;INPUTfrom L15 header
;
straylightcoeefs= $
L15header.RADIOMETERPROCESSING.MTFADAPTION.STRAYLIGHTCORRECTION[*,*,channel]
first_NonHRV_detline= $
l15header.IMAGEACQUISITION.RADIOMETERSETTING.SCANFirstLINE * 3
last_NonHRV_detline= $
l15header.IMAGEACQUISITION.RADIOMETERSETTING.SCANLastLINE * 3

first_NonHRV_pix = 1L
last_NonHRV_pix = 3834L

; OUTPUT
; this is the actual straylight correction field for each pixel
straylight_array =dblarr(last_NonHRV_pix-first_NonHRV_pix+1 $
,last_NonHRV_detline-first_NonHRV_detline+1)
;
;
; for each line i find the relevant Chebychev coefficients Cl,j
; FOR i=first_SLNonHRV_detline, last_SLNonHRV_detline DO BEGIN
;
coeffs_for_this_line_Clj=dblarr(8)
FOR l=0,7 DO BEGIN
; Chebychev interpolation at position i to get the coefficients of the line

coeffs_for_this_line_Clj(l)= $
MSG_CHEBYSHEV(first_NonHRV_detline), $
last_NonHRV_detline), $
straylightcoeefs[l,*], $
i)
END
;
; having obtained the coefficients, we now can obtain the straylight
; correction for each pixel
;
FOR j=first_NonHRV_pix, last_NonHRV_pix DO BEGIN
straylight_array[j-1,i-1]= $
MSG_CHEBYSHEV(first_NonHRV_pix, $
last_NonHRV_pix $,
coeffs_for_this_line, $
j)
END; j for columns
END ; i for lines

<!-- source_page: 129 -->

EUM/MSG/ICD/105
v8 e-signed, 26 September 2017
MSG Level 1.5 Image Data Format Description


Page 129 of 129

APPENDIX C LEVEL 1.0 CO-ORDINATE FRAME (10CF)

The level 1.0 co-ordinate frame is defined in terms of detector samples and is orientated in the
order of scan. It is referenced to a notional detector at the telescope focal point and is expressed
in terms of 3 km pixels. There are considered to be three detectors on the focal plane with the
same East-West position but displaced North -South with a single 3 km pixel spacing. The
frame is defined at the beginning of each repeat cycle and assumes spin rate is constant at that
applying at the start of the repeat cycle, and that there is no jitter. The North South datum is
the first detector of th e first scan line of the Repeat Cycle. East West each line is defined so
that the centre point of the line corresponds to the instant when a plane containing the MSF Y
and Z axis intersects the Earth ellipsoid centre.

The datum pixel is then the first sample of the most southerly detector for the first scan line of
the image. East-West pixels are in the order within one scan line. The next line North -South
consists of samples from the middle detector of the same scan line, than for the northerly
detector. The next 3 lines are for the next scan line North, etc.
