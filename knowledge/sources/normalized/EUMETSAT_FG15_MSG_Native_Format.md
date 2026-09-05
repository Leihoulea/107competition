# MSG Level 1.5 Native Format File Definition

## Document metadata

- Publisher: EUMETSAT
- Document ID: unknown
- Version: unknown
- Document date: 2002-12-10
- Original file: eumetsat_fg15_msg_native_format.pdf
- Raw SHA-256: 30afd3c2fa4bda3f32ca7081fb63a21ce1343fed4e9f6a7010116b9a43698e76

<!-- source_page: 1 -->

MSG Level 1.5 Native Format
File Definition
File: MSG_native_format_1_5.doc 1 Printed on: 10 December 2002

<!-- source_page: 2 -->

1.1 MSG Level 1.5 Native format
1.1.1 Product file structure :
{OutputProduct} : single file.
1.1.2 Product name :
{OutProductName} = MSGn-{AIID}-15-{AVBA}-{AVPA}-
YYYYMMDDHHMM-OrderId.nat
Example : MSG1-SEVI-15-NA-NA-2000071000-9999.nat
1.1.3 Product internal format :
File: MSG_native_format_1_5.doc 2 Printed on: 10 December 2002

<!-- source_page: 3 -->

1.1.3.1 MSG15 Native format definition
15_MAIN_PRODUCT_HEADER
15_SECONDARY_PRODUCT_HEADER
15HEADER
HEADER first selected line 15SUB_VIS/IRLINE first VIS/IRselected channel
HEADER first selected line 15SUB_VIS/IRLINE last VIS/IRselected channel
HEADER (firstselected line x 3) - 2 15SUB_HRVLINEHRVchannel (if selected)
HEADER (firstselected line x 3) - 1 15SUB_HRVLINEHRVchannel (ifselected)
HEADER (first selected line x 3) 15SUB_HRVLINEHRVchannel (if selected)
HEADER last selected line15SUB_VIS/IRLINEfirst VIS/IR selected channel
HEADER last selected line 15SUB_VIS/IRLINE last VIS/IRselected channel
HEADER (last selected line x 3) - 215SUB_HRVLINE HRV channel(if selected)
HEADER (last selected line x 3) - 115SUB_HRVLINE HRV channel(if selected)
HEADER (last selected line x 3) 15SUB_HRVLINE HRV channel(if selected)

15TRAILER
15HEADER and 15TRAILER are defined in ICD/003 §4.3.
Generic First selected line of selected VIS/IR Last selected line of selected VIS/IR header and HRV channels and HRV channels
Selected lines of selected VIS/IR and HRV channels
File: MSG_native_format_1_5.doc 3 Printed on: 10 December 2002

<!-- source_page: 4 -->

1.1.3.2 HEADER definition
GP_PK_HEADER
GP_PK_SH1
GP_PK_HEADER and GP_PK_SH1 are defined in ICD/003 §4.3.
1.1.3.3 15_MAIN _PRODUCT_HEADER definition
15_MAIN_PRODUCT_HEADER ::= RECORD
{FormatName
FormatDocumentName
FormatDocumentMajorVersion
FormatDocumentMinorVersion
CreationDateTime
CreatingCentre
DataSetIdentification
TotalFileSize
GORT
ASTI
LLOS
SNIT
AIID
SSBT
SSST
RRCC
RRBT
RRST
PPRC
PPDT
GPLV
APNM
AARF
UUDT
QQOV
UDSP
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
ARRAY SIZE(1..27) OF 15_PH_DATA_IDENTIFICATION,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA}
For GORT, ASTI, LLOS, SNIT, AIID, SSBT, SSST, RRCC, RRBT, RRST, PPRC, PPDT, GPLV, APNM, AARF,
UUDT, QQOV, UDSP, these attributes are defined in Appendix B.
Detailed description of the DataSetIdentification array:
Field 1: Main product header identification.
File: MSG_native_format_1_5.doc 4 Printed on: 10 December 2002

<!-- source_page: 5 -->

Filed 2: Second product header identification.
Field 3: Header identification.
Field 4: Image data set identification.
Field 5: Trailer identification.
1.1.3.4 15_SECONDARY _PRODUCT_HEADER definition
15_SECONDARY_PRODUCT_HEADER ::= RECORD
{ABID
SMOD
APXS
AVPA
LSCD
LMAP
QDLC
QDLP
QQAI
SelectedBandIDs
SouthLineSelectedRectangle
NorthLineSelectedRectangle
EastColumnSelectedRectangle
WestColumnSelectedRectangle
NumberLinesVISIR
NumberColumnsVISIR
NumberLinesHRV
NumberColumnsHRV
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA,
15_PH_DATA }
For ABID, SMOD, APXS, AVPA, LSCD, LMAP, QDLC, QDLP, QQAI, these attributes are defined in
Appendix B.
1.1.3.5 15_PH_DATA definition
15_PH_DATA ::= RECORD
CHARACTERSTRING SIZE (30),
{Name CHARACTERSTRING SIZE (50)} Value
File: MSG_native_format_1_5.doc 5 Printed on: 10 December 2002

<!-- source_page: 6 -->

1.1.3.6 15_PH_DATA_IDENTIFICATION definition
15_PH_DATA_IDENTIFICATION ::= RECORD
{Name CHARACTERSTRING SIZE (30),
Size CHARACTERSTRING SIZE (16),
Address CHARACTERSTRING SIZE (16)}
1.1.3.7 15SUB_VIS/IRLINE definition
15SUB_VIS/IRLINE::=RECORD
{15VIS/IRLINEVersion UNSIGNED BYTE (0),
LineSideInfo RECORD
{SatelliteId GP_SC_ID,
TrueRepeatCycleStart TIME_CDS_EXPANDED,
LineNumberInVIS_IRGrid INTEGER,
ChannelId GP_SC_CHAN_ID,
L10LineMeanAcquisitionTime TIME CDS SHORT,
LineValidity ENUMERATED BYTE
{Not Derived (0),
Nominal (1),
Based on missing data (2),
Based on corrupted data (3),

Based on replaced or interpolated data (4)},
LineRadiometricQuality ENUMERATED BYTE {Not Derived (0),
Nominal (1),
Usable (2),
Suspect (3),
Do not use (4)},
LineGeometricQuality ENUMERATED BYTE {Not Derived (0),
Nominal (1),
Usable (2),
Suspect (3),
Do not use (4)},
LineData ARRAY OF UNSIGNED (10)}
LineData size is computed with PacketLength value defined in GP_PK_HEADER defined in
ICD SPE/055 §2.6.21.
File: MSG_native_format_1_5.doc 6 Printed on: 10 December 2002

<!-- source_page: 7 -->

1.1.3.8 15SUB_HRVLINE definition
15SUB_HRVLINE::=RECORD
{15HRVLINEVersion UNSIGNED BYTE (0),
LineSideInfo RECORD
{SatelliteId GP_SC_ID,
TrueRepeatCycleStart TIME_CDS_EXPANDED,
LineNumberInVIS_IRGrid INTEGER,
ChannelId GP_SC_CHAN_ID,
L10LineMeanAcquisitionTime TIME CDS SHORT,
LineValidity ENUMERATED BYTE
{Not Derived (0),
Nominal (1),
Based on missing data (2),
Based on corrupted data (3),
Based on replaced or interpolated data (4)},
LineRadiometricQuality ENUMERATED BYTE {Not Derived (0),
Nominal (1),
Usable (2),
Suspect (3),
Do not use (4)},
LineGeometricQuality ENUMERATED BYTE {Not Derived (0),
Nominal (1),
Usable (2),
Suspect (3),
Do not use (4)},
LineData ARRAY OF UNSIGNED (10)}
LineData size is computed with PacketLength value defined in GP_PK_HEADER defined in
ICD SPE/055 §2.6.21.
File: MSG_native_format_1_5.doc 7 Printed on: 10 December 2002

<!-- source_page: 8 -->

1.1.3.9 Geographic subsetting
1.1.3.9.1 VIS_IR image
Structure of the VIS_IR image:
Here is the general structure of the VIS_IR image for MSG Level 1.5 format.
North
ActualL15CoverageVIS_IR
Actual L15CoverageVIS_IR
Planned CoverageVIS_IR
ReferenceGridVIS_IR
West
Figure 1: VISIR image structure
The difference between the planned and actual lines/columns is due to the rectification process.
Only the number of lines is expected to differ from the "planned".
The actual and planned lines are tilted with respect to each other, because the actual image is
computed into the reference grid geometry. For simplification reasons, this tilt does not appear
on the above diagram.
File: MSG_native_format_1_5.doc 8 Printed on: 10 December 2002

<!-- source_page: 9 -->

The VIS_IR image is defined by:
HEADER.ImageDescription.ReferenceGridVIS_IR
HEADER.ImageDescription.PlannedCoverageVIS_IR
TRAILER.ImageProductionStats.Actual15CoverageVIS_IR
The ReferenceGridVIS_IR is alwa ys 3712x3712 and the origin is defined by GridOrigin whose
value is South-East corner. For Level 1_5, the image scanning is modified according to
ImageProcDirection and PixelGenDirection parameters.
The PlannedCoverageVIS_IR has always 3712 pixels and normally 3712 lines except in case
of ReducedScan
The Actual15CoverageVIS_IR is included in PlannedCoverageVIS_IR
The pixels are defined by:
LineData ARRAY SIZE (1..3712) OF UNSIGNED (10)
LineData[0] = EasternColumnPlanned
LineData[3711] = WesternColumnPlanned
File: MSG_native_format_1_5.doc 9 Printed on: 10 December 2002

<!-- source_page: 10 -->

VIS_IR image in case of geo-subsetting:
North
Geo_subsetting I
II
III
ActualL15CoverageVIS_IR
PlannedCoverageVIS_IR
ReferenceGridVIS_IR
West
Areas definitions:
I: Area out of Planned coverage.
II: Area between Planned coverage and Actual coverage.
III: Actual Image.
Geo subsetting rectangle is defined in ReferenceGridVIS_IR with SE corner origin.
The format output file will cover the complete rectangle of the selected area:
- Area I: This area only exists in case of ReducedScan and thus the missing lines are filled with
- Area II: This area is included in LineData and the pixel value is already 0
- Area III: This area contains the ActualImage
File: MSG_native_format_1_5.doc 10 Printed on: 10 December 2002
0

<!-- source_page: 11 -->

In format output file:
PlannedCoverageVIS_IR parameters are not modified
Actual15CoverageVIS_IR are updated and correspond to area III
ValidL15ImageLines are updated.
File: MSG_native_format_1_5.doc 11 Printed on: 10 December 2002

<!-- source_page: 12 -->

1.1.3.9.2 HRV image
Structure of the HRV image:
Here is the general structure of the HRV image for MSG Level 1.5 format.
North
PlannedUpperCoverageH
PlannedUpperCoverageHRV
UpperActual15CoverageH
UpperActual15CoverageHRV
III III
Geo-subsetting
LowerActual15CoverageH
LowerActual15CoverageHRV
PlannedLowerCoverageH
PlannedLowerCoverageHRV ReferenceGridHR
ReferenceGridHRV
West
West Figure 2: HRV image subsetting
The difference between the planned and actual lines/columns is due to the rectification process.
Only the number of lines is expected to differ from the "planned".
The actual and planned lines are tilted with respect to each other, because the actual image is
computed into the reference grid geometry. For simplification reasons, this tilt does not appear
on the above diagram.
The HRV image is defined by:
File: MSG_native_format_1_5.doc 12 Printed on: 10 December 2002

<!-- source_page: 13 -->

HEADER.ImageDescription.ReferenceGridHRV
HEADER.ImageDescription.PlannedCoverageHRV

TRAILER.ImageProductionStats.Actual15CoverageHRV
The ReferenceGridHRV is always 11136x11136 and the origin is defined by GridOrigin whose
value is South-East corner. For Level1_5, the image scanning is modified according to
ImageProcDirection and PixelGenDirection parameters.
The PlannedCoverageHRV has always 5568 pixels and Upper + Lower areas have normally
11136 lines except in case of ReducedScan.
The Actual15CoverageHRV is included in PlannedCoverageHRV.
The pixels are defined by (Replace Lower by Upper for Upper area):
LineData ARRAY SIZE (1..5568) OF UNSIGNED (10)
LineData[0] = LowerEastColumnPlanned
LineData[5567] = LowerWestColumnPlanned
File: MSG_native_format_1_5.doc 13 Printed on: 10 December 2002

<!-- source_page: 14 -->

HRV image in case of geo-subsetting:
North
PlannedUpperCoverageH
PlannedUpperCoverageHRV
UpperActual15CoverageH
UpperActual15CoverageHRV
III III
III
I I
II
II
Geo-subsetting
I
III
Geo-subsetting
LowerActual15CoverageH
LowerActual15CoverageHRV
PlannedLowerCoverageH
PlannedLowerCoverageHRV ReferenceGridHR
ReferenceGridHRV
West
West Figure 2: HRV image subsetting
Areas definitions:
I: Area out of Planned coverage
II: Area between Planned coverage and Actual coverage. The maximal size is 18 lines.
III: Actual Image
The geographic subsetting is a rectangle defined in the SPH (SECONDARY_PRODUCT_HEADER)
by four parameters:
File: MSG_native_format_1_5.doc 14 Printed on: 10 December 2002

<!-- source_page: 15 -->

SouthLineSelectedRectangle
-
NorthLineSelectedRectangle
-
EastColumnSelectedRectangle
-
WestColumnSelectedRectangle
-
These co-ordinates are defined in ReferenceGridVIS_IR with a Southeast origin. A multiplier
factor of 3 is applied for HRV band to match with the higher definition of this band.
The complete rectangle is delivered in the formatted product. Missing data are filled with 0. The
rectangle is composed with 1, 2 or 3 different areas defined in figures 1 and 2.
- Area I: This area only exists in case of ReducedScan and missing lines are filled with 0
- Area II: This area is included in LineData and the pixel value is already 0
- Area III: This area contains the ActualImage
In format output file:
PlannedCoverageHRV parameters are not modified
Actual15CoverageHRV are updated and correspond to area III.
ValidL15ImageLines are updated.
File: MSG_native_format_1_5.doc 15 Printed on: 10 December 2002
