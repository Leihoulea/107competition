# MSG MPEF Algorithm Specification Document

## Document metadata

- Publisher: EUMETSAT
- Document ID: EUM/MSG/SPE/022
- Version: v7B e-signed
- Document date: 2015-10-23
- Original file: eumetsat_msg_met_products_atbd.pdf
- Raw SHA-256: 2707af6c4f55b8dfc1814e65dba0d7cc551a7536cf18928e52b3a553cb578296

<!-- source_page: 1 -->

© EUMETSAT































Doc.No. : EUM/MSG/SPE/022
Issue : v7B e-signed
Date : 23 October 2015
WBS/DBS :
MSG Meteorological Products Extraction Facility
Algorithm Specification Document



EUMETSAT
Eumetsat-Allee 1, D-64295 Darmstadt, Germany
Tel: +49 6151 807-7
Fax: +49 6151 807 555
http://www.eumetsat.int

<!-- source_page: 2 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Document Change Record
Issue /
Revision
Date DCN. No Changed Pages / Paragraphs
1.0 4/12/96 - First Issue
1.2 4/7/97 EUM/MSG/DCN/070
and
EUM/MSG/DCN/074
The two DCNs cover the changes of the
document from Issue 1.0 to Issue 1.2
2.0 16/3/98 EUM/MSG/DCN/085 See DCN for details
2.1 8/4/98 EUM/MSG/DCN/104 See DCN for details
2.2 19/6/98 EUM/MSG/DCN/143 CLM product added, see DCN for details.
2.3 2/3/98 EUM/MSG/DCN/163 See DCN for details
2.5 17/09/02 EUM/OPS-MSG/DCN/03/0014 See DCN for details – EUM/OPS-
MSG/DCN/03/0014
2.6 01/06/04 Reflects MSG MPEF Release 13.9
2.7 21/11/05 Reflects MSG MPEF Release 14.2
2.8 06/06/06 As detailed in AR 14307.2:
§5.2.1 - First paragraph rephrased for
better clarity.
§5.2.3 - Table "STATIC APPLICATION
DATA - THRESHOLDS AND
PARAMETERS", first parameter:
“thresH” --> “threshold”.
Figure 5-1 SCE Processing: typo “contine”
--> “continue”.
§5.3.2.6 – 2 typos on page: “M-X” -->
“MAX”.
§5.4 – Second table: Scenes types values
“1 to 96” expanded to list each value with
meaning.
§6.3.2.5 – Many instances of typo “then a
threshold” --> “than a threshold”.
§6.4.1 – Second table: Scenes types entry
added to reference or list each value with
meaning.

v3 02/07/07 New products added:
§20 DIV Divergence & §21 FIR Fire.
Corresponding references added to §3.1 &
§3.2.2.
Figure 2-3 updated to include all current
products.
§7 AMV: Extensive updates reflecting

<!-- source_page: 3 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Issue /
Revision
Date DCN. No Changed Pages / Paragraphs
new version 1.8, including height
assignment and target optimisation,
addition of Recursive Filter Function and
Upper Level Divergence.
§18.2.2 Table 18-1 provided with
number/caption.
§3.2.1 Corrections to titles:
World Meteorological Organisation 
World Meteorological Organization
Global Precipitation Centre Project 
Global Precipitation Climatology Project
International Satellite Cloud Climatology
Programme  International Satellite
Cloud Climatology Project
Products SCE, CLA, CDS, TH, SST, TOZ,
CRM: Table ‘Prec’/’Acc’ column values
for sun and satellite zenith angles, which
were variously 0.01, 0.1 or 1, corrected to
10
-6 (in most cases).
CLAI and CTH image products: Mention
of GRIB-2 encoding added.
Calculation of image size corrected from
1238 to 1237 pixels (§6.4.3 for CLAI, §8.4
for CTH).
Appendix C: Acronyms added: EBBT,
GSDPC, ICSU, WRCP.
v3A 15/11/07 §5 Scenes Analysis: Many updates made
throughout the section (for version 1.8).
§6.3.2.3 & §10.3.2: Multiplication sign in
formulae changed from ‘x’ to ‘*’ for
consistency.
v3B 27/12/07 New product added:
§22 MPE Multi-Sensor Precipitation
Estimate.
Corresponding references added to §3.1 &
§3.2.2, and updates to §1.2 and Figure 2-3.
All references to Requirements Spec
documents FRS and FMRS removed by
either deleting or replacing by suitable
alternative as necessary.
Acronym list updated to add many new
entries used in body text; a few others
corrected, or expanded in body text
instead.
v4 16/05/08 EUM/MSG/AR/17182.3
EUM/MSG/AR/17598.2
(with EUM/MSG/AR/14950.4)
EUM/MSG/AR/17715.2
§5 SCE Scenes Analysis: Updates to
channel availability criteria, and to
threshold tests for sunglint and scattering
angle, and addition of high viewing angles.
§6 CLA Cloud Analysis:
§6.3.3 Algorithm Description for Final

<!-- source_page: 4 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Issue /
Revision
Date DCN. No Changed Pages / Paragraphs
CLA clarified;
§6.4.1 Extra value 3 for ‘semi-transp_flag’
of Intermediate CLA Product;
§6.4.2 In table for Final CLA Product,
‘total cloud amount’ replaced by ‘effective
cloud amount’ (AR 17182).
§10 ASR All Sky Radiance product added.
§14 TH Tropospheric Humidity: ‘Missing’
setting if cloudy (AR 17598); ‘number of
cloudy pixels’ changed to ‘percentage of
cloudy pixels’; addition of quality
indicators; some typos.
v4A 01/11/08 ECP 814
EUM/MSG/AR/18113
§16.3.2.2.2 Cross Satellite Cal section
updated.
§2: Mention added of RSS, with new
section 2.2 inserted and updates to sections
2.1, 2.2.2.2, 3.2.2, 5.3.1, 5.3.2.1, 7.3.1,
19.2.2.
Acronym list: RSS added.
§6 CLA: Some values in table in §6.2.2
corrected. In §6.4.1 first table updated to
correct values and remove entries ‘cloud
phase’ and ‘semi-transparency flag’;
second table split into two and second part
rewritten to better describe
CLA_int_quality_flag.
§10.3.1: Step bulleted list numbering
corrected.
§22 FIR: Extensive updates for new Fire
algorithm.
v4B 02/12/08 EUM/MSG/AR/18587,
EUM/MSG/AR/18603
CRM product now derived every 2 h
between 06 & 20 UTC, not just at noon, so
text updates required in §3.2.2 (CRM
para), §5.3.2.7, §20.3.1 and §20.3.2.2.
AMV updates in release 14.8 require
document updates to:
§7.2.3 - new parameters in two new tables,
also existing param ‘max_pres_diff’
moved to new table.
§7.3.2.6 - sentence update.
§7.3.3.2.1 - addition of encoding filter
description (new section).
v4C 13/11/09 ECP 899,
AR 18745,
AR 19113,
AR 19273
§4 RTM: Extensive table and descriptive
updates resulting from replacement of
SYNSATRAD model by RTTOV,
including removal of semi-transparency
v5 16/11/09 §7 AMV: Further updates to tables for
Static Application Data and Final Product.

<!-- source_page: 5 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Issue /
Revision
Date DCN. No Changed Pages / Paragraphs
v5A 22/02/11 ECP 974, AR 19824 New chapters inserted after Scenes Analysis,
for BDRF Table and NDVI Product. NDVI
references added to §3.1 & §3.2.2, Figure 2-3
and Acronyms list.
TOZ: Algorithm description of final product
(now §20.3.2) updated to add also option to use
current repeat cycle. Also final product
segment size is now 3x3 not 32x32 pixels.
GII/RII: GII segment size change – update to
table Value entry and to sentence on horizontal
resolution (§21.2.2).
v5B 01/09/11 STM_DOCET_73 (after
OPS_ECPD_235)
Updates to §20 TOZ & §21 GII (TOZ now
generated as by-product of GII).
§7.4.2 updated for NDVI encoded product
generation.
v6 31/07/12 TBC Update to § 27 for new Volcanic ash Detection
and retrieval product generation specifications.
v6A 09/07/12 Update to §9 for change in AMV algorithm.
Specifically, Sections 9.3.2.5.9 through
9.3.2.5.15 were removed. Section 9.3.2.5
replaced them.
v6B 09/08/12 Formatting changes to match current
specifications for document template
v6C 09/09/12 New version added for configuration control of
document.
v7 28/03/13 Related ECP (ECR220) New sections 9.3.2.5.8 and 9.3.2.5.9 added.
Previous sections 9.3.2.5.8 and 9.3.2.5.9 moved
to new sections 9.3.2.5.10 and 9.3.2.5.11
v7A 20/03/14 Changes to AMV Height Assignment
Algorithm
9.3.2.5.6 Inversion Height Assignment text
changed
9.3.2.5.11 section added (Forecast
Best-Fit Pressure)
Added text to new section 9.3.2.5.12
9.3.3.1.2 Changed algorithm specifications for
Spatial Consistency Test
9.3.3.1.7 Added text to Image Correlation Test
9.4.2 Appended text to Final AMV Product
section
v7B 23/10/15 Related ECP (ECR 535), ECPD 544 Sections 9.3.2.6 and 9.4.2. changed with new
text to describe AMV algorithm.
2.3.2.1 Added the new RTM 2-path
transmission table to the list of RTM output
tables.
3.3 Removed reference to ‘IR’ in RTM, since
the new RTM includes solar affected channels.
Chapter 4 the solar channels are added in the
description of the RTM, since the new version
of RTTOV processes solar and IR channels.
4.2 Updated the version of RTTOV and the
coefficients file used in the RTM.
4.2 The SYNSATRAD specific input
parameters are removed from Tables 3, 4, 5,
and 6. Table 7 is added to include the input
parameters required for the 2-path transmission
table.

<!-- source_page: 6 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Issue /
Revision
Date DCN. No Changed Pages / Paragraphs
4.3.1 Added the solar affected channels
processed by the RTM and added the 2-path
transmission table to the list of generated RTM
tables.
4.3.2.3 Added description of the 2-path
transmission table.
4.4. Added table 11 detailing the output in the
2-path transmission table.
4.5 Ammended the test data and test results.
4.7 Updated the references for the RTTOV 11
documents and the MPEF validation test report.
4.8 Removed SYNSATRAD specific
Mnemonic descriptions from the Symbols and
Description table.

Added new chapter 18 to describe the OCA
product.

9.3.2.5.1 Added text to introduction defining
height assignment and the OCA product
9.3.2.5.3 Revised text describing pixels of the
“cold branch” used to calculate pressure
9.3.2.5.5 Added text for height assignment
9.3.2.5.9.1 Appended text at end of the section
describing EBBT pressure based on CCC using
all pixels.
9.3.2.5.11.2 Changed text defining the
temporary solution adapted for EBBT pressure.
Section 9.4.2 Corrections to Notes in table and
appendage of text at the end of the table.

<!-- source_page: 7 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Table of Contents
1  INTRODUCTION .................................................................................................................. ..... 18 
1.1  Purpose and Scope of the Specification .......................................................................... 18 
1.2  Document Structure ......................................................................................................... 18 
1.3  Purpose of the MPEF ...................................................................................................... 18 
1.4  Related Documents ......................................................................................................... 19 
1.4.1  Applicable Documents ........................................................................................ 19 
1.4.2  Reference Documents ........................................................................................ 19 
1.5  Identification of Requirements in this Document .............................................................. 19 
1.6  Acronyms/Abbreviations and Terms used in this Document ............................................ 19 
2  Introduction to Product Generation ....................................................................................... 23 
2.1  Introduction .................................................................................................................. .... 23 
2.1.1  Terminology ........................................................................................................ 23 
2.2  Rapid Scanning Service .................................................................................................. 24 
2.3  Product Generation Functions ......................................................................................... 24 
2.3.1  Data Preparation ................................................................................................. 25 
2.3.2  Application Data Preprocessing .......................................................................... 26 
2.3.3  Product Processing ............................................................................................. 27 
2.3.4  Product Verification ............................................................................................. 29 
2.3.5  Calibration Support ............................................................................................. 29 
3  Algorithms and Products ....................................................................................................... . 31 
3.1  Overview ...................................................................................................................... ... 31 
3.2  Summary Description of MPEF Products ......................................................................... 32 
3.2.1  Baseline Products ............................................................................................... 32 
3.2.2  New Products ...................................................................................................... 35 
3.2.3  Additional Products ............................................................................................. 37 
3.3  Prototyping ................................................................................................................... ... 38 
3.4  Structure and Interpretation of the Algorithm Specifications ............................................ 38 
4  IR Radiative Transfer Model .................................................................................................... 40 
4.1  Algorithm Configuration Information ................................................................................ 40 
4.1.1  Algorithm Name .................................................................................................. 40 
4.1.2  Algorithm Identifier .............................................................................................. 40 
4.1.3  Algorithm Specification Version History ............................................................... 40 
4.2  Inputs ............................................................................................................................... 40 
4.3  Algorithm Functional Specification ................................................................................... 44 
4.3.1  Overview ............................................................................................................. 44 
4.3.2  Algorithm Description .......................................................................................... 44 
4.3.3  Physical Principles .............................................................................................. 48 
4.3.4  Automatic Quality Control (AQC) ........................................................................ 48 
4.4  Outputs ....................................................................................................................... ..... 48 
4.5  Prototyping and Testing ................................................................................................... 55 
4.5.1  Prototyping .......................................................................................................... 55 
4.5.2  Test Data ............................................................................................................ 55 
4.5.3  Test Results ........................................................................................................ 55 
4.6  Future Enhancements ..................................................................................................... 55 
4.7  References .................................................................................................................... .. 55 
4.8  Symbols and Definitions .................................................................................................. 56 
5  Scenes Analysis ............................................................................................................... ....... 57 
5.1  Algorithm Configuration Information ................................................................................ 57 
5.1.1  Algorithm Name .................................................................................................. 57 
5.1.2  Algorithm Identifier .............................................................................................. 57 
5.1.3  Algorithm Specification Version History ............................................................... 57 
5.2  Inputs ............................................................................................................................... 57 
5.2.1  Image and Preprocessing Data (Dynamic Application Data) ............................... 57

<!-- source_page: 8 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



5.2.2  Data from other MPEF Algorithms (Dynamic Application Data)........................... 59 
5.2.3  Static Application Data ........................................................................................ 60 
5.3  Algorithm Functional Specification ................................................................................... 66 
5.3.1  Overview ............................................................................................................. 66 
5.3.2  Algorithm Description .......................................................................................... 69 
5.3.3  Automatic Quality Control (AQC) ........................................................................ 81 
5.4  Outputs ....................................................................................................................... ..... 82 
5.5  Prototyping and Testing ................................................................................................... 84 
5.5.1  Prototyping .......................................................................................................... 84 
5.5.2  Test Data ............................................................................................................ 84 
5.5.3  Test Results ........................................................................................................ 84 
5.6  Future Enhancements ..................................................................................................... 84 
5.7  References .................................................................................................................... .. 84 
6  BDRF Table Generation ......................................................................................................... . 85 
6.1  Introduction .................................................................................................................. .... 85 
6.2  Semi-empirical BDRF Model ............................................................................................ 85 
6.3  Model inversion ............................................................................................................... 86 
6.4  Table generation .............................................................................................................. 88 
6.5  References .................................................................................................................... .. 88 
7  Normalised Difference Vegetation Index (NDVI) Product Generation ......................... 89 
7.1  Algorithm Configuration Information ................................................................................ 89 
7.1.1  Algorithm Name .................................................................................................. 89 
7.1.2  Algorithm Identifier .............................................................................................. 89 
7.1.3  Algorithm Specification Version History ............................................................... 89 
7.2  Inputs ............................................................................................................................... 89 
7.3  Algorithm Functional Specification ................................................................................... 89 
7.3.1  Overview ............................................................................................................. 89 
7.3.2  Algorithm Description .......................................................................................... 89 
7.3.3  Automatic Quality Control (AQC) ........................................................................ 90 
7.4  Outputs ....................................................................................................................... ..... 90 
7.4.1  Daily product ....................................................................................................... 90 
7.4.2  Encoded product ................................................................................................. 90 
7.5  Future Enhancements ..................................................................................................... 90 
7.6  References .................................................................................................................... .. 90 
8  Cloud Analysis Product Generation ....................................................................................... 91 
8.1  Algorithm Configuration Information ................................................................................ 91 
8.1.1  Algorithm Name .................................................................................................. 91 
8.1.2  Algorithm Identifier .............................................................................................. 91 
8.1.3  Algorithm Specification Version History ............................................................... 91 
8.2  Inputs ............................................................................................................................... 91 
8.2.1  Image and Preprocessing Data (Dynamic Application Data) ............................... 91 
8.2.2  Data from other MPEF Algorithms (Dynamic Application Data)........................... 93 
8.2.3  Static Application Data ........................................................................................ 94 
8.3  Algorithm Functional Specification ................................................................................... 97 
8.3.1  Overview ............................................................................................................. 97 
8.3.2  Algorithm Description for Intermediate CLA ........................................................ 99 
8.3.3  Algorithm Description for the Final CLA Product ............................................... 107 
8.3.4  Algorithm Description for the CLA Image Product ............................................. 107 
8.3.5  Automatic Quality Control (AQC) ...................................................................... 107 
8.4  Outputs ....................................................................................................................... ... 108 
8.4.1  Intermediate CLA Product ................................................................................. 108 
8.4.2  Final CLA Product ............................................................................................. 110 
8.4.3  CLA Image Product ........................................................................................... 112 
8.5  Prototyping and Testing ................................................................................................. 112 
8.6  Future Enhancements ................................................................................................... 112 
8.7  References .................................................................................................................... 112

<!-- source_page: 9 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



9  Atmospheric Motion Vectors Product Generation .............................................................. 113 
9.1  Algorithm Configuration Information .............................................................................. 113 
9.1.1  Algorithm Name ................................................................................................ 113 
9.1.2  Algorithm Identifier ............................................................................................ 113 
9.1.3  Algorithm Specification Version History ............................................................. 113 
9.2  Inputs ............................................................................................................................. 114 
9.2.1  Image and Preprocessing Data (Dynamic Application Data) ............................. 114 
9.2.2  Data from other MPEF Algorithms (Dynamic Application Data)......................... 116 
9.2.3  Static Application Data ...................................................................................... 116 
9.3  Algorithm Functional Specification ................................................................................. 138 
9.3.1  Overview ........................................................................................................... 138 
9.3.2  Algorithm Description ........................................................................................ 141 
9.3.3  Automatic Quality Control (AQC) ...................................................................... 165 
9.3.4  Recursive Filter Function AQC Scheme ............................................................ 172 
9.3.5  Monitoring of the Product Quality ...................................................................... 174 
9.4  Outputs ....................................................................................................................... ... 176 
9.4.1  Intermediate AMV Product ................................................................................ 176 
9.4.2  Final AMV Product ............................................................................................ 178 
9.5  Future Enhancements ................................................................................................... 181 
9.6  References .................................................................................................................... 181 
10  Cloud Top Height Product Generation ................................................................................. 182 
10.1  Algorithm Configuration Information .............................................................................. 182 
10.1.1  Algorithm Name ................................................................................................ 182 
10.1.2  Algorithm Identifier ............................................................................................ 182 
10.1.3  Algorithm Specification Version History ............................................................. 182 
10.2  Inputs ............................................................................................................................. 182 
10.3  Algorithm Functional Specification ................................................................................. 183 
10.3.1  Overview ........................................................................................................... 183 
10.3.2  Algorithm Description ........................................................................................ 183 
10.3.3  Automatic Quality Control (AQC) ...................................................................... 183 
10.4  Outputs ....................................................................................................................... ... 184 
10.5  Prototyping and Testing ................................................................................................. 184 
10.6  Future Enhancements ................................................................................................... 184 
10.7  References .................................................................................................................... 184 
11  Clear Sky Radiances Product Generation ........................................................................... 185 
11.1  Algorithm Configuration Information .............................................................................. 185 
11.1.1  Algorithm Name ................................................................................................ 185 
11.1.2  Algorithm Identifier ............................................................................................ 185 
11.1.3  Algorithm Specification Version History ............................................................. 185 
11.2  Inputs ............................................................................................................................. 185 
11.2.1  Dynamic Application Data ................................................................................. 185 
11.2.2  Static Application Data ...................................................................................... 186 
11.3  Algorithm Functional Specification ................................................................................. 187 
11.3.1  Overview ........................................................................................................... 187 
11.3.2  Automatic Quality Control (AQC) ...................................................................... 189 
11.4  Outputs ....................................................................................................................... ... 190 
11.5  Prototyping and Testing ................................................................................................. 191 
11.6  Future Enhancements ................................................................................................... 191 
11.7  References .................................................................................................................... 191 
12  All Sky Radiances Product Generation ................................................................................ 192 
12.1  Algorithm Configuration Information .............................................................................. 192 
12.1.1  Algorithm Name ................................................................................................ 192 
12.1.2  Algorithm Identifier ............................................................................................ 192 
12.1.3  Algorithm Specification Version History ............................................................. 192 
12.2  Inputs ............................................................................................................................. 192 
12.2.1  Dynamic Application Data ................................................................................. 192

<!-- source_page: 10 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



12.2.2  Static Application Data ...................................................................................... 193 
12.3  Algorithm Functional Specification ................................................................................. 194 
12.3.1  Overview ........................................................................................................... 194 
12.4  Outputs ....................................................................................................................... ... 197 
12.5  Prototyping and Testing ................................................................................................. 198 
12.6  Future Enhancements ................................................................................................... 198 
12.7  References .................................................................................................................... 198 
13  Climate Data Set Product Generation .................................................................................. 199 
13.1  Algorithm Configuration Information .............................................................................. 199 
13.1.1  Algorithm Name ................................................................................................ 199 
13.1.2  Algorithm Identifier ............................................................................................ 199 
13.1.3  Algorithm Specification Version History ............................................................. 199 
13.2  Inputs ............................................................................................................................. 199 
13.2.1  Dynamic Application Data ................................................................................. 199 
13.2.2  Static Application Data ...................................................................................... 200 
13.3  Algorithm Functional Specification ................................................................................. 201 
13.3.1  Overview ........................................................................................................... 201 
13.3.2  Algorithm Description ........................................................................................ 201 
13.3.3  Automatic Quality Control (AQC) ...................................................................... 202 
13.4  Outputs ....................................................................................................................... ... 202 
13.5  Prototyping and Testing ................................................................................................. 203 
13.6  Future Enhancements ................................................................................................... 203 
13.7  References .................................................................................................................... 203 
14  High Resolution PI Product Generation ............................................................................... 204 
14.1  Algorithm Configuration Information .............................................................................. 204 
14.1.1  Algorithm Name ................................................................................................ 204 
14.1.2  Algorithm Identifier ............................................................................................ 204 
14.1.3  Algorithm Specification Version History ............................................................. 204 
14.2  Inputs ............................................................................................................................. 204 
14.3  Algorithm Functional Specification ................................................................................. 205 
14.3.1  Overview ........................................................................................................... 205 
14.3.2  Algorithm Description ........................................................................................ 205 
14.3.3  Automatic Quality Control (AQC) ...................................................................... 206 
14.4  Outputs ....................................................................................................................... ... 206 
14.4.1  Intermediate Product ......................................................................................... 206 
14.4.2  Final Product ..................................................................................................... 207 
14.5  Prototyping and Testing ................................................................................................. 207 
14.6  Future Enhancements ................................................................................................... 207 
14.7  References .................................................................................................................... 207 
15  ISCCP Data Set Product Generation .................................................................................... 208 
15.1  Algorithm Configuration Information .............................................................................. 208 
15.1.1  Algorithm Name ................................................................................................ 208 
15.1.2  Algorithm Identifier ............................................................................................ 208 
15.1.3  Algorithm Specification Version History ............................................................. 208 
15.2  Inputs ............................................................................................................................. 208 
15.3  Algorithm Functional Specification ................................................................................. 211 
15.4  Overview ...................................................................................................................... . 211 
15.4.1  Algorithm Description ........................................................................................ 211 
15.4.2  Automatic Quality Control (AQC) ...................................................................... 212 
15.5  Outputs ....................................................................................................................... ... 213 
15.6  Prototyping and Testing ................................................................................................. 213 
15.7  Future Enhancements ................................................................................................... 213 
15.8  References .................................................................................................................... 213 
16  Tropospheric Humidity Product Generation ....................................................................... 214 
16.1  Algorithm Configuration Information .............................................................................. 214 
16.1.1  Algorithm Name ................................................................................................ 214

<!-- source_page: 11 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



16.1.2  Algorithm Identifier ............................................................................................ 214 
16.1.3  Algorithm Specification Version History ............................................................. 214 
16.2  Inputs ............................................................................................................................. 214 
16.2.1  Dynamic Application Data ................................................................................. 214 
16.3  Algorithm Functional Specification ................................................................................. 215 
16.3.1  Overview ........................................................................................................... 215 
16.3.2  Algorithm Description ........................................................................................ 216 
16.3.3  Automatic Quality Control (AQC) ...................................................................... 217 
16.3.4  Verification of TH .............................................................................................. 218 
16.4  Outputs ....................................................................................................................... ... 219 
16.5  Prototyping and Testing ................................................................................................. 219 
16.5.1  Prototyping ........................................................................................................ 219 
16.5.2  Test Data .......................................................................................................... 220 
16.5.3  Test Results ...................................................................................................... 220 
16.6  Future Enhancements ................................................................................................... 220 
16.7  References .................................................................................................................... 220 
17  Sea Surface Temperature Product Generation ................................................................... 221 
17.1  Algorithm Configuration Information .............................................................................. 221 
17.1.1  Algorithm Name ................................................................................................ 221 
17.1.2  Algorithm Identifier ............................................................................................ 221 
17.1.3  Algorithm Specification Version History ............................................................. 221 
17.2  Inputs ............................................................................................................................. 221 
17.2.1  Dynamic Application Data ................................................................................. 221 
17.2.2  Static Application Data ...................................................................................... 222 
17.3  Algorithm Functional Specification ................................................................................. 222 
17.3.1  Overview ........................................................................................................... 222 
17.3.2  Algorithm Description ........................................................................................ 222 
17.3.3  Automatic Quality Control (AQC) ...................................................................... 223 
17.3.4  SST Verification ................................................................................................ 224 
17.4  Outputs ....................................................................................................................... ... 224 
17.5  Prototyping and Testing ................................................................................................. 224 
17.5.1  Prototyping ........................................................................................................ 224 
17.5.2  Test Data .......................................................................................................... 224 
17.5.3  Test Results ...................................................................................................... 224 
17.6  Future Enhancements ................................................................................................... 224 
18  OPTIMAL CLOUD ANALYSIS PRODUCT generation .......................................................... 225 
18.1  Algorithm Configuration Information .............................................................................. 225 
18.1.1  Algorithm Name ................................................................................................ 225 
18.1.2  Algorithm Identifier ............................................................................................ 225 
18.1.3  Algorithm Specification Version History ............................................................. 225 
18.2  Inputs ............................................................................................................................. 225 
18.2.1  Dynamic Application Data ................................................................................. 225 
18.2.2  Static Application Data ...................................................................................... 227 
18.3  Algorithm Functional Specification ................................................................................. 228 
18.3.1  Overview ........................................................................................................... 228 
18.3.2  Algorithm Description ........................................................................................ 228 
18.3.3  Variable Cloud State Parameters (x) ................................................................. 228 
18.3.4  Fixed Model Parameters (b) .............................................................................. 229 
18.3.5  The Measurements (y) ...................................................................................... 229 
18.3.6  Radiative Transfer Model .................................................................................. 230 
18.3.7  Cost Function .................................................................................................... 230 
18.3.8  Minimising the Cost Function ............................................................................ 230 
18.3.9  Processing mask ............................................................................................... 233 
18.4  Outputs ....................................................................................................................... ... 233 
18.4.1  Final Product ..................................................................................................... 233 
18.4.2  Encoded Products ............................................................................................. 234

<!-- source_page: 12 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



18.5  Future Enhancements ................................................................................................... 234 
18.6  References .................................................................................................................... 234 
19  CALIBRATION SUPPORT ...................................................................................................... 235 
19.1  Algorithm Configuration Information .............................................................................. 235 
19.1.1  Algorithm Name ................................................................................................ 235 
19.1.2  Algorithm Identifier ............................................................................................ 235 
19.1.3  Algorithm Specification Version History ............................................................. 235 
19.2  Inputs ............................................................................................................................. 235 
19.3  Algorithm Functional Specification ................................................................................. 241 
19.3.1  Overview ........................................................................................................... 241 
19.3.2  Algorithm Description ........................................................................................ 241 
19.3.3  Automatic Quality Control (AQC) ...................................................................... 249 
19.4  Outputs ....................................................................................................................... ... 250 
19.5  Prototyping and Testing ................................................................................................. 252 
19.6  Future Enhancements ................................................................................................... 252 
19.7  References .................................................................................................................... 252 
20  Cloud Mask Product Generation .......................................................................................... 253 
20.1  Algorithm Configuration Information .............................................................................. 253 
20.1.1  Algorithm Name ................................................................................................ 253 
20.1.2  Algorithm Identifier ............................................................................................ 253 
20.1.3  Algorithm Specification Version History ............................................................. 253 
20.2  Inputs ............................................................................................................................. 253 
20.3  Algorithm Functional Specification ................................................................................. 253 
20.3.1  Overview ........................................................................................................... 253 
20.3.2  Algorithm Description ........................................................................................ 254 
20.3.3  Automatic Quality Control (AQC) ...................................................................... 254 
20.4  Outputs ....................................................................................................................... ... 254 
20.5  Prototyping and Testing ................................................................................................. 254 
20.6  Future Enhancements ................................................................................................... 254 
20.7  References .................................................................................................................... 254 
21  TOTAL OZONE PRODUCT GENERATION ............................................................................ 255 
21.1  Algorithm Configuration Information .............................................................................. 255 
21.1.1  Algorithm Name ................................................................................................ 255 
21.1.2  Algorithm Identifier ............................................................................................ 255 
21.1.3  Algorithm Specification Version History ............................................................. 255 
21.2  Inputs ............................................................................................................................. 255 
21.3  Algorithm Functional Specification ................................................................................. 255 
21.3.1  Overview ........................................................................................................... 255 
21.3.2  Algorithm Description of the Final TOZ Product ................................................ 255 
21.3.3  Automatic Quality Control (AQC) ...................................................................... 255 
21.4  Outputs ....................................................................................................................... ... 256 
21.4.1  Output of the Final TOZ Product ....................................................................... 256 
21.5  Prototyping and Testing ................................................................................................. 257 
21.6  Future Enhancements ................................................................................................... 257 
21.7  References .................................................................................................................... 257 
22  Global and Regional Instability Indices Products Generation ................................... 258 
22.1  Algorithm Configuration Information .............................................................................. 258 
22.1.1  Algorithm Name ................................................................................................ 258 
22.1.2  Algorithm Identifier ............................................................................................ 258 
22.1.3  Algorithm Specification Version History ............................................................. 258 
22.2  Inputs ............................................................................................................................. 259 
22.2.1  Dynamic Application Data ................................................................................. 259 
22.2.2  Static Application Data ...................................................................................... 261 
22.3  Algorithm Functional Specification ................................................................................. 262 
22.3.1  Overview ........................................................................................................... 262 
22.3.2  Physical Retrieval Average Pixel-Based GII/RII Algorithm Description ............. 263

<!-- source_page: 13 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



22.3.3  Physical Retrieval Method ................................................................................. 264 
22.3.4  Automatic Quality Control (AQC) ...................................................................... 265 
22.3.5  Radiation Model ................................................................................................ 265 
22.4  Outputs ....................................................................................................................... ... 265 
22.5  Future Enhancements ................................................................................................... 266 
22.6  References .................................................................................................................... 266 
23  Clear Sky Reflectance Map ................................................................................................... 267 
23.1  Algorithm Configuration Information .............................................................................. 267 
23.1.1  Algorithm Name ................................................................................................ 267 
23.1.2  Algorithm Identifier ............................................................................................ 267 
23.1.3  Algorithm Specification Version History ............................................................. 267 
23.2  Inputs ............................................................................................................................. 267 
23.3  Algorithm Functional Specification ................................................................................. 267 
23.3.1  Overview ........................................................................................................... 267 
23.3.2  Algorithm Description ........................................................................................ 268 
23.3.3  Automatic Quality Control (AQC) ...................................................................... 268 
23.4  Outputs ....................................................................................................................... ... 268 
23.5  Prototyping and Testing ................................................................................................. 268 
23.6  Future Enhancements ................................................................................................... 268 
23.7  References .................................................................................................................... 268 
24  Divergence Product Generation ........................................................................................... 269 
24.1  Algorithm Configuration Information .............................................................................. 269 
24.1.1  Algorithm Name ................................................................................................ 269 
24.1.2  Algorithm Identifier ............................................................................................ 269 
24.1.3  Algorithm Specification Version History ............................................................. 269 
24.2  Inputs ............................................................................................................................. 269 
24.2.1  Data From Other MPEF Algorithms (Dynamic Application Data) ....................... 269 
24.2.2  Static Application Data ...................................................................................... 269 
24.3  Algorithm Functional Specification ................................................................................. 270 
24.3.1  Overview ........................................................................................................... 270 
24.3.2  Algorithm Description ........................................................................................ 271 
24.3.3  Automatic Quality Control (AQC) ...................................................................... 271 
24.4  Outputs ....................................................................................................................... ... 272 
24.5  Prototyping and testing .................................................................................................. 272 
24.6  Future Enhancements ................................................................................................... 272 
24.7  References .................................................................................................................... 272 
25  ACTIVE FIRE MONITORING PRODUCT GENERATION ....................................................... 273 
25.1  Algorithm Configuration Information .............................................................................. 273 
25.1.1  Algorithm Name ................................................................................................ 273 
25.1.2  Algorithm Identifier ............................................................................................ 273 
25.1.3  Algorithm Specification Version History ............................................................. 273 
25.2  Inputs ............................................................................................................................. 273 
25.2.1  Dynamic Application Data ................................................................................. 273 
25.2.2  Static Application Data ...................................................................................... 274 
25.3  Algorithm Functional Specification ................................................................................. 274 
25.3.1  Overview ........................................................................................................... 274 
25.3.2  Algorithm Description ........................................................................................ 274 
25.3.3  Automatic Quality Control (AQC) ...................................................................... 277 
25.4  Outputs ....................................................................................................................... ... 278 
25.4.1  GRIB-2 Encoded Product .................................................................................. 278 
25.4.2  ASCII-coded Product ........................................................................................ 278 
25.5  Future Enhancements ................................................................................................... 279 
25.6  References .................................................................................................................... 280 
26  Multi-Sensor Precipitation Estimate Product generation ........................................... 281 
26.1  Algorithm Configuration Information .............................................................................. 281 
26.1.1  Algorithm Name ................................................................................................ 281

<!-- source_page: 14 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



26.1.2  Algorithm Identifier ............................................................................................ 281 
26.1.3  Algorithm Specification Version History ............................................................. 281 
26.2  Inputs ............................................................................................................................. 281 
26.2.1  Dynamic Application Data ................................................................................. 281 
26.2.2  Static Application Data ...................................................................................... 282 
26.3  Algorithm Functional Specification ................................................................................. 284 
26.3.1  Overview ........................................................................................................... 284 
26.3.2  Algorithm Description ........................................................................................ 284 
26.3.3  Automatic Quality Control (AQC) ...................................................................... 286 
26.4  Outputs ....................................................................................................................... ... 286 
26.4.1  Intermediate Product ......................................................................................... 286 
26.4.2  GRIB-2 Encoded Product .................................................................................. 286 
26.5  Future Enhancements ................................................................................................... 286 
26.6  References .................................................................................................................... 287 
27  Aerosol Properties Over Sea Product Generation .............................................................. 288 
27.1  Algorithm Configuration Information .............................................................................. 288 
27.1.1  Algorithm Name ................................................................................................ 288 
27.1.2  Algorithm Identifier ............................................................................................ 288 
27.1.3  Algorithm Specification Version History ............................................................. 288 
27.2  Inputs ............................................................................................................................. 288 
27.2.1  Dynamic Application Data ................................................................................. 288 
27.2.2  Static Application Data ...................................................................................... 289 
27.3  Static Application Data Setup Parameters ..................................................................... 289 
27.4  Algorithm Functional Specification ................................................................................. 289 
27.4.1  Overview ........................................................................................................... 289 
27.4.2  Algorithm Description ........................................................................................ 289 
27.4.3  Final product ..................................................................................................... 290 
27.4.4  Automatic Quality Control (AQC) ...................................................................... 291 
27.5  Outputs ....................................................................................................................... ... 291 
27.5.1  Final Product ..................................................................................................... 291 
27.5.2  Encoded Product .............................................................................................. 291 
27.6  Future Enhancements ................................................................................................... 291 
27.7  References .................................................................................................................... 291 
28  Volcanic Ash Detection and Retrieval Product Generation ....................................... 292 
28.1  Algorithm Configuration Information .............................................................................. 292 
28.1.1  Algorithm Name ................................................................................................ 292 
28.1.2  Algorithm Identifier ............................................................................................ 292 
28.1.3  Algorithm Specification Version History ............................................................. 292 
28.2  Inputs ............................................................................................................................. 292 
28.2.1  Dynamic Application Data ................................................................................. 292 
28.2.2  Static Application Data ...................................................................................... 293 
28.3  Algorithm Functional Specification ................................................................................. 293 
28.3.1  Overview ........................................................................................................... 293 
28.3.2  Processing mask ............................................................................................... 293 
28.3.3  Algorithm Description ........................................................................................ 293 
28.3.4  Ash detection .................................................................................................... 293 
28.4  Outputs ....................................................................................................................... ... 295 
28.4.1  Intermediate Product ......................................................................................... 295 
28.4.2  Encoded Products ............................................................................................. 295 
28.5  Future Enhancements ................................................................................................... 295 
28.6  References .................................................................................................................... 295 
Appendix A: Open issues To be Decided or To be Confirmed .................................................. 296 
28.7  Issues To Be Decided (TBD) ......................................................................................... 296 
28.8  Issues To Be Confirmed (TBC) ...................................................................................... 296 
Appendix B: Glossary of Terms Used in this Document ........................................................ 297 
Appendix C: Applicable Documents Not in the Public Domain ................................................ 298

<!-- source_page: 15 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Table of Figures
Figure 1: Product Generation Application Data Flow Diagram ............................................................. 25 
Figure 2: Application Data Preprocessing Data Flows Diagram .......................................................... 26 
Figure 3: Product Processing Application Data Flow Diagram (Inter-algorithm interfaces). ................ 28 
Figure 4: Scenes Analysis SCE Processing ........................................................................................ 69 
Figure 5: CLA Processing ..................................................................................................... .............. 99 
Figure 6: AMV Processing ...................................................................................................... ........... 139 
Figure 7: AMV Processing - Target Optimisation .............................................................................. 140 
Figure 8: Target and Search Areas ............................................................................................ ....... 142 
Figure 9 Target Optimisation .................................................................................................. ........... 143 
Figure 10: Infrared counts as a function of the individual pixel contribution ....................................... 157 
Figure 11: Height Assignment in Clear-sky areas .............................................................................. 162 
Figure 12: Reference wind and test wind locations with auxiliary vectors. ........................................ 167 
Figure 13: The OCA cost minimisation scheme (taken from R2). ..................................................... 232 
Table of Tables
Table 1: Processing Segments in the MPEF Processing Area ............................................................. 29 
Table 2: IR Radiative Transfer Model: Thermodynamic input parameters ........................................... 41 
Table 3: IR Radiative Transfer Model: Thermodynamic input parameters ........................................... 41 
Table 4: IR Radiative Transfer Model: Thermodynamic input parameters ........................................... 42 
Table 5: IR Radiative Transfer Model: Thermodynamic input parameters ........................................... 42 
Table 6: IR Radiative Transfer Model: Atmospheric Correction Tables ................................................ 52 
Table 7: IR Radiative Transfer Model: Tropospheric Humidity Generation Tables ............................... 53 
Table 8: IR Radiative Transfer Model: Vicarious Calibration Tables .................................................... 53 
Table 9: IR Radiative Transfer Model: Contribution Function Tables ................................................... 53 
Table 10: Scenes Analysis Product: Input data required from the level 1.5 image data ....................... 58 
Table 11: Scenes Analysis Product: Data from other MPEF algorithms ............................................... 59 
Table 12: Scenes Analysis Product: Static Application Data Produced, ............................................... 61 
Table 13: Scenes Analysis Product: Static application data and parameters thresholds ...................... 65 
Table 14: Scenes Analysis, Threshold tests .................................................................................... .... 68 
Table 15: Scenes Analysis algorithm Pixels identified as cloudy ......................................................... 82 
Table 16: Scenes Analysis algorithm: Scenes type values .................................................................. 83 
Table 17: BDRF Table Generation: the retrieved model variables for Channel 1 ................................. 87 
Table 18: BDRF Table Generation: the retrieved model variables for Channel 2 ................................. 87 
Table 19: BDRF Table Generation: the retrieved model variables for Channel 3 ................................. 88 
Table 20: Cloud Analysis algorithm: Level 1.5 Image Data and Data Retrieved from the Image Data . 92 
Table 21: CLA Algorithm: Dynamic Application Data ........................................................................... 93 
Table 22: CLA Product: Static Data Sets-Thresholds and Parameters ................................................ 96 
Table 23: Intermediate Cloud Product, Components ......................................................................... 109 
Table 24: Final CLA Product Parameters......................................................................................... .. 111 
Table 25: AMV Product Level 1.5 Data and Data Derived from the Image Data ................................ 115 
Table 26: AMV Product: Data from other MPEF Algorithms ............................................................... 116 
Table 27: AMV Product Static Application Data (per channel used for AMV processing) ................... 123 
Table 28: AMV Product: Static Application Data for Height Assignment ............................................ 133 
Table 29: AMV Product: Static application data for recursive filter function ....................................... 136 
Table 30: AMV Product: Static application for encoding filter ............................................................. 137 
Table 31: AMV Product: Static application data for AMV averaging ................................................... 137 
Table 32: List of required outputs for the Intermediate AMV Product ................................................. 177 
Table 33: List of required outputs for the Final AMV Product ............................................................. 180 
Table 34: Data required for production of CTH Product ..................................................................... 182 
Table 35: Data produced for each CTH Processing Segment ............................................................ 184 
Table 36: Dynamic Application Data required for CSR Product ......................................................... 186

<!-- source_page: 16 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Table 37: Static Application Data required for CSR Product .............................................................. 186 
Table 38: Output parameters per CSR Processing Segment for ........................................................ 190 
Table 39: CSR Quality Flags and Bit breakdown ............................................................................... 191 
Table 40: ASR Product: Dynamic Application Data............................................................................ 193 
Table 41: ASR Product Static Application Data required ................................................................... 193 
Table 42: Output parameters per ASR processing segment .............................................................. 197 
Table 43: Climate Data Set: Dynamic Application Data inputs ......................................................... 200 
Table 44: Climate Data Set: Static Application Data inputs ............................................................... 200 
Table 45: Climate Data Set: Required outputs parameter definition .................................................. 203 
Table 46: High Resolution Precipitation Index Product Inputs ............................................................ 204 
Table 47: High Resolution Precipitation Index Intermediate Product outputs ..................................... 207 
Table 48: High Resolution Precipitation Index Final Product outputs ................................................. 207 
Table 49: ISCCP Data Set Input: ............................................................................................... ........ 210 
Table 50: ISCCP Data Set Outputs .................................................................................................... 213 
Table 51: ISCCP Data Set parameter to Bit value ............................................................................. 213 
Table 52: Tropospheric Humidity Product: Inputs, dynamic application data ..................................... 214 
Table 53: Tropospheric Humidity Product: Inputs, static application data .......................................... 215 
Table 54: Tropospheric Humidity Product: outputs ............................................................................ 219 
Table 55: Sea Surface Temperature Product inputs .......................................................................... 221 
Table 56: Sea Surface Temperature Product: Static Application Data ............................................... 222 
Table 57: Sea Surface Temperature Product: output parameters ...................................................... 224 
Table 58: Sea Surface Temperature Product: Parameter and bit value ............................................. 224 
Table 59: OPTIMAL CLOUD ANALYSIS Dynamic Application Data .................................................. 226 
Table 60: Optimal Cloud Analysis Static Application Data ................................................................. 227 
Table 61: Input parameters for calibration monitoring ........................................................................ 236 
Table 62: Input parameters for Absolute Calibration of windows channels ........................................ 236 
Table 63: Input parameters for absolute calibration of water vapour channels................................... 237 
Table 64: Input parameters for absolute calibration of ozone channel ............................................... 238 
Table 65: Input parameters for inclusion in product header ............................................................... 238 
Table 66: Input parameters for determination of the vicarious calibration constants .......................... 239 
Table 67: Input parameters for cross satellite calibration ................................................................... 239 
Table 68: Input parameters for absolute calibration ........................................................................... 240 
Table 69: Input parameters from off-line absolute calibration of VIS/NIR channels ............................ 240 
Table 70: Calibration Support required outputs .................................................................................. 252 
Table 71: Final TOZ Product required output ..................................................................................... 256 
Table 72: GII and RII Product dynamic application data for physical retrieval scheme ...................... 260 
Table 73: GII and RII Product Static Application Data for Physical Retrieval Scheme ...................... 261 
Table 74: Spectral characteristics of the SEVIRI channels ................................................................ 262 
Table 75: GII/RII product outputs ............................................................................................. .......... 266 
Table 76: Clear Sky Reflectance Map required outputs ..................................................................... 268 
Table 77: Divergence Product: dynamic application data from other MPEF algorithms ..................... 269 
Table 78: Divergence Product: Static Application Data ...................................................................... 270 
Table 79: Divergence Product: Outputs ......................................................................................... .... 272 
Table 80: Active Fire Monitoring Product: Level 1.5 image data ........................................................ 273 
Table 81: Active Fire Monitoring Product: static application data ....................................................... 274 
Table 82: Active Fire Monitoring Product: ASCII-Coded table requirements ...................................... 278 
Table 83: Multi-Sensor Precipitation Product dynamic application data ............................................. 281 
Table 84: Multi-Sensor Precipitation Product external data ............................................................... 281 
Table 85: Multi-Sensor Precipitation Product: Static application dat .................................................. 283 
Table 86: Aerosol Properties Over Sea Product: Dynamic application data ....................................... 288 
Table 87: Aerosol Properties Over Sea Product: Static application data-surface data ....................... 289 
Table 88: Aerosol Properties Over Sea Product: Outputs, final product ............................................. 291 
Table 89: Volcanic Ash Detection and Retrieval Product: Inputs, dynamic application data .............. 292 
Table 90: Volcanic Ash Detection and Retrieval Product: Static application data .............................. 293

<!-- source_page: 17 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




1 INTRODUCTION
1.1 Purpose and Scope of the Specification
This document is the Algorithm Specification Document (ASD) for the Meteosat Second Generation
(MSG) Meteorological Products Extraction Facility (MPEF).
The purpose of this document is to describe the scientific algorithms which will be used to extract the
Meteorological Products from the pre-processed Level 1.5 image data acquired by the Spinning
Enhanced Visible and Infra Red Imager (SEVIRI) on board the MSG series of satellites.
SEVIRI produces images in twelve spectral channels, in the Visible (VIS), Near InfraRed (NIR) and
InfraRed (IR, along with water vapour (WV)) part of the spectrum covering the following channels:
VIS 0.6m, VIS 0.8m, NIR 1.6m, IR 3.9m, WV 6.2m, WV 7.3m, IR 8.7m, IR 9.7m, IR
10.8m, IR 12.0m, IR 13.4m and High Resolution Visible (HRVIS) channel. The imaging yields a
resolution of 3 km (at satellite nadir) and 1 km for the HRVIS channel. Further information on the
SEVIRI instrument and the Level 1.5 image data can be found in [RD1]. This document should be
understood by anyone with a basic university level understanding of Mathematics. A background in
either Meteorology or Remote Sensing is also required in order to understand the more detailed
scientific requirements.
This document provides detailed scientific requirements for the algorithms; however, the requirements
will need some interpretation by the contractor in order for the algorithms to be implemented.
This document describes the algorithms in sufficient detail to ensure that their implementation is
scientifically correct, but does not attempt to impose an overall software design.
1.2 Document Structure
This document contains the following sections:
Chapter 1 Describes the purpose and scope of the document, lists any open issues or
assumptions which have been made in the production of this specification, provides
an overview of the MPEF, defines the applicable and reference documents and
identifies how requirements are specified in the remainder of the document.
Chapter 2 Contains an introduction to the Product Generation function of the MPEF and
explains the terminology used in the document. The Product Generation
sub-functions are also described.
Chapter 3 Contains an introduction to the MP EF products and the algorithms required to
generate them. It also provides information on the algorithm prototyping and on
how to interpret the algorithm specifications.
Chapters 4 Contain the specifications for the individual algorithms.
1.3 Purpose of the MPEF
The MPEF is a part of the MSG Ground Segment, its primary function is the generation of
Meteorological Products from the Level 1.5 image data supplied by the Image Processing Facility
(IMPF). The products are then quality controlled and encoded prior to being passed to the Data
Acquisition and Dissemination Facility (DADF) for delivery to users. Additionally, the products

<!-- source_page: 18 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



generated by the MPEF are transferred to the MSG Unified Meteorological Archive and Retrieval
Facility (UMARF) for online and off-line retrieval.
1.4 Related Documents
1.4.1 Applicable Documents
The applicable documents for this specificatio n are referenced in the individual algorithm
specifications, as defined in Section 3.4.
1.4.2 Reference Documents
The following documents are the reference documents for this specification. Where referred to in the
text these are referenced using the form RD.n, where n is the appropriate number from the list below.

RD.1 Level 1.0 and Level 1.5 Image Data Characteristics, EUM/MSG/TEN/068, Issue 1.1, 2/7/96.
RD.2 Radiances to Brightness Temperature Conversion, EUM/OPS/TEN/05/2556
RD.3 Conversion from Radiance to Reflectance for
SEVIRI Warm Channels
EUM/MSG/TEN/05/2986
1.5 Identification of Requirements in this Document
This document concentrates on the lower level requirements imposing the use of specific algorithms
for the product generation. Requirements are not explicitly numbered. The following formatting has
identifies tasks that contain mandatory requirements:
The word ‘shall’ (in bold and underlined) indicates that the function/task is mandatory.
1.6 Acronyms/Abbreviations and Terms used in this Document
A list of words or expressions with a specific meaning in the context of this document can be found in
0, and are also described in Section 2.1.1. Where relevant, such terms are indicated by italics in text. A
list of acronyms and abbreviations used in this document is below. On first use in a section, an
acronym or abbreviation will be spelled out.
Example: Development of the Rapid Scanning Service (RSS) will continue in the future.
Acronym Meaning
A&R Analysis and Reporting
AES Aerosol Properties Over Sea Product
AMV Atmospheric Motion Vectors Product
AMVI Atmospheric Motion Vectors Image Products
AOT Aerosol Optical Thickness
AQC Automatic Quality Control
ASD Algorithm Specification Document
ASR All Sky Radiances Product
AVHRR Advanced Very-High Resolution Radiometer
BDRF Bi-Directional Reflectance Function
BUFR Binary Universal Form for the Representation of meteorological data

<!-- source_page: 19 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Acronym Meaning
CAL Calibration Support Product
CDP Collocated Data Point
CDS Climate Data Set Product
CLA Cloud Analysis Product
CLAI Cloud Analysis Image Product
CLM Cloud Mask Product
CMS Centre de Métorologie Spatiale (of Météo-France, in Lannion)
CRM Clear Sky Reflectance Map Product
CSICC Cross Satellite Instantaneous Calibration Coefficient
CSOCC Cross Satellite Operational Calibration Coefficient
CSR Clear Sky Radiances Product
CTH Cloud Top Height Product
DADF Data Acquisition and Dissemination Facility
DCP Data Collection Platforms
DIV Divergence Product
DMSP Defense Meteorological Satellite Program (of USA)
EBBT Equivalent Black Body Temperature
ECMWF European Centre for Medium-range Weather Forecasting
EMD External Meteorological Data
EPS EUMETSAT Polar System
EPS EUMETSAT Polar System
ESA European Space Agency
EUMETCast EUMETSAT’s data distribution system, which multicasts meteorological and
environmental data and products to the user community via telecommunication
satellites
EUMETSAT European Organisation for the Exploitation of Meteorological Satellites
FFT Fast Fourier Transform
FIR Active Fire Monitoring Product
FOV Field Of View
FSD Foreign Satellite Data (e.g. in Low Earth Orbit)
FTP File Transfer Protocol
GII Global Instability Index Product
GMS Geostationary Meteorological Satellite (of Japan)
GOES Geostationary Operational Environmental Satellite
GPCP Global Precipitation Climatology Project
GRIB General Regularly-distributed Information in Binary form (WMO standard for
exchanging gridded data; GRIB Edition 2 (GRIB-2) is current version)
GSDPC Geostationary Satellite Data Processing Centre
GTS Global Telecommunication System
HPI GPCP High Resolution Precipitation Index Product

<!-- source_page: 20 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Acronym Meaning
ICAO International Civil Aviation Organization
ICSU International Council for Science
IDS ISCCP Data Set Product
IGBP International Geosphere-Biosphere Programme
IR Infrared (channels of SEVIRI)
ISCCP International Satellite Cloud Climatology Project
LEO Low Earth Orbit
LSD Local Standard Deviation
LST Land Surface Temperature (product of Land Surface Analysis SAF)
LUT Look-Up Table
M&C Monitoring and Control
MODIS Moderate Resolution Imaging Spectroradiometer
MOP Meteosat Operational Programme
MPE Multi-sensor Precipitation Estimate Product
MPEF Meteorological Products Extraction Facility
MQC Manual Quality Control
MSG Meteosat Second Generation
MTP Meteosat Transition Programme
NDVI Normalised Difference Vegetation Index Product
NIR Near Infrared (NIR1.6 channel of SEVIRI)
NOAA National Oceanic and Atmospheric Administration (also the series of LEO satellites
operated by this organisation)
NRT Near Real Time
NTC Normalised Total Contribution
NTCC Normalised Total Cumulative Contribution
NWP Numerical Weather Prediction
OCC Operational Calibration Coefficient
OCA Optimal Cloud Analysis
PB Processing Box
PNG Portable Network Graphics (image format)
PQM Product Quality Monitoring
QI Quality Index
RFF Recursive Filter Function
RII Regional Instability Index Product
RMS Root Mean Square
RSM Radiance Sampling Method
RSS Rapid Scanning Service
RTM Radiative Transfer Model
RTTOV Radiative Transfer model for TOVS

<!-- source_page: 21 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document



Acronym Meaning
SAFNWC SAF to support Nowcasting and Very Short-Range Forecasting
SCC Satellite Calibration Centre
SCE Scenes Analysis Product
SD Standard Deviation
SEVIRI Spinning Enhanced Visible and InfraRed Imager (on MSG satellites)
SNR Signal-to-Noise Ratio
SPC Sector Processing Centre
SSM/I Special Sensor Microwave Imager (instrument on the US DMSP polar satellites)
SSP Sub-Satellite Point
SST Sea Surface Temperature Product
STC Semi-Transparency Correction
TBC To be confirmed
TBD To be defined
TH Tropospheric Humidity Product
TIROS Television and InfraRed Observation Satellite (US polar satellite series)
TOA Top of Atmosphere
TOVS TIROS Operational Vertical Sounder
TOZ Total Ozone Product
UMARF Unified Meteorological Archive and Retrieval Facility (also known as EUMETSAT
Archive or EUMETSAT Data Centre)
UTC Coordinated Universal Time
VAS VISSR Atmospheric Sounder (GOES instrument)
VICC Vicarious Instantaneous Calibration Coefficient
VIS Visible (VIS0.6, VIS0.8, HRVIS channels of SEVIRI)
VISSR Visible and Infrared Spin Scan Radiometer (GOES instrument)
VOCC Vicarious Operational Calibration Coefficient
VOL Volcanic Ash Detection Product
WCRP World Climate Research Programme
WMO World Meteorological Organization
WV Water Vapour (WV6.2, WV7.3 channels of SEVIRI)

<!-- source_page: 22 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




2 INTRODUCTION TO PRODUCT GENERATION
2.1 Introduction
This chapter provides an introduction to the MPEF Product Generation function. The descriptions in
this chapter are applicable to both the standard operational service as well as to the Rapid Scanning
Service (RSS) (see Section 2.2).
The product generation task can be further subdivided into a number of functions, namely:
 Data Preparation (on- and off-line)
 Application Data Preprocessing
 Product Processing
 Product Verification
 Calibration Support
Description of these major functions are included in Section 2.3.
2.1.1 Terminology
The following general terms have a specific meaning when used in this document. As such, their
specific meanings should be thoroughly understood when reading this document. Most of these terms
are also defined in 0 at the end of the document, but are repeated here for clarity. Although both types
of data are described below, this document concentrates mainly on the application data.

Term Meaning
Data ‘Data’ is used in a generic sense in this document to refer to all types of
‘information’ which may be required in order for the MPEF or its scientific
algorithms to operate. The term ‘data’ may thus refer to input/output products,
databases, data files, individual parameters, control data, monitoring data etc.
Application Data The scientific data required for, and produced by, the scientific algorithms, e.g. all
input data, the products, intermediate products.
System Data These data are required by the facility to allow it to operate.
Algorithm A ‘self contained’ routine which inputs data, performs certain processing and then
outputs data, e.g. Scenes Analysis. An algorithm may generate a product or may
generate intermediate results required by subsequent processes.
Product A product may be classed as a collection of parameters which are generated by an
algorithm(s) and which are supplied to an external facility. For all products it will
be possible to specify the destination(s).
Intermediate Product Any intermediate results or product which is generated during processing which
is not disseminated to users but is required to generate another product. These
products may be required to be stored in the UMARF.
Processing Segment A ‘segment’ of size n by n level 1.5 image pixels, where n is configurable and
product-specific.
Superpixel A processing segment made up of nominally 3 by 3 level 1.5 image pixels.
Synoptic scale Providing a horizontal accuracy of 100 km or better, this corresponds nominally
to a processing segment of between 16 × 16 and 32 × 32 level 1.5 image pixels.

<!-- source_page: 23 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




2.2 Rapid Scanning Service
In addition to the operational service with a 15-minute image frequency, a Rapid Scanning Service
(RSS) is provided, using the backup spacecraft when available. This service provides a 5-minute
image frequency over a limited area, from 15° N to 70° N (approximately). Due to hardware
limitations, the MPEF RSS processing area is further limited from 35° N to 70°̵ N (approximately).
The following MPEF products are produced for the rapid scan area:

Product Frequency Comments
AMV 20 minutes AMV Channel 2 (VIS 0.8) and 9 (IR 10.8) only
CSR 15 minutes
MPE 5 minutes
FIR 5 minutes
GII 5 minutes Segment size is 3 × 3 pixels

The basic approach for RSS is to apply the same product algorithm as for the normal scanning. For
products where this is not the case, the differences are described in the respective product section
below.
After a planned hardware upgrade, the full RSS image area will be processed and more AMV
channels and the Divergence product will be added.
It is emphasised that the MSG MPEF Rapid Scanning Service is on trial basis, with outstanding issues
to be clarified in an ongoing process. The main purpose with the trial service is to make it possible for
users to gain experience of the products.
2.3 Product Generation Functions
This section contains a description of all the MPEF functions relating to the Product Generation
function.
Figure 1 shows the relationship of these functions in terms of the application data flows. This diagram
is concerned solely with the scientific flows rather than the system data-related flows like Monitoring
and Control.
To implement the scientific functionality to produce the required results, functions have been
subdivided into a number of algorithms. However, it should be noted that the grouping of the
algorithms into these functional groups should not be considered to be a design constraint.

<!-- source_page: 24 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





Figure 1: Product Generation Application Data Flow Diagram
2.3.1 Data Preparation
Data Preparation is split into the online and off-line functions described below:

Online Data
Preparation
This involves the preprocessing of the near-real-time level 1.5 image data
supplied by the IMPF, formatting the Foreign Satellite Data (FSD) and the
decoding and reformatting of the External Meteorological Data (EMD) (i.e.
forecast and observation data) supplied by the DADF. The dynamic application
data required by the subsequent algorithms are derived from these input data.

Off-line Data
Preparation

This covers the tailoring of the static application data sets for the MPEF
processing. Examples of these data sets are background surface data,
coastline data or spectral response curves for the SEVIRI channels. All
these data sets are held under configuration control.


I2 MetForecasts
I3 MetObservations
I4 FSD
I1 Image Data
O1
Products
Data
Preparation
A121
Application
Data Preprocessing
A122
Product
Processing
A123
Calibration
Support
A125
AMV, CLA, CTH,
CSR, IDS, GPI,
CDS, TH
Prepared
MetForecasts
Prepared FSD
Prepared &
Inferred
Image Data
Temporally
Interpolated
MetForecasts
RTM Tables
Scenes
Analysis
Output
O2
Verified
Products
Prepared
MetObservations
MetObservations
RTM Tables
I5
Static Application Data
MetForecasts
RTM Tables
Product
Verification
A124Products
for Verification
Temporally Interp.
F/C Temp +Wind
Profiles
MSG Spectral
Reponse Functions
IR ImagesFor Next
Repeat
Cycle
A126
CSR
Previous CSR
CalMon Data
Verified
SST
SST,AMV,TH
CLA

<!-- source_page: 25 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




2.3.2 Application Data Preprocessing
Application data preprocessing involves the generation of data which are required by many of the
subsequent algorithms. There are two major processes which must be performed, radiation modelling
and scenes analysis Figure 2 shows the application data flows for these functions.

Figure 2: Application Data Preprocessing Data Flows Diagram
2.3.2.1 Radiation Modelling
Radiation Modelling is the process of modelling the radiative state of the atmosphere under a range of
atmospheric states and satellite viewing angles.
The Radiative Transfer Model (RTM) is used for all SEVIRI channels. The IR RTM will be able to
calculate the IR channel radiance at the top of the atmosphere (TOA) in the direction of the satellite
taking these factors into account:
 the absorption and re-emission of the infrared radiance by different atmospheric gases;
 the emissivity of the surfaces (clouds and earth surfaces);
 the influence of clouds at different levels on the infrared radiation.
The solar RTM will be able to calculate the 2-path transmittances in all channels affected by solar
radiation, taking into account:
 the absorption of radiance by different atmospheric gases and discounting extinction by
molecular scattering (Rayleigh);
The radiative transfer calculation will include the spectral response function for each of the SEVIRI
channels given above.
It is assumed that the specified IR radiation model is used to support both the near-real-time product
generation and the calibration support processing.
For the support of product generation, the RTM will use forecast data. The forecast data are provided
nominally on a 1 by 1 grid for 31 atmospheric levels requiring the RTM to produce results for all
grid points within the EMD processing area for cloud-free cases and assuming opaque clouds at a
configurable number of levels, nominally 15.
I2
Prepared &
Inferred
Image Data
I1
Prepared
MetObservations
O3
Scenes
Analysis
Output
I3
Prepared
MetForecasts
O4
MetObservations
RTM Tables
O1
Temporally
Interpolated
MetForecasts
RTM Tables
Scenes
Analysis
A1221
F/C based
IR RTM
A1222
OBS based
IR RTM
A1223
Image
Header
Temporal
RTM Output
Interpolation
A1224F/C based
IR RTM
Tables
every repeat cycle
every repeat cycle
before next F/C
validity time is passed
at scheduled times
I4
Static Application Data



RTM Level
F/C Temp
+ Wind Prof.
O2Temporally Interp.
F/C Temp +Wind
Profiles
I5 Previous CSR

<!-- source_page: 26 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The RTM produces the following output tables for product generation support:
 atmospheric correction tables
 semi-transparency correction tables
 tropospheric humidity generation tables
 contribution function tables.
 two-path transmission tables.
For calibration support, meteorological observations data will be used in the IR RTM processing. The
output of the RTM based on meteorological observation data will contain results only at the location
of the observations. The RTM produces the following output tables for calibration support:
 vicarious calibration tables.
2.3.2.2 Scenes Analysis
Several products which are derived from the MSG image data require information on the type of
scene contained within a pixel. While some products are derived from cloudy pixels (e.g. Cloud Top
Height), others are derived from clear pixels only (e.g. Clear Sky Radiances). For calibration
monitoring and vicarious calibration, it is very important that the pixels of selected Earth targets are
really cloud-free. Thus the classification of the pixels within the image, i.e. Scenes Analysis, is a
critical process within the MPEF.
The main function of Scenes Analysis is to identify whether a pixel contains clouds or not. In this
process, pixels partially covered by clouds or covered with semi-transparent clouds will also be
marked as cloudy. Pixels identified as clear will contain the information of the surface type (taken
from the surface type mask), except for pixels which are identified by the algorithm as snow-covered
or ice-covered, which will be marked accordingly.
Scenes Analysis is based on currently operational threshold techniques and includes functionality that
uses the data of the previous image as a prediction for the current image. Additionally, use is also
made of spatial information (maximum, minimum, mean, standard deviation). The threshold
technique makes optimal use of the spectral information provided for each pixel for all twelve
channels.
The Scenes Analysis result is produced on a pixel basis for the whole MPEF processing area.
2.3.3 Product Processing
This function is responsible for the generation of the meteorological products. The data which have
been produced by the Data Preparation and Application Data Preprocessing functions are used as
input, with further calculations performed using these data in order to derive the meteorological
products.
Figure 3 shows the top-level breakdown into the product generation algorithms. The diagram shows
the MPEF application data flows, the inputs, outputs and interactions between these algorithms. These
diagrams are concerned solely with the scientific flows rather than the system data-related flows, for
example monitoring and control (M&C).

<!-- source_page: 27 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




SST
Scenes Analysis
Output
CLA
IDS
TH
HPI
CSR
CDS
AMV
CTH
Prepared & Inferred
Image Data
Temporally Interpolated
Met Forecasts
RTM Tables
Temporally Interpolated
F/C Temp+Wind Profiles
SST for Verif.
Products for
Verification
CSR
CLA
CLA Image
CDS
IDS
AMV
AMV for Verif.
AMV Image
TH for Verif.
TH
CTH
HPI
DIV DIV
TOZ
GII / RII GII
FIR FIR
CRM CRM
CLM CLM
TOZ
Products for
dissemination via
GTS, EUMETCast
MPE MPE
SSM/I Microwave
Data from DMSP
Satellites
ASR ASR
VOL VOL
AES AES
NDVI NDVI

Figure 3: Product Processing Application Data Flow Diagram (Inter-algorithm interfaces) Note: Static
application data input, which applies to all products, has been omitted from this diagram.

<!-- source_page: 28 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





Disseminated products are produced at varying horizontal scales. These horizontal scales are
product-specific and configurable, and are defined by means of the product-specific
processing segment,, e.g. synoptic scale (nominally between 16 × 16 and 32 × 32 Level 1.5 image
pixels) or superpixel scale (nominally 3 × 3 Level 1.5 image pixels). Table 1 shows the approximate
number of pixels within the MPEF processing area for various different processing segment sizes.
By implication, once the processing segment size is specified, the level 1.5 image pixels which are
contained in each segment (line and column numbers) and the physical location of each segment,
(corners and centre), in terms of latitude and longitude, are fixed.

Processing Segment Size # nominal segments # HRVIS segments
Pixels 9274440 54473190
3 pixels by 3 pixels 1030493 6052577
32 pixels by 32 pixels 9058 53197
1 by 1 14217 14217
Table 1: Processing Segments in the MPEF Processing Area
The products have different dissemination frequencies which are published on the EUMETSAT
website:
Access to Data/ Meteosat Meteorological Products/Product Schedule
Due to the repeat cycle concept of MSG, the products to be disseminated are not extracted at ‘fixed’
times but will be extracted from the repeat cycle(s) which are closest to the required UTC. However,
the products may be extracted from more repeat cycles, with only those relating to the required
dissemination times actually being disseminated.
2.3.4 Product Verification
Some products have their quality verified and continuously monitored using independent
meteorological data (as radiosonde observations) and/or forecast data. The methods are further
described in the respective product descriptions below and the results are stored in a database within
the EUMETSAT ground segment.
2.3.5 Calibration Support
Calibration Support is composed of two main areas which are described below:
 Calibration Monitoring for both VIS/NIR and IR channels
 Absolute Calibration for both VIS/NIR and IR channels
2.3.5.1 Calibration Monitoring - IR Channels
Level 1.0 data received from the satellite and the Primary Ground Station are transformed into level
1.5 data which are radiometrically and geometrically corrected. This task is performed operationally
by the IMPF. Part of the process of radiometrically transforming the data from level 1.0 to level 1.5
involves calibration of the IR SEVIRI channels using the on-board black body. MPEF receives the
level 1.5 data in the form of corrected counts and a set of calibration coefficients which are used to
transform the counts to radiances valid at the top of the atmosphere (TOA), convolved with the
spectral response function of each spectral channel.
The radiometric accuracy of the level 1.5 data has to be assured over the lifetime of the satellite.

<!-- source_page: 29 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Calibration monitoring will involve the extraction of statistical data (bias and RMS) describing the
difference between the measured level 1.5 radiances (for clear sky cases) and the radiances calculated
from external data (such as observations or other satellites and meteorological forecasts), in order to
detect whether any changes are required to the calibration coefficients.
The results from calibration monitoring will be sent to the IMPF; results include a flag indicating
whether a change to the calibration coefficients currently being used is required.
2.3.5.2 Absolute Calibration - IR Channels
Absolute Calibration is responsible for deriving absolute calibration coefficients for the eight infrared
channels of MSG:
 IR3.9
 WV6.2
 WV7.3
 IR8.7
 IR9.7
 IR10.8
 IR12.0
 IR13.4
This is done independently from the on-board calibration. The output of this process consists of tables
describing the temporal evolution of the Absolute Calibration Coefficient. This information is
provided to the IMPF for further processing.
The Absolute Calibration Coefficients are calculated as a weighted mean of the Vicarious Operational
Calibration Coefficient, derived using forecast data, meteorological observations, and the Cross
Satellite Operational Calibration Coefficient derived from Foreign Satellite Data.
2.3.5.3 Calibration Support - Solar (VIS/NIR) Channels
The solar radiation modelling required to support the calibration monitoring and absolute calibration
of the SEVIRI VIS/NIR channels is not part of the MSG MPEF processing.
There is no on-board calibration foreseen on MSG for the VIS channels, unlike for the IR channels,
The calibration coefficients and monitoring information for the VIS/NIR channels and different
surface types are transferred off-line to the MSG MPEF from whence they will be transferred online
to the IMPF, together with the IR calibration monitoring results.
2.3.5.4 Calibration Campaigns
A calibration campaign is planned as early as possible after an MSG satellite launch. The campaign
will cover the calibration of the thermal IR channels and the VIS and NIR channels. The results will
be used to verify the pre-launch calibration of the SEVIRI channels and will provide a reference for
the operational calibration and the MPEF calibration monitoring. The calibration campaigns will use
level 1.5 image data from the DADF or the UMARF. There is no functionality required in the MSG
MPEF to support the calibration campaigns.

<!-- source_page: 30 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




3 ALGORITHMS AND PRODUCTS
This chapter provides further information on the products themselves and the algorithms which are
required to generate them. It also provides information on the structure of the algorithm specifications
and how to interpret them.
3.1 Overview
There are two types of algorithms which are specified in this document  those which have been
prototyped and those which have not.
The algorithms which have been prototyped are those for which there is a high scientific content.
Where the existing MOP or MTP algorithms have required significant modifications, or completely
new algorithms have been developed, prototyping has been used to ensure that these new or modified
algorithms are scientifically valid, can produce the expected results, and can meet the required
accuracy criteria.
The remaining algorithms, which have not been prototyped, perform much simpler, non-scientific
tasks like reformatting of data, and thus do not need the same level of investigation and testing as the
former category.
The current issue of the ASD covers the specifications of the following products to be generated by
the MPEF. These products form the baseline for the MSG MPEF development:
 Atmospheric Motion Vectors (AMV)
 Cloud Analysis (CLA)
 Cloud Analysis Image (CLAI)
 Cloud Top Height (CTH)
 Clear Sky Radiances (CSR)
 Climate Data Set (CDS)
 High Resolution Precipitation Index (HPI)
 ISCCP Data Set (IDS)
 Tropospheric Humidity (TH)
 Calibration Monitoring Data (CAL)
Furthermore, specifications for other products are also included in the current issue of the ASD. These
products will be used in the internal product generation process, but will not be distributed to the endusers. If the baseline changes it shall
be required to distribute these products as well:
 Sea Surface Temperature (SST)
The following products are new and have been added to the ASD during the course of the MPEF
development:
 Aerosol Properties Over Sea (AES)
 All Sky Radiances (ASR)
 Cloud Mask (CLM)
 Clear Sky Reflectance Map (CRM)
 Divergence (DIV)

<!-- source_page: 31 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




 Active Fire Monitoring (FIR)
 Global Instability Index (GII) / Regional Instability Index (RII)
 Multi-Sensor Precipitation Estimate (MPE)
 Total Ozone (TOZ)
 Volcanic Ash Detection (VOL)
 Normalised Difference Vegetation Index (NDVI)
 Optimal Cloud Analysis (OCA)
The Atmospheric Motion Vectors Image (AMVI) product has been removed from baseline MPEF
product generation. The AMVI product can still be generated as an output of AMV product
generation, but it is expected that this will not be scheduled to take place in the future.
Most MPEF products are required to be disseminated in a particular format, e.g. BUFR, as defined by
the World Meteorological Organization (WMO). Where this is required it has been indicated in the
relevant specifications of the ASD. Product formats are explicitly specified in these cases in order to
provide continuity with those products which are currently operational, to ensure minimum disruption
for the users. However, the formatting and encoding of the products is not explicitly described in this
document.
3.2 Summary Description of MPEF Products
3.2.1 Baseline Products
In this section, top-level descriptions of the baseline products are provided.

Atmospheric Motion Vectors (AMV)
Motion in the atmosphere can be derived from satellite images by the tracking of clouds and other
atmospheric constituents, e.g. water vapour patterns and ozone. The product derived from tracking
these atmospheric motions on a synoptic scale (100 km or better) using MSG imagery is the
Atmospheric Motion Vectors (AMV) product.
The product is based on the measurement of clouds or atmospheric constituents displacement
between two or more consecutive images. The displacement is derived by means of matching a
target area containing the tracer to the search area, and an interpolation in the matching surface.
The height at which the vector is measured is defined by the temperature of the tracer and
converted to a pressure level via the forecast temperature-to-pressure profile of the atmosphere.
Corrections for semi-transparent clouds, atmospheric absorption and cloud base for low-level
clouds are also considered.
The AMV baseline product will be derived continuously from five spectral SEVIRI channels. The
derivation of vectors from other channels, e.g. Ozone and further IR channels, is considered as
Future Enhancements.
It is the intention that the AMV Image Products will not be generated as part of MPEF baseline
product generation. It will however be possible if required to produce AMV Image Products from
the AMV product containing bit map images with wind vectors derived for low, medium and highlevel height bands (one image per band) together with coastlines on the MSG projection.

<!-- source_page: 32 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The AMV product generation, and especially the matching, which is based on cross-correlation, is
the main contributor to overall processing load requirements. The AMV product is a key product
and is required on a routine basis for the data assimilation process of numerical forecast models.

Cloud Analysis (CLA)
The Cloud Analysis product is based on the Scenes Analysis results and will provide on a synoptic
scale (i.e. 100 km or better) information about cloud cover, cloud top temperature, cloud top
pressure and cloud type and phase. As with the Scenes Analysis processing, the CLA product is
based on a threshold technique.
The CLA product includes the height assignment of the identified clouds and the correction for
semi-transparent clouds.
A CLA Image product will be derived from the intermediate CLA product and will contain
information about the identified cloud type for cloudy pixels and the surface type for clear pixels.
The CLA product will also provide internally input to the AMV, CTH and CDS products and
needs therefore to be continuously derived at pixel resolution. The distribution of the product to
the end-users will be nominally at three-hourly intervals and with a reduced resolution described
in the CLA product description below.

Cloud Top Height (CTH)
The CTH product, based on a subset of the information derived during the cloud analysis
processing, is an image-based product which indicates the height of the highest cloud within a
superpixel of size 3 × 3 pixels.
The CTH product will provide a vertical resolution equivalent to 300 meter height-bands.

Clear Sky Radiances (CSR)
The CSR product is a subset of the information derived during the Scenes Analysis processing.
The product provides the radiances for a subset of the MSG channels averaged over all pixels
within a processing segment which has been identified as ‘clear’, except for channel WV6.2 where
the CSR is also derived for areas containing low-level clouds. The accuracy of the product
depends mainly on the accuracy of the calibrated image data and the accuracy of the scenes
analysis processing.
The product will provide valuable input to numerical weather prediction models. The horizontal
resolution will be on synoptic scale (100 km or better).

<!-- source_page: 33 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Tropospheric Humidity (TH)
The TH product provides estimates of the relative humidity in the troposphere on a synoptic scale
(i.e. 100 km or better). Due to the fact that MSG will have two channels providing information
about the water vapour content in the troposphere and one IR channel highly affected by the
low-layer humidity, the TH product will be derived in the form of a mean layer tropospheric
humidity, providing the mean relative humidity in at least two layers. The following MSG
channels are used to derive mean-layer humidities:
 with channel WV6.2, the mean layer relative humidity nominally between 600 hPa and
300 hPa, upper tropospheric humidity (UTH)
 with channel WV7.3, the mean layer relative humidity between nominally 850 hPa and
600 hPa, mid-tropospheric humidity (MTH)
The TH product is needed as input for numerical models and as a climatological product.

Climate Data Set (CDS)
The CDS product provides statistical information of the classified clusters in pre-defined
processing segments of the image. The Scenes Analysis, providing the input to the CDS, provides
information on pixel resolution. The CDS product will provide the results on a synoptic scale, e.g.
32 ൈ 32 pixel segments.
The CDS product is not disseminated in real-time but is provided by means of off-line retrieval by
the UMARF.

High Resolution Precipitation Index (HPI)
The High Resolution Precipitation Index product is primarily generated to support the Global
Precipitation Climatology Project (GPCP). In the framework of this project, the supporting center
(MPEF) is acting as a “Geostationary Satellite Data Processing Centre (GSDPC)”. The HPI
product provides BBT class histograms (three per hour) to support the estimation of the
accumulated convective precipitation for the box bounded by 40 of latitude and  50 of
longitude from the SSP on a 1 by 1 grid.
The GPCP HPI product is not disseminated in real-time. The non-real-time delivery is done in
accordance with the WMO/ICSU Global Precipitation Climatology Project rules.
It is assumed that MSG will support GPCP (as during MOP and MTP) although the HPI product
extraction method and the amount of requested data may be modified.

<!-- source_page: 34 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




ISCCP Data Set (IDS)
The IDS has to support the International Satellite Cloud Climatology Project (ISCCP) of the
World Climate Research Programme (WCRP) of the WMO. In this programme satellite data in
different forms is collected. The IDS product has to provide three data formats: the AC-data, the
B1-data and the B2-data. The AC-data are satellite data of all channels of a satellite in full
resolution, including navigation and calibration information. The AC-data have to be recorded in
coordination with an overpass of polar-orbiting meteorological satellites for geographical areas of
about 2000 km x 2000 km. The AC-data set has to be recorded approximately five times per
month. The B1-data are a reduced data set for the whole MSG field of view with a nominal
resolution of 10 km. The reduction is achieved by averaging and sampling. The B2-data are a
further compressed data set derived from B1-data by further sampling the data to a nominal 30-km
spacing.
It is assumed that MSG will support ISCCP (as during MOP and MTP) although the amount of
requested data may be modified.
The IDS product is not disseminated in real-time. The non-real-time delivery is done in
accordance with the ISCCP requirements.

3.2.2 New Products
This section provides a top-level description of the new products which have been added during the
course of the MPEF development is provided.

Aerosol Properties Over Sea (AES)
The AES intermediate product,, generated every repeat cycle, consists of the optical thickness for
the three visible channels and the Angström coefficient, for every pixel over sea. The retrieval is
based on pre-calculated look-up tables.
A daily product is also derived by temporally and spatially averaging the intermediate products
over processing segments.

All Sky Radiances (ASR)
The ASR product is (as with CSR) a subset of the information derived during the Scenes Analysis
processing. The product provides brightness temperatures for the MSG infrared channels averaged
over all pixels within a processing segment and in six separate categories: all pixels, clear pixels,
cloudy pixels, and low-, mid- and high-level cloud pixels.

Cloud Mask (CLM)
The Cloud Mask product is an image-based product derived from the Scenes Analysis results and
provides information about the cloud contamination and non-static surface types (i.e. snow/ice
cover) on a pixel basis for every repeat cycle.

<!-- source_page: 35 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





Clear Sky Reflectance Map (CRM)
The Clear Sky Reflectance Map product is an image-based product derived from the Scenes
Analysis results. It shows the remote sensing reflectance (uncorrected for atmospheric or viewing
angle reflection effects) that would be seen by the satellite in the visible and near infrared channels
over a cloud-free Earth. The product is derived from a set of seven-day averages of cloud-free
pixels of images corresponding to daily times of every two hours between 06:00 and 20:00 UTC,
for the full visible disc except for the polar regions.

Divergence (DIV)
The Divergence product is derived directly from the Atmospheric Motion Vector results for the
WV6.2 channel. It describes the convergence and divergence in the upper troposphere on a 1º x 1º
grid and is produced at hourly intervals. The product is particularly applicable for showing the
development of tropical convective cells, i.e. small-scale divergence.

Active Fire Monitoring (FIR)
The Active Fire Monitoring product, which is in full pixel resolution, displays information on the
presence of fire within a pixel. It has been developed primarily for detecting and quantifying
biomass burning in Africa. Generated every image, the product compares the brightness
temperatures of the IR3.9, 8.7 and 10.8 channels over cloud-free land areas and assigns a
‘fire-free’ status or a ‘potential’ (i.e. possible) or ‘probable’ fire status to each pixel. The algorithm
used is based on threshold values and will be further developed.

Global Instability Index (GII) / Regional Instability Index (RII)
The air mass analysis mission is a new mission for MSG. The Global Instability Index product
(along with the computationally identical Regional Instability Index product) is considered as an
example of such a product to be provided with priority. However, operational retrieval of
temperature and humidity profiles and derived instability parameters have been performed since
1987 from the GOES VAS instrument.
The GII Statistical Retrieval algorithm has been developed as a prototype, and demonstrated on
the basis of existing satellite data. It is assumed that the method will use SEVIRI information from
the lower and mid troposphere and the earth’s surface. The results from the cloud analysis will
also be needed.
The product is required at better resolution than synoptic scale in order to provide a representative
sample of the geographic distribution of instability areas. It should be noted that there is probably
no ‘global’ index which will serve as a successful predictor for different regions. Therefore the
production of several indices will be required to ensure a forecast with high performance.

<!-- source_page: 36 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Multi-Sensor Precipitation Estimate (MPE)
The Multi-Sensor Precipitation Estimate product provides estimated instantaneous rain rates in full
pixel resolution. The algorithm is based on a combination of MSG images from the IR10.8
channel and passive microwave data from the SSM/I instrument on the US DMSP polar satellites.
The product is most suitable for convective precipitation, and is intended mainly for areas with
poor radar coverage (especially in Africa and Asia).

Total Ozone (TOZ)
The Total Ozone product makes use of the new SEVIRI Ozone IR 9.7 m channel and of the other
IR and WV channels of SEVIRI. The Total Ozone product is derived as an intermediate TOZ
product (TOZint) on a pixel basis for each repeat cycle and as a final TOZ product (TOZfin), which
will be distributed to the end-users. The final TOZ summarises the intermediate TOZ information
for a TOZ processing segment.

Volcanic Ash Detection (VOL)
The VOL product is an image-based product in full pixel resolution that displays information on
the presence of volcanic ash within a cloudy pixel. The algorithm is applied in areas within 5° of
known active volcanoes, and applies a series of reflectance ratio tests for visible channels and
brightness temperature differences for infrared in order to detect thin/thick ash clouds and
hotspots.

Normalised Difference Vegetation Index (NDVI)
The NDVI product is derived as part of the Scenes Analysis processing, based on visible and nearinfrared reflectances from channels VIS0.6 and VIS0.8. It is an image-based product in full pixel
resolution that displays information on vegetative cover and its seasonal variation. The product is
encoded in HDF5 format, both daily and weekly (the latter being an accumulation of daily data).
3.2.3 Additional Products
In this section, a top-level description of the additional products is provided.

Sea Surface Temperature (SST)
The SST product currently derives for every repeat cycle, for all pixels identified as clear ocean by
the Scenes Analysis algorithm, an estimate of the sea surface temperature. It is foreseen that this
product be used in the calibration support process and may also be used off-line to monitor the
performance of the Scenes Analysis algorithm.
If required the repeat cycle-based data could be segmented into the required horizontal scale and
averaged over a given time period for dissemination as an SST product.

<!-- source_page: 37 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




3.3 Prototyping
In order to support the specification of the algorithms, prototyping has been performed for a subset of
the baseline algorithms which are considered as critical for the development of the MPEF.
For the following algorithms, the specifications in this document are based on prototype software and
test data sets:
 Radiative Transfer Model (RTM)
 Scenes Analysis (SCE)
 Cloud Analysis (CLA)
 Atmospheric Motion Vectors (AMV)
 Tropospheric Humidity (TH)
 Global Instability Index (GII)
 Sea Surface Temperature (SST)
The detailed descriptions of the prototype software and of the test data available for each of these
algorithms are included in the relevant algorithm specifications later in this document.
The use of simulated SEVIRI test data for prototyping is problematic as some of the spectral channels
have not been operated on board a geostationary satellite or are only available at a reduced horizontal
resolution. The test data used during the prototyping came from the following satellites/instruments:
Meteosat, GOES-8/VISSR, GOES-8/VAS and NOAA/AVHRR. Test data from the NIR 1.6 m and
the IR 8.7 m channel have not been explored yet.
3.4 Structure and Interpretation of the Algorithm Specifications
Each algorithm specification in this document contains seven sections. A brief description of the
purpose of each of these sections follows.

1. Algorithm Configuration Information
Provides information about the algorithm; its name, identifier and version.

2. Inputs
Describes all the input data required by the algorithm. All inputs are listed in a tabular form
together with their source. An example of the input data table is shown below together with some
notes on the usage of each column. No guidance concerning the format of the input data are given,
unless these are already fixed by an external source, e.g. format of the Level 1.5 image data from
the IMPF.

Parameter Mnemonic Units Min Max Precision Accuracy Resolution Source
Name Note 1 Note 2 Note 3 Note 3 Note 4 Note 4 Note 5 Text description
Note 1 The Mnemonic for the parameter may be us ed in preference to the full name in
the specification to improve clarity particularly in scientific formulae. The
parameters should be referred to using only their full name or mnemonic in order
to avoid confusion.

<!-- source_page: 38 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Note 2 The Units which are specified are those to which the parameters are required to
be converted for the relevant scientific equations to be valid.
Note 3 The Min and Max columns provide the expected minimum and maximum values
for the inputs in the units as given, where these are available.
Note 4 The Accuracy column specifies the accu racy to which a parameter should be
calculated, while the Precision column specifies the number of decimal places to
which the parameter should be supplied, both columns supplied in the units
given, where these are available.
Note 5 The required Resolution of the parameter, on a pixel basis or processing segment
basis or a superpixel basis, is given where appropriate.

3. Algorithm Functional Specification
Provides all the information about what the algorithm does and gives all the formulae necessary to
calculate the required parameters. Where an established scientific technique is available to
perform a function, a reference to the relevant literature / prototype software is given rather than
distilling the scientific content of the technical paper or complex code into the specification. This
section also gives details of the Automatic Quality Control (AQC) functionality required.
The section covers also the product verification/check against meteorological observations and
forecast data where appropriate.

4. Outputs
Describes all the output data generated by the algorithm. All outputs are listed in a tabular form,
together with their destination. Again no guidance concerning the format of the output data are
given, unless these are already fixed by an external source. The definition of the mnemonic, units,
min, max, accuracy, precision and resolution columns are the same as for the input data. The
source column is replaced by a column specifying the destination of the outputs.

5. Prototyping and Testing
If the algorithm has been prototyped this provides an overview of the prototyping activities
together with any caveats concerning the implementation of the algorithm.
This section also provides information about the test data and expected results which will be
supplied with the prototype algorithm in order to fully test its scientific functionality. No test data
or expected results are supplied with algorithms which have not been prototyped.

6. Future Enhancements
This section describes any potential product improvements which can be expected to be included
in the algorithm in a later release.

7. References
Gives all the scientific references used in the definition of the algorithm. All references shall be
treated as Applicable Documents.

<!-- source_page: 39 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




4 IR RADIATIVE TRANSFER MODEL
4.1 Algorithm Configuration Information
No specific information on configuration.
4.1.1 Algorithm Name
IR Radiative Transfer Model (RTM)

4.1.2 Algorithm Identifier
EUM_MSG_RTM_A001
4.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 S. A. Tjemkes RTM Baseline
1.1 16/5/97 S. A. Tjemkes TBD resolved, errors corrected.
1.2 1/7/97 S. A. Tjemkes Some functionality descoped and
clarifications/simplifications added.
1.3 8/12/97 H. K. Wilson Requirements Analysis clarification points added.
1.4 11/3/98 H. K. Wilson Peer Group Review changes added.
1.5 12/08/02 S. J. Fowler Surface emissivity added.
1.6 18/09/09 J. D. Jackson SYNSATRAD replaced by RTTOV.
Removed the semi-transparency and spectroscopic tables.
1.7 13/10/15 J. D. Jackson Upgraded the version of RTTOV from 9.3 to 11.2.
New 2-path visible transmission tables added.

4.2 Inputs
RTTOV 11.2 LBLRTM coefficients file (refer to NWPSAF-MO-UD-016 in Section 4.7).
The tables on the following pages detail each input.

<!-- source_page: 40 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 41 of 298

THERMODYNAMIC INPUT PARAMETERS FOR THE ATMOSPHERIC CORRECTION TABLES
Parameter Mnemonic Units Min Max Acc Prec Source
Pressure p hPa 0 1050 10-2 10-3 Forecast
Temperature T K 0 400 1 1 Forecast
Water vapour mixing ratio qh20 kg/kg - 50 10-3 10-7 10-8 Forecast
Ozone volume mixing ratio m o3 kg/kg - - - - Forecast
Satellite viewing angle   0 90 10-1 10-1 Level 1.5 image data
Number of pressure levels Z - 0 100 1 1 Forecast
Minimum water vapour mixing ratio qho2
min kg/kg 0 20 10-3 10-7 10-8 Set-up
Table 2: IR Radiative Transfer Model: Thermodynamic input parameters for the Atmospheric Correction Tables

THERMODYNAMIC INPUT PARAMETERS FOR THE TROPOSPHERIC HUMIDITY CORRECTION TABLES
Parameter Mnemonic Units Min Max Acc Prec Source
Pressure p hPa 0 1050 10-2 10-3 Forecast
Temperature T K 0 400 1 1 Forecast
Ozone volume mixing ratio mo3 kg/kg - - - - Forecast
Water vapour relative humidity RH % 0 100 1 1 Set-up
Pressure threshold parameter THR1 hPa 0 <THR2 10-2 10-3 Set-up
Pressure threshold parameter THR2 hPa >THR1 1050 10 -2 10 -3 Set-up
Minimum water vapour mixing ratio qho2
min kg/kg 0 20 10-3 10-7 10-8 Set-up
Satellite viewing angle   0 90 10 -1 10 -1 Level 1.5 image data
Number of pressure levels Z - 0 100 1 1 Forecast
Table 3: IR Radiative Transfer Model: Thermodynamic input parameters for the Tropospheric Humidity Correction Tables

<!-- source_page: 41 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 42 of 298


THERMODYNAMIC INPUT PARAMETERS FOR THE VICARIOUS CALIBRATION TABLES
Parameter Mnemonic Units Min Max Acc Prec Source
Pressure p hPa 0 1050 10-2 10-3 Observations
Temperature T K 0 400 1 1 Observations
Water vapour mixing ratio qh20 kg/kg - 20 10-3 10-7 10-8 Observations
Ozone volume mixing ratio m o3 kg/kg - - - - Observations
Satellite viewing angle   0 90 10-1 10-1 Level 1.5 image data
Number of pressure levels Z - 0 100 1 1 Forecast
Table 4: IR Radiative Transfer Model: Thermodynamic input parameters for the VICARIOUS Calibration Tables.

THERMODYNAMIC INPUT PARAMETERS FOR THE CONTRIBUTION FUNCTION TABLES
Parameter Mnemonic Units Min Max Acc Prec Source
Pressure p hPa 0 1050 10-2 10-3 Forecast
Temperature T K 0 400 1 1 Forecast
Water vapour Mixing ratio qh20 kg/kg - 20 10-3 10-7 10-8 Forecast
Ozone volume mixing ratio m o3 kg/kg - - - - Forecast
Satellite viewing angle   0 90 10 -1 10 -1 Level 1.5 image data
Number of pressure levels Z - 0 100 1 1 Forecast
Table 5: IR Radiative Transfer Model: Thermodynamic input parameters for the Contribution Function Tables

<!-- source_page: 42 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 43 of 298


THERMODYNAMIC INPUT PARAMETERS FOR THE TWO-PATH TRANSMISSION TABLES
Parameter Mnemonic Units Min Max Acc Prec Source
Pressure p hPa 0 1050 10-2 10-3 Forecast
Temperature T K 0 400 1 1 Forecast
Water vapour Mixing ratio qh20 kg/kg - 20 10-3 10-7 10-8 Forecast
Ozone volume mixing ratio m o3 kg/kg - - - - Forecast
Satellite viewing angle   0 90 10 -1 10 -1 Level 1.5 image data
Number of pressure levels Z - 0 100 1 1 Forecast
Table 7: IR Radiative Transfer Model: Thermodynamic input parameters for the 2-Path Transmission Tables

<!-- source_page: 43 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




4.3 Algorithm Functional Specification
4.3.1 Overview
This algorithm is responsible for calculating the radiances at the top of the atmosphere and various
level based radiance and transmission quantities in the eight IR channels of MSG (IR3.9, WV6.2,
WV7.3, IR8.7, IR9.7, IR10.8, IR12.0, and IR13.4) propagating into the direction of the satellite, under
a range of atmospheric conditions. In addition the algorithm is responsible for calculating the
two-path transmission for solar-affected channels (VIS0.6, VIS0.8, NIR1.6, and IR3.9).
The output of the Radiative Transfer Model consists of tables describing synthetic
radiances/transmittances in the IR and visible channels, which will be used for various other
algorithms. These tables are as follows:
 Atmospheric Correction Tables
 Tropospheric Humidity Generation Tables
 Vicarious Calibration Tables
 Contribution Function Tables
 Two-Path Transmission Tables
The tables are generated using the Radiative Transfer Model for different atmospheric situations. The
Atmospheric Correction Tables, Tropospheric Humidity Generation Tables, Vicarious Calibration
Tables for the window channels (IR3.9, IR8.7, IR10.8 and IR12.0), Contribution Function Tables, and
Two-Path Transmission Tables shall
be based on the forecast data.
The forecast model grid has a nominal horizontal resolution of 1° x 1°. Furthermore, nominally 30
levels at fixed pressure values are used to describe the vertical state of the atmosphere, plus the values
at the surface and 2 metres above the surface. These data arrive nominally twice a day. Each forecast
has a base time (to), and contains a number of forecast predictions, e.g. (to+6h, to+12h, to+18h, to+24h,
to+30h). The generation of the radiation tables is driven by the arrival of the forecast data.
The Vicarious Calibration Tables are calculated for the absorber channels (WV6.2, WV7.3, IR 9.7,
and IR13.4) and shall be based on observations by radiosondes. These Vicarious Calibration Tables
shall be based on all available observations, subject to quality control within a cut-off time, defined
by a set-up parameter, after the observational time.
Further details of the Vicarious Calibration Process can be found in Chapter 19.
The Contribution Function Tables shall be based on Radiative Transfer calculations for clear sky
scenes. These calculations shall adopt the surface state and vertical distribution of temperature and
radiative active gases as specified by the forecast profiles for each point of the original forecast grid.
The spectral response functions of the channels and the satellite viewing angle shall be taken into
account. The Two-Path Transmission Tables for the solar affected channels shall use the solar zenith
angle at the forecast grid point and time in addition to the satellite zenith angle to define the two-path
geometry.
4.3.2 Algorithm Description
The following steps shall be performed:
 Meteorological Data Preparation,
 Radiative Transfer Calculations for IR and solar channels,
 Radiation Table Generation.

<!-- source_page: 44 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




4.3.2.1 Meteorological Data Preparation
The following tasks shall be performed:
1. The meteorological profiles from either the forecast model or the observations are used to
describe the vertical structure of the atmosphere at specific pressure levels, defined by set-up
parameters in the atmosphere. The vertical distribution of radiative active gases other than
water vapour and ozone shall not be specified, but the default values in RTTOV are assumed.
The specific humidity at each level shall exceed a minimum threshold defined by a set-up
parameter. The data describing the vertical structure of the atmosphere are supplemented by
data describing the surface properties, like surface temperature, surface emissivity, 2 m water
vapour and 2 m temperature.
2. The observation profiles shall
be filtered according to their completeness. Only profiles with at
least 10 levels which reach at least from 850 hPa to 300 hPa shall be used. From the highest
observation level to the highest RTM level a linear interpolation is performed. At the highest
RTM level the temperature shall be 205 K and the water vapour mixing ratio shall be 0.
4.3.2.2 Radiative Transfer Calculations
The following tasks for the Radiative Transfer Calculations shall be performed:
1. The atmosphere temperature structure shall be described by a finite number of levels
(nominally 32). The number of these levels and the actual position are defined by set-up
parameters.
2. The vertical distribution of water vapour and ozone shall be described by a finite number of
levels. These levels coincide with the levels at which the temperature profile is described.
3. The following RTTOV output is used to generate the RTM tables for each solar channel:
1. Transmittance from TOA to each standard pressure level to TOA along combined
sun-surface-satellite path.
4. The following RTTOV output is used to generate the RTM tables for each IR channel:
1. Clear sky radiance.
2. Radiance at the top of atmosphere (TOA) when a black cloud is at each standard
pressure level.
3. Radiance emitted by a black cloud at each pressure level except the surface.
4. Above-cloud upwelling atmospheric radiance for each pressure level down to the
surface.
5. Above-cloud downwelling atmospheric radiance for each pressure level down to
the surface.
6. Transmittance from each standard pressure level to top of atmosphere.
7. Transmittance from each standard pressure level to the surface.

<!-- source_page: 45 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




4.3.2.3 Radiation Table Generation
1. Atmospheric Correction Tables
The Atmospheric Correction Tables represent the radiance in the eight IR channels, emitted
by an opaque cloud at each of the standard pressure levels. The fast radiative transfer model
(RTTOV) calculates the emitted upwelling and downwelling radiance from above and below
an opaque cloud using the transmission of each layer. The transmission of each layer is
determined by the atmospheric state vector and predictors based on the LBLRTM. These
parameters, including the transmission of the layers and the emissivity values used to
determine the surface contribution, are included in the atmospheric correction table.
The radiances shall
be based on radiative transfer calculations for clear sky and opaque cloud
scenes at any of the standard levels. For the clear sky scene, the calculations shall adopt the
surface state and the vertical distribution of temperature and radiative active gases as specified
by the forecast profiles for each of the original forecast grids. For the opaque cloud scenes,
the vertical distribution of temperature and radiative active gases shall
be taken from the
forecast model for each of the original forecast grid points, with an opaque cloud inserted at
the standard levels between the surface and top of atmosphere, nominally 31 levels. The
spectral response functions of the channels and the satellite viewing angle shall be taken into
account.
2. Tropospheric Humidity Generation Tables
The Tropospheric Humidity Generation Tables represent the synthetic radiances for the
WV6.2 and WV7.3 channels for each of the original forecast grids under specific clear sky
atmospheric conditions. The synthetic radiances shall be based on radiative transfer
calculations. The spectral response function of WV6.2 and WV7.3, and the satellite viewing
angle shall be taken into account. The radiative transfer calculations make certain
assumptions concerning the atmospheric profiles. The temperature profile used is the forecast
one. The vertical distribution of radiative gases other than water vapour shall be the same as
specified by the forecast profiles for each of the original forecast grid points. The forecast
specific humidity profile is not used. Instead, the radiative transfer calculations for these two
channels shall be made with two synthetic specific humidity profiles. In both profiles the
variation of specific humidity with height in the layers between the surface and a threshold
(defined by a set-up parameter) shall be calculated from the assumption that the relative
humidity in these layers is constant. Two values, defined by set-up parameters, shall be
adopted for this constant relative humidity. For levels above another threshold (defined by
set-up parameter) the specific humidity shall
be taken to be constant as defined by a set-up
parameter for both profiles. For the levels between the two height thresholds the variation of
the specific humidity shall
be based on an interpolation between the specific humidity value
at the second threshold level and the value at first threshold level. This interpolation shall be
based on the assumption that the specific humidity depends on the third power of pressure,
but shall not be less than the constant value above the first threshold.
3. Vicarious Calibration Tables
The Vicarious Calibration Tables represent the radiance in the Water Vapour channels, the
Ozone channel and the Carbon Dioxide channel, at the top of the atmosphere, propagating in
the direction of the satellite. These radiances shall be based on radiative transfer calculations
for particular clear sky scenes. The calculations shall adopt the surface state and the vertical

<!-- source_page: 46 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




distribution of temperature and radiative active gases as specified by observed profiles. The
spectral response functions of the channels and the satellite viewing angle shall be taken into
account.
4. Two-Path Transmission Tables
The Two-Path Transmission Tables represent the transmission from the TOA to each standard
pressure level and back to TOA in the solar affected channels. The two-path transmission is
determined by the fast radiative transfer model (RTTOV) using the forecast data provided
along with the satellite and calculated solar viewing angles. In addition to the two-path
transmission the calculated path-length for each grid point shall be provided. The solar angle
shall
be limited to 70 degrees.
5. Contribution Function Tables
The Contribution Function Tables shall contain as a function of pressure the normalised total
contribution function and the normalised total cumulative contribution function for radiation
propagating upwards towards the satellite for each of the eight infrared channels.
The Contribution Function shall be based on radiative transfer calculations for clear sky
scenes. These calculations shall adopt the surface state and the vertical distribution of
temperature and radiative active gases as specified by the forecast profiles for each of the
original forecast grids. The spectral response functions of the channels and the satellite
viewing angle shall be taken into account.
The generation of the Contribution Function tables for each of the eight infrared channels shall
include the following steps:
1) At the upper boundary of the highest layer the total atmospheric transmission for radiation
propagating in the upward direction towards the satellite shall be set to a value defined by a
set-up parameter.
2) At the lower boundary of each layer, the total atmospheric transmission for radiation
propagating in the upward direction towards the satellite shall be calculated as the product
of the total atmospheric transmission for radiation propagating in the upward direction
towards the satellite at the upper boundary of that layer and the transmission for radiation
propagating in the upward direction towards the satellite of that layer.
3) At each level, the cumulative contribution function for radiation propagating in the upward
direction towards the satellite shall
be calculated as the product of the upwelling radiance
of radiation propagating in the upward direction towards the satellite and the total
atmospheric transmission for radiation propagating in the upward direction towards the
satellite.
4) At each level, the contribution function for radiation propagating in the upward direction
towards the satellite shall be calculated as the derivative of the cumulative contribution
function for radiation propagating in the upward direction towards the satellite and the
natural logarithm of pressure.
5) At each level, the total cumulative contribution function for radiation propagating in the
upward direction towards the satellite covering the spectral region of the particular channel
shall be calculated as the arithmetic mean of the cumulative contribution function for
radiation propagating in the upward direction towards the satellite, weighted with the
spectral response function.

<!-- source_page: 47 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




6) At each level, the total contribution function of radiation propagating in the upward
direction towards the satellite covering the spectral region of the particular channel shall be
calculated as the arithmetic mean of the contribution function for radiation propagating in
the upward direction towards the satellite, weighted with the spectral response function.
7) At each level, the normalised total cumulative contribution function for radiation
propagating in the upward direction towards the satellite covering the spectral region of the
particular channel shall be calculated as the ratio of the total cumulative contribution
function for radiation propagating in the upward direction towards the satellite covering the
spectral region of the particular channel and the total radiance at the top of the atmosphere
of radiation propagating in the upward direction towards the satellite covering the spectral
region of the particular channel.
8) At each level, the normalised total contribution function of radiation propagating in the
upward direction towards the satellite shall be calculated as the ratio of the total contribution
function of radiation propagating in the upward direction towards the satellite and the
maximum value of the total contribution function of radiation propagating in the upward
direction towards the satellite.
4.3.3 Physical Principles
For a detailed description of the RTTOV algorithms, refer to the RTTOV 11 Science and Validation
Plan (NWPSAF-MO-TV-032).
4.3.4 Automatic Quality Control (AQC)
No AQC checks are required.
4.4 Outputs
The tables that follow detail each table to be produced. Each table shall be produced:

<!-- source_page: 48 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 49 of 298

ATMOSPHERIC CORRECTION TABLES
Parameter Mnemonic Units Min Max Acc Prec To
Radiance at top of the atmosphere 

38. ,pt
mWm-2sr-1(cm-1) -1 0 - - - SCE, AMV, CAL, CLA,
CDS
Clear sky and opaque cloud at standard levels,
including position, zenith angle 

62. ,pt
mWm-2sr-1(cm-1) -1 0 - - -
on the original forecast grid within the EMD
processing area 

73. ,pt
mWm-2sr-1(cm-1) -1 0 - - -


87. ,pt
mWm-2sr-1(cm-1) -1 0 - - -


97. ,pt
mWm-2sr-1(cm-1) -1 0 - - -


10 8. ,pt
mWm-2sr-1(cm-1) -1 0 - - -


12 0. ,pt
mWm-2sr-1(cm-1) -1 0 - - -


13 4. ,pt
mWm-2sr-1(cm-1) -1 0 - - -
Radiance at bottom of atmosphere 

38. ,pb
mWm-2sr-1(cm-1) -1 0 - - - SCE, AMV, CAL, CLA,
CDS
Clear sky and black cloud at standard levels,
including position, zenith angle 

62. ,pb
mWm-2sr-1(cm-1) -1 0 - - -
on the original forecast grid within the EMD
processing area 

73. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


87. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


97. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


10 8. ,pb
mWm-2sr-1(cm-1) -1 0 - - -

<!-- source_page: 49 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 50 of 298

ATMOSPHERIC CORRECTION TABLES
Parameter Mnemonic Units Min Max Acc Prec To


12 0. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


13 4. ,pb
mWm-2sr-1(cm-1) -1 0 - - -
Downwelling atmospheric radiance from above a
black cloud at each of the standard pressure levels   ,8.3 bp
mWm-2sr-1(cm-1) -1 0 - - - OCA
Black cloud at each standard pressure level  

,2.6 bp
mWm-2sr-1(cm-1) -1 0 - - -
on the original forecast grid within the EMD
processing area  

,3.7 bp
mWm-2sr-1(cm-1) -1 0 - - -
 

,7.8 bp
mWm-2sr-1(cm-1) -1 0 - - -
 

,7.9 bp
mWm-2sr-1(cm-1) -1 0 - - -
 

,8.10 bp
mWm-2sr-1(cm-1) -1 0 - - -
 

,0.12 bp
mWm-2sr-1(cm-1) -1 0 - - -
 

,4.13 bp
mWm-2sr-1(cm-1) -1 0 - - -
Upwelling atmospheric radiance from above a black
cloud at each of the standard pressure levels 

38. ,pb
mWm-2sr-1(cm-1) -1 0 - - - OCA
Black cloud at each standard pressure level 

62. ,pb
mWm-2sr-1(cm-1) -1 0 - - -
on the original forecast grid within the EMD
processing area 

73. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


87. ,pb
mWm-2sr-1(cm-1) -1 0 - - -

<!-- source_page: 50 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 51 of 298

ATMOSPHERIC CORRECTION TABLES
Parameter Mnemonic Units Min Max Acc Prec To


97. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


10 8. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


12 0. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


13 4. ,pb
mWm-2sr-1(cm-1) -1 0 - - -
Upwelling atmospheric radiance from below a black
cloud at each of the standard pressure levels 

38. ,pb
mWm-2sr-1(cm-1) -1 0 - - - OCA
Black cloud at each standard pressure level 

62. ,pb
mWm-2sr-1(cm-1) -1 0 - - -
on the original forecast grid within the EMD
processing area 

73. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


87. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


97. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


10 8. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


12 0. ,pb
mWm-2sr-1(cm-1) -1 0 - - -


13 4. ,pb
mWm-2sr-1(cm-1) -1 0 - - -
Transmission to top of atmosphere from each
standard pressure level    ,8.3 bp

- 0 1 - - OCA
on the original forecast grid within the EMD
processing area    ,2.6 bp

- 0 1 - -

<!-- source_page: 51 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 52 of 298

ATMOSPHERIC CORRECTION TABLES
Parameter Mnemonic Units Min Max Acc Prec To
   ,3.7 bp

- 0 1 - -
   ,7.8 bp

- 0 1 - -
   ,7.9 bp

- 0 1 - -
   ,8.10 bp

- 0 1 - -
   ,0.12 bp

- 0 1 - -
   ,4.13 bp

- 0 1 - -
Transmission to surface from each standard pressure
level    ,8.3 bp

- 0 1 - - OCA
on the original forecast grid within the EMD
processing area    ,2.6 bp

- 0 1 - -
   ,3.7 bp

- 0 1 - -
   ,7.8 bp

- 0 1 - -
   ,7.9 bp

- 0 1 - -
   ,8.10 bp

- 0 1 - -
   ,0.12 bp

- 0 1 - -
Emissivity at the surface - - 0 1 - - OCA
Table 6: IR Radiative Transfer Model: Atmospheric Correction Tables

<!-- source_page: 52 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 53 of 298



TROPOSPHERIC HUMIDITY GENERATION TABLES
Parameter Mnemonic Units Min Max Acc Prec To
Radiance at top of the atmosphere 

62. ,pt
mWm-2sr-1(cm-1) -1 0 - - - TH
for two values of relative humidity on the original
forecast grid within the EMD processing area 

73. ,pt
mWm-2sr-1(cm-1) -1 0 - - -
Table 7: IR Radiative Transfer Model: Tropospheric Humidity Generation Tables
VICARIOUS CALIBRATION TABLES
Parameter Mnemonic Units Min Max Acc Prec To
Radiance at top of the atmosphere 

62. ,pt
mWm-2sr-1(cm-1) -1 0 - - - CAL


73. ,pt
mWm-2sr-1(cm-1) -1 0 - - -


97. ,pt
mWm-2sr-1(cm-1) -1 0 - - -


13 4. ,pt
mWm-2sr-1(cm-1) -1 0 - - -
Table 8: IR Radiative Transfer Model: Vicarious Calibration Tables
CONTRIBUTION FUNCTION TABLES
Parameter Mnemonic Units Min Max Acc Prec To
Normalised total contribution function and total
cumulative contribution function as a function of
pressure (for all the standard pressure levels
provided by the ECMWF as defined by the set-up
parameter) for all eight IR channels, i
NTCi, NTCCi - 0 1 10-3 10-4 AMV
Table 9: IR Radiative Transfer Model: Contribution Function Tables

<!-- source_page: 53 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 54 of 298


TWO-PATH TRANSMISSION TABLES
Parameter Mnemonic Units Min Max Acc Prec To
Path-Length l - 2 6.787 (note 1) - - OCA
2-Path Transmission    ,6.0 bp

- 0 1 - -
on the original forecast grid within the EMD
processing area    ,8.0 bp

- 0 1 - -
   ,6.1 bp

- 0 1 - -
   ,8.3 bp

- 0 1 - -
Table 11: IR Radiative Transfer Model: 2-Path Transmission Tables. (Note 1: This is a function of the maximum angles permitted in the calculation. The maximum
solar angle is currently 70 degrees and the maximum satellite angle currently is 75 degrees).

<!-- source_page: 54 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




4.5 Prototyping and Testing
This section describes the prototyping activities, highlighting the major problems which were
encountered with this development.
4.5.1 Prototyping
4.5.1.1 Installation
Installation details are described in the documentation provided by the supplier.
4.5.2 Test Data
An internal EUMETSAT validation was performed comparing different MPEF products generated
using the MPEF RTM using RTTOV 9.3 and RTTOV 11.2.
4.5.3 Test Results
For a detailed description of the internal EUMETSAT validation, refer to the product validation report
(EUM/TSS/REP/14/781236).
4.6 Future Enhancements
No future enhancements are currently foreseen.
4.7 References
Reference Title Date Author(s)
Int. J. Remote Sensing,
Vol 19, No 14, 2753 –
2774
Classification-based emissivity for
land surface temperature
measurement from space
1998 W.C. Snyder, W, Wan, Y.
Zang and Y.Z. Feng
J. Atmos. Oceanic. Tech.
Vol 13, No. 1, 126 – 141
Wind speed effects on Sea Surface
Emission and Reflection from the
Along Track Scanning
Radiometer
1996 Watts, P.D., Allen, M.R.,
Nightingale, T.J.
NWPSAF-MO-UD-028 RTTOV v11 Users Guide 2014 J Hocking, P Rayer, D
Rundle, R Saunders.
NWPSAF-MO-TV-032 RTTOV 11 Science and
Validation Plan
2013 R Saunders
EUM/TSS/REP/14/781236 MPEF Release 2.1 Validation Test
Report
2014 S Joro

<!-- source_page: 55 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




4.8 Symbols and Definitions
A list of all variables used in this algorithm, toge ther with their meanings and units, is in the table
below.

Mnemonic Parameter Units
 Wavenumber cm -1
µ cos  -
 Satellite viewing angle degree
Sol Solar zenith angle degree
p Pressure hPa
pb Pressure at lower boundary hPa
po Reference pressure hPa
p1 Reference pressure hPa
  Total upward propagating radiance mWm -2sr-1(cm-1)-1
 Total downward propagating radiance mWm-2sr-1(cm-1)-1
v
 Upward propagating radiance mWm -2sr-1(cm-1)-1
v
 Downward propagating radiance mWm-2sr-1(cm-1)-1
 Transmission -
 2-Path Transmission -
 Surface emissivity -
B Planck function mWm-2sr-1(cm-1)-1
T Temperature K
Tsfc Surface temperature K
qi Mixing ratio of the ith radiative active gas kg kg -1
NTC Normalised Total Contribution Function -
NTCC Normalised Total Cumulative Contribution Function -
l Path Length -

<!-- source_page: 56 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




5 SCENES ANALYSIS
5.1 Algorithm Configuration Information
No specific information on configuration.
5.1.1 Algorithm Name
Scenes Analysis (SCE).
5.1.2 Algorithm Identifier
EUM_MSG_SCE_A001
5.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 H.-J. Lutz SCE Baseline
1.1 26/5/97 H.-J. Lutz Updated for the resolution of AMV and CLA TBDs.
1.2 2/7/97 H.-J. Lutz Additional tests added to improve the robustness of the
algorithm to give greater confidence in the classification of a
pixel as cloudy or clear.
1.3 8/12/97 H. K. Wilson Kick-off clarification points added, Requirements Analysis
clarification points added.
1.4 11/3/98 H. K. Wilson Peer Group Review changes added.
1.5 15/1/99 H.-J. Lutz Detailed Design Phase changes added.
1.6 31/1/02 H.-J. Lutz Changes added, according to ECPs 297, 298, 299.
1.7 25/7/05 T. Heinemann Updated according to AR 10973.
1.8 7/09/07 O. Samain Updated according to AR 10095, 15892, 16003 and ECP 804.
1.9 05/05/08 O. Samain Updated for specific channel availability criteria and threshold
test applications.
5.2 Inputs
5.2.1 Image and Preprocessing Data (Dynamic Application Data)
The main input of the Scenes Analysis algorithm is the level 1.5 data from all MSG channels. The
image data shall be available in the form of reflectances (%) for the VIS/NIR channels, and in the
form of equivalent black body brightness temperatures (EBBT) in kelvin (K) for the IR/WV channels.
For information on the derivation of the EBBT and of the reflectances, see Table 10 and Table 11,
also the EUMETSAT website:
Access to Data > Meteosat Meteorological Products > Calibration > Meteosat Second
Generation
Additionally, the Scenes Analysis algorithm shall use data from a subset of channels from the
previous repeat cycle. The following table defines the input data required from the level 1.5 image
data.

<!-- source_page: 57 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 58 of 298


LEVEL 1.5 IMAGE DATA AND DATA DERIVED FROM THE IMAGE DATA
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Reflectances for channels VIS0.6, VIS0.8, NIR1.6, IR3.9_sol,
HRVIS
REFLchannel % 0 150 0.1 0.1 pixel Derived from level 1.5
image data
EBBTs for channels IR3.9, WV6.2, WV7.3, IR8.7, IR9.7, IR10.8,
IR12.0, IR13.4
EBBTIchannel K 170 350 0.1 0.1 pixel Derived from level 1.5
image data
Local mean, minimum, maximum and standard deviation on a 3 x
3 pixel segment for channels VIS0.6, VIS0.8, NIR1.6, IR3.9,
IR8.7, IR9.7, IR10.8, IR12.0, IR13.4, WV6.2, WV7.3, HRVIS
mn_REFL/EBBT
max_REFL/EBBT
min_REFL/EBBT
std_REFL/EBBT
- - - - - pixel Derived from level 1.5
image data

Reflectances of the previous repeat cycle for channels VIS0.6,
VIS0.8
prev_REFLchannel % 0 120 0.1 0.1 pixel Derived from previous
level 1.5 image data
EBBTs of the previous repeat cycle for channels: IR3.9, IR10.8,
IR12.0
prev_EBBTIchannel K 170 350 0.1 0.1 pixel Derived from previous
level 1.5 image data
Start times of current and previous repeat cycle start_current_image
start_previous_image
mins - - 1 1 - Derived from level 1.5
image data
Solar Zenith Angle sol_zenith degrees 0 90 0.1 0.1 pixel Derived from level 1.5
image data
Satellite Observing Angle sat_zenith degrees 0 90 0.1 0.1 pixel Derived from level 1.5
image data
Relative azimuth angle sun/sat sol_sat_azimuth degrees 0 360 0.1 0.1 pixel Derived from level 1.5
image data
Line radiometric quality flag (per channel) LRQF_channel - - - - - image line Level 1.5 data header
Table 10: Scenes Analysis Product: Input data required from the level 1.5 image data

<!-- source_page: 58 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 59 of 298

5.2.2 Data from other MPEF Algorithms (Dynamic Application Data)
The Scenes Analysis algorithm shall use data from other MPEF algorithms, as defined in the following table:

DATA FROM OTHER MPEF ALGORITHMS
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Scenes Analysis Data from previous repeat cycle prev_scene_type - 0 255 1 1 pixel SCE of previous repeat cycle
Clear sky reflectances from previous repeat cycle for
channels: VIS0.6, VIS0.8, NIR1.6
prev_CSR_REFL % 0 150 0.1 0.1 CSR processing segment CSR intermediate product of previous
repeat cycle
Clear sky brightness temperatures from previous
repeat cycle for channels: IR3.9, IR8.7, IR9.7, IR10.8,
IR12.0, IR13.4, WV6.2, WV7.3
prev_CSR_EBBT K 230 350 0.1 0.1 CSR processing segment CSR intermediate product of previous
repeat cycle
Forecast brightness temperatures for channels: IR3.9,
WV6.2, WV7.3, IR8.7, IR9.7, IR10.8, IR12.0, IR13.4
for_EBBTchannel K 230 350 0.1 0.1 pixel RTM
MSG Clear Sky Reflectance Map, for channels:
VIS0.6, VIS0.8, NIR1.6, IR3.9_sol
MRMchannel % 0 100 0.1 0.1 pixel SCE - clear sky reflectances image,
updated multiple times per day
Mean solar zenith, satellite zenith and relative azimuth
angle for the Clear Sky Reflectance Map
MRM_sol_zenith
MRM_sat_zenith
MRM_rel_azi
degrees
degrees
degrees
0
0
0
90
90
360
0.1
0.1
0.1
0.1
0.1
0.1
pixel
pixel
pixel
SCE - clear sky reflectances image,
updated multiple times per day
Table 11: Scenes Analysis Product: Data from other MPEF algorithms

<!-- source_page: 59 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




5.2.3 Static Application Data
The static application data used by the Scenes Analysis algorithm shall consist of the following:
 pixel-based map of surface-type. The surface types are as follows:
 evergreen needle-leaf forest, evergreen broadleaf forest, deciduous needle-leaf forest,
deciduous broadleaf forest, mixed deciduous forest, closed shrubland, open shrubland, woody
savannah, savannah, grassland, permanent wetland, cropland, urban, crop/natural vegetation
mosaic, permanent snow/ice, barren/desert, water bodies, tundra and mixed land/water (land
pixels containing small rivers or lakes)
 pixel-based map of surface elevation
 pixel-based map containing the distance of each pixel to the nearest coast (in km)
 spectral albedo tables for channels VIS0.6, VIS0.8, NIR1.6, IR3.9 and for each surface type
 the normalised bi-directional reflectance functions ( BDRF) for each surface type;
the normalisation is with respect to the spectral bi-hemispherical albedo
 static thresholds
 static parameters for the different mathematical expressions used in the algorithm
The static data sets needed for the Scenes Analysis processing are summarised in the following tables,
one for surface information including spectral properties of the different surface types and one for
SCE thresholds and SCE parameters.
The tables that follow detail the static application data that shall be produced.

<!-- source_page: 60 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 61 of 298



STATIC APPLICATION DATA - SURFACE DATA/SPECTRAL PROPERTIES
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Surface elevation elevation m 0 8900 100 100 pixel Static data
Surface-Type-Map surface_type_map - 0 99 1 1 pixel Static data
Nearest Coast Map Nearest_coast 0 1000 1 1 pixel Static data
Spectral albedo for each surface type, for channels: VIS0.6, VIS0.8,
NIR1.6 and IR3.9
clim_alb % 0 100 0.1 0.1 - Static data
Normalised bi-directional reflectance function for each surface type,
for channels: VIS0.6, VIS0.8, NIR1.6 and IR3.9
norm_BDRF - 0 1.5 0.01 0.01 - Static data
Table 12: Scenes Analysis Product: Static Application Data Produced, Surface Data Spectral Properties
STATIC APPLICATION DATA –AND PARAMETERS THRESHOLDS
Parameter Mnemonic Units Min Max Pre Acc Res Source
Solar zenith threshold for normalisation
Solar zenith threshold for day
Solar zenith threshold for night
SZ_normalize
SZ_day
SZ_night
degrees
degrees
degrees
0
0
0
90
90
100
1
1
1
1
1
1
-
-
-
Static data
Static data
Static data
Nominal repeat cycle duration rc_nom_dur mins 0 15 0.5 0.5 - Static data
Static SCE thresholds:
Max temperature difference between CSR EBBT in channel
IR10.8 and the forecast EBBT in step 1
max_temp_diff

K -20 20 0.1 0.1 - Static data
Search area size for clear pixels in step 1 m1 pixel 0 32 1 1 - Static data
Search area enlargement factor in step 1 nenl 1 4 1 1 - Static data

<!-- source_page: 61 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 62 of 298

STATIC APPLICATION DATA –AND PARAMETERS THRESHOLDS
Parameter Mnemonic Units Min Max Pre Acc Res Source
Time threshold for maximum start time difference between two
repeat cycles for step 1
max_time minutes 0 360 1 1 - Static data
Search area size for CSR in step 1 m2 pixel 0 32 1 1 - Static data
Max SD for step 1 std_maxchan K 0 20 0.1 0.1 - Static data
Reflectance and temperature thresholds - step 3 refl_min % 0 150 0.1 0.1 - Static data
temp_min K 170 350 0.1 0.1 - Static data
temp_max K 170 350 0.1 0.1 - Static data
Threshold to determine max start time difference between two
repeat cycles for step 4
max_num - 0 6 1 1 - Static data
Reflectance threshold for step 4 VIS_change % 0 150 0.1 0.1 - Static data
Temperature value to determine the IR threshold in step 4 step4_temp K 170 350 0.1 0.1 - Static data
Thresholds for tests 1a to 1d refl_test1a_add_max_{land,coast,sea} % 0 50 0.1 0.1 - Static data
refl_test1b_add_max_{land,coast,sea} % 0 50 0.1 0.1 - Static data
refl_test1b_add_min_{land,coast,sea} % 0 50 0.1 0.1 - Static data
refl_test1c_add_max_{land,coast,sea} % 0 50 0.1 0.1 - Static data
refl_test1c_add_min_{land,coast,sea} % 0 50 0.1 0.1 - Static data
refl_test1d_add_max_{land,coast,sea} % 0 50 0.1 0.1 - Static data
refl_test1d_add_min_{land,coast,sea} % 0 50 0.1 0.1 - Static data
Thresholds for tests 2a to 2f a0,max1,2a to a0,max1,2f - - - - - - Static data
a 0,max2,2a to a0,max2,2f - - - - - - Static data

<!-- source_page: 62 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 63 of 298

STATIC APPLICATION DATA –AND PARAMETERS THRESHOLDS
Parameter Mnemonic Units Min Max Pre Acc Res Source
a0,min1,2a to a0,min1,2f - - - - - - Static data
a 0,min2,2a to a0,min2,2f - - - - - - Static data
a1,max1,2a to a1,max1,2f - - - - - - Static data
a 1,max2,2a to a1,max2,2f - - - - - - Static data
a1,min1,2a to a1,min1,2f - - - - - - Static data
a 1,min2,2a to a1,min2,2f - - - - - - Static data
Thresholds for tests 3a to 3d temp3a_{land, coast, sea}_{min, max} K 0 50 0.1 0.1 - Static data
temp3b_{land, coast, sea}_{min, max} K 0 50 0.1 0.1 - Static data
temp3c_{land, coast, sea}_{min, max} K 0 50 0.1 0.1 - Static data
temp3d_{land, coast, sea}_{min, max} K 0 50 0.1 0.1 - Static data
Correction for diurnal temperature cycle Dtc_corr_fac(Surface type) K 0 50 0.1 0.1 - Static data
Correction for forecast grid surface type Undef_corr_min K 0 50 0.1 0.1 - Static data
Maximum cloud temperature temp_cloud_max_sea K 0 500 1 1 - Static data
temp_cloud_max_land K 0 500 1 1 - Static data
Minimum surface temperature temp_clear_min_sea K 0 500 1 1 - Static data
temp_clear_min_land K 0 500 1 1 - Static data
Thresholds for tests 4a to 4j a0,4a to a0,4k - - - - - - Static data
a 1,4a to a1,4k - - - - - - Static data
a2,4a to a2,4k - - - - - - Static data
b 0,4a to b0,4k - - - - - - Static data
b 1,4a to b1,4k - - - - - - Static data

<!-- source_page: 63 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 64 of 298

STATIC APPLICATION DATA –AND PARAMETERS THRESHOLDS
Parameter Mnemonic Units Min Max Pre Acc Res Source
b2,4a to b2,4k - - - - - - Static data
c 0,4d to c2,4d - - - - - - Static data
test4d_lat_limit - 0 90 0.1 0.1 - Static data
Thresholds for tests 5a to 5h test5a_{land, sea} % 0 50 0.1 0.1 - Static data
test5b_{land, sea} % 0 50 0.1 0.1 - Static data
test5c_{land, sea} % 0 50 0.1 0.1 - Static data
test5d_{land, sea} % 0 50 0.1 0.1 - Static data
test5e_{land, sea} K 0 50 0.1 0.1 - Static data
test5f_{land, sea} K 0 50 0.1 0.1 - Static data
test5g_{land, sea} K 0 50 0.1 0.1 - Static data
test5h_{land, sea} K 0 50 0.1 0.1 - Static data
Coefficients to derive thresholds for test6 c1_vis_{06, 08}
c2_vis_{06, 08}
K
%
-
-
-
-
-
-
-
-
-
-
Static data
Static data
Temperature threshold for test7 tempsnow0 K 170 280 0.1 0.1 Static data
Tempsnow1 K -100 100 0.1 0.1 Static data
Tempsnow2 K -100 100 0.1 0.1 Static data
Tempsnow3 K -100 100 0.1 0.1 Static data
Tempsnow4 K -100 100 0.1 0.1 Static data
Reflsnow1 % 0 100 0.1 0.1 Static data
Reflsnow2 % 100 100 0.1 0.1 Static data
Reflsnow3 % 100 100 0.1 0.1 Static data

<!-- source_page: 64 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 65 of 298

STATIC APPLICATION DATA –AND PARAMETERS THRESHOLDS
Parameter Mnemonic Units Min Max Pre Acc Res Source
Threshold to define sunglint conditions sgl_criteria degrees 0 90 0.1 0.1 - Static data
Max time difference for updating Clear Sky Reflectance Map map_max_time hours 0 6 0.25 0.25 - Static data
Elevation EBBT elevation_EBBT m 0 10000 1 1 - Static data
Temperature gradient (K/km) temp_elev_corr K 0 50 0.1 0.1 - Static data
Time interval time_int minutes 0 360 1 1 - Static data
Min number of tests required for AQC MinTestRequired - 1 100 1 1 - Static data
Distance to Coast DistCoast pixel 0 3712 1 1 Static data
Near coast temperature adjustment over ocean (array for all 8 IR
channels)
TempAdjustWater K -100 100 0.1 0.1 Static data
Near coast temperature adjustment over land (array for all 8 IR
channels)
TempAdjustLand K -100 100 0.1 0.1 Static data
Maximum difference between sun and viewing zenith angle MaxScatAngle degrees 0 180 1 1 - Static data
Latest Clear Sky Reflectance Map (CRM) of the day. CrmHourHigh hours 0 24 0 24 - Static data
First CRM of the day. CrmHourLow hours 0 24 0 24 - Static data
Noon definition CrmNoon hours 0 24 12 12 - Static data
Time step for multiple CRM per day CrmUpdateStep hours 0 24 2 2 - Static data
Temperature below which the correction for cold desert surfaces
applies
ColdSurfCorrTstart K 0 500 0.1 0.1 - Static data
Slope for the cold surface correction ColdSurfCorrTslope K/K 0 1 0.1 0.1 - Static data
Maximum for the cold surface correction ColdSurfCorrMax K 0 10 0.1 0.1 - Static data
Table 13: Scenes Analysis Product: Static application data and parameters thresholds
Note: All static application data specified in the above tables shall be configurable.

<!-- source_page: 65 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




5.3 Algorithm Functional Specification
5.3.1 Overview
Several products which are derived from the MSG image data require information on the type of
scene contained within a pixel. While some products are derived from cloudy pixels like Cloud Top
Height (CTH), Atmospheric Motion Vectors (AMV), others are derived from clear pixels only (Clear
Sky Radiances (CSR), for example). For calibration monitoring and vicarious calibration, it is very
important that the pixels of selected Earth targets are really cloud-free. Thus the classification of the
pixels within a segment, like Scenes Analysis, is a critical process within the MPEF.
The main function of the Scenes Analysis algorithm is to identify whether a pixel contains clouds or
not. In this process, pixels partially covered by clouds or covered with semi-transparent clouds will be
marked as cloudy pixels. The algorithm can also identify if the pixel is clear with confidence. In some
situations when it is difficult to decide between clear and cloudy, the result of the algorithm may be
‘unknown’. Pixels identified as clear will contain the information of the surface type which comes
from the surface type map. In the case of snow or ice covered pixels, specific checks are used to avoid
false cloud detection.
The concept of the Scenes Analysis algorithm is based on a threshold technique, which has been
prototyped using AVHRR and GOES data. The algorithm is performed nominally on a pixel basis,
however this shall
be configurable. The following steps are performed for the Scenes Analysis. These
are shown graphically in Figure 4.

Step 1 Prediction of the clear sky brightness temperature: Predict the clear sky brightness
temperature for channels IR3.9, WV6.2, WV7.3, IR8.7, IR9.7, IR10.8, IR12.0 and
IR13.4 by using the Scenes Analysis results, the measured EBBTs and the clear sky
radiances product of the previous repeat cycle and by using the output tables of the
RTM.

Step 2 Solar zenith angle check: Check the solar zenith angle data for each pixel to determine
the local time, i.e. day, dawn/dusk and night. This defines the channels and the
threshold tests which are required to be used in the following steps

Step 3 Channel availability and quality check: Check channel availability and quality for
each pixel using the information from the data preparation to determine which of the
channels can be used, i.e. which of the threshold tests can be applied.

Step 4 Data comparison with previous repeat cycle: Compare the data of the current repeat
cycle with the data from the previous repeat cycle for some channels, to determine if the
data have changed. If no change (within given boundaries) is detected, it is assumed that
the Scenes Analysis algorithm will provide the same result as the previous run,
therefore the previously identified scene can be used and all other steps skipped. This
step shall have the possibility to be disabled.

<!-- source_page: 66 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Step 5 Threshold determination: Determine the thresholds to be used for each of the tests of
the scenes type identification.

Step 6 Scenes type identification: Identify the scenes type using threshold tests.

The threshold technique is based on the concept of comparing the image data with thresholds which
mark the border between the physical signal (i.e. EBBT and reflectance) of a pixel without clouds and
a pixel containing clouds. The Scenes Analysis algorithm can also use the data of the previous image
as a prediction for the current image. Also, spatial information (maximum, minimum, mean, standard
deviation) is used to supplement the Scenes Analysis process. The threshold technique makes optimal
use of the spectral information provided for each pixel with the measurements in all twelve channels.
The following threshold tests shall
be used as a baseline in the Scenes Analysis algorithm:

Test Specification
Test1a reflectance test using channel VIS0.6
Test1b reflectance test using channel VIS0.8
Test1c reflectance test using channel NIR1.6
Test1d reflectance test using channel IR3.9_sol
Test2a reflectance difference test VIS0.8/VIS0.6
Test2b reflectance difference test NIR1.6/VIS0.6
Test2c reflectance difference test IR3.9_sol/VIS0.6
Test2d reflectance difference test NIR1.6/VIS0.8
Test2e reflectance difference test IR3.9_sol/VIS0.8
Test2f reflectance difference test IR3.9_sol/NIR1.6
Test3a temperature test using channel IR3.9
Test3b temperature test using channel IR8.7
Test3c temperature test using channel IR10.8
Test3d temperature test using channel IR12.0
Test4a temperature difference IR10.8 – IR3.9
Test4b temperature difference IR10.8 – IR6.2
Test4c temperature difference IR10.8 – IR7.3
Test4d temperature difference IR10.8 – IR8.7
Test4e temperature difference IR10.8 – IR12.0
Test4f temperature difference IR10.8 – IR13.4
Test4g temperature difference IR12.0 – IR3.9
Test4h temperature difference IR12.0 – IR6.2
Test4i temperature difference IR12.0 – IR7.3
Test4j temperature difference IR12.0 – IR8.7
Test4k temperature difference IR12.0 – IR13.4
Test5a standard deviation of channel HRVIS for n x n processing segment (n is nominally 9)

<!-- source_page: 67 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Test Specification
Test5b standard deviation of channel VIS0.6 for n x n processing segment (n is nominally 3)
Test5c standard deviation of channel VIS0.8 for n x n processing segment (n is nominally 3)
Test5d standard deviation of channel NIR1.6 for n x n processing segment (n is nominally 3)
Test5e standard deviation of channel IR3.9 for n x n processing segment (n is nominally 3)
Test5f standard deviation of channel IR8.7 for n x n processing segment (n is nominally 3)
Test5g standard deviation of channel IR10.8 for n x n processing segment (n is nominally 3)
Test5h standard deviation of channel IR12.0 for n x n processing segment (n is nominally 3)
Test6 cloud test for sunglint conditions using channels IR3.9 and IR10.8
Test7 snow and ice test – during day
Table 14: Scenes Analysis, Threshold tests
During the lifetime of the satellite the algorithm may be updated, e.g. using more of the spectral
channels or including additional/disabling existing threshold tests, using the portable application
module concept (Future Enhancement). Therefore it is required that the algorithm shall
be designed
and implemented in such a way that these enhancements can be easily added.
Set-up parameters shall define which of the above tests are overall enabled, enabled over sea only,
enabled over land only, or overall disabled. In addition, the map indicating the distance of each pixel
to the nearest coast is used to select specific threshold parameters (when available) or to disable tests
that are not reliable along the coastlines.
The conditions under which each of these tests should be applied are described in the algorithm
description. At the beginning of the cloud threshold tests, each pixel is first assumed to be unknown.
The results of Scenes Analysis are quality checked for every pixel. For these quality checks, counters
indicating the number of individual tests reporting ‘cloud’, ‘clear’ or ‘unknown’ are used to provide a
quality mark indicating the confidence in the Scenes Analysis results.

<!-- source_page: 68 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




solar zenith angle
check
day / dawn /night
information
channel availability check
if required channels are available
continue processing
static datasets:
static solar zenith angle
thresholds

image data:
all channels of current image, subset of channels from previous
repeat cycle
MPEF products and pre-processed data:
Scenes Analysis and CSR of previous repeat cycle, forecasted EBBT,
clear sky reflectance map, sun / satellite geometry
pixel-based image data, products, pre-processed data
processing segment-based clear sky radiances (CSR)
static datasets:
static SCE parameters for
data comparison
data comparison with previous
repeat cycle
if changes have been detected
continue processing
static datasets:
static SCE parameters for
availability check


static datasets:
static SCE thresholds,
static SCE parameter,
pixel-based static surface
data
threshold prediction
thresholds for the different threshold tests

threshold tests
scenes type,
threshold test flag
automatic quality
control (AQC)
scenes type
test flag
quality flag
output data:
scenes type, location of the pixel, test flag, quality flag,
Clear Sky Reflectance Map, Predicted EBBT
if required channels are
not available stop
further processing
if no changes have been
detected use the results
of the previous repeat
cycle and stop further
processing
Update Clear Sky
Reflectance Map
CS_Ref_Map
previous,
scenes_type, Solar
Channels Image
Data
prediction of the clear sky EBBT

Figure 4: Scenes Analysis SCE Processing
5.3.2 Algorithm Description
The Scenes Analysis algorithm is performed in six steps, which are described in detail below. These
steps shall be performed for each pixel. All static application data, e.g. thresholds, parameters and
constants, shall be configurable.
The outcome of the third step (channel availability and quality check), the fourth step (data
comparison with previous repeat cycle) and each threshold test of the sixth step shall be marked with
a flag indicating its result. This flag is called hereafter the test flag.
For all threshold tests, the test flag shall be able to reflect four conditions, i.e. ‘test failed’, ‘cloud
detected’, ‘clear scene’ or ‘unknown scene’. Finally, the post-processing step of updating of the Clear
Sky surface Reflectance Map is described.

<!-- source_page: 69 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




5.3.2.1 Step 1: Prediction of Clear Sky EBBT
For tests Test3aTest3d (temperature tests) and for use by the CLA and AMV height assignment, the
clear sky brightness temperature (EBBT) shall be determined for channels IR3.9, WV6.3, WV7.3,
IR8.7, IR9.7, IR10.8, IR12.0 and IR13.4. The predicted EBBT (EBBTpred) shall be in units of kelvin
(K). The predicted EBBT shall be derived as follows:
 The scenes type from the previous repeat cycle shall be used to find within an m1 x m1 pixel
segment surrounding the current pixel location the three closest clear pixels. The EBBT
values of these pixels shall be averaged for each of the above-defined channels from the
previous repeat cycle. If the current pixel is located over land, only clear pixels with a land
surface type shall be used. Similarly for the sea pixels. The difference in starting time
between the previous and the current repeat cycle shall not exceed max_time. If not enough
clear pixels can be found as required above or if the time difference exceeds the threshold, the
Clear Sky Radiances product of the previous repeat cycle shall be used.
 The Clear Sky Radiances product of the previous repeat cycle is derived on an m2 x m2 pixel
segment. The CSR value with its location closest to the current pixel location shall be
selected. The difference in starting time between the previous and the current repeat cycle
shall not exceed max_time. The distance between the location of the CSR value and the
current pixel location shall not exceed m2+1 pixels. The standard deviation provided with the
CSR shall not exceed std_max. The clear sky radiance shall be converted to clear sky
equivalent black body brightness temperature (EBBT).
 Additionally, the Scenes Analysis algorithm shall use forecast EBBT derived from the
radiative transfer model, interpolated in time (to image frequency intervals representing the
expected nominal time of the repeat cycle) and space (to the pixel location). If the surface
elevation of the pixel is larger than elevation_EBBT, the forecast clear sky EBBT of channels
IR3.9, IR8.7, IR10.8 and IR12.0 shall be corrected by subtracting (pixel_elevation –
elevation_EBBT) * temp_elev_corr / 1000.
If the clear pixel averaging method or the CSR cannot be applied (as described above), or if the
difference between their value and the forecast EBBT is larger than max_temp_diff, the forecast
EBBT shall be used if it is valid for the whole image. Otherwise, the algorithm shall repeat this step
with max_time=max_time+time_int and by enlarging the search area size by a factor of nenl.
 The predicted EBBT for the above-specified channels shall be stored for later use in the
Cloud Analysis (CLA) and Atmospheric Motion Vector (AMV) algorithms. Pixels for which
the predicted EBBT is not derived shall
be set to a default value.
 In addition to the above, a predicted coldest EBBT for each pixel shall be derived from the
radiative transfer model, interpolated in time (to image frequency intervals representing the
expected nominal time of the repeat cycle). The values shall be derived from the surrounding
gridpoint with the coldest forecast EBBT in channel IR10.8.
5.3.2.2 Step 2: Solar Zenith Angle Check
The Scenes Analysis algorithm shall use information about the elevation of the sun in the form of the
solar zenith angle for each pixel. According to the solar zenith angle the local time of the day for a
single pixel shall be identified as the following:

<!-- source_page: 70 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




 day, if the solar zenith angle is lower than or equal to a threshold (SZ_day)
 night, if the solar zenith angle is greater than or equal to a threshold (SZ_night)
 dawn/dusk (i.e. either dawn or dusk), if the solar zenith angle is between the two above
thresholds (SZ_day, SZ_night)
5.3.2.3 Step 3: Check Channel Availability and Quality
For an optimal performance of the Scenes Analysis algorithm all MSG channels should be available
including the statistical information (i.e. mean, max, min, standard deviation) of n x n pixel matrices
derived for each pixel of all channels, where n is configurable and is nominally 3. As a minimum, two
channels out of the following shall be available:
 during daytime: two out of (VIS0.6/VIS0.8/NIR1.6/IR8.7/IR10.8/IR12.0).
 at dawn/dusk and during night: two out of IR3.9/IR8.7/IR10.8/IR12.0.
The line radiometric quality flag of the level 1.5 data header shall be checked for each channel, and
all pixels in a line flagged as ‘suspect’ or ‘do not use’ for this channel shall not be used.
Additionally the data shall be checked for unrealistic values, i.e. temperatures below a minimum
threshold (temp_min) and above a maximum threshold (temp_max), and reflectances below a
minimum threshold (refl_min) and above a maximum threshold (refl_max).
Where the channels are not available any tests using these channels cannot be performed and shall be
disabled via the updating of the test enable/disable set-up parameters.
If the minimum channels required, as stated above, are not available or if they are showing unrealistic
values, then:
 the scenes type shall be set to a default value stating ‘no scene identified, data not available’
 the test flag for this test shall be set to a value stating ‘no scene identified, data not available’
 the quality flag shall be set to a default value
 the following steps shall be skipped.
5.3.2.4 Step 4: Data Comparison with Previous Image
The current and previous image data in the form of EBBT/reflectances shall be compared in certain of
the channels for each pixel to verify whether there has been a significant change in the data. This
check shall
accept differences in starting time between the current and the previous repeat cycle of up
to a value max_num. The difference is defined as
n = (start_current_image - start_previous_image)/rc_nom_dur
Provided the most recent previous repeat cycle has a value of n smaller than or equal to max_num
then the absolute difference between the current and the previous image data is calculated for a subset
of the channels:
Absolute difference = ABS(current - previous)
As a minimum, two channels out of the following (VIS0.6, VIS0.8, IR3.9, IR10.8, IR12.0) shall
be
used for this check. If channel IR3.9 is available, it shall be one of these two channels because of its
sensitivity to any changes of the scene. During dawn/dusk and night channels VIS0.6 and VIS0.8
shall not be used for this check. The selection of the channels to be used for the check shall be
configurable.
For channels VIS0.6 and VIS0.8 a static threshold (VIS_change) shall be used for this check.

<!-- source_page: 71 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




For channels IR3.9, IR10.8 and IR12.0 the following formula shall be applied:
IR_threshold = (n +1) * step4_temp
where: n = (start_current_image - start_prev ious_image) / nominal repeat cycle duration
As stated above, if n is larger than max_num these tests shall not be performed and the algorithm
shall continue with the next step.
If no change has been detected in all channels used for this check (i.e. if the absolute differences are
smaller than the thresholds), then:
 the value of prev_scene_type for the pixel shall be used
 the test flag for this test shall be set to a value identifying the above and the test flags of
the previous threshold tests shall be used
 the quality flag from the previous AQC shall be used
 the subsequent processing steps shall be skipped
5.3.2.5 Step 5: Threshold Determination
For each of the threshold tests, the thresholds have to be determined. There are both static and
dynamic thresholds. Static thresholds are fixed physical values which are valid nominally for the
lifetime of the satellite. Dynamic thresholds are physical values which are changing (with a different
timescale) during the lifetime of the satellite and therefore need to be updated frequently.
THRESHOLD DETERMINATION FOR TEST1A, TEST1B, TEST1C AND TEST1D
For Test1a, Test1b, Test1c and Test1d (reflectance tests) the algorithm shall use a pixel-based
reflectance map to determine the reflectance for each pixel, for channels VIS0.6, VIS0.8, NIR1.6, and
IR3.9_sol. The reflectance maps shall be updated on a weekly basis by using clear sky reflectances
observed in channels VIS0.6, VIS0.8, NIR1.6 and IR3.9_sol for each of the pixels.
As these maps are only valid for a few specific times of the day (i.e. specific sun/satellite geometries)
the algorithm shall correct the read value for the specific angle dependency by using look-up tables
describing the bi-directional reflectance function (BDRF) dependency related to the solar zenith
angle, the satellite zenith angle and the relative azimuth angle (sun/satellite) and to the surface type,
and shall interpolate the BDRF values from the closest triple of angles (solar zenith, satellite zenith
and relative azimuth) to the current pair of angles, using a linear interpolation. The determined
reflectance for each of the three channels shall be derived by using the relationship:
REFL i,c = REFL i,m * BDRF i,c / BDRF i,m
where
 REFL i,c is the predicted clear sky reflectance in channel i for the current image c in %.
 REFL i,m is the clear sky reflectance in channel i from the Clear Sky Reflectance Map (CRM) m
in %. If multiple CRM per day are available, then the correct CRM to be used is the one whose
time stamp is equal to:
tepCrmUpdateStepCrmUpdateS
CrmHourLowtIntCrmHourLow c 




 




  14/1

Equation 1

if tc ≤ CrmNoon
or

<!-- source_page: 72 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




tepCrmUpdateStepCrmUpdateS
thCrmHourHigInthCrmHourHig c 




 




  14/1

Equation 2

if tc > CrmNoon
where:
tc is the time of the current image in hours

So, for example, for a time step of 2 hours, at 09:30 UTC the 10:00 UTC CRM shall be used, whereas
at 17:00 UTC the 16:00 UTC CRM shall be used.
In the case that a given CRM is not available, the CRM at noon shall be used instead.
 BDRF i,c is the normalised bi-directional reflectanc e function value for channel i valid for the
sun/satellite geometry at pixel location for the current image c.
 BDRF i,m is the normalised bi-directional reflectance function value for channel i valid for the
sun/satellite geometry at pixel location of the Clear Sky Reflectance Map m.
How this map is derived is described in Section 5.3. 2.7. If no Clear Sky Reflectance Map is available,
climatological albedo values, clim_alb, valid for the different surface types, for each of channel
VIS0.6, VIS0.8, NIR1.6 and IR3.9_sol, and for each month of the year, shall be used. The reflectance
value will be derived by multiplying the albedo with the BDRF valid for the sun/satellite geometry at
pixel location for the current image. The final threshold shall be derived as follows:
THR_TEST1A_MAX i = REFL i,c + refl_test1a_add_max
THR_TEST1A_MIN i = REFL i,c + refl_test1a_add_min
THR_TEST1B_MAX i = REFL i,c + refl_test1b_add_max
THR_TEST1B_MIN i = REFL i,c + refl_test1b_add_min
THR_TEST1C_MAX i = REFL i,c + refl_test1c_add_max
THR_TEST1C_MIN i = REFL i,c + refl_test1c_add_min
THR_TEST1D_MAX i = REFL i,c + refl_test1d_add_max
THR_TEST1D_MIN i = REFL i,c + refl_test1d_add_min

THRESHOLD DETERMINATION FOR TEST2A – TEST2F
For test_index = Test2a to Test2f the thresholds shall
be derived as follows:
THR_TEST(test_index)_MAX1 = a0,,max1,test_index + REFLmeas,0.6 * a1,max1,test_index
THR_TEST(test_index)_MAX2 = a0,max2,test_index + REFLmeas,0.6 * a1,max2,test_index
THR_TEST(test_index)_MIN1 = a0,min1,test_index + REFLmeas,0.6 * a1,min1,test_index
THR_TEST(test_index)_MIN2 = a0,min2,test_index + REFLmeas,0.6 * a1,min2,test_index
where REFL meas,y is the measured reflectance in channel y. The coefficients a 0,xx,yy and a 1,xx,yy are
different for land and sea.

<!-- source_page: 73 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




THRESHOLD DETERMINATION FOR TEST3A TO TEST3D
For Test3a to Test3d (temperature test) the clear sky brightness temperature (EBBT) shall be
determined for channels IR3.9, IR8.7, IR10.8 and IR12.0. The thresholds shall be determined from
the predicted EBBT (EBBT pred), which are derived in step 1 and which shall be in addition adjusted
for the following cases:
If the surface type of the pixel is land and different from the ones of the grid points (e.g. small
islands):
EBBT pred = EBBT pred + TempAdjustLand
If the surface type of the pixel is water and different from the ones of the grid points (e.g. small
lakes/rivers):
EBBT pred = EBBT pred + TempAdjustWater
If the pixel is within DistCoast of a coastline then:
EBBT pred = EBBT pred coldest
The final thresholds shall be derived as follows (with coefficient test_index = 3a to 3d):
For sea:
THR_TEST(test_index)_MAX = MIN(T_cloud_max,(EBBTpred – temp(test_index)_sea_max )
THR_TEST(test_index)_MIN = MIN(T_cloud_max, MAX(T_clear_min, (EBBTpred –
temp(test_index)_sea_min – test3_corr_min) ) )
For land:
THR_TEST(test_index)_MAX = MIN(T_cloud_max,(EBBTpred – temp(test_index)_land_max)
)
THR_TEST(test_index)_MIN = MIN(T_cloud_max, MAX(T_clear_min, (EBBTpred –
temp(test_index)_land_min – test3_corr_min) ) )
with test3_corr_min = Elev_corr + Undef_corr + DTC_corr + Cold_surf_corr
and where: T_cloud_max is the maximum cloud temperature
T_clear_min is the minimum surface temperature
Elev_corr takes into account the decrease of temperature with altitude and is defined as:
Elev_corr = pixel_elevation * temp_elev_corr / 1000
where:
pixel_elevation is the elevation (in metres) taken from the pixel-based map of surface elevation
temp_elev_corr is the altitude temperature gradient in kelvin/km.
Undef_corr is given a value of 6 when the RTM forecast grid point surface type does not match with
pixel surface, and is null otherwise.
DTC_corr is a term to prevent false cloud detection near sunrise. It shall be calculated as follows:
If (tsunrise - 3 < timage < tsunrise + 3) then

   )1(35.0)(___ sunriseimageimageinterp ttABStTTfaccorrDTCcorrDTC 
else 0_ corrDTC
with:  2/12/)(cos1_)(  sunriseimageimage ttcorrDTCtT ,

<!-- source_page: 74 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document







)(2
)(12/)(cos1
)(12/)(cos1
12
12
21
int
forecastforecast
forecastimagesunriseforecast
imageforecastsunriseforecast
erp
tt
tttt
tttt
T 


 


where: timage is the image timestamp in hours
tforecast1 and tforecast2 are the RTM forecast times used to interpolate the pixel EBBT
tsunrise is apparent sunrise UTC time
For more details about how this correction is derived, see Appendix A in Cloud Detection for MSG -
Algorithm Theoretical Basis Document.
Cold_surf_corr is a term to prevent false cloud detection for cold desert surfaces at night, when the
forecast surface temperature is overestimated:






)*))8.10((,(
else
)8.10( if 0
__
0
0
rrTslopeColdSurfCoTTrrMaxColdSurfCoMin
TT
corrsurfCold
forecast
forecast

correlevTempelevationPixelrrTstartColdSurfCoT __*_with 0 
THRESHOLD DETERMINATION FOR TEST4A TO TEST 4J
For Test4a to Test 4j (temperature difference tests) the following static thresholds shall be derived:
THR_TEST4A_MAX = a0,4a+ EBBTpred,10.8* a1,4a+ EBBTpred,3.9* a2,4a – test4a_corr_max
THR_TEST4A_MIN = b0,4a+ EBBTpred,10.8* b2,4a+ EBBTpred,3.9* b2,4a – test4a_corr_min
THR_TEST4B = a0,4b + EBBTpred,10.8 * a1,4b + EBBTpred,6.2* a2,4b – DTC_corr
THR_TEST4C = a0,4c + EBBTpred,10.8 * a1,4c + EBBTpred,7.3* a2,4c – DTC_corr
THR_TEST4D_MIN = a0,4d + EBBTpred,10.8 * a1,4d + EBBTpred,8.7* a2,4d – DTC_corr
THR_TEST4D_MAX1 = b0,4d + EBBTpred,10.8 * b1,4d + EBBTpred,8.7* b2,4d
THR_TEST4D_MAX2 = c0,4d + EBBTpred,10.8 * c1,4d + EBBTpred,8.7* c2,4d
THR_TEST4E = a0,4e + EBBTpred,10.8 * a1,4e + EBBTpred,12.0* a2,4e
THR_TEST4F = a0,4f + EBBTpred,10.8 * a1,4f + EBBTpred,13.4* a2,4f + test4f_corr – DTC_corr
THR_TEST4G_MAX = a0,4g + EBBTpred,12.0* a1,4g + EBBTpred,3.9* a2,4g
THR_TEST4G_MIN = b0,4g + EBBTpred,12.0 * a1,4g + EBBTpred,3.9* b2,4g
THR_TEST4H = a0,4h + EBBTpred,12.0 * a1,4h + EBBTpred,6.2* a2,4h
THR_TEST4I = a0,4i + EBBTpred,12.0 * a1,4I + EBBTpred,7.3* a2,4I
THR_TEST4J = a0,4j + EBBTpred,12.0 * a1,4j + EBBTpred,8.7* a2,4j
THR_TEST4K = a0,4k + EBBTpred,12.0 * a1,4k + EBBTpred,13.4* a2,4k
where EBBTpred, nnn is the predicted clear sky EBBT of channel nnn as derived in step1 and DTC_corr
is a correction to prevent false cloud detection at sunrise (see previous section).
test4a_corr_min is used to correct the thresholds at day time for the solar reflec tion in channel IR3.9.
This term shall be calculated as follows:
For water bodies: test4a_corr_min = MIN(0, sunglint_angle * 0.3 - 15)

<!-- source_page: 75 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




test4a_corr_max = 0
For other surface types: test4a_corr_min = – Climate_albedo(surface_type)*0.3
test4a_corr_max = – Climate_albedo(surface_type)*0.3
test4f_corr is a correction term for the emissivity effects over bare and low vegetated soils. It shall be
set to -2 for barren/desert, grasslands and open shrublands and to 0 for other surface types.
The coefficients a0, a1, a2, b0, b1, b2 shall be different for day/night and land/sea (i.e. day/sea,
day/land, night/sea, night/land).

THRESHOLD DETERMINATION FOR TEST5A TO TEST5H
For Test5a to Test5h (standard deviation) the thresholds shall
be set as follows:
For sea: THR_TEST5A = test5a_sea
THR_TEST5B = test5b_sea
THR_TEST5C = test5c_sea
THR_TEST5D = test5d_sea
THR_TEST5E = test5e_sea
THR_TEST5F = test5f_sea
THR_TEST5G = test5g_sea
THR_TEST5H = test5h_sea
For land: THR_TEST5A = test5a_land
THR_TEST5B = test5b_land
THR_TEST5C = test5c_land
THR_TEST5D = test5d_land
THR_TEST5E = test5e_land
THR_TEST5F = test5f_land
THR_TEST5G = test5g_land
THR_TEST5H = test5h_land

THRESHOLD DETERMINATION FOR TEST6
The threshold shall
be determined by using the following relationship:
THR_TEST6 = maximum of c1 and c1 * REFLVIS0.8 / c2
where REFLVIS0.8 is the measured reflectance in channel VIS0.8 in units of %. If channel VIS0.8 is
not available channel VIS0.6 shall be used instead with different coefficients c1, c2.

THRESHOLD DETERMINATION FOR TEST7
The thresholds shall be determined only for day and dawn/dusk.
For night no thresholds are derived, since the test is not applied during night.
The thresholds are directly taken from the set-up parameters list.

<!-- source_page: 76 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




5.3.2.6 Step 6: Scenes Type Identification
All tests for each local time type, i.e day, dawn/dusk or night, shall be performed independently of
each other. Each test shall be enabled/disabled by a set-up parameter. Several test counters shall be
used on each pixel to calculate the following numbers:

Test_count for the total number of tests actually used on that pixel
Max_clear_count for the total number of tests that may actually report ‘clear’
Cloud_count for the total number of tests reporting ‘cloudy’
Clear_count for the total number of tests reporting ‘clear’
Unknown_count for the total number of tests reporting ‘unknown’

The threshold tests shall be performed as specified below.
DESCRIPTION OF THE THRESHOLD TESTS
For each test used, Test_count shall be incremented by one.
TEST1A to TEST1D
If it is day (not dawn/dusk), Max_clear_count shall be incremented by one for each of the tests used
in this group.
If the reflectance in channel VIS0.6 is larger than THR_TEST1A_MAX, then the test flag for this test
shall be set indicating ‘cloud detected’ and the number of tests reporting ‘cloudy’ shall be
incremented by one.
Else, if it is not dawn or dusk and if the reflectance in channel VIS0.6 is less than
THR_TEST1A_MIN, then the test flag for this test shall be set indicating ‘clear detected’ and the
number of tests reporting ‘clear’ shall be incremented by one.
If none of these conditions are fulfilled, then the test flag for that test shall be set indicating
‘unknown’ and the number of tests reporting ‘unknown’ shall be incremented by one.
TEST1B to TEST1D shall be applied similarly.
TEST2A to TEST2F
Max_clear_count shall be incremented by one for each of the tests used in this group.
If the difference VIS0.6-VIS0.8 is larger than THR_TEST2A_MAX1 OR lower than
THR_TEST2A_MIN1, then the test flag for that test shall be set indicating ‘cloud detected’, and the
number of tests reporting ‘cloudy’ shall be incremented by one.
Else, if the difference VIS0.6-VIS0.8 is lower than THR_TEST2A_MAX2 AND larger than
THR_TEST2A_MIN2, then the test flag for this test shall be set indicating ‘clear detected’ and the
number of tests reporting ‘clear’ shall be incremented by one.
If none of these conditions are fulfilled, then the test flag for that test shall be set indicating
‘unknown’ and the number of tests reporting ‘unknown’ shall be incremented by one.
TEST2B to TEST2F shall be applied similarly.
TEST3A to TEST3D
Max_clear_count shall be incremented by one for each of the tests used in this group.
If the brightness temperature in channel IR3.9 is smaller than THR_TEST3A_MIN, then the test flag
for that test shall be set to ‘cloud detected’ and the number of tests reporting ‘cloudy’ shall be
incremented by one.

<!-- source_page: 77 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Else, if the brightness temperature in channel IR3.9 is larger than THR_TEST3A_MAX, then the test
flag for that test shall be set to ‘clear detected’ and the number of tests reporting ‘clear’ shall be
incremented by one.
If none of these conditions are fulfilled, then the test flag for that test shall be set indicating
‘unknown’ and the number of tests reporting ‘unknown’ shall be incremented by one.
TEST3B to TEST3D shall be applied similarly.
TEST4A
If it is daytime, Max_clear_count shall be incremented by one when this test is used.
If the difference IR10.8-IR3.9 is larger than THR_TEST4A_MAX during night OR smaller than
THR_TEST4A_MIN, then the test flag for that test shall be set indicating ‘cloud detected’ and the
number of tests reporting ‘cloudy’ shall be incremented by one.
Else, if it is daytime and IR10.8-IR3.9 is larger than THR_TEST4A_MAX, then the test flag for that
test shall be set to ‘clear detected’ and the number of tests reporting ‘clear’ shall be incremented by
one.
If none of these conditions are fulfilled, then the test flag for that test shall be set indicating
‘unknown’ and the number of tests reporting ‘unknown’ shall be incremented by one.
TEST4B, TEST4C, TEST4F and TEST4H to TEST4K
If the difference IR10.8-IR6.2 is lower than THR_TEST4B_MIN, then the test flag for that test shall
be set indicating ‘cloud detected’ and the number of tests reporting ‘cloudy’ shall be incremented by
one.
Else, the test flag for that test shall be set indicating ‘unknown’ and the number of tests reporting
‘unknown’ shall be incremented by one.
TEST4C, TEST4F and TEST 4H to TEST4K shall be applied similarly.
TEST4D
If the difference IR10.8-IR8.7 is lower than THR_TEST4D_MIN, then the test flag for that test shall
be set indicating ‘cloud detected’ and the number of tests reporting ‘cloudy’ shall be incremented by
one.
If the pixel latitude is larger than threshold_4D_lat_limit AND the difference IR10.8-IR8.7 is larger
than THR_TEST4D_MAX1, then the test flag for that test shall be set indicating ‘cloudy’ and the
number of tests reporting ‘cloudy’ shall be incremented by one (case of fog or low stratus).
If the pixel latitude is lower than threshold_4D_lat_limit AND the pixel surface type is barren/desert,
then Max_clear_count shall be incremented by one and the following test issued: If the difference
IR10.8-IR8.7 is larger than THR_TEST4D_MAX2, then the test flag for that test shall be set to ‘clear
detected’ and the number of tests reporting ‘clear’ shall be incremented by one.
If none of these conditions are fulfilled, then the test flag for that test shall be set indicating
‘unknown’ and the number of tests reporting ‘unknown’ shall be incremented by one.
TEST4G
If the difference IR12.0-IR3.9 is larger than THR_TEST4G_MAX OR smaller than
THR_TEST4G_MIN, then the test flag for that test shall be set indicating ‘cloud detected’ and the
number of tests reporting ‘cloudy’ shall be incremented by one.
Else, the test flag for that test shall be set indicating ‘unknown’ and the number of tests reporting
‘unknown’ shall be incremented by one.
TEST5A to TEST5H

<!-- source_page: 78 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




These tests shall not be applied to n x n pixel areas which contain a mixture of land and sea pixels.
If the standard deviation in channel HRVIS is larger than THR_TEST5A and the measured
reflectance in channel HRVIS is higher than the mean value of the n x n pixel array, then the test flag
for that test shall be set indicating ‘cloud detected’ and the number of tests reporting ‘cloudy’ shall be
incremented by one.
Else, the test flag for that test shall be set indicating ‘unknown’ and the number of tests reporting
‘unknown’ shall be incremented by one.
TEST5B to TEST5D shall be applied similarly.
If the standard deviation in channel IR3.9 is larger than THR_TEST5E and the measured brightness
temperature in channel IR3.9 is smaller than the mean value of the n x n pixel array, then the test flag
for that test shall
be set indicating ‘cloud detected’, and the number of tests reporting ‘cloudy’ shall
be incremented by one.
Else, the test flag for that test shall be set indicating ‘unknown’ and the number of tests reporting
‘unknown’ shall be incremented by one.
TEST5F to TEST5H shall be applied similarly.
TEST6
If the difference IR3.9-IR10.8 is larger than THR_TEST6, then the test flag for that test shall be set
indicating ‘cloud detected’, and the number of tests reporting ‘cloudy’ shall be incremented by one.
Else, the test flag for that test shall be set indicating ‘unknown’ and the number of tests reporting
‘unknown’ shall be incremented by one.
SCENE DETERMINATION
The final scene type is obtained by using the counters defined at the beginning of the section. In
addition, the two following numbers shall be used:
- Clear% = (Clear_count / Max_clear_count) * 100
- Cloud% = (Cloud_count / Test_count) * 100
If Clear_count is larger than 0 AND Cloud_count is null, then the scenes type shall be set to the
surface type and the quality index set to 10.
If Clear_count is null AND Cloud_count is null, then the scenes type shall be set to the surface type
and the quality index set to 30.
If Clear_count is larger than 0 AND Cloud_count larger than 0, then the following checks shall be
done:
If Clear% is larger than Cloud% is AND Clear_count is larger than or equal to Cloud_count,
then scenes type shall be set to the surface type and the quality index set to 40.
Else, if Cloud% is larger than Clear%, then the scenes type shall be set to ’cloudy’ and the
quality index set to 60.
If none of these two conditions are fulfilled, then the scenes type shall be set to ’unknown’ and
the quality index set to 50.
If Clear_count is null AND Cloud_count is larger than 0 AND Unknown_count is larger than 0, then
the scenes type shall be set to ’cloudy’ and the quality index set to 90.
If Clear_count is null AND Cloud_count is larger than 0 AND Unknown_count is null, then the
scenes type shall be set to ’cloudy’ and the quality index set to 100.
TEST7

<!-- source_page: 79 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Test7 shall be applied after the Scene determination, since this test will change the overall quality
index. This test will reset cloudy pixels to the value clear (ice and snow cover) if a clear snow- or icecovered surface has been falsely classified as cloud.
The test shall be applied only at day or dawn/dusk conditions as follows:
Calculate the normalised snow index (NSI) as follows:
NSI = (REFL0.6 – REFL1.6) / (REFL0.6 + REFL1.6)
At daytime, if the pixel is cloud covered according to one of the tests above,
and if the reflectance in channel VIS06 is smaller than a threshold ReflSnow1,
and if the normalised snow index is larger than a threshold ReflSnow2,
and if the predicted EBBT of channel IR10.8 is lower than a threshold TempSnow0,
and if the measured EBBT of channel IR10.8 is greater than the predicted EBBT for that channel plus
a threshold TempSnow1,
and if the difference EBBT10.8-EBBT12.0 is greater than a threshold TempSnow2, then:
Reset the Scene Type to ‘clear snow land’ if pixel is on land or to ‘clear ice water’ if the pixel is on
water. Set the test flag of this test to ‘snow detected’ and set the overall quality flag to 25%.
At dawn/dusk, if the pixel is cloud covered according to one of the tests above,
and if the normalised snow index is larger than a threshold ReflSnow3,
and if the predicted EBBT of channel IR10.8 is lower than a threshold TempSnow0,
and if the measured EBBT of channel IR10.8 is greater than the predicted EBBT for that channel plus
a threshold TempSnow3,
and if the difference EBBT10.8-EBBT12.0 is greater than a threshold TempSnow4, then:
Reset the Scene Type to ‘clear snow land’ if pixel is on land, or to ‘clear ice water’ if the pixel is on
water. Set the test flag of this test to ‘snow detected’ and set the overall quality flag to 25%.
APPLICATION OF THE THRESHOLD TESTS
The threshold tests described above shall
be performed independently. They shall be used in the
following context:
 First, the scenes type shall be set to ‘unknown’.
 For day pixels the following tests shall be applied (see exceptions below):
TEST1A to TEST1D, TEST2A to TEST2F, TEST3A to TEST3D, TEST4A to TEST4K, TEST5A
to TEST5H, TEST7.
 For dawn and dusk pixels the following tests shall be applied (see exceptions below):
TEST1A to TEST1D, TEST2A to TEST2F, TEST3A to TEST3D, TEST4A to TEST4K, TEST5A
to TEST5H, TEST7.
TEST1A to TEST1D shall be disabled if a Clear Sky Reflectance Map with a valid value is not
available (climatological albedo is not accurate enough).
TEST4A shall not be applied over sea.
TEST1A to TEST1D shall not be applied if the viewing angle from the satellite is higher than 55º
(to avoid strong backscattering / “hot spot” situations).
 For day, dawn and dusk pixels the following exceptions shall be applied:
Sunglint
If the following sunglint criteria are fulfilled:

<!-- source_page: 80 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




- the pixel is located over water surfaces (i.e. lake or ocean)
- ABS(COS-1(COS(sol_zenith)*COS(sat_zenith) – SIN(sol_zenith)*SIN(sat_zenith)
*COS(relative azimuth)) is smaller than a threshold sgl_criteria
then TEST1A to TEST1D, TEST2A to TEST2F, TEST3A, TEST4G, and TEST5A to TEST
5G shall be disabled and TEST6 shall be enabled.
Scattering angle
If the angle between the sun and the satellite directions is higher than max_scat_angle over
land and max_scat_angle – 10º over sea, then the following tests shall be disabled:
TEST1A to TEST1D, TEST3A, TEST4A, and TEST5A to TEST5H.
High viewing angles
If the satellite viewing angle is higher than 55º, then the following tests shall be disabled:
TEST1A to TEST1D.
 For night pixels the following tests shall be applied:
TEST3A to TEST3D, TEST4A to TEST4K, TEST5E to TEST5H. However, Test4A shall be
disabled at night if the surface type is barren/desert, grassland or open shrubland.
 For all time conditions the following tests shall be excluded if the pixel is closer than DistCoast
to the nearest coastline:
TEST1A to TEST1D, TEST2A to TEST2F, TEST4A, TEST4G, TEST5A to TEST5H.
5.3.2.7 Update of the Clear Sky Reflectance Map
This post-processing function shall update existing CRM files and create new CRM files. New CRM
files for each CRM derivation time (every two hours between 06:00 and 20:00 UTC) shall be created
daily. For the other CRM time stamps new CRM files shall be created twice a week, on Sundays and
Wednesdays. The time stamps for which CRM files are created and updated are the full hours, starting
from CrmHourLow to CrmHourHigh every CrmUpdateSteps hours.
For the two closest repeat cycles (these shall be within map_max_time hours) of each CRM time
stamp the files are updated.
For each pixel the reflectance value for each of channels VIS0.6, VIS0.8, NIR1.6 and IR3.9_sol for
clear scenes shall be collected for a period of seven days and averaged, i.e. clear sky reflectance of
channel VIS0.6, VIS0.8, NIR1.6 and IR3.9_sol for that pixel.
For each pixel the mean solar zenith angle and the mean relative azimuth angle (sun/satellite) at the
CRM time stamp at the SSP for that seven-day period shall be determined.
If a pixel has no clear scene in that seven-day period the value of the previous seven-day period shall
be used. If that value is not available, the value shall be set to a default invalid value.
5.3.3 Automatic Quality Control (AQC)
The Scenes Analysis algorithm is designed in a way that there is a high confidence in the
determination of a pixel to be clear or cloud contaminated. Therefore the automatic quality control
(AQC) shall be applied to all pixels. The AQC shall provide a quality index (QI) for each pixel,
which is a number ranging between 0% and 100%. The number 0% has the meaning of 0%
confidence for cloud contamination (i.e. 100% confidence clear) and the number 100% has the
meaning of 100% confidence for cloud contamination. The QI shall be derived as detailed in the
Scene determination section in §5.3.2.6. The following table summarises the possible values for the
scene type and QI:

<!-- source_page: 81 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





Case Scene Type Quality Index
Scenes analysis not performed 0 0
Clear, high confidence Surface type map 10
Clear, confidence Surface type map 30
Clear, low confidence Surface type map 40
Unknown Unknown scene 50
Cloud, low confidence Cloud 60
Cloud, confidence Cloud 90
Cloud, high confidence Cloud 100

5.4 Outputs
The results of the Scenes Analysis algorithm (i.e. scenes type) shall be provided per pixel as follows:
 for pixel with no image data available, the scenes type shall be set to a default value stating ‘no
scenes identified, missing image data’.
 for pixel identified as clear, the scenes type shall be set either to the value of the surface type
(including the surface type ‘snow/ice’), or to a value stating ‘sunglint’.
 for pixels identified as cloudy, the scenes type shall be set to a value stating ‘cloudy’.

Parameter Mnemonic Units Min Max Prec Acc To
Scenes type scenes_type - 0 255 1 1 CLA, CAL,
SST, SCE, GII
Predicted EBBTs for all IR
channels
pred_EBBT_c
han
K 170 350 0.1 0.1 CLA, AMV
SCE test flag test_flag - - - - - CLA, SCE next
SCE quality index QI % 0 100 1 1 All products
Clear Sky Reflectance
Map
csr_map % × 10 0 1500 1 1 SCE next
Table 15: Scenes Analysis algorithm Pixels identified as cloudy
Parameter Value Meaning
Scenes type 0 No scenes identified, missing input data
1 Evergreen needleleaf forest
2 Evergreen broadleaf forest
3 Deciduous needleleaf forest
4 Deciduous broadleaf forest
5 Mixed forest
6 Closed shrublands
7 Open shrublands
8 Woody savannahs
9 Savannahs

<!-- source_page: 82 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Parameter Value Meaning
10 Grasslands
11 Permanent wetlands
12 Croplands
13 Urban and built-up
14 Cropland mosaics
15 Permanent snow/ice
16 Bare soil and rocks
17 Water bodies
18 Tundra
19 Mixed land/water
20 to 49 (Spare)
50 Unknown scene
51 to 96 (Spare)
97 Snow/ice over land
98 Snow/ice over water (ocean)
99 Clear sunglint
100 Cloudy
Table 16: Scenes Analysis algorithm: Scenes type values

SCENE TEST FLAG
Each test result shall be stored using 2 bits and coded as following:
Value (binary) Test result
0 (00) Clear
1 (01) Unknown
2 (10) Cloud
3 (11) Test failed
The test flags shall be written into a 2-bytes integer from right to left according to the position given
in the table here below (i.e., Test 1A is at the right end, or lowest binary exposure). To limit the size
of the test flag file, only the results of the tests currently used are stored.
Nb Position Test Nb Position Test
1 0 1A 9 16 4D
2 2 1B 10 18 4F
3 4 1C 11 20 5C
4 6 2A 12 22 5G
5 8 3C 13 24 7
6 10 4A 14 26 Unused
7 12 4B 15 28 Unused
8 14 4C 16 30 Unused

<!-- source_page: 83 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




5.5 Prototyping and Testing
This section describes the prototyping activities, highlighting the major problems which were
encountered with this development.
5.5.1 Prototyping
The prototyping activities provide information about the scientific background for the Scenes Analysis
algorithm and verify that the algorithm is scientifically correct. The scientific background of the prototype is
mainly based on existing algorithms, i.e. APOLLO, SCANDIA and the model used at CMS in France.
References are listed in Section 5.7. Additionally new ideas have been included, e.g. using the data from the
previous repeat cycle as a first guess for the current image.
5.5.2 Test Data
The major problem is to simulate the MSG channels. The prototype uses existing data from:
 GOES-8/Imager, which helps to simulate channels VIS0.6, IR3.9, WV6.2, IR10.8 and IR12.0 on a similar
horizontal resolution as MSG.
 GOES-8/Sounder, which helps to simulate channels VIS0.8, IR3.9, WV6.2, WV7.3, IR9.7, IR10.8, IR12.0
and IR13.4 on a lower horizontal resolution. During prototyping and testing only these channels have been
used and the other ‘MSG’ channels have been regarded as missing.
 AVHRR, which helps to simulate channels VIS0.6, VIS0.8, IR3.9, IR10.8 and IR12.0 on a higher
horizontal resolution than MSG. The new generation of AVHRR will also provide an NIR1.6 channel in
the near future.
The surface type map was only available in the form of a land-sea mask. Also the surface albedo was only
specified for land (16% albedo) and ocean (8%). A more detailed global surface type map, with 18 different
surface types on a 0.167° grid resolution, is provided with the test data together with the spectral albedo for the
different surface types. The surface temperature analysis is made available as part of the External
Meteorological Data.
5.5.3 Test Results
Tests have been performed for several slots of the GOES-8 images. For one slot the results from each single
threshold test and the final cloud mask are available. For the other slots the results are only available in the form
of the final cloud mask.
5.6 Future Enhancements
The following Future Enhancements shall be foreseen in the algorithm design as indicated above:
 Inclusion of additional tests, adding new AQC checks or disabling existing tests or AQC checks.
 Use of a pixel-based surface emissivity map.
 Use of level 1.5 image data from additional spectral channels.
5.7 References
Reference Title Date Author(s)
Int. J. of Remote Sensing,
Vol. 9, pp. 123-150
An improved method for detecting
clear sky and cloudy radiances from
AVHRR data
1988 Saunders, R.W. and Kriebel,
K.T.
Remote Sensing of Environ.,
Vol. 46, pp. 246-267
Automatic cloud detection applied to
NOAA-11/AVHRR imagery
1993 Derrien, M. et al.
SMHI Reports Meteorology and
Climatology, No. 67, Jan 1996
Cloud classifications with the
SCANDIA model
1996 Karlson, K.-G.

<!-- source_page: 84 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




6 BDRF TABLE GENERATION
6.1 Introduction
The Bi-Directional Reflectance Function (BDRF) describes for a surface the ratio of the reflected
radiance L to the incident irradiance I, for a given wavelength  and geometry.

)cos().,(
),,(.),,,( sI
L
s
v
vs

 

Equation 3


where s, v and  are respectively the source zenith angle, the view zenith angle and the relative
azimuth angle. Provided as a static data table, the BDRF is used in MPEF by the SCE algorithm (see
under Sections 5.3.2.4 and 5.3.2.5) for calculating the expected top-of-atmosphere reflectance, and by
the NDVI algorithm (described in Chapter 7) to attenuate the effect of the solar zenith angle
variability.
This chapter explains how this BDRF table is generated.
6.2 Semi-empirical BDRF Model
An analytic reflectance model is used to represent the BDRF, whose values are finally extracted to
write the static tables for a sampling of geometries. Many different models are available (Maignan et
al., 2004). The Ross/Roujean semi-empirical kernel model (Roujean et al.,1992, also used by the
LAND-SAF for BDRF and albedo determination) has been selected, with the advantage of being
linear, and so easy to invert against observations.
The model has three terms representing respectively the isotropic, geometric (shading effects) and
volumic (multiple reflections) contributions. A fourth specular reflection term has been added for the
reflectance over water and deserts.
),,(),,(),,(. 3322110  vs
spec
vs
vol
vs
geo fkfkfkk 
Equation 4


where:

<!-- source_page: 85 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




 
radians) in be willS degrees; in (with 002.01.0S
cossinsincoscos)cos(
S1
)2cos(25.025.1
cossinsincoscoscos
3
1sincos2coscos
1
3
4
costantan2tantan
,,(tantan1tantansincos2
1
00
0
3
2
22
1
ss
vsvs
sspec
vsvs
vs
vol
vsvs
vsvsvs
geo
sgl
sglf
f
f
















 

 



k0, k1, k2, k3 are the model variables, for a given wavelength and surface type.
In the expressions for    , 

  
2
and
0S
sgl note that the angles  ,  , sgl and 0S
are expressed in radians.
6.3 Model inversion
Clear-sky observations for each surface type are accumulated by collecting several archived clear-sky
reflectance maps (see Chapter 23), at different times of the year, in order to get a sufficient angular
sampling.
These observations are used to invert the BDRF model using a standard least squares regression
technique. This method, however, does not work properly for deserts, because this surface type covers
in fact many different soil types, with different reflectance levels. So for deserts, the model variables
have been defined empirically. A similar manual fitting was performed for water bodies, the goal
being here to mimic the modelled sea reflectance from P.D. Watts’ study on aerosols for an optical
thickness of 0.2 (see references in Section 6.5).
The following tables show the retrieved model variables for each channel surface type:

Channel 1
Surface type K0 K1 K2 K3
Evergreen needleleaf forest 0.133 0.004 0.119 0
Evergreen broadleaf forest 0.112 0.001 0.115 0
Deciduous needleleaf forest 0.139 0.004 0.131 0
Deciduous broadleaf forest 0.117 0.003 0.117 0
Deciduous mixed forest 0.095 0.001 0.152 0
Closed shrubland 0.143 0.008 0.140 0
Open shrubland 0.224 0.007 0.098 0
Woody savannah 0.114 0.001 0.133 0
Savannah 0.139 0.004 0.102 0
Grassland 0.189 0.007 0.068 0
Permanent wetland 0.143 0.008 0.134 0

<!-- source_page: 86 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Channel 1
Cropland 0.151 0.005 0.092 0
Urban 0.150 0.006 0.107 0
Crop vegetation 0.139 0.005 0.096 0
Permanent snow 0.407 0.022 –0.066 0
Barren deserts 0.200 0 0.050 0.10
Water bodies 0.080 0.027 0.005 0.65
Tundra 0.100 0 0.050 0
Table 17: BDRF Table Generation: the retrieved model variables for Channel 1
Channel 2
Surface type K0 K1 K2 K3
Evergreen needleleaf forest 0.240 0.016 0.050 0
Evergreen broadleaf forest 0.224 0.016 0.044 0
Deciduous needleleaf forest 0.250 0.014 0.049 0
Deciduous broadleaf forest 0.223 0.015 0.049 0
Deciduous mixed forest 0.212 0.013 0.080 0
Closed shrubland 0.210 0.018 0.081 0
Open shrubland 0.261 0.017 0.049 0
Woody savannah 0.216 0.015 0.061 0
Savannah 0.216 0.014 0.064 0
Grassland 0.242 0.016 0.038 0
Permanent wetland 0.214 0.017 0.087 0
Cropland 0.222 0.012 0.063 0
Urban 0.214 0.015 0.069 0
Crop vegetation 0.227 0.015 0.052 0
Permanent snow 0.386 0.036 –0.073 0
Barren deserts 0.250 0 0.050 0.10
Water bodies 0.060 0.027 0.005 0.70
Tundra 0.100 0 0.050 0
Table 18: BDRF Table Generation: the retrieved model variables for Channel 2
Channel 3
Surface type K0 K1 K2 K3
Evergreen needleleaf forest 0.243 0.026 –0.017 0
Evergreen broadleaf forest 0.202 0.018 0.008 0
Deciduous needleleaf forest 0.237 0.023 –0.015 0
Deciduous broadleaf forest 0.237 0.021 -0.010 0
Deciduous mixed forest 0.204 0.023 0.029 0
Closed shrubland 0.247 0.027 0.000 0
Open shrubland 0.366 0.027 –0.021 0
Woody savannah 0.216 0.019 0.015 0
Savannah 0.262 0.023 –0.015 0
Grassland 0.322 0.025 –0.054 0
Permanent wetland 0.216 0.022 0.047 0
Cropland 0.273 0.024 –0.022 0

<!-- source_page: 87 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Channel 3
Surface type K0 K1 K2 K3
Urban 0.253 0.026 0.002 0
Crop vegetation 0.255 0.023 –0.018 0
Permanent snow 0.225 0.031 –0.071 0
Barren deserts 0.250 0 0.050 0.10
Water bodies 0.040 0.027 0.005 0.73
Tundra 0.100 0 0.050 0
Table 19: BDRF Table Generation: the retrieved model variables for Channel 3
6.4 Table generation
As the fi functions require intensive calculations, for every pixel, the reflectance values are stored in a
static table, in which the entries are the surface type, the sun zenith angle, the view zenith angle and
the relative azimuth angle. The sampling resolutions for the latter are respectively 10°, 10° and 30°.
6.5 References
Reference Title Date Author(s)
Remote Sensing of
Environment , 90 (2004)
210–220
Bidirectional reflectance of Earth
targets: Evaluation of analytical
models using a large set of
spaceborne measurements with
emphasis on the Hot Spot
2004 F. Maignan, F.-M. Bréon,
R. Lacaze
Journal of Geophysical
Research, vol. 97, pp.
20,455 – 20,468
A bi-directional reflectance model
of the earth’s surface for the
correction of remote sensing data
1992 J.L. Roujean, M. Leroy,
P.Y. Deschamps
RAL/TN/EUM/004 Aerosol Properties derived from
Meteosat Second Generation
Observations
2000

P.D. Watts, M.R. Allen,
C.T. Mutlow
EUM/OPS/TEN/10/1901 BDRF function for MSG MPEF 2010 O. Samain

<!-- source_page: 88 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




7 NORMALISED DIFFERENCE VEGETATION INDEX (NDVI)
PRODUCT GENERATION
7.1 Algorithm Configuration Information
7.1.1 Algorithm Name
Normalised Difference Vegetation Index (NDV)
7.1.2 Algorithm Identifier
EUM_MSG_NDV_A001
7.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 01/01/11 O. Samain NDVI Baseline
7.2 Inputs
The Normalised Difference Vegetation Index (NDVI) generation is technically part of the Scenes
Analysis processing. For more technical information on the processing of input data, see Chapter 5 .
7.3 Algorithm Functional Specification
7.3.1 Overview
The NDVI is an indicator of the photosynthetic activity of the vegetation. It varies between zero
(deserts) and 1 (dense vegetation).
7.3.2 Algorithm Description
The NDVI is defined as the following ratio:
)()(
)()(
VISRNIRR
VISRNIRRNDVI 


Equation 5

where R(VIS) is the reflectance in the 0.6 µm channel and R(NIR) the reflectance in the 0.8 µm
channel.
Usually, this formula applies to top-of-canopy reflectances, i.e. corrected for atmospheric
transmission effects for low orbit sensors. In the case of MSG, top-of-atmosphere reflectances are
used. The consequences are greater distortions due to high view zenith angles and changing sun zenith
angles during the year. To reduce these distortions, a corrected NDVI is calculated instead:
)_,,,(
)_,0,0,0( where
)()(
)()(
typesufaceBDRF
typesufaceBDRFRR
VISRNIRR
VISRNIRRNDVIcor
vs
mescor
corcor
corcor




Equation 6

Rmes is the actual top-of-atmosphere reflectance and s, v and  are respectively the sun zenith angle,
the view zenith angle and the relative azimuth a ngle. The BDRF function refers to the BDRF table
described in Chapter 6.

<!-- source_page: 89 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




7.3.3 Automatic Quality Control (AQC)
There is no automatic quality control mechanism in the algorithm. However, the number of
accumulations in the generated product can be used as a quality indicator. A higher number indicates
that the calculated NDVI is more accurate.
7.4 Outputs
7.4.1 Daily product
The NDVI daily product is generated by incremental update at each repeat cycle, every time a new
clear-sky observation is available for a given pixel.
The output file contains the following fields:
 Minimum NDVI for the day
 Maximum NDVI for the day
 Mean NDVI
 Number of accumulations
7.4.2 Encoded product
The daily NDVI product is encoded in HDF5 format.
In addition, a so-called 10-day NDVI product is generated, also in HDF5, by accumulating the data of
the daily product. This product is generated for every month according to the following scheme:
 Day 1–10
 Day 11–20
 Day 21 – end of month
7.5 Future Enhancements
No future enhancements are foreseen.
7.6 References
None

<!-- source_page: 90 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8 CLOUD ANALYSIS PRODUCT GENERATION
8.1 Algorithm Configuration Information
8.1.1 Algorithm Name
Cloud Analysis (CLA)
8.1.2 Algorithm Identifier
EUM_MSG_CLA_A001
8.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 H.-J. Lutz CLA Baseline
1.1 26/5/97 H.-J. Lutz TBDs resolved, bid clarification points added, errors
corrected.
1.2 1/7/97 H.-J. Lutz Clarifications added and updates as a result of the
improvements to the SCE algorithm.
1.3 8/12/97 H. K. Wilson Requirements Analysis clarification points added.
1.4 13/3/98 H. K. Wilson Peer Group Review changes added.
1.5 15/1/99 H.-J. Lutz Detailed Design Phase changes added.
1.6 31/1/02 H.-J. Lutz Updated according to ECP 295.
1.7 25/7/05 J. Gustafsson Added inversion height assignment.
8.2 Inputs
8.2.1 Image and Preprocessing Data (Dynamic Application Data)
The Cloud Analysis algorithm uses the level 1.5 data from all MSG channels. As defined below, the
image data shall be available in the form of equivalent black body brightness temperatures (EBBT)
(unit K) for all IR/WV channels and in the form of reflectances (unit %) for all VIS/NIR channels.

<!-- source_page: 91 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 92 of 298



LEVEL 1.5 IMAGE DATA AND DATA DERIVED FROM THE IMAGE DATA
Parameter Mnemonic Units Min Max Prec Acc Res Source
Reflectances for channels VIS0.6, VIS0.8,
NIR1.6, HRVIS, IR3.9_sol
REFLchannel % 0 150 0.1 0.1 pixel Derived from level 1.5 data
EBBTs for channels: IR3.9, WV6.2,
WV7.3, IR8.7, IR9.7, IR10.8, IR12.0,
IR13.4
EBBTIchannel K 170 350 0.1 0.1 pixel Derived from level 1.5 data
Radiances for channels: IR3.9, WV6.2,
WV7.3, IR8.7, IR9.7, IR10.8, IR12.0,
IR13.4
RadIchannel mWm-2sr-1(cm-1)-1 0 - - - pixel Derived from level 1.5 data
Local mean, minimum, maximum and
standard deviation on a 3 x 3 pixel segment
for channels VIS0.6, VIS0.8, NIR1.6,
IR3.9, WV6.2, WV7.3, IR8.7, IR9.7,
IR10.8, IR12.0, IR13.4
mn_REFL/EBBT
max_REFL/EBBT
min_REFL/EBBT
std_REFL/EBBT
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
pixel
pixel
pixel
pixel
Derived from level 1.5 data
Derived from level 1.5 data
Derived from level 1.5 data
Derived from level 1.5 data
Solar Zenith Angle sol_zenith degrees 0 90 10-6 10-6 pixel Derived from level 1.5 data
Satellite Zenith Angle sat_zenith degrees 0 90 10 -6 10 -6 pixel Derived from level 1.5 data
Relative azimuth angle sun/sat sol_sat_azimuth degrees 0 360 0.1 0.1 pixel Derived from level 1.5 data
Table 20: Cloud Analysis algorithm: Level 1.5 Image Data and Data Retrieved from the Image Data

<!-- source_page: 92 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 93 of 298

8.2.2 Data from other MPEF Algorithms (Dynamic Application Data)
The Cloud Analysis algorithm uses data from other MPEF algorithms, as defined in the following table:
DATA FROM OTHER MPEF ALGORITHMS
Parameter Mnemonic Units Min Max Prec Acc Res Source
Scenes Type scenes_type - - - - - pixel SCE
Predicted clear sky temperatures for all IR
channels
pred_EBBT_chan K 170 350 0.1 0.1 pixel SCE
SCE quality index QI - 0 100 10 10 pixel SCE
Scenes Type prev_scenes_type - 0 100 - - pixel CLA int previous
Cloud Phase prev_cld_phase - 0 3 - - pixel CLA int previous
Cloud Top Temperature prev_cld_ctt K 170 300 0.1 0.1 pixel CLA int previous
Cloud Top Height prev_cld_cth hPa 100 1050 50 1 pixel CLA int previous
Cloud Optical Thickness prev_cld_opt - 0 200 1 1 pixel CLA int previous
Effective Cloud amount prev_cld_neff % 0 100 1 1 pixel CLA int previous
Forecast EBBTs for all IR channels including
calculations for semi-transparency and
different cloud layers
for_EBBTch._clear
for_EBBTch._cloud
for_EBBTch._semi
K
K
K
230
200
200
350
300
320
0.1
0.1
0.1
0.1
0.1
0.1
pixel
pixel
pixel
Derived from RTM output
Derived from RTM output
Derived from RTM output
Forecast radiances for all IR channels
including calculations for semi-transparency
and different cloud layers
for_Radch._clear
for_Radch._cloud
for_Radch._semi
mWm-2sr-1(cm-1)-1
mWm-2sr-1(cm-1)-1
mWm-2sr-1(cm-1)-1
0
0
0
-
-
-
-
-
-
-
-
-
pixel
pixel
pixel
Derived from RTM output
Derived from RTM output
Derived from RTM output
Tropopause Height trop_ht hPa 0 1030 1 1 pixel Derived from Forecast
Forecast temperature profiles on the pressure
levels of the ECMWF model
for_prof K 170 350 0.1 0.1 pixel Derived from Forecast
Table 21: CLA Algorithm: Dynamic Application Data

<!-- source_page: 93 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 94 of 298

8.2.3 Static Application Data
The static application data used by the Cloud Analysis algorithm consists of the following:
 static thresholds
 static parameters for the different mathematical expressions used in the algorithm

STATIC DATA SETS - THRESHOLDS AND PARAMETERS
Parameter Mnemonic Units Min Max Pre. Acc. Res Source
Solar Zenith Thresholds SZ_thresh degrees 0 100 1 1 - Set-up
CLA processing segment size ps_size pixel 1 64 1 1 - Set-up
Min number of pixels to be included in final product min_cld_pixel - 1 1024 1 1 - Set-up
Sub-level for final CLA sub_levels hPa 25 200 25 25 - Set-up
Min pixels for image product min_ima_pixels - 1 25 1 1 - Set-up
Max time delay allowed max_hours hours 0 6 0.25 0.25 - Set-up
Max delay in repeat cycles max_cycles - 0 24 1 1 - Set-up
Temperature difference allowed in step 2 step2_temp K 0 5 0.1 0.1 - Set-up
Lower Pressure limit for band low_level_cloud_pressure hPa 600 900 25 25 - Set-up
Mid-level Pressure limit for band high_level_cloud_pressure hPa 300 600 25 25 - Set-up
VIS threshold for step 2 VIS_change % 0 10 0.1 0.1 - Set-up
Repeat cycle nominal duration rc_nom_dur mins 0 15 0.5 0.5 - Set-up
Max difference VIS0.6 -VIS0.8 Threshold THR_D1VIS_PCMAX % -50 50 0.1 0.1 - Set-up
Min difference VIS0.6 -VIS0.8 Threshold THR_D1VIS_PCMIN % -50 50 0.1 0.1 - Set-up
EBBT Difference Threshold IR3.9-IR10.8 Fog THR_D1IR_FOG_DAY K -20 20 0.1 0.1 - Set-up
EBBT SD IR10.8 Threshold Cumulus THR_STDIR108_CUM K 0 50 0.1 0.1 - Set-up
EBBT SD IR10.8 Threshold Altocumulus/Altostratus THR_STDIR108_AC K 0 50 0.1 0.1 - Set-up

<!-- source_page: 94 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 95 of 298

STATIC DATA SETS - THRESHOLDS AND PARAMETERS
Parameter Mnemonic Units Min Max Pre. Acc. Res Source
Reflectance Threshold VIS0.6 THR_VIS06_NS % 0 150 0.1 0.1 - Set-up
EBBT Difference Threshold IR10.8-IR12.0 Nimbostratus THR_D2IR_NS K -20 20 0.1 0.1 - Set-up
EBBT Difference Threshold IR3.9-IR10.8 Cumulonimbus THR_D1IR_CB1 K -20 20 0.1 0.1 - Set-up
EBBT SD IR10.8 Threshold Cumulonimbus THR_IR108_CB K 0 50 0.1 0.1 - Set-up
EBBT Difference Threshold IR3.9-IR10.8 Partly Cloudy THR_D1IR_PC K -50 50 0.1 0.1 - Set-up
EBBT Difference Threshold IR3.9-IR10.8 Fog Night THR_D1IR_FOG_NIGHT K -50 50 0.1 0.1 - Set-up
Intermediate QA check EBBT threshold Int_QA_thresh_1 K -50 50 0.1 0.1 - Set-up
Intermediate QA check height threshold Int_QA_thresh_2 hPa -50 50 0.1 0.1 - Set-up
Minimum number. of values from LUT to be used for
interpolation for cloud optical thickness
nmin - 0 10 1 1 - Set-up
Emissivity correction factor for cloud top height rat_cor_6.2/7.3/13.4 - 0 2 0.01 0.01 - Set-up
Maximum effective cloud amount neff_max % 100 150 1 1 - Set-up
Minimum effective cloud amount for opaque clouds neff_min % 0 100 1 1 - Set-up
Coefficients for derivation of cloud top height a 0, a1, a2, a3 - 0 1 0.01 0.01 - Set-up
Coefficients for derivation of cloud top temperature b0, b1, b2, b3 - 0 1 0.01 0.01 - Set-up
Coefficients for derivation of effective cloud amount c 0, c1, c2, c3 - 0 1 0.01 0.01 - Set-up
Vertical interpolation interval for forecast profiles vertical_int hPa 1 100 1 1 - Set-up
Optical Thickness Look up Table OT_lut - - - - - - Set-up
Threshold for Cloud Phase test temp_ice_max K 170 350 0.1 0.1 - Set-up
Threshold for Cloud Phase test temp_ice_min K 170 350 0.1 0.1 - Set-up
Minimun difference between predicted and measured
EBBT in ch. 10.8 (or 12.0), ch. 6.2, 7.3 and 13.4
DiffBase,
Diff62, Diff73, Diff134
K -100 100 0.1 0.1 - Set-up

<!-- source_page: 95 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 96 of 298

STATIC DATA SETS - THRESHOLDS AND PARAMETERS
Parameter Mnemonic Units Min Max Pre. Acc. Res Source
Standard deviation threshold EBBT ch. 6.2, 7.3, 13.4 Std62, Std73, Std134 K 0 100 0.1 0.1 - Set-up
Cloud phase ratio threshold CloudPhRat1, CloudPhRat2 - 0 100 0.1 0.1 - Set-up
Cloud phase difference for IR10.8-IR3.9, IR10.8-IR8.7,
IR10.8-IR12.0
CloudPhTdiff1, 2, 3, 4
CloudPhTdiff5, 6, 7, 8
K -100 100 0.1 0.1 - Set-up
Cloud phase maximum and minimum EBBT CloudPhT1, CloudPhT2,
CloudPhT3, CloudPhT4,
K 170 350 0.1 0.1 - Set-up
Semi-transparency ratio threshold SemiTrRat1, SemiTrRat2 - 0 100 0.1 0.1 - Set-up
Standard deviation threshold EBBT ch. 10.8 for
semi-transparency
SemiTrStdDev1,
SemiTrStdDev2
K 0 100 0.1 0.1 - Set-up
Semi-transparency EBBT difference for IR10.8-IR3.9,
IR10.8-IR8.7, IR10.8-IR12.0
SemiTrTdiff1, 2, 3, 4
SemiTrTdiff5, 6, 7, 8
K -100 100 0.1 0.1 - Set-up
Inversion height correction level set-up parameters inv_C1 - 0 1 1 1 - Set-up
inv_C2 - 0 1 1 1 - Set-up
inv_C3 - 0 1 1 1 - Set-up
Inversion height correction surface offset inv_surf_offset - 0 100 1 1 - Set-up
Inversion height correction inversion magnitude inv_magnitude - -10 10 0.1 0.1 - Set-up
Inversion height correction max inversion level inv_low_FC_pres_thres - 100 1100 1 1 - Set-up
Inversion height correction max AMV level inv_low_AMV_pres_thres - 100 1100 1 1 - Set-up
Table 22: CLA Product: Static Data Sets-Thresholds and Parameters
Note: All static data shall be configurable.

<!-- source_page: 96 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8.3 Algorithm Functional Specification
8.3.1 Overview
The Cloud Analysis (CLA) algorithm generates cloud information for every repeat cycle and for
every pixel determined as cloudy in the Scenes Analysis of the same repeat cycle. For the cloudy
pixels the scenes type provided by the SCE algorithm is updated in this algorithm to provide the
detailed cloud type. Additional cloud information such as cloud phase, cloud optical thickness, cloud
top temperature and cloud height estimations, including a semi-transparency correction, are produced.
This information is used as an intermediate CLA product within MPEF, to support the generation of
the Atmospheric Motion Vectors (AMV) product and others. The final CLA product,
which will be
distributed to the end-users, summarises the CLA information for a CLA processing segment. A third
kind of CLA product, the CLA image product, will be distributed to end-users in GRIB-2 data format,
providing, on a CLA image processing segment basis, the scenes type.
The following general requirements shall be applied:
 The intermediate CLA product shall update the scenes type for cloudy pixels with the detailed
cloud type; it shall also derive additional cloud information in the form of cloud phase, cloud
top temperature and cloud top height on a pixel basis for every repeat cycle. It shall also
include a flag for semi-transparent clouds / partly cloudy pixels for the VIS channels and the IR
channels, and according to the semi-transparency/partly cloudiness an effective cloud amount
for every pixel.
 The final CLA product shall
derive cloud information on a CLA processing segment in the
form of the overall cloud cover, and for at least three cloud level bands (low-level, mid-level,
high-level) the cloud type, the cloud phase for every cloud type, the cloud cover for every cloud
type, the cloud top temperature and height for every cloud type.
The final CLA product and the CLA image product for the CLA processing segments shall
be
generated using the intermediate CLA product which has been produced for the repeat cycle which is
closest to the required extraction time(s) of the final CLA product and the CLA image product.
Currently ten cloud types are specified:

Level Type
low-level cloud Fog or Stratus
low-level cloud Cumulus or Stratocumulus
low-level cloud unknown type
mid-level cloud Nimbostratus
mid-level cloud Altocumulus or Altostratus
mid-level cloud unknown type
high-level cloud Cumulonimbus
high-level cloud Cirrus
high-level cloud unknown type
unknown cloud type

<!-- source_page: 97 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Four cloud phases are specified:
 water phase
 ice phase
 mixed phase
 unknown phase
The CLA algorithm shall first generate the intermediate CLA product for every pixel and for every
repeat cycle as shown in Figure 5 and described below:

Step 1 Scenes type check: Check whether the scenes type provided by the Scenes Analysis has
been identified as clear or cloudy.

Step 2 Solar zenith angle check: Check the solar zenith angle data for every pixel to determine
the local time, i.e. day, dawn and night. This is to define the channels to be used in the
following steps and to define the tests to be used later.

Step 3 Comparison with previous repeat cycle: Use the current and previous image data from
a subset of the channels to detect if the image data have changed significantly. If there
has been no significant change the results of the previous intermediate CLA product can
be used.

Step 4 Threshold prediction: Currently the algorithm uses only static thresholds. For Future
Enhancements using additional MSG channels which may require more complex
threshold predictions, this functionality shall be foreseen.

Step 5 Cloud type, cloud phase, semi-transparency identification, cloud top height, cloud
top temperature, and effective cloud amount estimation: Identify the cloud phase;
identify whether the clouds are semi-transparent, partly cloudy or opaque; derive the
cloud top height, the cloud top temperature, the effective cloud amount; and identify the
cloud type on a pixel basis.

<!-- source_page: 98 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




scenes type check
if scenes type is cloudy
continue further
processing
data comparison with
previous repeat cycle
if changes have been
detected
continue processing
image data:
all channels of current image, all channels of previous repeat cycle
MPEF products and pre-processed data:
Scenes Analysis results, forecasted EBBT, satellite geometry,
CLA results of previous repeat cycle
pixel-based image data, products, pre-processed
data
static datasets:
static solar zenith angle
thresholds
solar zenith angle
check
day/night
information
static datasets:
static CLA thresholds,
static CLA parameter
threshold determination
thresholds for the different cloud tests
automatic quality control
(AQC)
output data: scenes type (updated with cloud type), cloud phase,
semi-transparency/partly cloudy flag, cloud top height and temperature,
effective cloud amount, location of the pixel, quality flag
static datasets:
static CLA parameters for
data comparison
determination of cloud phas, semitransparency/partly cloudy pixel,
cloud top height, cloud top temp.,
effective cloud amount and cloud type
cloud phase, semi-transparency/partly cloudy flag,
flagcloud top height and temperature,
effective cloud amount and scenes type updated with cloud type
if scenes type is not
cloudy
stop further processing
no clouds identified
scenes type
unchanged
quality flag of SCE
if no changes have been
detected use the results of
the previous repeat cycle
and stop further processing
previous CLA results
previous quality flag
quality flag

Figure 5: CLA Processing
8.3.2 Algorithm Description for Intermediate CLA
In the following, the steps listed above are described in detail. All static application data, thresholds,
parameters and numbers mentioned below shall be configurable. The algorithm for the intermediate
CLA shall be performed for every pixel.

<!-- source_page: 99 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8.3.2.1 Step 1: Scenes Type Check
The CLA algorithm shall use the scenes type information provided by the Scenes Analysis and check
whether it states clear or cloudy scene. If the scene has been identified as clear, the following steps
shall be skipped. Otherwise, the scenes type shall be updated according to the findings of the cloud
type tests specified below in Step 5.
8.3.2.2 Step 2: Solar Zenith Angle Check
The CLA Analysis algorithm shall use information about the elevation of the sun in the form of the
solar zenith angle for every pixel. According to the solar zenith angle the local time of the day for a
single pixel shall
be identified as:
 day, if the solar zenith angle is lower than a threshold (SZ_thres)
 night, if the solar zenith angle is greater than or equal to a threshold (SZ_thres)
8.3.2.3 Step 3: Data Comparison with Previous Repeat Cycle
The current and previous image data in the form of EBBT/reflectances shall be compared for
channels VIS0.6 (day only), VIS0.8 (day only), NIR1.6 (day only), IR3.9, IR8.7, IR10.8, IR12.0 for
each pixel to verify whether there has been a significant change in the data. This check shall accept
differences in starting time between the current and the previous repeat cycle of up to max_hours.
This is done by calculating the absolute difference between the current and the previous image data
for a subset of the channels:
absolute difference = ABS(current - previous)
For channels VIS0.6, VIS0.8 and NIR1.6 a static threshold (VIS_change) shall
be used for this check.
For the remaining IR channels the following formula shall be applied:
IR_threshold = (n +1) * step2_temp
with: n = (start_current_image - start_previous_image) /rc_nom_dur
If n is larger than max_cycles these tests shall not be performed and the algorithm shall continue with
the next step.
If no change has been detected in all channels used for this check (i.e. if the absolute differences are
smaller than the thresholds), then:
 the value of prev_scenes_type for the pixel shall be used
 the quality flag from the previous AQC shall be used
 the subsequent processing steps shall be skipped
8.3.2.4 Step 4: Threshold Prediction
Currently, the CLA Analysis algorithm uses only static thresholds for the determination of the cloud
type, cloud phase and the semi-transparency identification, according to the time of the day. But
Future Enhancements (e.g. use of additional channels) may have the need to introduce more complex
functions to predict the thresholds.

<!-- source_page: 100 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8.3.2.5 Step 5: Cloud Type, Cloud Phase, Semi-Transparency Identification, Cloud Top
Height, Cloud Top Temperature and Effective Cloud Amount Estimation
The cloud type and cloud phase shall be identified using threshold tests, which depend on the
availability of the input channels, and on the time of the day. In the following sections the threshold
tests are defined depending on the local time of the day.
8.3.2.5.1 Description of the Tests to be applied for Daytime Pixels
1. Cloud Phase Test
The cloud phase shall first be set to unknown phase.
If the ratio REFL1.6 / REFL0.6 is larger than a threshold ClouPhRat1, or
if the EBBT difference IR10.8-IR8.7 is smaller than a threshold CloudPhTdiff1, or
if the EBBT difference IR10.8-IR12.0 is smaller than a threshold CloudPhTdiff2, or
if the EBBT of IR10.8 is larger than a threshold CloudPhT1, then:
The cloud phase shall be set to water phase.

Otherwise, if the ratio REFL1.6 / REFL0.6 is smaller than a threshold ClouPhRat2, or
if the EBBT difference IR10.8-IR8.7 is larger than a threshold CloudPhTdiff3, or
if the EBBT difference IR10.8-IR12.0 is larger than a threshold CloudPhTdiff4, or
if the EBBT of IR10.8 is smaller than a threshold CloudPhT2 , then:
The cloud phase shall be set to ice phase.
Otherwise the cloud phase shall be set to mixed phase.

2. Semi-Transparency Test
The semi_transp_flag shall initially be set to a default flag stating opaque.
If the cloud phase is set to water phase then:
If the standard deviation in channel IR10.8 is larger than a threshold SemiTrStdDev1, and
if the ratio REFL0.8/REFL0.6 is between the thresholds SemiTrRat1 and SemiTrRat2, or
if the EBBT difference IR10.8-IR3.9 is smaller than a threshold SemiTrTdiff1, or
if the EBBT difference IR10.8-IR12.0 is larger than a threshold SemiTrTdiff2, then:
The semi-transparency flag shall be set to partly cloudy.
Otherwise:
If the EBBT difference IR10.8-IR8.7 is smaller than a threshold SemiTrTdiff3, or
if the EBBT difference IR10.8-IR12.0 is smaller than a threshold SemiTrTdiff4, then:
The semi-transparency flag shall be set to semi-transparent.

3. Cloud top height, cloud top temperature and effective cloud amount estimation
A detailed description of the derivation of the cloud top height, cloud top temperature and effective
cloud amount is given in Section 8.3.2.6.

<!-- source_page: 101 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




4. Cloud Type Test

Low-level clouds: If the pressure of the cloud top height is higher than
low_level_cloud_pressure, then:
 The scenes type shall be set to low-level cloud.
 If the EBBT-difference IR3.9-IR10.8 is larger than a threshold
(THR_D1IR_FOG_DAY), then the scenes type shall be set to fog/stratus.
 Otherwise, if the standard deviation of the EBBT in channel IR10.8 is
larger than a threshold (THR_STDIR108_CUM), then the scenes type
shall be set to Cumulus/Stratocumulus.

Mid-level clouds: If the pressure of the cloud top height is higher than
high_level_cloud_pressure, and lower than low_level_cloud_pressure,
then:
 The scenes type shall be set to mid-level cloud.
 If the standard deviation in channel IR10.8 is larger than a threshold
(THR_STDIR108_AC), then the scenes type shall be set to
Altocumulus/Altostratus.
 Otherwise, if the reflectance in channel VIS0.6 is larger than a threshold
(THR_VIS06_NS) and if the EBBT-difference IR10.8-IR12.0 is smaller
than a threshold (THR_D2IR_NS), then the scenes type shall be set to
Nimbostratus.

High-level clouds: If the pressure of the cloud top height is lower than
high_level_cloud_pressure, then:
 The scenes type shall be set to high-level cloud.
 If the EBBT-difference IR3.9-IR10.8 is larger than a threshold
(THR_D1IR_CB1) and if the standard deviation of channel IR10.8 is
larger than a threshold THR_IR108_CB), then the scenes type shall be
set to Cumulonimbus.
If the cloud_phase is equal to ice phase and if the scenes type is not
Cumulonimbus, then:
 The scenes type shall be set to Cirrus.

8.3.2.5.2 Description of the Tests to be applied for Night-time Pixels
1. Cloud Phase Test
The cloud phase shall first be set to unknown phase.
If the EBBT difference IR10.8-IR8.7 is smaller than a threshold CloudPhTdiff5, or
if the EBBT difference IR10.8-IR12.0 is smaller than a threshold CloudPhTdiff6, or
if the EBBT of IR10.8 is larger than a threshold CloudPhT3, then:
The cloud phase shall be set to water phase.
Otherwise, if the EBBT difference IR10.8-IR8.7 is larger than a threshold CloudPhTdiff7, or

<!-- source_page: 102 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




if the EBBT difference IR10.8-IR12.0 is larger than a threshold CloudPhTdiff8, or
if the EBBT of IR10.8 is smaller than a threshold CloudPhT4 , then:
The cloud phase shall be set to ice phase.

Otherwise the cloud phase shall be set to mixed phase.
2. Semi-Transparency Test
The semi_transp_flag shall initially be set to a default flag stating opaque.
If the cloud phase is set to water phase then:
If the standard deviation in channel IR10.8 is larger than a threshold SemiTrStdDev2, and
if the EBBT difference IR10.8-IR3.9 is smaller than a threshold SemiTrTdiff5, or
if the EBBT difference IR10.8-IR12.0 is larger than a threshold SemiTrTdiff6, then:
The semi-transparency flag shall be set to partly cloudy.
Otherwise:
If the EBBT difference IR10.8-IR8.7 is smaller than a threshold SemiTrTdiff7, or
if the EBBT difference IR10.8-IR12.0 is smaller than a threshold SemiTrTdiff8, then:
The semi-transparency flag shall be set to semi-transparent.
3. Cloud top height, cloud top temperature and effective cloud amount estimation
A detailed description of the derivation of the cloud top height, cloud top temperature and effective
cloud amount is given in Section 8.3.2.6.
4. Cloud Type Test

Low-level clouds: If the pressure of the cloud top height is higher than
low_level_cloud_pressure, then:
 the scenes type shall be set to low-level cloud
 if the EBBT-difference IR3.9-IR10.8 is smaller than a threshold
(THR_D1IR_FOG_NIGHT), then the scenes type shall be set to
fog/stratus.
 otherwise if the standard deviation of the EBBT in channel IR10.8 is
larger than a threshold (THR_STDIR108_CUM), then the scenes type
shall
be set to Cumulus/Stratocumulus.

Mid-level clouds: If the pressure of the cloud top height is higher than
high_level_cloud_pressure, and lower than low_level_cloud_pressure,
then:
 the scenes type shall be set to mid-level cloud
 if the standard deviation in channel IR10.8 is larger than a threshold
(THR_STDIR108_AC), then the scenes type shall be set to
Altocumulus/Altostratus
 if the EBBT-difference IR10.8-IR12.0 is smaller than a threshold
(THR_IR_NS), then the scenes type shall be set to Nimbostratus.

<!-- source_page: 103 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




High-level clouds: If the pressure of the cloud top height is lower than
high_level_cloud_pressure, then:
 the scenes type shall be set to high-level cloud
 if the EBBT-difference IR3.9-IR10.8 is larger than a threshold
(THR_IR108D1IR_CB) and if the standard deviation of channel IR10.8 is
larger than a threshold (THR_D1IR_CB2), then the scenes type shall be
set to Cumulonimbus
If the cloud_phase is equal to ice phase and if the scenes type is not
Cumulonimbus, then:
 the scenes type shall be set to Cirrus.
8.3.2.6 Cloud Top Height, Cloud Top Temperature and Effective Cloud Amount
Estimation
This function shall derive the cloud top temperature (in kelvin), the cloud top height (in hPa) and the
effective cloud amount (in %).
The cloud top height, the cloud top temperature and the effective cloud amount shall be determined
on a pixel basis for all pixels flagged as cloudy as follows:
 Interpolate the data provided by the RTM (which already has been horizontally interpolated) in
the vertical to fixed vertical_int hPa pressure levels between the tropopause and the surface.
 Extract the level with the smallest difference of measured and calculated radiances in channel
IR10.8 between the tropopause and the surface (i.e. lowest possible cloud level). Extract: the
pressure of that level, i.e. the cloud top height in hPa (PCLH0), the temperature of that level, i.e.
the cloud top temperature in kelvin (TCTH0) and set the effective cloud amount of the level to
100% (NEFF0). If the extracted level is equal to the surface and if the cloud is flagged as opaque
in the cloud analysis, the cloud height shall be set to the pressure of the closest level above the
surface, the cloud top temperature shall be set to the predicted temperature of that level, the
effective cloud amount shall be set to 100%, the cloud type shall be reset to fog/stratus and the
following steps shall be skipped.
 Calculate the difference between the measured radiance of channel IR10.8 and the predicted clear
sky radiance of that channel (RADDIF10.8, measured). If channel IR10.8 is not available channel
IR12.0 shall be selected instead.
 Calculate the difference between the measured radiance of channel IR13.4 and the predicted clear
sky radiance of that channel. (RADDIF13.4, measured)
 Calculate the difference between the measured radiance of channel WV6.2 and the predicted clear
sky radiance of that channel. (RADDIF6.2, measured)
 Calculate the difference between the measured radiance of channel WV7.3 and the predicted clear
sky radiance of that channel. (RADDIF7.3, measured)
 Calculate the following ratios:
RATIO1 = rat_cor_13.4 * RADDIF13.4, measured / RADDIF10.8, measured
RATIO2 = rat_cor_6.2 * RADDIF6.2, measured / RADDIF10.8, measured
RATIO3 = rat_cor_7.3 * RADDIF7.3, measured / RADDIF10.8, measured
where
rat_cor_13.4, rat_cor_6.2, rat_cor_7.3 are correction factors given in a static data set. These
correction factors depend on the cloud phase.

<!-- source_page: 104 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




 Calculate the difference between the calculated radiance (from the RTM) of channel IR10.8 and
the predicted clear sky radiance of that channel for all pressure levels between the tropopause and
the lowest possible cloud level. (RADDIF10.8, calculated (p))
 Calculate the difference between the calculated radiance (from the RTM) of channel IR13.4 and
the predicted clear sky radiance of that channel for all pressure levels between the tropopause and
the lowest possible cloud level. (RADDIF13.4, calculated (p))
 Calculate the difference between the calculated radiance (from the RTM) of channel WV6.2 and
the predicted clear sky radiance of that channel for all pressure levels between the tropopause and
the lowest possible cloud level. (RADDIF6.2, calculated (p))
 Calculate the difference between the calculated radiance (from the RTM) of channel WV7.3 and
the predicted clear sky radiance of that channel for all pressure levels between the tropopause and
the lowest possible cloud level. (RADDIF7.3, calculated (p))
 Calculate the following ratios for each pressure level between the tropopause and the lowest
possible cloud level:
RATIO1 (p) = rat_cor_13.4 * RADDIF13.4, calculated (p) / RADDIF10.8, calculated (p)
RATIO2 (p) = rat_cor_6.2 * RADDIF6.2, calculated (p) / RADDIF10.8, calculated (p)
RATIO3 (p) = rat_cor_7.3 * RADDIF7.3, calculated (p) / RADDIF10.8, calculated (p)
where rat_cor_13.4, rat_cor_6.2, rat_cor_7.3 are correction factors given in a static data set.
These correction factors depend on the cloud phase.
 For each of the three channel combinations find the level (LCLD,1 , LCLD,2 , LCLD,3 ) between the
tropopause and the lowest possible cloud level with the best agreement (minimum difference)
between the ratio with measured radiances (i.e. RATIO1, RATIO2, RATIO3) and the ratio with
calculated radiances (i.e. RATIO1 (p) , RATIO2 (p) , RATIO3 (p).
 For each of the three channel combinations extract the pressure of that level, i.e. the cloud top
height in hPa (PCTH 1, 2, 3).
 For each of the three channel combinations extract the temperature of that level, i.e. the cloud top
temperature in kelvin (TCTH 1, 2, 3).
 For each of the three channel combinations the effective cloud amount (NEFF in units of %) is
derived as follows:
- Extract the difference between the calculated radiance and the clear sky radiance in channel
10.8 at the derived cloud level (RADDIF10.8 , calculated, lcld).
- Derive the effective cloud amount by building the following ratio:
NEFF1, 2, 3 = 100 * RADDIF10.8 , measured / RADDIF10.8, calculated, LCLD, 1, 2, 3
If the effective cloud amount is larger than neff_max, it shall be reset to neff_max.
If the effective cloud amount is smaller than neff_min and if the semi_transp_flag is set to
opaque, the semi_transp_flag shall be reset to semi-transparent/partly cloudy.
The final product output for the cloud top height, the cloud top temperature and the effective cloud
amount will be derived as follows:
 If the cloud phase is set to ice phase or to mixed phase and if the EBBT measured in channel
IR10.8 or channel IR12.0 is colder than the predicted EBBT by a threshold DiffBase, then the
cloud top parameters shall be derived as follows:
Cloud top height, PCTH = a0 + a1 * PCTH1 + a2 * PCTH2 + a3 * PCTH3

<!-- source_page: 105 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Cloud top temperature, TCTH = b0 + b1 * TCTH1 + b2 * TCTH2 + b3 * TCTH3
Effective cloud amount, NEFF = c0 + c1 * NEFF1 + c2 * NEFF2 + c3 * NEFF3
The coefficients in the above equations shall be set as follows:
 A flag for channel WV6.2 is set to true, if the channel available and if the measured EBBT in
the channel is colder than the predicted EBBT by a threshold Diff62 and if the standard
deviation of the EBBT in the channel is larger than a threshold Std62.
 The same check shall be applied to channels WV7.3 and IR13.4.
 If for all three channels the flag is set to true, the pre-set coefficients from the set-up data set
shall be used to derive the cloud top height, the cloud top temperature and the effective cloud
amount.
 Otherwise the following procedure shall be applied:
- All coefficients are set to 0.
- If the flag for channel IR13.4 is set to true, its relevant coefficients are set to 1.0.
- Otherwise if the flag for channel WV7.3 is set to true, its relevant coefficients are set to 1.0.
- Otherwise if the flag for channel WV6.2 is set to true, its relevant coefficients are set to 1.0.
- Otherwise the opaque cloud top values (PCTH0, TCTH0, NEFF0 ) are used instead.
 Otherwise, if the cloud phase is not set to ice phase or to mixed phase and if the EBBT
measured in channel IR10.8 or channel IR12.0 is not colder than the predicted EBBT by a
threshold DiffBase:
The cloud top height, PCTH, shall be set to PCTH0.
The cloud top temperature, TCTH, shall be set to TCTH0.
The effective cloud amount, NEFF, shall be set to NEFF0.
For all cloud top heights, PCTH, with a pressure bigger than inv_low_AMV_pres_thres (nominally
600 hPa) the inversion height assignment shall be performed. The inversion height assignment shall:
1. Extract the minimum forecast temperature (min_temp) and maximum forecast temperature
(max_temp) between inv_low_FC_pres_thres (nominally 700 hPa) and the layer closest to the
surface pressure plus inv_surf_offset (nominally 40 hPa).
2. Extract the pressure corresponding to min_temp (pres_of_min_temp) and pressure
corresponding to max_temp (pres_of_max_temp).
3. If temp_grad (max_temp – min_temp) > inv_magnitude (nominally 0 K) then
inv_pres = (inv_C1 * pres_of_min_temp + inv_C2 * pres_of_max_temp) / (inv_C1 +
inv_C2) + inv_C3
and
inv_temp = (inv_C1 * min_temp + inv_C2 * max_temp) / (inv_C1 + inv_C2) + inv_C3
where inv_C1, inv_C2 and inv_C3 are set-up parameters.
4. If steps 2 and 3 were successful, then reset PCTH to inv_pres as new cloud top height and
temperature to inv_temp as new cloud top temperature.

<!-- source_page: 106 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8.3.3 Algorithm Description for the Final CLA Product
In the following the determination of the final CLA product, which shall be disseminated, is described
in detail. The final CLA product shall be derived on a CLA processing segment of size CLA_ps_size
using the pixel-based results of the intermediate CLA product. The following parameters shall be
derived on this CLA processing segment:
 For every CLA processing segment the total effective cloud amount shall be calculated by
summing the effective cloud amount of every pixel in the segment, and by dividing by the
total number of pixels. If fewer than min_cld_pixels cloudy pixels can be found for the whole
segment then default values shall be provided indicating ‘no clouds’.
 The effective cloud amount for each cloud type and for each sub-level shall be calculated
similarly.
 The mean cloud top height, the mean cloud top temperature and the mean optical thickness
shall be determined for each cloud type in each sub-level.
8.3.4 Algorithm Description for the CLA Image Product
In the following the determination of the CLA image product, which shall be disseminated, is
described. The CLA image product shall be derived on a CLA image processing segment basis using
the pixel-based information of the intermediate CLA product. Depending on the extracted
information, this image shall either provide the most significant surface type if the number of clear
pixels is greater than min_ima_pixels (i.e. surface type for majority of pixels in the segment) if the
segment is clear, or otherwise it shall provide the most significant cloud type (i.e. cloud type for
majority of pixels in the segment) if the segment is cloudy. Currently 21 surface types (as specified
for the Scenes Analysis algorithm) and 10 cloud types (as specified above) are used.
8.3.5 Automatic Quality Control (AQC)
8.3.5.1 Intermediate CLA Product
The following automatic quality control steps shall be applied only for the intermediate CLA product.
It shall be applied to the cloud top height estimation.
The AQC shall be performed as follows:
Spatial Consistency AQC check for the cloud top height
For each pixel all surrounding neighbouring pixels shall be checked for the cloud top height. If the
neighbouring pixels have the same cloud type as the investigated one, if the measured EBBTs are
within int_QA_thresh_1 kelvin and the derived cloud top height is within int_QA_thresh_2 hPa, the
CLA intermediate quality flag shall be set indicating ‘cloud_top_height related parameters, good
quality’ else it shall be set to ‘cloud_top_height related parameters, bad quality’.
Spatial Consistency AQC check for the cloud type
For each pixel all surrounding neighbouring pixels shall be checked for the cloud type. If none of the
neighbouring pixels has the same cloud type as the investigated one, the CLA intermediate quality
flag shall be set indicating ‘cloud_type, bad quality’.
8.3.5.2 Final CLA Product
The following automatic quality control steps shall be applied only for the final CLA product. It shall
be applied for each cloud type identified in the CLA processing segment, the cloud top temperature of
that cloud type and the cloud height of that cloud type.

<!-- source_page: 107 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The AQC shall be performed as follows:
 If any pixel comprising the Final Product processing segment has CLA_int_quality flag in the
Intermediate Product flagged as ‘Cloud Type poor quality’, the CLA_quality_flag in the Final
Product will be flagged as ‘Cloud Type poor quality’ for that processing segment.
 If any pixel comprising the Final Product processing segment has a value for the cloud_top_temp
in the Intermediate Product which differs by more than Int_QA_thres_1 from the mean cloud top
temperature of the relevant cloud type, the CLA_quality_flag in the Final Product will be flagged
as ‘Cloud Top Temperature poor quality’ for that processing segment.
 If any pixel comprising the Final Product processing segment has a value for the
cloud_top_pressure in the Intermediate Product which differs by more than Int_QA_thres_2 from
the mean cloud top pressure of the relevant cloud type, the CLA_quality_flag in the Final Product
will be flagged as ‘Cloud Top Pressure poor quality’ for that processing segment.
 An average value of the SCE quality flag shall be derived from all cloudy pixels in the Final
Product processing segment. If this average value indicates a confidence greater than 90% the
CLA_quality_flag in the Final Product will be flagged as ‘Cloud Dectection confidence >90%’
for that processing segment. If this average value is between 70% and 90% the CLA_quality_flag
in the Final Product will be flagged as ‘Cloud Dectection confidence 70% - 90%’ for that
processing segment. If this average value is below 70% the CLA_quality_flag in the Final
Product will be flagged as ‘Cloud Dectection confidence <70%’ for that processing segment.
8.4 Outputs
Three types of products shall be generated, i.e. the intermediate CLA product, the final CLA product
and the CLA image product.
8.4.1 Intermediate CLA Product
This product shall be used for further internal MPEF processing (e.g. AMV) and shall be provided on
a pixel basis for every repeat cycle.

<!-- source_page: 108 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




INTERMEDIATE CLA PRODUCT
Parameter Mnemonic Units Min Max Prec Acc To
Scenes type scenes_type - 0 110 - - AMV, CDS, CSR, CLAima,
CLAfinal, CLAnext
Cloud top temperature cloud_top_temp K 170 300 1 1 CLA final, CLAnext
Cloud top pressure cloud_top_pressure hPa 100 1050 50 1 AMV, CTH, CLAfinal,
CLAnext
Effective cloud amount cloud_am ount_eff % 0 100 1 1 AMV, CLA final, CLAnext
SCE quality index QI - 0 100 10 10 CSR
CLA intermediate
quality flag
CLA_int_quality_
flag
- - - - - AMV, CLA next
Table 23: Intermediate Cloud Product, Components
Parameter Value Meaning
scenes_type 0 – 100 See details in Section 5.4
101 Fog or Stratus
102 Cumulus or Stratocumulus
103 Low-level unknown cloud
104 Nimbostratus
105 Altocumulus or Altostratus
106 Mid-level unknown cloud
107 Cumulonimbus
108 Cirrus
109 High-level unknown cloud
110 Unknown cloud

Parameter Bit No. Meaning Value Meaning
CLA_int_quality_flag Bits 0-1 Cloud phase

0
1
2
3
Unknown
Water
Ice
Mixed
Bits 2-3 SCE quality flag
Bit 4 Cloud type quality 0
1
Good
Bad
Bit 5 Cloud height
quality
0
1
Good
Bad
Bits 6-7 Semi-transparency
flag
0
1
2
3
Opaque
Partly cloudy
Semi-transparent
Semi-transparency
correction failed / not
processed

<!-- source_page: 109 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8.4.2 Final CLA Product
This product shall be provided on CLA processing segment basis for the required extraction times.

Parameter Value Meaning
CLA_quality_flag Bit 0 : 1 Cloud Type poor quality
Bit 1 : 1 Cloud Top Temperature poor quality
Bit 2 : 1 Cloud Top Height poor quality
Bit 3 : 1 Cloud Determination 100% confidence (from SCE quality flag)
Bit 4 : 1 Cloud Determination 75% confidence (from SCE quality flag)
Bit 5 : 1 Cloud Determination 50% confidence (from SCE quality flag)

Table 24 that follows presents the Final CLA Product Parameters.

<!-- source_page: 110 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 111 of 298


FINAL CLA PRODUCT
Parameter Mnemonic Units Min Max Prec Acc To
Total effective cloud amount tot_eff_cloud_amount % 0 100 1 1 Final CLA
Total cloud amount of all low-level clouds cloud_amount_llc % 0 100 1 1
All cloud types of low-level cloud cloud_typei_llc - - - - -
Cloud amount of every low-level cloud type cloud_amount_type i % 0 100 1 1
Cloud phase of every low-level cloud type cloud_phase_typei - - - - -
Mean cloud top temperature of every low-level cloud type cloud_top_temp_type i K 170 300 1 1
Mean cloud top height of every low-level cloud type cloud_top_height_typei hPa 100 1050 50 1
Cloud amount of all mid-level clouds cloud_amount_mlc % 0 100 1 1
All cloud types of mid-level clouds cloud_typei_mlc - - - - -
Cloud amount of every mid-level cloud type cloud_amount_type i % 0 100 1 1
Cloud phase for every mid-level cloud type cloud_phase_typei - - - - -
Mean cloud top temperature of every mid-level cloud type cloud_top_temp_type i K 170 300 1 1
Mean cloud top height of every mid-level cloud type cloud_top_height_typei hPa 100 1050 50 1
Cloud amount of all high-level-clouds cloud_amount_hlc % 0 100 1 1
All cloud types of high-level clouds cloud_typei_hlc - - - - -
Cloud amount of every high-level cloud type cloud_amount_type i % 0 100 1 1
Cloud phase of every high-level cloud type cloud_phase_typei - - - - -
Mean cloud top temperature of every high-level cloud type cloud_top_temp_type i K 170 300 1 1
Mean cloud top height of every high-level cloud type cloud_top_height_typei hPa 100 1050 50 1
CLA quality flag CLA_qu ality_flag - - - - -
Table 24: Final CLA Product Parameters

<!-- source_page: 111 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8.4.3 CLA Image Product
This product shall be provided on a CLA image processing segment basis in the form of a GRIB
Edition 2 encoded product for the required extraction times. The segment size is 3 × 3 pixels of the
original intermediate CLA product. Since the latter contains 3712 × 3712 pixels, the area of CLAI
containing actual information is given by:
3712 ÷ 3 = 1237.3 = 1237 (rounded down) thus: 1237 × 1237 pixels.
The product shall
contain for every segment the scenes type.

CLA IMAGE PRODUCT
Parameter Mnemonic Units Min Max Prec Acc To
Scenes type scenes_type - - - - - CLAimage
8.5 Prototyping and Testing
The prototyping software is available for deriving the cloud type, cloud phase and the semitransparency flag.
The inclusion of the semi-transparency correction, the cloud optical thickness, cloud top temperature
and the cloud top height calculations is a Future Enhancement.
8.6 Future Enhancements
The following Future Enhancements shall be foreseen in the algorithm design:
 Use of level 1.5 image data from additional channels
 Dynamic threshold prediction
8.7 References
None

<!-- source_page: 112 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9 ATMOSPHERIC MOTION VECTORS PRODUCT GENERATION
9.1 Algorithm Configuration Information
9.1.1 Algorithm Name
Atmospheric Motion Vectors (AMV)
9.1.2 Algorithm Identifier
EUM_MSG_AMV_A001
9.1.3 Algorithm Specification Version History

Version Date Modified By Description
1.0 26/11/96 K. Holmlund AMV Baseline
1.1 26/5/97 K. Holmlund TBDs resolved, bid clarification points added, errors
corrected.
1.2 1/7/97 K. Holmlund Clarifications added and improvement to the AQC
checks added.
1.3 8/12/97 H. K. Wilson Kick-off clarification points added, Requirements
Analysis clarification points added.
1.4 20/3/98 H. K. Wilson Peer Group review comments added.
1.5 15/1/99 H.-J. Lutz Detailed Design Phase changes added.
1.6 04/12/01 K. Holmlund Target extraction and height assignment (ECP290).
1.7 25/7/05 A. de Smet, G. Dew, J.
Gustafsson
Various updates, mainly to height assignment.
1.8 27/3/07 A. de Smet, G. Dew, J.
Gustafsson
Various updates including height assignment and target
optimisation. Addition of Recursive Filter Function and
Upper Level Divergence.
1.9 02/12/08 J. Gustafsson Addition of Encoding Filter. Addition of two parameters
for use in final vector derivation.
1.10 27/10/09 A. de Smet Description of AMV Inversion Height Assignment
rewritten to reflect actual implementation (AR 18745).
Updates to both output tables with respect to introduction
of land-sea flag (AR 19113) and to remove two duplicate
entries.

<!-- source_page: 113 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.2 Inputs
The Atmospheric Motion Vector (AMV) generation shall use the Level 1.5 image data from all
spectral channels selected by the AMV channel selection table. Initially, the AMV is extracted from
the following spectral channels:
 VIS 0.8
 IR 10.8
 WV 6.2
 WV 7.3
 HRVIS
AMV extraction is also possible from the VIS0.6 channel, but this option is currently switched off.
The use of other channels, i.e. IR8.7 and IR9.7, shall be possible as a future enhancement.
The AMV shall use clear-sky radiances tables that relate the effect of opaque cloud at different
heights to the radiances in the eight IR channels and atmospheric correction tables provided by the
RTM. This information shall
be provided to the AMV as EBBTs. It is foreseen that the RTM shall
provide the clear sky contribution functions for the selected IR channels. This RTM table shall in the
AMV retrieval be used as a continuous function interpolated in time and space to the gravity centre of
the target. This implies that, as the table is provided only at discrete levels, the table values shall also
be interpolated in height, when necessary.
The results from the RTM and the Cloud Analysis shall be used to define the suitability of the
channels to provide good displacement vectors at all locations, image enhancement and height
assignment for each tracer. The AMV shall also use the forecast temperature profiles for height
assignment. Finally, the AMV requires an ensemble of AMV set-up parameters (static application
data) to control the different processes.
9.2.1 Image and Preprocessing Data (Dynamic Application Data)
The dynamic input is time-dependent and is different for each repeat cycle. The implementation shall
make all data available for all the extractions performed, i.e. for every specified channel. The table is
specific for the baseline configuration. For future enhancements, also the possibility to include further
channels (e.g. IR9.7 and IR8.7) shall be anticipated

<!-- source_page: 114 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 115 of 298


LEVEL 1.5 DATA AND DATA DERIVED FROM THE IMAGE DATA
Parameter Mnemonic Units Min Max Prec Acc Source
Local mean and local standard deviation
data from the currently processed channel
ima_stat_dat - - - - - Derived from level 1.5 image data
HRVIS level 1.5 image data HRVIS_ima_dat % 0 150 0.1 0.1 Level 1.5 image data
VIS0.6 level 1.5 image data VIS06_ima_dat % 0 150 0.1 0.1 Level 1.5 image data
VIS0.8 level 1.5 image data VIS08_ima_dat % 0 150 0.1 0.1 Level 1.5 image data
NIR1.6 level 1.5 image data NIR16_ima_dat % 0 150 0.1 0.1 Level 1.5 image data
IR3.9 level 1.5 image data IR38_ima_dat K 170 350 0.1 0.1 Level 1.5 image data
IR8.7 level 1.5 image data IR87_ima_dat K 170 350 0.1 0.1 Level 1.5 image data
IR9.7 level 1.5 image data IR97_ima_dat K 170 350 0.1 0.1 Level 1.5 image data
IR10.8 level 1.5 image data IR108_ima_dat K 170 350 0.1 0.1 Level 1.5 image data
IR12.0 level 1.5 image data IR120_ima_dat K 170 350 0.1 0.1 Level 1.5 image data
IR13.4 level 1.5 image data IR134_ima_dat K 170 350 0.1 0.1 Level 1.5 image data
WV6.2 level 1.5 image data WV62_ima_dat K 170 350 0.1 0.1 Level 1.5 image data
WV7.3 level 1.5 image data WV73_ima_dat K 170 350 0.1 0.1 Level 1.5 image data
Radiances for channels:
IR3.9,
WV6.2,
WV7.3,
IR8.7,
IR9.7,
IR10.8,
IR12.0,
IR13.4
Rad
Ichannel mWm -2sr-1(cm-1)-1 0 - - - Derived from level 1.5 image data
Table 25: AMV Product Level 1.5 Data and Data Derived from the Image Data

<!-- source_page: 115 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.2.2 Data from other MPEF Algorithms (Dynamic Application Data)
DATA FROM OTHER MPEF ALGORITHMS
Parameter Mnemonic Units Min Max Prec Acc Source
Pressure, temperature and
wind forecast profiles
temp_prof - - - - - Forecast
Tropopause Height trop_ht hPa 0 1030 1 1 Derived from
Forecast
Atmospheric Correction
Table
RTM_acc_tab mWm-2sr-1(cm-1)-1 0 - - - RTM
Semi-Transparency
Correction Table
RTM_stc_tab mWm -2sr-1(cm-1)-1 0 - - - RTM
Contribution Function
Tables
NTC, NTCC - 0 1 10-3 10-4 RTM
Scenes Type scenes_type - - - - - CLA intermediate
Cloud Phase cloud_phase - - - - - CLA intermediate
Cloud Top Height cl_top_ht hPa 100 1050 50 1 CLA intermediate
Predicted EBBTs for all
IR channels
pred_EBBT_chan K 170 350 0.1 0.1 SCE
Table 26: AMV Product: Data from other MPEF Algorithms
9.2.3 Static Application Data
The static application data input controls the complete AMV process. These data are changed
infrequently during operations but shall be configurable.
The static application data used by the AMV algorithm shall consist of the following:
 Pixel-based map of surface-type
 Pixel-based map of distance to nearest coastline
 Pixel-based description of processing area
 Static parameters for different mathematical expressions and channel instrument characteristics
 Set-up parameters specific to the AMV processing algorithm
The static input shall be specified separately for every baseline channel used for the extraction of
displacement vectors. The same approach shall also be adapted for the channels foreseen as Future
Enhancements.

STATIC APPLICATION DATA – SURFACE DATA
Parameter Mnemonic Units Min Max Prec Acc Source
Surface-Type-Map Surface_type_map - 0 99 1 1 Static data
Nearest coast distance Nearest_coast_dist km 0 10000 - - Static data
Processing_area Proc_area pixels 0 10000 - - Static data

<!-- source_page: 116 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 117 of 298

STATIC APPLICATION DATA – OTHER
Parameter Mnemonic Units Min Max Prec Acc Source
Mathematical expressions, channel specific constants Alg_data - - - - - Static data


STATIC APPLICATION DATA (PER CHANNEL USED FOR AMV PROCESSING)
Parameter Mnemonic Units Min Max Prec Acc Res Source
AMV channel ID AMV_chan_id - 1 12 1 1 - Static
AMV channel selection table AMV_chan_tab - - - - - - Static
Flag indicating method to be used for scenes analysis AMV_use_dynamic_scenes - 0 1 - - - Static
Minimum cluster size (pixels) in dynamic scenes analysis cluster_min_size pixels 1 1024 - - pixel Static
Minimum 3-point histogram frequency his_min_freq - 5 10 - - - Static
Gaussian point 2 histogram offset hi s_off_coeff1 - 1 10 - - - Static
Gaussian point 3 histogram offset his_off_coeff2 - 1 10 - - - Static
Number of histogram bins n_hist_bin - 10 200 - - - Static
Maximum number of clustered scenes n_cloud_clusters - 1 20 - - - Static
Histogram analysis maximum number of cycles max_class_cycles - 1 4 - - - Static
Minimum acceptable no. of occurrences of histogram peaks min_peak_occ - 1 10 - - - Static
Histogram analysis minimum difference in peak mean to avoid
merging
peak_min_diff - 1 10 - - - Static
Histogram analysis minimum difference in peak std to avoid
merging
peak_std_diff - 1 10 - - - Static
Minimum scene distance min_scene_dist K 0 100 0.1 0.1 - Static
Minimum number of pixels for a valid scene min_sce_size pixels 1 232-1 1 1 pixel Static
Computation grid grid_distance pixels 1 2 32-1 1 1 pixel Static

<!-- source_page: 117 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 118 of 298

STATIC APPLICATION DATA (PER CHANNEL USED FOR AMV PROCESSING)
Parameter Mnemonic Units Min Max Prec Acc Res Source
Maximum target overlap max_tar_overlap pixels 1 232-1 1 1 pixel Static
Minimum tracer size min_tracer_size pixels 1 2 32-1 1 1 pixel Static
Minimum standard deviation min_sd K 0 100 0.1 0.1 - Static
Minimum number of pixels with high standard deviation min_num_high_sd pixels 1 2 32-1 1 1 pixel Static
Cloud target size Cl_tar_size pixels 1 232-1 1 1 pixel Static
Clear sky target size CS_tar_size pixels 1 2 32-1 1 1 pixel Static
Cloud search area size Cl_sar_size pixels 1 232-1 1 1 pixel Static
Clear sky search area size CS_sar_size pixels 1 2 32-1 1 1 pixel Static
Target optimisation area tar_opt_area pixels 1 232-1 1 1 pixel Static
Target extraction method tar_ex_met - 0 7 1 1 - Static
Target extraction scheme tar_extraction - 0 7 1 1 - Static
Flag to define application of coastal check lcoast_flag Logica false true - - - Static
Apply image enhancement l_enhance - no yes - - - Static
Matching method Mm - 0 7 1 1 - Static
Scene limit factor cl_lim - 0.0 300.0 0.01 0.01 - Static
Tracer masking type TM - 0 1 - - - Static
Contrast factor CF - 0.0 300.0 0.01 0.01 - Static
Flag indicating cloud coverage for the WV channels wv_cloud_type - 0 2 - - - Static
SCM regression factor for large contrast SCM_RF_L - 0.0 1000.0 0.01 0.01 - Static
SCM regression factor for small contrast SCM_RF_S - 0.0 1000.0 0.01 0.01 - Static
SCM regression offset for large contrast SCM_RO_L K 0.0 1000.0 0.01 0.01 - Static
SCM regression offset for small contrast SCM_RO_S K 0.0 1000.0 0.01 0.01 - Static

<!-- source_page: 118 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 119 of 298

STATIC APPLICATION DATA (PER CHANNEL USED FOR AMV PROCESSING)
Parameter Mnemonic Units Min Max Prec Acc Res Source
Temperature threshold for SCM selection SCM_T K 0 350 0.01 0.01 - Static
Apply low pass filtering FFT_low - no yes - - - Static
Refinement of displacement n_fit - 0 255 1 1 - Static
Number of cycles used to generate final product N_gen - 0 96 1 1 - Static
Minimum quality for targets after one cycle first_cycle_min_qi - 0 1 0.01 0.01 - Static
Minimum quality for targets after more than one cycle new_cycle_min_qi - 0 1 0.01 0.01 - Static
Set-up parameters for AQC Forecast Consistency test AQC_FC_A - 0 1 0.01 0.01 - Static
AQC_FC_B - 0 1 0.001 0.001 - Static
AQC_FC_C - 0 10 0.1 0.1 - Static
AQC_FC_D - 0 10 0.1 0.1 - Static
Set-up parameters for AQC Temporal Vector Consistency test AQC_TC_A - 0 1 0.01 0.01 - Static
AQC_TC_B - 0 1 0.001 0.001 - Static
AQC_TC_C - 0 10 0.1 0.1 - Static
AQC_TC_D - 0 10 0.1 0.1 - Static
Maximum pressure difference to surrounding vectors AQC_SC_max_pp hPa 0 1100 0.1 0.1 - Static
Set-up parameters for AQC Spatial Vector Consistency test AQC_SC_A - 0 1 0.01 0.01 - Static
AQC_SC_B - 0 1 0.001 0.001 - Static
AQC_SC_C - 0 10 0.1 0.1 - Static
AQC_SC_D - 0 10 0.1 0.1 - Static
Local consistency distance weight flag lc_dist_weight Logica false true - - - Static
Number of best matches for local consistency N_best_lc - 1 100 1 1 - Static
Set-up parameters for AQC Spatial Height Consistency test AQC_HC_A - 0 1 0.01 0.01 - Static

<!-- source_page: 119 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 120 of 298

STATIC APPLICATION DATA (PER CHANNEL USED FOR AMV PROCESSING)
Parameter Mnemonic Units Min Max Prec Acc Res Source
AQC_HC_B - 0 100 1 1 - Static
AQC_HC_C - 0 10 1 1 - Static
Set-up parameters for AQC Temporal Speed Consistency test AQC_TSC_A - 0 1 0.01 0.01 - Static
AQC_TSC_B - 0 1 0.001 0.001 - Static
AQC_TSC_C - 0 10 0.1 0.1 - Static
AQC_TSC_D - 0 10 0.1 0.1 - Static
Set-up parameters for AQC Temporal Direction Consistency
test
AQC_TDC_A - 0 100 0.1 0.1 - Static
AQC_TDC_B - 0 100 0.1 0.1 - Static
AQC_TDC_C - 0 100 0.1 0.1 - Static
AQC_TDC_D - 0 100 0.1 0.1 - Static
AQC_TDC_E - 0 100 0.1 0.1 - Static
Set-up parameters for AQC Temporal Height Consistency test AQC_TPC_A - 0 1 0.001 0.001 - Static
AQC_TPC_B - 0 1 0.001 0.001 - Static
AQC_TPC_C - 0 1 0.01 0.01 - Static
AQC_TPC_D - 0 100 1 1 - Static
Set-up parameters for AQC Inter-Channel Consistency AQC_IC_A - 0 1 0.001 0.001 - Static
AQC_IC_B - 0 1 0.001 0.001 - Static
AQC_IC_C - 0 1 0.01 0.01 - Static
AQC_IC_D - 0 100 1 1 - Static
ic_low_press hPa 0 1100 1 1 - Static
ic_min_spd m/s 0 100 1 1 - Static

<!-- source_page: 120 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 121 of 298

STATIC APPLICATION DATA (PER CHANNEL USED FOR AMV PROCESSING)
Parameter Mnemonic Units Min Max Prec Acc Res Source
low_ic_check_dist km 0 200 1 1 - Static
ic_press_diff hPa 0 1100 1 1 - Static
Set-up parameters for AQC Image Correlation test AQC_HA_A - 0 1 0.001 0.001 - Static
AQC_HA_B - 0 1 0.001 0.001 - Static
AQC_HA_C - 0 1 0.01 0.01 - Static
AQC_HA_PP - 0 100 1 1 - Static
Weight of forecast consistency test final quality mark AMV_Q_Weights_forecast - - - - - - Static
Weight of image correlation test in final quality mark AMV_Q_Weights_ha - - - - - - Static
Weight of inter-channel consistency test in final quality mark AMV_Q_Weights_ic - - - - - - Static
Weight of spatial height test in final quality mark AMV_Q_Weights_ shc - - - - - - Static
Weight of spatial vector test in final quality mark AMV_Q_Weights_swc - - - - - - Static
Weight of temporal vector consistency test in final quality mark AMV_Q_Weights_tc - - - - - - Static
Weight of temporal direction consistency test in final quality
mark
AMV_Q_Weights_tdc - - - - - - Static
Weight of temporal height consistency test in final quality mark AMV_Q_Weights_tpc - - - - - - Static
Weight of temporal speed consistency test in final quality mark AMV_Q_Weights_tsc - - - - - - Static
Weight of height assignment consistency test in final quality
mark
AMV_Q_Weights_hac - - - - - - Static
Weights of intermediate temporal vector tests in final product N_Gen_AQC_Weights_tc - Static
Weights of intermediate temporal direction tests in final
product
N_Gen_AQC_Weights_tdc - Static
Weights of intermediate image correlation tests in final product N_Gen_AQC_Weights_tha - Static

<!-- source_page: 121 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 122 of 298

STATIC APPLICATION DATA (PER CHANNEL USED FOR AMV PROCESSING)
Parameter Mnemonic Units Min Max Prec Acc Res Source
Weights of intermediate temporal pressure tests in final product N_Gen_AQC_Weights_tpc - Static
Weights of intermediate temporal speed tests in final product N_Gen_AQC_Weights_tsc - Static
AMV Verification vector set-up parameter pr_vec hPa 0 10 1 1 - Static
AMV Verification pressure set-up parameter pr_pres hPa 0 1100 1 1 - Static
AMV Verification temperature set-up parameter pr_temp K 0 100 1 1 - Static
Parameter to indicate whether CLA quality is to be used AMV_use_CLA_quality - - - - - - Static
Width of bands for mean and SD calculation AMV_merge_pressure hPa 0 100 1 1 - Static
Maximum number of cloudy pixels allowed in CS target CS_max_cloud_pix pixels 1 2 32-1 1 1 pixel Static
Percentage of surface scene type which must be present in a
suitable target
tar_sel_bckg_frac % 0 100 1 1 target
area
Static
Maximum difference allowed between repeat cycles for
primary targets
max_ptarget_age minute
s
0 360 1 1 - Static
Minimum number of intermediate AMVs to be used for
deriving the final AMV vector
min_derivations - 0 10 1 1 - Static
Set-up parameters for AMV AQC temporal test search area A1 - 0 1000 0.01 0.01 - Static
A2 - 0 1000 0.01 0.01 - Static
B1 - 0 1000 0.01 0.01 - Static
B2 - 0 1000 0.01 0.01 - Static
A1_p - 0 1000 0.01 0.01 - Static
A2_p - 0 1000 0.01 0.01 - Static
B1_p - 0 1000 0.01 0.01 - Static
B2_p - 0 1000 0.01 0.01 - Static
prev_gen_pp hPa 0 1000 1 1 - Static

<!-- source_page: 122 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 123 of 298

STATIC APPLICATION DATA (PER CHANNEL USED FOR AMV PROCESSING)
Parameter Mnemonic Units Min Max Prec Acc Res Source
Speed threshold for low-quality winds speed_threshold m/s 0 1000 1 1 - Static
Pressure threshold for low-level winds low_level_pressure_
threshold
hPa 0 1000 1 1 - Static
Table 27: AMV Product Static Application Data (per channel used for AMV processing)
STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Minimum number of consecutive neighbouring
cloud-free pixels inside the sampling window
n_clear pixels 1 25 1 1 pixel Static
Maximum time difference between image data and
oldest upgrading of the cloud-free radiance data set
dif_time_cfr Hours 0 24 0.25 0.25 - Static
Minimum distance (in km) to coast lines dist_coast km 0 100 1 1 - Static
Number of interpolation points in the pressure domain m_levels - 1 1000 1 1 - Static
Number of image lines of the target sampling window Ibox - 1 96 1 1 pixel Static
Number of image columns of the target sampling
window
Jbox - 1 96 1 1 pixel Static
Default number of image columns to move the sampling
window inside the target
Jstep - 1 15 1 1 pixel Static
Default number of image lines to move the sampling
window inside the target
Istep - 1 15 1 1 pixel Static
Minimum number of consecutive neighbouring cloudy
pixels inside the sampling window
n_cloud pixels 1 25 1 1 pixel Static
Flag for representative radiances of cloud classes iflag_cloud_cla ss - 0 1 - - - Static
Flag for representative radiances of cloud-free classes iflag_clear_class - 0 1 - - - Static

<!-- source_page: 123 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 124 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Minimum fraction of the target area occupied by the
cloud-free pixels
t_clear % 0 100 1 1 target
area
Static
Minimum fraction of sampled cloudy pixels inside the
target to process class
f_class % 0 100 1 1 target
area
Static
Flag for averaging cloudy radiances inside the sampling
window
iflag_cloudy - 0 1 - - - Static
Flag for averaging clear radiances inside the sampling
window
iflag_clear - 0 1 - - - Static
Flags for setting the mechanism to select valid samples
used for the regression analysis
iflag_dif_IRWV
iflag_snr_IRWV
iflag_lsd_IRWV
-
-
-
0
0
0
1
1
1
-
-
-
-
-
-
-
-
-
Static
Maximum fraction of cloudy pixels for weighted mean
radiance inside sampling window
f_sample % 0 100 1 1 sampling
window
Static
Max. fraction of cloud-free pixels for weighted mean
radiance inside sampling window
f_clear % 0 100 1 1 sampling
window
Static
Noise Equivalent Radiance (NER) of channel IR10.8
@Tref=300 K
nedr_ir10.8 mWm-2sr-1(cm-1)-1 0 2 0.001 0.001 - Static
Noise Equivalent Radiance (NER) of channel IR12.0
@Tref=300 K
nedr_ir12.0 mWm -2sr-1(cm-1)-1 0 3 0.001 0.001 - Static
Noise Equivalent Radiance (NER) of channel IR13.4
@Tref=250 K
nedr_ir13.4 mWm-2sr-1(cm-1)-1 0 10 0.001 0.001 - Static
Noise Equivalent Radiance (NER) of channel WV6.2
@Tref=250 K
nedr_wv6.2 mWm -2sr-1(cm-1)-1 0 1 0.001 0.001 - Static

<!-- source_page: 124 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 125 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Noise Equivalent Radiance (NER) of channel WV7.3
@Tref=250 K
nedr_wv7.3 mWm-2sr-1(cm-1)-1 0 1 0.001 0.001 - Static
Weight for Semi-Transparency Correction with IR10.8
+ WV6.2
iflag_iSTC_wv6.2 - 0 1 - - - Static
Weight for Semi-Transparency Correction with IR10.8
+ WV7.3
iflag_iSTC_wv7.3 - 0 1 - - - Static
Weight for IR/WV Ratioing with IR10.8 + WV6.2 iflag_iIRWV_wv6.2 - 0 1 - - - Static
Weight for IR/WV Ratioing with IR10.8 + WV7.3 iflag_iIRWV_wv7.3 - 0 1 - - - Static
Weight for IR/WV Two Channel Ratioing with
IR10.8+WV6.2+ WV7.3 using cloud class
representative radiances
iflag_iIRWV_2wv_rr - 0 1 - - - Static
Weight for IR/WV Two Channel Ratioing with
IR10.8+WV6.2+ WV7.3 using sample radiances
iflag_iIRWV_2wv_sr - 0 1 - - - Static
Weight for CO2 Absorption Method with
IR13.4+IR10.8 using cloud class representative
radiances
iflag_iCO2ABS_ir10.8_rr - 0 1 - - - Static
Weight for CO2 Absorption Method with
IR13.4+IR10.8 using sample radiances and arithmetic
averaging
iflag_iCO2ABS_ir10.8_sr_
arithmt
- 0 1 - - - Static
Weight for CO2 Absorption Method with
IR13.4+IR10.8 using sample radiances and histogram
analysis
iflag_iCO2ABS_ir10.8_sr_
histgrm
- 0 1 - - - Static
Weight for CO2 Absorption Method with
IR13.4+IR10.8 using sample radiances and cumulative
histogram analysis
iflag_iCO2ABS_ir10.8_sr_
cumhist
- 0 1 - - - Static

<!-- source_page: 125 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 126 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Weight for CO2 Absorption Method with
IR13.4+IR12.0 using cloud class representative
radiances
iflag_iCO2ABS_ir12.0_rr - 0 1 - - - Static
Weight for CO2 Absorption Method with
IR13.4+IR12.0 using sample radiances and arithmetic
averaging
iflag_iCO2ABS_ir12.0_sr_
arithmt
- 0 1 - - - Static
Weight for CO2 Absorption Method with
IR13.4+IR12.0 using sample radiances and histogram
analysis
iflag_iCO2ABS_ir12.0_sr_
histgrm
- 0 1 - - - Static
Weight for CO2 Absorption Method with
IR13.4+IR12.0 using sample radiances and cumulative
histogram analysis
iflag_iCO2ABS_ir12.0_sr_
cumhist
- 0 1 - - - Static
Weight for CO2 Absorption Method with IR13.4-
+IR10.8+IR12.0 using cloud class representative
radiances
iflag_iCO2ABS_irwv_rr - 0 1 - - - Static
Weight for CO2 Absorption Method with IR13.4-
+IR10.8+IR12.0 using sample radiances and arithmetic
averaging
iflag_iCO2ABS_irwv_sr_ar
ithmt
- 0 1 - - - Static
Weight for CO2 Absorption Method with IR13.4-
+IR10.8+IR12.0 using sample radiances and histogram
analysis
iflag_iCO2ABS_irwv_sr_hi
stgrm
- 0 1 - - - Static
Weight for CO2 Absorption Method with IR13.4-
+IR10.8+IR12.0 using sample radiances and cumulative
histogram analysis
iflag_iCO2ABS_irwv_sr_cu
mhist
- 0 1 - - - Static
Weight for Clear-sky EBBT height assignment method iflag_ClearSky_EBBT - 0 1 - - - Static

<!-- source_page: 126 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 127 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Weight for Clear-sky maximum NTC height assignment
method
iflag_ClearSky_MaxNTC - 0 1 - - - Static
Weight for Clear-sky NTCC HL height assignment
method
iflag_ClearSky_NTCC_HL - 0 1 - - - Static
Weight for Clear-sky NTCC LL height assignment
method
iflag_ClearSky_NTCC_LL - 0 1 - - - Static
Minimum relative humidity for good chance of clouds rh_crit % 0 100 1 1 - Static
Maximum pressure difference between cloud top and
top of boundary layer
dp_BL hPa 0 1000 10 10 - Static
Minimum pressure at top of boundary layer p_crit_bl hPa 0 1000 10 10 - Static
Maximum. pressure difference between surface and
cloud top
dp_SUF hPa 0 1000 10 10 - Static
Cloud base pressure threshold Pcbpt hPa 0 1000 10 10 - Static
Pressure scaling factor Psc_10.8 hPa 0 1000 10 10 - Static
Amplitude factor of the correction (for pressure at cloud
base)
K_10.8 - 0 10 0.1 0.1 - Static
Pressure scaling factor Psc_12.0 hPa 0 1000 1 1 - Static
Amplitude factor of the correction (for pressure at cloud
base)
K_12.0 - 0 10 0.1 0.1 - Static
Flag for critical parameter to Semi-Transparency
Correction
iflag_out_STC - 0 1 - - - Static
Minimum SNR of contrast in WV6.2, in Semi-
Transparency Correction
snr_crit_wv6.2_STC - 0 1000 1 1 - Static

<!-- source_page: 127 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 128 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Minimum SNR of contrast in WV7.3, in Semi-
Transparency Correction
snr_crit_wv7.3_STC - 0 1000 1 1 - Static
Minimum SNR of contrast in IR10.8, in Semi-
Transparency Correction
snr_crit_ir10.8_STC - 0 1000 1 1 - Static
Minimum contrast of WV6.2, in Semi-Transparency
Correction
dif_crit_wv6.2_STC - 0 100 1 1 - Static
Minimum contrast of WV7.3, in Semi-Transparency
Correction
dif_crit_wv7.3_STC - 0 100 1 1 - Static
Minimum contrast of IR10.8, in Semi-Transparency
Correction
dif_crit_ir10.8_STC - 0 100 1 1 - Static
Flag for critical parameter in IR/WV Ratioing iflag_out_IRWV - 0 1 - - - Static
Minimum SNR of contrast in WV6.2, in IR/WV
Ratioing
snr_crit_wv6.2_IRWV - 0 1000 1 1 - Static
Minimum SNR of contrast in WV7.3, in IR/WV
Ratioing
snr_crit_wv7.3_IRWV - 0 1000 1 1 - Static
Minimum SNR of contrast in IR10.8, in IR/WV
Ratioing
snr_crit_ir10.8_IRWV - 0 1000 1 1 - Static
Minimum contrast of samples in WV6.2, in IR/WV
Ratioing
dif_crit_wv6.2_IRWV - 0 100 1 1 - Static
Minimum contrast of samples in WV7.3, in IR/WV
Ratioing
dif_crit_wv7.3_IRWV - 0 100 1 1 - Static
Minimum contrast of samples in IR10.8, in IR/WV
Ratioing
dif_crit_ir10.8_IRWV - 0 100 1 1 - Static

<!-- source_page: 128 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 129 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Minimum local SD of samples in WV6.2, in IR/WV
Ratioing
lsd_crit_wv6.2_IRWV - 0 - 1 1 - Static
Minimum local SD of samples in WV7.3, in IR/WV
Ratioing
lsd_crit_wv7.3_IRWV - 0 - 1 1 - Static
Minimum local SD of samples in IR10.8, in IR/WV
Ratioing
lsd_crit_ir10.8_IRWV - 0 - 1 1 - Static
contrast in WV6.2, in IR/WV Ratioing dif_cont_wv6.2_IRWV - 0 100 1 1 - Static
contrast in WV7.3, in IR/WV Ratioing dif_cont_wv7.3_IRWV - 0 100 1 1 - Static
contrast in IR10.8, in IR/WV Ratioing dif_cont_ir10.8_IRWV - 0 100 1 1 - Static
Minimum fraction of valid samples of target sampling
window in IR/WV Ratioing
f_crit_samples_IRWV % 0 100 1 1 sampling
window
Static
Proportion of pixels required for merged IR/WV f_crit_pixels_IRWV % 0 100 1 1 - Static
Minimum number of pixels for merged IR/WV n_crit_merged_IRWV - 0 - 1 1 - Static
Critical correlation coefficient in IR/WV ratioing crit_corr_IRWV - 0 1 - - - Static
Flag for critical parameters in IR/WV Two Channel
Ratioing
iflag_out_2WV - 0 1 - - - Static
Confidence for different slopes, in IR/WV Two Channel
Ratioing
conf_dif_slopes_2WV % 0 100 1 1 - Static
Critical ratio of slopes, in IR/WV Two Channel Ratioing crit_rat_2WV - 0 1 0.01 0.01 - Static
Minimum fraction of valid samples of target sampling
window in IR/WV Two Channel Ratioing
f_crit_samples_2WV % 0 100 1 1 sampling
window
Static
Minimum SNR of IR13.4 contrast, in CO2 Absorption
Method
snr_crit_ir13.4_CO2ABS - 0 100 1 1 - Static

<!-- source_page: 129 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 130 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Minimum SNR of IR10.8 contrast, in CO2 Absorption
Method
snr_crit_ir10.8_CO2ABS - 0 100 1 1 - Static
Minimum SNR of IR12.0 contrast, in CO2 Absorption
Method
snr_crit_ir12.0_CO2ABS - 0 100 1 1 - Static
Minimum contrast of samples in IR13.4, in CO2
Absorption Method
dif_crit_ir13.4_ CO2ABS - 0 100 1 1 - Static
Minimum contrast of samples in IR10.8, in CO2
Absorption Method
dif_crit_ir10.8_ CO2ABS - 0 100 1 1 - Static
Minimum contrast of samples in IR12.0, in CO2
Absorption Method
dif_crit_ir12.0_ CO2ABS - 0 100 1 1 - Static
Minimum fraction of valid samples of target sampling
window in CO2 Absorption Method
f_crit_samples_CO2ABS % 0 100 1 1 - Static
Histogram smoothing factor his_smoothing_factor hPa 0 1000 1 1 - Static
Minimum number of sampled CO2 pressures to be used his_min_n_samples - 0 10000 1 1 sampling
window
Static
Minimum inflexion CO2 his_min_infl_slope - 0 1 0.001 0.001 - Static
Width of pressure histogram bins for analysis of
sampled CO2 pressures
his_bin_width hPa 0 1000 1 1 - Static
Offset i(1) in CO2 sampled pressure histogram analysis his_i1 hPa 0 1000 1 1 - Static
Offset i(2) in CO2 sampled pressure histogram analysis his_i2 hPa 0 1000 1 1 - Static
Offset i(3) in CO2 sampled pressure histogram analysis his_i3 hPa 0 1000 1 1 - Static
Offset j(1) in CO2 sampled pressure histogram analysis his_j1 hPa 0 1000 1 1 - Static
Offset j(2) in CO2 sampled pressure histogram analysis his_j2 hPa 0 1000 1 1 - Static
Offset j(3) in CO2 sampled pressure histogram analysis his_j3 hPa 0 1000 1 1 - Static

<!-- source_page: 130 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 131 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Offset k(1) in CO2 sampled pressure histogram analysis his_k1 hPa 0 1000 1 1 - Static
Offset k(2) in CO2 sampled pressure histogram analysis his_k2 hPa 0 1000 1 1 - Static
Offset k(3) in CO2 sampled pressure histogram analysis his_k3 hPa 0 1000 1 1 - Static
Window width for analysis of CO2 sampled pressures his_win_width hPa 0 1000 1 1 - Static
Minimum pressure to start the analysis of the sampled
CO2 pressures
his_min_pressure hPa 0 1000 1 1 - Static
Step size in CO2 pressure histogram analysis his_win_step hPa 1 50 1 1 - Static
Minimum RTM radiance contrast for lowest level crit_con_rtm_13.4 - 0 100 1 1 - Static
Minimum RTM radiance contrast for lowest level crit_con_rtm_12.0 - 0 100 1 1 - Static
Minimum RTM radiance contrast for lowest level crit_con_rtm_10.8 - 0 100 1 1 - Static
Standard error of cloud-free outgoing radiance in
channel x
sigma_rsuf (x) mWm -2sr-1(cm-1)-1 -5 5 0.001 0.001 - Static
Standard error of black cloud outgoing radiance in
channel x at level Pc
sigma_rbcd (x) mWm-2sr-1(cm-1)-1 -5 5 0.001 0.001 - Static
Pressure threshold for applying the Inversion Height
Assignment
inv_height_thres - Static
Minimum pressure difference between surface and
bottom of inversion layer
inv_surface_offset - Static
Minimum pressure (highest level) for bottom of
inversion layer
inv_pressure_thres - Static
Minimum strength of temperature inversion, i.e.
minimum temperature difference between top and
bottom of inversion layer
inv_magnitude_thres - Static

<!-- source_page: 131 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 132 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Atmospheric level to start the search for temperature
inversion layers
start_pressure - Static
Parameters in the derivation of the inversion height
assignment
inv_c1 - Static
inv_c2 - Static
inv_c3 - Static
Thresholds for the NTCC to derive the three single level
heights in clear sky areas
NTCC_LL
NTCC_N
NTCC_HL
-
-
-
0
0
0
100
100
100
0.001
0.001
0.001
0.0001
0.0001
0.0001
-
-
-
Static
Threshold in derivation of clear-sky height standard
deviation according to NTCC_N method
NTCC_threshold 0.01 0.5 - - - Static
Threshold in derivation of clear-sky height standard
deviation according to MaxNTC method
NTC_threshold - 0.5 1.0 - - - Static
Fraction of coldest pixels to be used for clear-sky EBBT
height assignment
frac_cs_ebbt % 0 100 1 1 target
area
Static
Minimum fraction of clear-sky pixels in a clear-sky
target
min_cs_fraction % 0 100 1 1 target
area

Flag indicating use of sequential height assignment iflag_sequence_ha - 0 1 - - - Static
Temperature threshold for the CO2 method in sequential
height assignment
temp_thresh_co2 K 0 1000 - - - Static
Pressure threshold for the IR/WV method in sequential
height assignment
height_thresh_irwv hPa 0 1000 - - - Static
Pressure threshold for the STC method in sequential
height assignment
height_thresh_stc hPa 0 1000 - - - Static

<!-- source_page: 132 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 133 of 298

STATIC APPLICATION DATA FOR HEIGHT ASSIGNMENT
Parameter Mnemonic Units Min Max Prec Acc Res Source
Temperature threshold for the STC 6_2 method in
sequential height assignment
temp_thresh_stc6_2 K 0 1000 - - - Static
Temperature threshold for the STC 7_3 method in
sequential height assignment
temp_thresh_stc7_3 K 0 1000 - - - Static
Temperature threshold for the IRWV 6_2 method in
sequential height assignment
temp_thresh_irwv6_2 K 0 1000 - - - Static
Temperature threshold for the IRWV 7_3 method in
sequential height assignment
temp_thresh_irwv7_3 K 0 1000 - - - Static
Critical correlation coefficient for IRWV regression
analysis
crit_corr_IRWV_1 - 0 1 - - - Static
Critical correlation coefficient for IRWV regression
analysis
crit_corr_IRWV_2 - 0 1 - - - Static
Table 28: AMV Product: Static Application Data for Height Assignment

STATIC APPLICATION DATA FOR RECURSIVE FILTER FUNCTION
Parameter Mnemonic Units Min Max Prec Acc Res Source
Analysis field latitude interval rff_delta_lat degrees 1 10 1 1 - Static
Analysis field longitude interval rff_delta_lon degrees 1 10 1 1 - Static
Forecast field pseudo latitude interval rff_pseudo_density_lat degrees 1 10 1 1 - Static
Forecast field pseudo longitude interval rff_pseudo_density_lon degrees 1 10 1 1 - Static
Apply stagger to forecast field longitude sampling rff_stagger - No Yes - - - Static
Height re-adjustment best fit weight in direction rff_weight_direction - 1 10000 - - - Static
Height re-adjustment best fit weight in pressure rff_weight_pressure - 1 10000 - - - Static

<!-- source_page: 133 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 134 of 298

STATIC APPLICATION DATA FOR RECURSIVE FILTER FUNCTION
Parameter Mnemonic Units Min Max Prec Acc Res Source
Height re-adjustment best fit weight in speed rff_weight_speed - 1 10000 - - - Static
Height re-adjustment best fit weight in temperature rff_weight_temp - 1 10000 - - - Static
Height re-adjustment best fit weight in velocity rff_weight_velocity - 1 10000 - - - Static
Initial First Pass Dimensionality of Analysis rff_initial_firstpass_dim - 1 3 - - - Static
Initial First Pass forecast weight rff_initial_firstpass_fc_ weight - 0 1 - - - Static
Initial First Pass No. of Iterations rff_initial _firstpass_no_ iterations - 1 10 - - - Static
Initial First Pass No. of Smoothing Passes rff_initial_firstpass_no_
smoothing_passes
- 1 10 - - - Static
Initial First Pass Quality Exponent rff_initial_firstpass_quality_exp - 1 10.0 - - - Static
Initial First Pass Radius of Influence rff_initial_firstpass_radius_influence km 1 1000 - - - Static
Initial First Pass Radius Scale Factor rff_initial_firstpass_radius_scale_factor - 1 100 - - - Static
Initial First Pass Control Fit of Analysis to Data rff_initial_firstpass_rf - 0.0 1.0 - - - Static
Initial First Pass Error Tolerance rff_initial_f irstpass_ tolerance m/s 0 10000 - - - Static
Initial First Pass Vertical Coupling rff_initial_firstpass_vert_ coup km 1 1000 - - - Static
Initial Second Pass Dimensionality of Analysis rff_initial_secondpass_dim - 1 3 - - - Static
Initial Second Pass forecast weight rff_initial_secondpass_fc_ weight - 0 1 - - - Static
Initial Second Pass No. of Iterations rff_initial_secondpass_no_
iterations
- 1 10 - - - Static
Initial Second Pass No. of Smoothing Passes rff_initial_secondpass_no_
smoothing_passes
- 1 10 - - - Static
Initial Second Pass Quality Exponent rff_initial_secondpass_
quality_exp
- 1 10.0 - - - Static

<!-- source_page: 134 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 135 of 298

STATIC APPLICATION DATA FOR RECURSIVE FILTER FUNCTION
Parameter Mnemonic Units Min Max Prec Acc Res Source
Initial Second Pass Radius of Influence rff_initial_secondpass_
radius_influence
km 1 1000 - - - Static
Initial Second Pass Radius Scale Factor rff_initial_secondpass_
radius_scale_factor
- 1 100 - - - Static
Initial Second Pass Control Fit of Analysis to Data rff_initial_secondpass_rf - 0.0 1.0 - - - Static
Initial Second Pass Error Tolerance rff_initial _secondpass_ tolerance m/s 0 10000 - - - Static
Initial Second Pass Vertical Coupling rff_initial_secondpass_ vert_ coup km 1 1000 - - - Static
Main Analysis Dimensionality of Analysis rff_ main _dim - 1 3 - - - Static
Main Analysis forecast weight rff_ main _fc_ weight - 0 1 - - - Static
Main Analysis No. of Iterations rff_ main _no_ iterations - 1 10 - - - Static
Main Analysis No. of Smoothing Passes rff_ main _no_ smoothing_passes - 1 10 - - - Static
Main Analysis Quality Exponent rff_ main _quality_exp - 1 10.0 - - - Static
Main Analysis Radius of Influence rff_ main _radius_influence km 1 1000 - - - Static
Main Analysis Radius Scale Factor rff_main _radius_ scale_factor - 1 100 - - - Static
Main Analysis Control Fit of Analysis to Data rff_ main _rf - 0.0 1.0 - - - Static
Main Analysis Error Tolerance rff_ ma in _ tolerance m/s 0 10000 - - - Static
Main Analysis Vertical Coupling rff_ main _vert_ coup km 1 1000 - - - Static
Final Analysis Dimensionality of Analysis rff_ final_dim - 1 3 - - - Static
Final Analysis forecast weight rff_ final _fc_ weight - 0 1 - - - Static
Final Analysis No. of Iterations rff_ final _no_ iterations - 1 10 - - - Static
Final Analysis No. of Smoothing Passes rff_ final _no_ smoothing_passes - 1 10 - - - Static
Final Analysis Quality Exponent rff_ final _quality_e xp - 1 10.0 - - - Static

<!-- source_page: 135 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 136 of 298

STATIC APPLICATION DATA FOR RECURSIVE FILTER FUNCTION
Parameter Mnemonic Units Min Max Prec Acc Res Source
Final Analysis Radius of Influence rff_ final _radius_influence km 1 1000 - - - Static
Final Analysis Radius Scale Factor rff_ fina l _radius_ scale_factor - 1 100 - - - Static
Final Analysis Control Fit of Analysis to Data rff_ final _rf - 0.0 1.0 - - - Static
Final Analysis Error Tolerance rff_ fi nal _ tolerance m/s 0 10000 - - - Static
Final Analysis Vertical Coupling rff_ final _vert_ coup km 1 1000 - - - Static
Table 29: AMV Product: Static application data for recursive filter function

<!-- source_page: 136 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 137 of 298

STATIC APPLICATION DATA FOR ENCODING FILTER (PER CHANNEL)
Parameter Mnemonic Units Min Max Prec Acc Res Source
Minimum average forecast consistency qual_forecast % 0 100 - - - Static
Minimum number of AMVs with QI (exFC) > qual_qi qual_num_good - 0 - - - Static
Maximum number of AMVs with pressure < qual_pressure qual_num_high - 0 - - - Static
Pressure threshold for qual_num_high qual_pressure hPa 0 - - - Static
Quality threshold for qual_num_good qual_qi % 0 100 - - - Static
Minimum average vector consistency qual_vector % 0 100 - - - Static
Minimum proportion of AMVs with QI (exFC) > qual_qi related to
total for channel. For HRV and VIS only low levels are considered.
qual_proportion % 0 100 Static
Table 30: AMV Product: Static application for encoding filter
STATIC APPLICATION DATA FOR AMV AVERAGING
Parameter Mnemonic Units Min Max Prec Acc Res Source
Maximum pressure difference between different
intermediate vector heights
max_pres_diff hPa 0 200 - - - Static
Maximum direction difference between different
intermediate vector heights
max_dir_diff ° 0 360 - - - Static
Maximum speed difference between different
intermediate vector heights
max_speed_diff m/s 0 - - - Static
Table 31: AMV Product: Static application data for AMV averaging

<!-- source_page: 137 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.3 Algorithm Functional Specification
9.3.1 Overview
The following steps shall be performed in order to derive one single displacement vector for one
channel for the intermediate AMV product. These are described in more detail in the following
sections:
1. Target selection
2. Image data preparation
3. Image enhancement
4. Derivation of target displacement
5. Height assignment
This algorithm initially derives the Atmospheric Motion Vectors intermediate product for three out of
every four repeat cycles for all specified channels over the processing area.
It shall extract all possible targets within each image and find the position of the same targets in the
following image. The primary targets shall be centralised around the locations of the end position of
the successfully tracked targets from the previous cycle. It shall additionally complement these targets
with new targets extracted by the target selection scheme. Only targets with a quality higher than
first_cycle_min_qi (nominally 0)–in the case that the target has been tracked only over one cycle, or
new_cycle_min_qi (nominally 0)–in the case that the target has been tracked over two or more cycles,
shall
be kept for further processing. The target selection will be initialised on an equidistant grid
specified by grid_distance.
The target position shall be optimised within the target search area to gain maximum contrast within
the target area. Specific targets shall be enhanced to increase contrast with respect to lower level
scenes. The vectors successfully extracted with cloud targets shall be assigned a height corresponding
to the temperature at which the cloud is radiating. The other vectors shall be assigned a height related
to a representative layer of the displacement.
Finally, all vectors shall be subjected to an Automatic Quality Control (AQC) for both the
intermediate and final products where appropriate. The information derived from a single repeat cycle
shall be an intermediate product.
The final AMV product shall be generated at scheduled times. It shall be based on intermediate AMV
products, where the number of intermediate products which shall be used is specified by the set-up
parameter N_Gen which is nominally three (3).
In the nominal case, intermediate products are generated with time stamps of 15, 30 and 45 minutes
into the synoptic hour. The final product is generated with a time stamp of 45 minutes into the
synoptic hour. This means that, for example, for the 15-minute time stamp intermediate product, each
target is selected from the image data (scan) starting at 0 minutes. The target displacement is extracted
from the image data (scan) starting at 15 minutes into the synoptic hour. Then everything is shifted
forward one repeat cycle for the next intermediate product. No intermediate products are generated at
the 0-minute synoptic time. In effect, four images are used each hour to generate three intermediate
products and a final product. The Rapid Scanning Service (RSS) similarly uses three intermediate
products to form a final product three times an hour, with time stamps of 15, 35 and 55 minutes into
the synoptic hour. The AMV processing flow is shown graphically in Figure 6. The target
optimisation, being a complex process, is shown separately in Figure 7.

<!-- source_page: 138 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




.

Initialize
New Cycle
Get Setup data
Get previous cycle data
Get grid point image
& Stat. data
Extract new
targets
Target optimisation
valid target
Image Enhancement
Matching
Height Assignment
Extr. Product
AQC
Create product
Disseminate
Yes
Yes
Combine vector fields
Yes
No
No
No

Figure 6: AMV Processing

<!-- source_page: 139 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





Retrieve local mean & Sd
Extract max and min local
mean, max Sd.
Valid location
Enough cloudy pixels
Enough pixels
with large SD
Extract contrast
Extract Entropy
New maximum
Store location
Last optimisation point
Valid cloud tracer
Clear Sky
Tracer?
Yes
Yes
Yes
Yes
Yes
Yes
Retrieve local mean & Sd
Extract max and min local
mean, max Sd.
Valid location
Enough Clear sky pixels
Enough pixels
with large SD
Extract contrast
Extract Entropy
New maximum
Store location
Last optimisation point
Valid Clear Sky tracer
Yes
Yes
Yes
Yes
Yes
Yes
Yes
No valid tracer found
Flag location as non valid
No
No
No
No
No
No
No
No
No
No
No
No
No

Figure 7: AMV Processing - Target Optimisation

<!-- source_page: 140 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.3.2 Algorithm Description
9.3.2.1 Target Selection
The main inputs for the target selection are the image data in all the specified channels and the scenes
type provided by Scenes Analysis. Further inputs are set-up parameters controlling the actual selection
procedure and the vectors derived during the previous cycle.
The target size shall be specified separately for each channel and target type by Cl_tar_size
(nominally 24 and for HRVIS 32) and CS_tar_size (nominally 32). Two types of targets shall be used
to derive the baseline products: clouds and moisture features. The use of ozone targets shall be
foreseen as a Future Enhancement. The targets shall be extracted in two separate steps. The primary
targets shall be the targets extracted from the previous extraction cycle so that the target position will
be located at the best position indicated by the matching surface (in the case of cross correlation at the
maximum correlation value). Primary targets shall only be valid if they are derived from a repeat
cycle within max_ptarget_age of the current repeat cycle. In addition, primary targets for VIS and
HRVIS channels shall only be valid for solar zenith angles less than (nominally) 87 degrees.
The secondary targets shall be extracted at an equidistant grid specified grid_distance (nominally 24
and for HRVIS 32). The search for the optimum secondary target in the vicinity of each grid point
shall be limited to an optimisation area and it shall also take into account the positions of the already
identified targets. This shall be controlled by tar_opt_area (nominally 48 and for HRVIS 64), which
defines the optimisation area size and max_tar_overlap (nominally 288) which defines the acceptable
target overlap in total pixels. Secondary targets for VIS and HRVIS channels shall only be valid for
solar zenith angles less than (nominally) 87 degrees.
The concept of target and search areas is shown in Figure 8.

<!-- source_page: 141 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Cloud
Image 1
Optimised Target Area
Image 2
Cloud
Search Area
Vector

Figure 8: Target and Search Areas
The optimisation of the target position shall extract the location within the optimisation area at which
the contrast within the target area and/or entropy is maximised. Entropy (E) is defined as follows:
EP P i
i
N
i


1
2l o g

Equation 7

where Pi is the probability that a pixel has the value i.
This shall further be controlled with a selection based on the cumulative histogram of the local
standard deviation. The selection between maximum contrast and maximum entropy shall be selected
by setting tar_ex_met (nominally 1= maximum contrast).
The target optimisation process is illustrated graphically in Figure 9.

<!-- source_page: 142 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Cloud
Cloud
Specified Computation Grid
Original Location of Target Optimised Location of Target

Figure 9 Target Optimisation
The following steps shall be performed in order to find a suitable target:
1. Use Cl_tar_size
2. Retrieve local means and local standard deviations (computed over 3 × 3 pixels) for each
location in the target search area.
3. For all possible locations within the target search area: the primary target locations are defined
by the vector of the previous extraction having a quality greater than new_cycle_min_qi
(nominally 0.0).
4. Control that the current location is valid–the overlap with previously identified targets must be
less than max_tar_overlap. For each valid location, continue with steps 4 to 12. If the location
is invalid, skip to the next location.
5. a) In the case of Cl_tar_size, check the number of cloudy pixels for all locations. For the
water vapour channels, the definition of which cloud layers contribute to the final number of
cloudy pixels should be defined by wv_cloud_type (nominally 2 for WV6.2 and WV7.3).
The possible values of wv_cloud_type are = 0, 1, 2 and correspond to all cloud layers (0),
high cloud only (1), high and medium cloud only (2). For all other channels all cloud layers
contribute to the definition of the number of cloudy pixels. (If a pixel does not contribute to a
cloudy target, it will automatically be considered to contribute to a clear sky target.) If the
number of cloudy pixels in the location is less than min_tracer_size (nominally 50), skip to
next location.
b) In the case of CS_tar_size, the location shall
be skipped if it contains more than
CS_max_cloud_pix (nominally 50 for WV channels and -1 for other channels) cloud pixels.
The parameters are set to ensure that nominally clear sky targets can only be generated for
the water vapour channels.
6. Derive maximum local mean, minimum local mean, maximum local standard deviation, and
number of pixels with a local standard deviation greater than min_sd for each of these
possible target locations.
7. Check that more than min_num_high_sd number of pixels have a standard deviation larger
than min_sd.

<!-- source_page: 143 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8. Extract the contrast as the local standard deviation at the target centre.
9. Extract the entropy.
10. Find position of maximum contrast/entropy within the target optimisation area.
11. Check that the background location is valid. This shall be carried out using the
Surface_type_map. A set-up flag lcoast_flag is used to determine which location is valid. It
can take the following values:
0 = Any background is valid: land, sea or coast.
1 = Land or sea but no coastline, where e.g.

 fracbckgseltarlandpixelsofnumberseapixelsofnumber
landpixelsofnumberseapixelsofnumberMAX _______
__,__*100 
Equation 8

(tar_sel_bckg_frac nominally has a value of 100 %).
2 = Land only (set tar_sel_bckg_frac to a value of 100 %) or land/coastline (set
tar_sel_bckg_frac to a value of 0%).
3 = Sea only (set tar_sel_bckg_frac to a value of 100 %) or sea/coastline (set
tar_sel_bckg_frac to a value of 0 %).
4 = Coast only (set tar_sel_bckg_frac to a value of 100 %).
Number_of_seapixels and number_of_landpixels shall be determined from the static
land/sea-mask, where any pixel location containing sea or water is assigned to
number_of_seapixels. The nominal values for lcoast_flag and tar_sel_bckg_frac are 1 and
100 % respectively.
12. Determine the centre position of the target.
13. Compute the mean and standard deviation of all scenes for all channels within the target
area, using only the pixels within the target area.
14. If a successful optimum location was found then return. Use Cl_tar_size (nominally 24) and
Cl_sar_size for matching.
15. If no location contains enough cloudy pixels then if CS_tar_size is greater than zero,
re-compute steps 2 to 13 using CS_tar_size (and step 5b rather than 5a).
16. Compute the number of cloudy pixels for the final location. If the total number is greater
than min_tracer_size , skip return and identify the location with no valid target and proceed
to next grid point.
17. If the number of cloudy pixels is less than min_tracer_size then return. Use CS_tar_size and
CS_sar_size for matching.
The following four alternative target extraction schemes shall be implemented:
1. The primary targets are always used and are always complemented by the secondary targets.
2. The primary targets are always used and the secondary targets shall be extracted only from
the first image of a new generation cycle.
3. As 1) except no primary targets are extracted from the first image of a new generation cycle.
4. As 3) except secondary targets shall be extracted only from the first image of a new
generation cycle.

<!-- source_page: 144 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




It shall be possible to select the extraction scheme with the appropriate setting of tar_extraction
(nominally 4). The target optimisation will provide the position of the optimised target location for
the follow-on processes together with a flag stating the validity of the location. The target area and
search area of the matching shall
be centred at the location-optimised location.
9.3.2.2 Image Data Preparation
9.3.2.2.1 Introduction
The purpose of the Image Data Preparation task is to combine the information provided by CLA into
scenes relevant to the AMV. This is required at two stages of the overall processing:
a) Prior to Image Enhancement (see Section 9.3.2.3)
b) Prior to Height Assignment (see Section 9.3.2.5)
In item a), the image data preparation shall be performed after the target selection with the optimised
target. However, it will only be performed for those AMV channels in which image enhancement is
applied. Its aim is to provide the AMV Image Enhancement with suitable scene mean and standard
deviations derived from the target area (prior to target displacement).
In b) the image data preparation shall be performed after the derivation of target displacement, and
will be performed on the displaced target area (i.e. in the new target position) for all AMV channels.
The aim is to provide the AMV height assignment with relevant scenes derived from the displaced
target area.
The main inputs for the Image Data Preparation are the image data in all the specified channels, the
scenes type, and the additional cloud information from CLA. Further inputs are the set-up parameters
controlling the actual procedure.
There are two alternative schemes for Image Data Preparation which can be selected by a set-up
parameter AMV_use_dynamic_scenes. One separates the data into fixed bands (0) and the other uses a
dynamic clustering scheme based on histogram analysis (1). The nominal value for
AMV_use_dynamic_scenes is 0.
9.3.2.2.2 Cloud Clustering Based on Fixed Bands
For image data preparation prior to image enhancement, the process shall perform the following steps
for the AMV processing channel:
1. The process shall loop over all pixels within the target area. If AMV_use_CLA_quality is true
then only use pixels where the CLA quality is good, otherwise (nominal case) use all pixels. The
process shall compute the mean, standard deviation, and mean pressure for all channels of all
scenes containing pixels of the same cloud phase in bands of AMV_merge_pres hPa (nominally
200 hPa).
2. The process shall compare the computed means for all successfully classified scenes. Cloud
scenes shall not be compared to surface scenes. Identify the two scenes with the smallest mean
pressure difference. If the difference is smaller than min_scene_dist (nominally 2 hPa) the two
scenes shall be reclassified to provide a new combined scene type.
3. If a reclassification was performed in step 2, then re-compute the means and standard deviation of
the new reclassified scene and then go back to step 2.
4. Count the numbers of pixels belonging to each scene type. Only scene types containing more than
min_sce_size (nominally 20) pixels shall be considered to be valid.

<!-- source_page: 145 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




If the image data preparation has identified more than two valid cloud scenes, the two coldest cloud
scenes shall be extracted, with the remaining ones discarded.
All surface pixels are combined into a single surface scene and the mean and standard deviation
computed.
For image data preparation prior to height assignment, the above steps are carried out with the
following exceptions:
a) No means and standard deviations are calculated – the aim is to assign each pixel to a particular
scene.
b) All valid cloud scenes shall be used – there is no filtering to the two coldest cloud scenes.

9.3.2.2.3 Cloud Clustering Based on Histogram Analysis
Surface scenes shall be merged to create a single surface scene.
The clustering of cloud pixels shall be performed through an algorithm based on histogram analysis of
the cloud top height (as provided by the CLA algorithm). No distinction is made between cloud
phases.
A future enhancement shall be to consider separate histogram analyses of opaque and
semi-transparent scenes.
The total number of clustered scenes extracted by the clustering algorithm shall not exceed
n_cloud_clusters (nominally 6). The smallest clusters will be removed to achieve this end.
The cloudy pixels shall individually be assigned to one of n_hist_bin (nominally 100) histogram bins,
to provide a histogram of cloud top heights.
The histogram analysis shall be performed to detect peaks as follows:
 From the original histogram submitted to histogram analysis, a secondary ‘smoothed’ histogram
shall be constructed where each bin contains the average of three adjacent bins.
 For each histogram bin in the ‘smoothed’ histogram, two additional bins shall be selected at
offsets defined by set-up parameters hist_off_coeff1 (nominally 1) and hist_off_coeff2 (nominally
two).
 Three sets of offsets shall be defined: i(ii), j(ii),k(ii), ii=1,3 where nominally
i(1) = 0, j(1) = hist_off_coeff1, k(1) = hist_off_coeff2
i(2) = 0, j(2) = 2 × hist_off_coeff1, k(2) = 2 × hist_off_coeff2
i(3) = 0, j(3) = 3 × hist_off_coeff1, k(3) = 3 × hist_off_coeff2
 Using the values of the three selected bins (xi, xj and xk) and their corresponding frequencies of
occurrence (fi, fj and fk), for all cases in which the combined three-point frequency exceeds
hist_min_freq (nominally 5), the mean (x0), the standard deviation (σ) and the peak frequency (f0)
of the Gaussian curve that fits these values shall be calculated according to the following
formulae:

<!-- source_page: 146 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





x0 =
[xi
2 × log(fj/fk) - xj
2 × log(fi/fk) + xk
2 × logf(fi/fj)] / 2 × [xi × log(fj/fk) -
xj × log(fi/fk) + xk × logf(fi/fj)]
σ2 = [( x j- x0)2 - ( xi- x0)2] / 2 × log(fi/fj)
f0 = f i × exp(xi- x0)2/ 2σ2
Equation 9

 Where valid values of these quantities can be found, they shall be stored and x0 shall be assumed
to define a peak in the histogram.
 Once the entire ‘smoothed’ histogram has been processed, peaks (values of x0) that are detected
fewer than min_peak_occ (nominally 2) times shall be discarded unless no other peak has been
found.
 Peaks that are too close to each other (defined by the thresholds peak_mean_diff (nominally 2) and
peak_std_diff (nominally 2)) shall be merged together.
 For each peak found at least min_peak_occ times, average values of x0, σ and f0 shall be
calculated.
The peaks detected by the histogram analysis shall be assumed to correspond to particular clustered
scenes.
Pixel values for a particular clustered scene shall be assumed to conform to a normal distribution such
that the peaks detected by the histogram analysis shall be assumed to correspond to peak values of a
Gaussian curve. This means that for each cloud cluster, all contributing histogram bins are truncated to
ensure the individual bin frequencies lie under or on a Gaussian curve.
The clustered scenes extracted by the histogram analysis shall be characterised by the peak value, the
mean value and the standard deviation of the corresponding Gaussian curve.
If the number of pixels in the cluster is less than cluster_min_size (nominally 20), the cluster shall be
removed.
After performing the histogram analysis, individual pixels shall be assigned to the clustered scene that
has the nearest mean value. The assignment of pixels to clustered scenes shall be performed through a
number of iterations, limited by max_class_cycles (nominally 1), until no further reassignment is
required.
An individual pixel shall only be assigned to a clustered scene if it lies within three standard
deviations of the cluster mean value.
Pixels that cannot be assigned to a cluster shall be set to ‘unclassified’.
At each iteration in the assignment of pixels to clusters; the mean and standard deviation of each
cluster shall be re-calculated according to the values of the pixels that have been assigned to it.
At each iteration, if the number of pixels in the cluster is less than cluster_min_size, the cluster shall
be removed.
Prior to Image Enhancement
In the case of image data preparation prior to image enhancement, if there are more than two cloud
scenes left at the end of the cluster analysis, the two coldest scenes shall be extracted.

<!-- source_page: 147 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Prior to Height Assignment
For image data preparation prior to height assignment, a further check will be carried out to modify
(and filter out for WV channels) low-level scenes analysis as follows. If all cloud scenes have a (CLA
determined) mean pressure above low_level_pressure_threshold (nominally 600 hPa) then for WV
channel winds they will be ignored and the number of cloud scenes for the target shall be set to zero
(WV targets are not expected at these low levels), otherwise (for other channels) they are merged in
the following way. If there are fewer than three cloud scenes, all scenes are merged into a single scene.
If there are three or more scenes, all scenes excepting the warmest are merged into a single scene. All
cloud scenes left at the end of the analysis shall be retained. A flag shall be set to define the scenes
status of the target for use in the height assignment methodology: either undefined, low level, low
level (with merging), or medium-high level.
9.3.2.3 Image Enhancement
9.3.2.3.1 Introduction
The image enhancement shall use the image data extracted at the location around the optimised target
position and the scenes data output from the Image Data Preparation (see Section 9.3.2.2). The mean
count and standard deviation, as derived by the Image Data Preparation process, shall be applied
equally to the target and the search area.
The image enhancement shall be performed only for specific channels defined by l_enhance.
Nominally it shall not be used for any channel. The image enhancement shall increase the contrast
between the selected target and possible lower level surfaces. The image enhancement type will be
specified by the number of relevant scenes. The number of relevant scenes shall be defined as the sum
of the number of relevant cloud scenes and a maximum of one (the warmest) surface type.
The following methods shall be applied for enhancement of cloud tracers:
 In single scene cases: Pixel masking.
 In areas with two scenes: Linear or non-linear histogram enhancement.
 In multi-layered scenes (three or more scenes) the Spatial Coherence Method (SCM)
shall be applied.
The use of CLA information and histogram enhancement for image enhancement in cloud-free areas is
a Future Enhancement.
9.3.2.3.2 Single Scene Case
The target shall be specified by the scene limit counts which are defined by the following:

sceneofcountMeanC
whereclCC
andclCC
cl
clcl
clcl

,lim_
lim_
max
min






Equation 10

cl_lim is the scene limit factor and  is the standard deviation of the pixels belonging to the scene.
A given pixel of the target or search area shall be masked if its radiance (count value) is less than the
minimum limit count of the tracer Ccl
min or bigger than the maximum count C cl
max , otherwise it retains
its original value. The masking function shall be specified as the following:

<!-- source_page: 148 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




CC CC C
CC CC C T M C
d
cl cl
new
cl cl
new random
min max
min max,
  
   
Equation 11

where TM is a set-up parameter (0 or 1) and Crandom is a random value generated between Ccl
min and
C cl
max . If TM is 0 the pixel value = 0 and it shall not be used in the correlation computations.
The information about the number of masked pixels in the target area, the number of masked pixels in
the search area and the number of cloud layers shall be made available for the Automatic Quality
Control procedures.
9.3.2.3.3 Two Scene Case
If the target area contains two scenes the following transformation shall be performed:

CC C T M C
CC C C C
CC C C C CC
CC
CC C C
coldcl
new random
coldcl coldcl
new
coldcl warmcl
new
coldcl
coldcl CF
warmcl coldcl CF
warmcl
new
warmcl
  
  
    

 

min
min
()
() 1

Equation 12


where:


C mean count of the colder scene
C = mean count of the warmer scene
C C cl lim
standard deviation of cold scene
cl_ lim = scene limit factor
CF = contrast factor
C
coldcl
warmcl
min
coldcl coldcl
cold
cold
min
coldcl




_ 

CCrandom
warmcl


9.3.2.3.4 Multi-layered Scenes
THREE SCENES
The aim of the image filtering is to enhance the highest cloud tracer suitable for tracking in the target
area. The spatial coherence filtering shall be applied in cases with three scene types (that is, at least
two cloud layers) in a segment. The multispectral image analysis provides the mean counts ( C1, C2 and
C3) for the three scenes, but they shall be modified during the target selection procedure to represent a

<!-- source_page: 149 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




mean derived only from the cloud points present in the target area. At present a simple parabolic
function best suited to fit the arch-like relationship between local standard deviation (C) and local
mean count Clm(C) is used (Schmetz et al., 1993). Outside the two scenes Ci and Cj the arch shall be
set to 0; between the two scenes Ci and Cj the arch shall be described by the function:

)C-C(C)C-C(C
)C-C(
4-
= (C) j
m
i
m2ji
topij
)( )( 


Equation 13

where:
Cm(C) is the local mean value attributed to the pixel with the satellite radiance C
(C) is the local standard deviation attributed to the same pixel
top is the maximum standard deviation corresponding to the top of the arch

topij is parameterised as a piecewise linear function of the brightness-temperature difference T
between Ci and C j , which in a three-scene case shall be defined by:

)()( 1212 CTCTT 
)()( 1313 CTCTT 
)()( 2323 CTCTT 
and

TSCMTABSifLROSCMTLRFSCM
TSCMTABSifSROSCMTSRFSCM
ijij
top
ijij
top
ij
ij
_)(____
_)(____





Equation 14

where:
(i,j) = (1,2), (1,3) or (2,3)
T(Ci) = the temperature in kelvin attached to the average count of the scene Ci

and
SCM_RF_S = Regression factor for small temperature differences
SCM_RO_S = Regression offset for small temperature differences
SCM_RF_L = Regression factor for large temperature differences
SCM_RO_L = Regression offset for large temperature differences
SCM_T = Temperature threshold
which are given by the set-up configuration.

<!-- source_page: 150 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Principally, the image filtering shall project all counts into a basic radiometric range, defined as the
range between C1 and C3 . There shall be seven different cases identified, which are addressed
sequentially (case 0 to 6) and shall only be applied at the first valid occasion. These cases are, in the
order they shall be applied:


3
23
11
12
13
12
13
33
1
1
min
)()( :5
)()( :4
)()( :3
:2
:1
:0
CCCCcase
CCC
CC
CCCCCcase
CCCCcase
CCCCcase
CCCCcase
CTMCCCcase
new
new
new
new
new
randomnew












Equation 15

Case 6: For this case, the pixels are within the basic radiometric range between C1 and C3 and are
assumed to contain information from all three scenes. Here, in addition to scaling with fractional cloud
amount (which is the principal in case 4), a scaling with local standard deviations shall be performed:

2
23
2
12
2
13
11
12
13
13
13
'),()('
,'),()('
,)(')(
)(')(')(')(
)()(
CCCCCC
andCCCCCC
whereCCC
CCCCC
CC
CC
CC
CCCnew
























Equation 16

where (C) is the local standard deviation as computed over 3 × 3 pixels and ij(C) describes the arch
between the scenes i and j where (i,j) take the values (1,2), (1,3) and (2,3).
C1
min CCrandom
3
.

FOUR OR MORE SCENES
If the data preparation has identified more than three valid scenes for the target area, the results for the
two coldest clouds and the warmest surface scene as identified by the Image Data Preparation process
shall
be used. The image enhancement as described in the three-scenes case shall then be utilised.
9.3.2.3.5 Cloud-free Areas (WV and/or Ozone Tracers)
In the baseline set-up there is no enhancement of clear sky targets. The introduction of an image
enhancement for clear sky areas shall be foreseen as a Future Enhancement.

<!-- source_page: 151 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.3.2.4 Derivation of Target Displacement
9.3.2.4.1 Introduction
The derivation of the target displacement shall utilise the image data at locations centralised around
the locations provided by the target selection scheme. For the channels specified for image
enhancement the data shall be provided by the image enhancement scheme. The derivation of the
target displacement shall be performed for every obtained pair of consecutive images. It will be based
on the derivation of a matching surface derived by matching the selected target within the defined
search area in the next image. The matching shall be performed by a matching algorithm selected by
the parameter mm. The following three alternative matching methods shall be implemented as a
baseline: Cross Correlation (CC) in time domain, Sum of Squared Distances (SSD) and Cross
Correlation in the Fourier domain (CCF). Only one method will be used operationally as specified by
mm. It shall be possible to introduce additional matching methods.
The parameter mm can be used to specify separate tracking techniques for cloud and clear sky targets.
The set-up parameter options are:
1. cross-correlation spatial (CC) for all targets;
2. cross-correlation Fourier (CCF) for all targets;
3. Euclidean distance (SSD) for all targets;
4. CC for cloud and SSD for clear sky;
5. CCF for cloud and SSD for clear sky.
The nominal value is 2 for non-WV channels and 5 for WV channels.
9.3.2.4.2 Perform Matching
The matching process is the core of the AMV task. This is both from a mathematical point of view,
because it is the basic scheme retained for the measurement of the tracers displacement, and also from a
computational load point of view – it represents probably the most time-consuming operation of all the
meteorological products. For these reasons, a detailed mathematical definition is presented here, followed
by three alternative suggestions for implementing this operation.
a) Cross Correlation in the time domain
The correlation used for AMV extraction shall be based on the classical formula defining the correlation
coefficient CC between two random variables T and S:
 STST
E{S}E{T} - S}E{T = )}S - (S)T - E{(T = CC 




Equation 17


Assuming a square target size with a side length of NT, the total number of pixels used to compute one
correlation value is N = NT
2. If we identify the pixels within the target area with (i,j) and the target
location within the search area with (n,m), such that the target is always fully contained within the search
area, then T
i,j and Sn+i,m+j shall uniquely define pixel count values within the target and search areas. The
expression for the CC shall then be expanded by:

<!-- source_page: 152 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




E { T } = T = 1
N T
T
2
i=1
N
j=1
N
i, j
TT
 

Equation 18


E{S } = S = 1
N Sn,m n,m
T
2
i=1
N
j=1
N
n+i,m+ j
TT
 

Equation 19


STN
1 = }SE{T j+mi,+nji,
N
j=1
N
=1i
2
T
mn,
TT


Equation 20


T
T
2
i=1
N
j=1
N
i,j
2
S n,m
T
2
i=1
N
j=1
N
n+i,m+ j n,m
2
= 1
N (T - T )
= 1
N (S - S )
TT
TT







Equation 21

In order to improve the correlation quality, two actions shall be foreseen: first the enhancement of the
target area and the search area pixels. The second improvement is the introduction of masked pixels both
in the target and the search areas (see image enhancement). Masking a pixel means that this pixel shall be
completely ignored by the correlation, i.e. it doesn’t contribute to any of the above terms. As both the
target area and the search area contain masked pixels, only the pixels which are simultaneously not
masked in both areas shall contribute to the correlation. Therefore NT
2 has to be replaced by N, which is
the total number of pixels contributing to the correlation.
b) The Fast Fourier Transform implementation
Implementing convolutions or correlations in the frequency domain using Fast Fourier Transform
(FFT) is a classical solution for reducing the computational load. The larger the arrays having to be
correlated, filtered or convolved, the more efficiently these can be implemented. The problem in the
present case resides in the space variability of the correlated arrays, due to the masked pixels. This
implies an extra analysis of the problem in order to get a fast solution.
First, when considering the set of formulae defined in a), the following correlation products
(marked *), appear, where MT and MS are the masking functions:
H
] S)(MS*T)(MT [ = }SE{T
mn,
mn,
mn,


Equation 22

<!-- source_page: 153 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




E{T } = T = [ (MS)* (MT T) ]
H
n,m n,m
n,m
n,m


Equation 23


H
] (MT)*S)(MS [ = S = }E{S
mn,
mn,
mn,mn,


Equation 24


T n,m
2
n,m n,m
2
= E { T } -E { T}
Equation 25



Equation 26


Snm
2
n,m n,m
2
= E { S } -E { S},
Equation 27


=
[(MS S ) *( M T )]
H -
[(MS S)* (MT) ]
H
n,m
n,m
n,m
2
n,m
 2

Equation 28


and: H = [ M S*M T ]n,m n,m
Equation 29


These formulae can be completely rewritten using the partial convolutions H, A, B, C, D, E defined as
follows:

MT*S MS= E
MS*T MT= D
TMT*S MS= C
MT*S MS= B
MS*T MT= A
MS* MT= H
2
2






Equation 30

The correlation surface CC can then be expressed as a function of these arrays:

  /HB - E/HA - D
/HBA - C =CC
22 


Equation 31

<!-- source_page: 154 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The correlation surface shall be defined as a scalar combination of the elements of the six partial
correlations H, A, B, C, D and E. An algorithm implementing these partial convolutions in the
frequency domain shall
perform the following steps:
1. Generate and format the six basic arrays: MS, MT, MS.S, MT.T, MS.S2 and MT.T2.
2. Perform six two-dimensional FFTs on these arrays.
3. Perform six array multiplications in the frequency domain, in order to obtain the spectra of H,
A, B, C, D and E.
4. Perform six two-dimensional inverse FFTs, the result being the arrays H, A, B, C, D and E.
5. Compute the correlation surface array as a scalar combination of the partial convolution arrays.
This method shall deliver all the correlation coefficients in full resolution.
It shall be possible to define a low pass filtering function as specified by FFT_low to be applied to the
correlation coefficients for later improvements.
c) Sum of Squared Distances
The Sum of Squared Distances (SSD) is equivalent to the squared Euclidean distance or norm. Using the
same assumptions and definitions as for cross correlation, the normalised SSD can then be expressed by:

  SSD = 1
N n+i,m+ j ijn,m
T
2
i=1
N
j= 1
NTT
S T  ,
2

Equation 32


As for CC in the time and Fourier domains, the impact of masking has to be taken into account.
In these cases NT
2 shall be replaced by N, which is the total number of pixels contributing to the
correlation, and the difference shall only be computed when both Sn+i,m+i and Ti,j are non-zero.
9.3.2.4.3 Derivation of Displacement
The matching surface shall be considered as valid, and computed, only for relative positions of target and
search areas (nominally 80 × 80 pixels, for HRVIS nominally 96 × 96 pixels) such that the target area is
always completely included in the search area. The positions in the output arrays corresponding to invalid
cross correlation positions shall be set to zero in all the result arrays. The point corresponding to zero
relative displacement shall be the centre of the output surfaces. The matching surface shall be made
available for further processing.
The extracted matching surface shall be used to derive a sub-grid location of the best fit position. This
shall be done with a polynomial fit in the vicinity of the best fit location within the matching surface.
The fitting shall utilise the n_fit locations around the maximum for the extraction, where n_fit is a setup parameter. Based on the extracted maximum correlation value (or minimum distance) at a sub-grid
accuracy, the measured displacement as a function of pixels shall
be converted to longitude and
latitude positions as defined by the central location of the target in the image pair.
In the second step the distance between the two latitude/longitude locations shall be derived and an
‘instantaneous’ wind speed and direction shall be computed from these locations.

<!-- source_page: 155 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The latitude/longitude assigned to the intermediate AMV shall be the centre of the displaced target
area. The displaced target area found from the matching algorithm shall be used for the height
assignment.
9.3.2.5 Height Assignment
9.3.2.5.1 Introduction
This section describes the retrieval of cloud heights for high, medium and low-level clouds, and the
height assignment of clear-sky tracers.
The height assignment shall be based on information from the Scenes Analysis (SCE) product (see
Section 5), as well as on the Cloud-Top Height (CTH) values derived by the Cloud Analysis (CLA)
product. See Section 8. Besides this, a height assignment based on the newly-developed Optimal
Cloud Analysis (OCA) product shall be provided.

The AMV algorithm shall be flexible, allowing for any changes to the underlying height assignment
product that is selected. This will accommodate use of the most accurate and best-validated methods in
the cloud-height assignment field. All the pixel-based information derived by Scenes Analysis, Cloud
Analysis and Optimal Cloud Analysis (OCA) shall be made available.
The height assignment shall be performed for every target requested by the AMV.
The cross-correlation contribution (CCC) method shall be implemented, and shall be available for
every class of cloudy pixels inside each target, during operations.
The cloud classes and single cloud-free class shall be derived as specified in the Image Data
Preparation (see section 9.3.2.2).
9.3.2.5.2 Cross-Correlation Contribution (CCC) Method
This CCC method shall be applied by default to all cloudy and clear-sky targets.
The degree of matching between pixel counts a and b between the two images A and B shall be given
by the following two-dimensional cross-correlation coefficient:

b
ij
M
i
N
j a
njmi bb
nm
nmaa
NMnmCC 

 


11
,
),(
),(1),(

Equation 33

where (m,n) represents the (lines, elements) displacement of the target box in image B from the initial
position in the first image A.
The correlation coefficient CC(m,n) is normalized to values between -1 (mirror structures) and +1
(identical structures). The symbols ā and a represent the average and the standard deviation of the
count value a in image A, respectively (correspondingly for b in image B).

<!-- source_page: 156 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Values M and N correspond to the box size, nominally 32 × 32 for HRVIS and 24 × 24 for all other
channels. According to Büche et al. (2006), the correlation coefficient can also be written as follows:


NM
ji
ij nmCCnmCC
,
,
),(),(

Equation 34


where the symbol CCij expresses how much the individual pairs of pixels (i,j) and (i+m,j+n) contribute
to the total correlation coefficient of the pair a(m,n) and b within the target boxes in the two images.
Usually, coldest and warmest pixels in the target box contribute the most to CC(m,n). In the case of a
clear distinction between cold and warm scenes within the target box, the relative individual pixel
contributions, CCij, present a clear ‘C-shaped’ distribution, as shown in Figure 10. The distance
between the two branches corresponds to the contrast of the structures within the target area. Several
pixels have a negative CCij, which generally corresponds to pixels that have very different radiative
properties but the same position within the two target boxes in the image 1 and image 2. Appearance
and/or decay of clouds between image 1 and 2 generally induce such negative CCij. Pixels that
contribute the most to CC(m,n) are defined as those that have CCij greater than the average CCij,
<CCij>, represented by the dashed blue line on Figure 10.

Figure 10: Infrared counts as a function of the individual pixel contribution
9.3.2.5.3 Cloudy Targets in Infrared and Water Vapor Channels
The height assignment of the AMVs shall be computed using a cloud height product, which gives an
estimation of the cloud-top height for all the cloudy pixels. In the current operational algorithm, the
cloud height information provided by the SCE and CLA products shall be used.
The AMV pressure P shall be calculated as the average cloud-top height (CTH) pressure of the
selected pixels, weighted by their individual contribution to the correlation coefficient, CCij:

<!-- source_page: 157 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document










thrCCijCC
branchcold
ij
thrCCijCC
branchcold
ijij
ij
ij
CC
CTHCC
P
_
_
_
_

Equation 35

At first, the value of CCij_thres shall be dynamically set to the average CCij, <CCij>, calculated using
the pixels present within the target area. If no cold pixels satisfy this condition, then the value of
CCij_thres_def shall be set to 0. When the target area contains very large and homogeneous cloudy
layers, it may happen that no cold pixels have a CCij greater than the average <CCij>. In such case all
pixels of the cold branch with a CCij greater than 0 shall be used to calculate the pressure.
For AMVs derived using infrared or water vapour channels, only the pixels of the ‘cold branch’ of
Figure 10 (those with a count value smaller than th e average count value within the target area) that
have a successful CTH value and a CCij value greater than CCij_thres shall be selected to calculate the
pressure.
A weighted pressure standard deviation, P, shall be calculated accordingly, and associated to the
pressure P, using the same set of pixels. This standard deviation gives information on the variability
present within the target box, and shall be given in hPa. The pressure standard deviation shall be
given by the following:


2
_
_
_
_
2
PCC
CTHCC
thrCCijCC
branchcold
ij
thrCCijCC
branchcold
ijij
P
ij
ij









Equation 36

9.3.2.5.4 Cloudy Targets in Visible Channels
As for the infrared channels, the cross-correlation contribution process uses the contrast of the pixels
present within the target box, and the same kind of plot as that in Figure 11: Height Assignment in
Clear-sky areas can be produced considering the visible radiance as a function of the individual pixel
contribution.
In the visible part of the spectrum the scattering of photons on cloud particles dominates the radiative
transfer processes. Therefore the cloud tops which correspond to pixels having the smallest radiance in
the IR or WV channels correspond now to the pixels which have the largest reflectance in the visible
channels.
For AMVs derived using visible channels, only the pixels of the ‘warm branch’ of Figure 11.
(i.e. those with a count value larger than the average count value within the target area) that have a
successful CTH value and a CCij value greater than CCij_thres shall be selected to calculate the
pressure.
The pressure shall then be computed as follows:

<!-- source_page: 158 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document











thrCCijCC
branchwarm
ij
thrCCijCC
branchwarm
ijij
ij
ij
CC
CTHCC
P
_
_
_
_

Equation 37

A pressure standard deviation shall be computed for the visible channels in a similar way to that
described in section 9.3.2.5.3 for the IR and WV channels:


2
_
_
_
_
2
PCC
CTHCC
thrCCijCC
branchwarm
ij
thrCCijCC
branchwarm
ijij
P
ij
ij









Equation 38


9.3.2.5.5 OCA Height for Cloudy Targets in Infrared, Water Vapour and Visible Channels
As mentioned in 9.3.2.5.1, a height assignment based on the cloud height information provided by the
OCA product shall be provided. The process shall be identical to that described in 9.3.2.5.3, replacing
the CLA cloud-top height (CTH) pressure by that from the OCA product.
9.3.2.5.6 Analysis of Results and Derivation of Final Cloud Height
9.3.2.5.6.1 Analysis of the Results
The output from each retrieval technique shall consist of:
1. Method_Applied and Method_Success flags.
2. For each of the classes of cloudy pixels with successful results:
For each estimate:
 The derived cloud-top pressure
 Confidence provided by the statistical analysis
 Cloud-top pressure standard deviation
 Fraction of pixels associated with the cloud-top estimate
 Mean cloud-top temperature
 Cloud-top temperature standard deviation
To evaluate the final results of the CCC method with the forecast profile, the cloud-top mean pressure
of every class of estimates shall be compared with the atmospheric pressure at the top of every layer
whose relative humidity exceeds a critical value rh_crit. If there is such a layer in the range of one
RMS of the estimated cloud-top mean pressure, then the following parameters shall be calculated:

<!-- source_page: 159 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




(1) Absolute value of the following ratio: difference between the estimated cloud-top mean
pressure and the forecast pressure at the top of that atmospheric layer of high humidity,
divided by the forecast pressure at the top of the layer.

(2) Ratio between the root mean square (RMS) of the respective class of estimates of the
cloud-top pressure and the thickness of that same atmospheric layer of high humidity.
The evaluation of the final results, as described above by splitting the results into two groups, at
present has no direct impact on the wind information written out to the products. Its usefulness will be
reviewed as a Future Enhancement.
9.3.2.5.6.2 Derivation of the Final Cloud Height
The final cloud height shall be that corresponding to the CCC method. The values for pressure
standard deviation, temperature and temperature standard deviation shall be those corresponding to
the CCC method.
9.3.2.5.7 Inversion Height Assignment
The inversion height assignment algorithm shall be applied to infrared and visible channel targets
only. For the WV channels a different approach shall be used (see 9.3.3.1.7).
For all targets with a final pressure, fin_pres, bigger than inv_height_thres (nominally 600 hPa) the
inversion height assignment shall be performed. The inversion height assignment shall:
1. Find the temperature T-bottom (and corresponding pressure P-bottom) at the bottom of the
inversion layer. The bottom of the inversion layer is defined as the lowest level (index j) at which
T(j) < T(j+1). The search for T-bottom will fail if P-bottom is not between inv_height_thres and
the surface pressure + inv_surface_offset (this parameter has a nominal value of 40 hPa). In that
case quit the inversion height assignment, without changing fin_pres.
2. Find the temperature T-top (and corresponding pressure P-top) at the top of the inversion layer.
The top of the inversion layer is defined as the lowest level (index j) above the bottom of the
inversion layer at which T(j) > T(j+1). The search for T-top will fail if P-top is smaller than
inv_height_thres. In that case quit the inversion height assignment, without changing fin_pres.
3.
If (T-top - T-bottom) > inv_magnitude_thres (nominally 0 K) then
inv_pres = (inv_c1 * P-bottom + inv_c2 * P-top) / (inv_c1 + inv_c2) + inv_c3
where nominally inv_c1 = 1, inv_c2 = 0 and inv_c3 = 0. Otherwise, quit the inversion height
assignment, without changing fin_pres.
4. If inv_pres > fin_pres then define inv_pres as height of the AMV.
9.3.2.5.8 Cloud Base Height Assignment
The cloud-base height assignment shall not be applied within the AMV algorithm as of this release.
9.3.2.5.9 Window Channel IR EBBT Method Based on CCC Pixels
The window channel IR EBBT method shall be applied to all representative radiance cloud classes,
based only on those pixels used by the Cross-Correlation Contribution (CCC) method. Nominally, for
non-WV channels the RCd
IR10.8 shall be converted into the respective EBBTs. For WV channels the
RCd
WV shall be converted.
The associated pressure Pc shall be derived from the atmospheric profile data. The uncertainty pc (and
the corresponding t) in the height assignment shall be defined by the following:

<!-- source_page: 160 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





 
22
   PPPP ccpc
Equation 39


where P- and P+ are the pressure associated with (RCd
x + Cd
x) and (RCd
x - Cd
x) respectively.
9.3.2.5.9.1 Low-level Cloudy Water Vapour Winds
It may happen that a pressure is found at low levels associated to an AMV extracted from the water
vapour 6.3 µm or 7.3 µm channels. Such cases are not realistic because only the high and mid levels of
the troposphere can be seen using the water vapour channels. These cases correspond to targets that
have been identified as cloudy because low-level clo uds are present in the target boxes, but the AMVs
correspond to the motion of water vapour features located at higher levels in the troposphere, above
the low clouds. So, if an AMV is extracted from a wate r vapour channel and its pressure is larger than
a given threshold, then the EBBT pressure based on CCC using all pixels (not only cloudy) shall
be
used (see 9.3.2.5.11.2). The following prescribed thresholds shall be used for WV cloudy
AMVs: 450 hPa for the 6.2 µm channel, and 650 hPa for the 7.3 µm channel.
9.3.2.5.10 Low-level AMV Correction
Whenever there is a temperature inversion and the EBBT pressure computed is larger than the
corrected AMV pressure, then the EBBT pressure based on CCC pixels shall be used. This prevents
that pixels whose height was inversion-corrected upwards in the atmosphere during the CLA process
contribute to the low-level AMV having an artificially too high altitude. Thus, winds associated to
clouds below the inversion layer effectively remain below the inversion layer.
9.3.2.5.11 Height Assignment in Clear Sky Areas
9.3.2.5.11.1 Normalized contribution RTM methods
Height assignment for clear sky targets shall be carried out only for the WV6.2 and WV7.3 channels.
It shall use the normalised total contribution (NTC) and the normalised total cumulative contribution
(NTCC) tables provided by the RTM for these channels. Three single level heights shall be estimated.
The first height, PmaxNTC, shall be defined as the level at which NTC reaches a maximum (i.e. equals
1). The second height, PNTCC_N, shall be defined as the level at which NTCC exceeds the value
NTCC_N (nominally 50 %). The difference P = (PNTCC_N - PM) defines the reliability of the single
level height and shall also be provided as an output.
The representative layer thickness, PLT, is defined by PLT = PNTCC_LL - PNTCC_HL, where PNTCC_LL and
PNTCC_HL are defined as the levels where the NTCC assumes the values NTCC_LL (nominally 10  %)
and NTCC_HL (nominally 90 %).
This process is shown graphically in Figure 11.

<!-- source_page: 161 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




NTCCNTC
PHL
PMAX
PN
PLL
NLL HL
Height

Figure 11: Height Assignment in Clear-sky areas
A third height, Pwv,EBBT, is derived from the average EBBT of the coldest water vapour pixels in the
clear sky cluster. The number of pixels from which the average EBBT is derived is determined by the
fraction frac_cs_ebbt (nominally 30% of the total cluster size).
All derived heights, i.e. P
maxNTC, PNTCC_N, PLT, PNTCC_LL and PNTCC_HL as well as Pwv,EBBT, shall be saved
for further processing.
The final height associated with the target shall be computed in one of two ways. If iflag_sequence_ha
= 0, a weighted mean of the three single level heights shall be computed, using set-up parameter
values for iflag_ClearSky_MaxNTC, iflag_ClearSky_NTCC_N and iflag_ClearSky_EBBT (nominally
all 1). If iflag_sequence_ha = 1 (nominal value), the final height shall be set to PNTCC_N .
9.3.2.5.11.2 CCC Method Using Water Vapour Brightness Temperature
The EBBT pressure based on CCC (described in 9.3.2.5.9) shall be computed for all clear-sky water
vapour winds. All pixels within the target box shall be considered–not only cloudy pixels.

9.3.2.5.12 Forecast Best-Fit Pressure
A forecast best-fit pressure value shall be computed, based on the algorithm used at the Met Office.
First, the forecast speed and direction profiles at the wind location, FcstWindSpeed and
FcstWindDirection, shall be extracted. Then, the U and V components of the forecast profile shall be
computed as follows:
FcstWindUi = FcstWindSpeedi · cos(270 – FcstWindDirectioni);
FcstWindVi = FcstWindSpeedi· sin(270 – FcstWindDirectioni);
where i represents each forecast level.

<!-- source_page: 162 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The minimum and maximum forecast speeds within a prescribed range of the wind pressure, PresDiff
(currently set to 150 hPa), shall be computed, namely WindMinSpeed and WindMaxSpeed. Then, the
forecast level with the pressure closest to the computed wind pressure, ClosestLevel, shall be found.
The U and V components of the wind shall be computed as follows:
WindU = WindSpeed · cos(270 – WindDirection);
WindV = WindSpeed · sin(270 – WindDirection).
Then, the vector difference between the wind and the forecast shall be computed at all levels:

  
22
iii FcstWindVWindVFcstWindUWindUVecDiff 
Equation 40

The best-fit level, BestFitLevel, is the forecast level for which the vector difference is minimal. If the
best-fit level is the first level in the forecast profile, P3 is smaller than TopPres (currently set to 100
hPa), or V2 equals V1 or V3, where:

P1 = FcstPressure(BestFitLevel–1); V1 = VecDiff(BestFitLevel–1);
P2 = FcstPressure(BestFitLevel); V2 = VecDiff(BestFitLevel);
P3 = FcstPressure(BestFitLevel+1); V3 = VecDiff(BestFitLevel+1);

then, the best-fit pressure shall be set to P2. Otherwise, a parabolic fit shall be used in order to find
the best-fit pressure:

     
      12323212
123232125.02
22
VVPPVVPP
VVPPVVPPPssureBestFitPre 


Equation 41


The U and V components of the best-fit level shall be computed using a linear interpolation as
follows:
BestFitU = FcstWindUbelow · (1 – Prop) + FcstWindUabove · Prop;
BestFitV = FcstWindVbelow · (1 – Prop) + FcstWindVabove · Prop;
where:

  






;12/1
;
;1
2
PPPssureBestFitPreProp
elBestFitLevLevelAbove
elBestFitLevLevelBelow
ssureBestFitPreP

  






.23/2
;1
;
2
PPPssureBestFitPreProp
elBestFitLevLevelAbove
elBestFitLevLevelBelow
ssureBestFitPreP

Equation 42

<!-- source_page: 163 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





  






;12/1
;
;1
2
PPPssureBestFitPreProp
elBestFitLevLevelAbove
elBestFitLevLevelBelow
ssureBestFitPreP

  






.23/2
;1
;
2
PPPssureBestFitPreProp
elBestFitLevLevelAbove
elBestFitLevLevelBelow
ssureBestFitPreP

Equation 43


Finally, the computed best-fit pressure shall be used only if BestFitLevel is not 0, the minimum vector
difference, MinVecDiff, is smaller than 4.0 m/s, and the vector difference is larger than MinVecDiff + 2
m/s outside of the band BestFitPressure ± 100 hPa. Otherwise, the wind shall be marked as poorly
constrained, and the best-fit pressure value shall not be used.
9.3.2.6 Derivation of the Final Vector
The derivation of the final vector shall be based on the N_gen Intermediate Products, where N_gen is
nominally three. Vectors originating from the same target shall be combined to provide a final vector.
The combination shall take into account all possible single repeat cycle vectors. It shall also take into
consideration the impact of possible reduced scan configurations. The total number of vectors used to
derive the final vector shall be transferred to the follow-on processes.
There are two alternative methods available for computing the final vector. These are selected by the
set-up parameter iflag_sequence_ha (nominally 1).
 Weighted Mean (iflag_sequence_ha = 0)
 Sequential Method (iflag_sequence_ha = 1)
For the weighted mean, the combination shall be linear, providing an average speed and direction
maintained during the specified generation cycle. The location shall be the average location of the
target location in each cycle used to generate the final vector. The height and temperature shall be the
arithmetic mean of the coldest scene within the target area. This applies to both cloud and clear-sky
targets. Only targets based on at least min_derivations shall be used.
For the Sequential Method, for each cloud target, an arithmetic mean shall be used to calculate the
height estimate for the final vector, using the intermediate components associated with the most
frequently occurring height assignment method. Prior to the introduction of the CCC method, if,
for example, components 1 and 3 were obtained using the EBBT method, and component 2 by the CO 2
method, only components 1 and 3 were used for the final vector. Now, because there is only one
height assignment method (i.e. CCC), all components shall
be used. Any of the component heights
which are not within max_pres_diff (nominally 50 hPa), max_dir_diff (nominally 20°) or
max_speed_diff (nominally 10 m/s) of at least one of the others shall not be considered (and both
shall be ignored if this happens when there are only two components remaining). If the number of
components left is less than min_derivations, the final vector shall not be calculated.
For clear-sky targets, an arithmetic mean of the coldest scene within the target area shall be computed
for the final vector height, as for the weighted mean method.

<!-- source_page: 164 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The temperature, speed, direction and position associated with the final vector shall be an arithmetic
mean of the components used for calculating the height.
As a temporary solution, the pressure value corresponding to the CCC method shall be stored in
component 6 of the array of height assignment methods to be written to the AMV BUFR file, as part
of the AMV Final Product. Additionally, the pressure plus one standard deviation shall be stored in
component 8 of the mentioned array as an indication of the height error.
As a temporary solution, the pressure value corresponding to the forecast best-fit shall be stored in
component 19 of the array of height assignment methods in the AMV Intermediate Product. Besides, it
shall be stored in component 10 of the array of hei ght assignment methods to be written to the AMV
BUFR file, as part of the AMV Final Product.
As a temporary solution, the pressure value corresponding to the use of the OCA cloud-top height
shall be stored in component 18 of the array of he ight assignment methods in the AMV Intermediate
Product. Besides, it shall be stored in component 3 of the array of height assignment methods to be
written to the AMV BUFR file, as part of the AM V Final Product. Additionally, the OCA pressure
plus one standard deviation shall be stored in component 5 of the mentioned array as an indication of
the height error.
As a temporary solution, the EBBT pressure base d on CCC of WV clear-sky and low-level cloudy
AMVs shall be stored in component 17 of the array of height assignment methods in the AMV
Intermediate Product.   Besides, it shall be stored in component 9 of the array of height assignment
methods to be written to the AMV BUFR file, as part of the AMV Final Product.
9.3.3 Automatic Quality Control (AQC)
The Automatic Quality Control shall apply a set of tests to the extracted vectors. Each test shall
provide a normalised output value such that they can be linearly combined to obtain a final quality
estimate of each of the vectors, or be used as a multiplicator on the obtained final quality estimate.
This final reliability estimate shall form the basis of further evaluation of the vectors and shall be
disseminated together with the vectors. A selection mechanism shall be introduced, which prevents
vectors with a quality less than a specified threshold from being disseminated. In the following, some
relevant tests are described, but the AQC shall provide the flexibility to easily introduce new tests: this
is considered a future enhancement.
9.3.3.1 AQC for Intermediate AMV Product
9.3.3.1.1 Forecast Consistency Test
This process shall generate the quality mark Mforecast , which is a measure of the consistency of the
forecast AMV.
To do this, the vector difference of the AMV vector and the forecast vector interpolated to the same
location and pressure level shall be computed.
The computation shall be done for all AMV vectors in every intermediate AMV product, according to the
following equation:
 CFCAQCBFCAQCyxFyxSAFCAQC
yxFyxS - 1 =i M
DFCAQC
forecast
__
__)__,2/,,__max(
),(),(tanh)( 
















<!-- source_page: 165 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




where AQC_FC_A to AQC_FC_D are set-up parameters included in the static data file.
All interpolated forecast wind directions shall be derived by interpolating the u and v components, then
calculating the resultant direction.
9.3.3.1.2 Spatial Consistency Check
This process shall generate the quality mark MSWC which is a measure of the spatial vector consistency of
the AMV.
The process shall also generate the quality mark MSHC which is a measure of the spatial height
consistency of the AMV.
To calculate the spatial vector consistency, the AMV values shall be compared with the AMVs computed
at the neighbouring grid points.
The quality mark shall be computed against all vectors within the height threshold, AQC_SC_max_pp,
for which ELL_DIST < 1, where:

ELL_DIST = (X/A) 2 + (Y/B) 2
where:
A = A1 + WindSpeed · A2;
B = B1 + WindSpeed · B2;
X = WindDist · cos(WindAngle);
Y = WindDist · sin(WindAngle);
and WindSpeed is the reference wind speed. In order to compute the distance between the reference
wind and the test wind locations, and the angle of the line containing both locations with respect to the
reference wind direction (WindDist and WindAngle, respectively), the following vectors shall
be
defined first (see Figure 12):

VectorC(1) = cos(WindLat) · cos(WindLon);
VectorC(2) = cos(WindLat) · sin(WindLon);
VectorC(3) = sin(WindLat);
VectorE(1) = cos(TestLat) · cos(TestLon);
VectorE(2) = cos(TestLat) · sin(TestLon);
VectorE(3) = sin(TestLat);
VectorV(1) = –sin(WindLon);
VectorV(2) = cos(WindLon);
VectorV(3) = 0.0;

where: WindLon and WindLat are the longitude and latitude, respectively, of the reference wind, and
TestLon and TestLat are the longitude and latitude, respectively, of the test wind.

<!-- source_page: 166 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document






Figure 12: Reference wind and test wind locations with auxiliary vectors
(assuming Earth Radius = 1, for clarity).

If the difference in latitude for the reference and test winds is smaller than a given threshold
(10–6 rad), then the vector from the reference wind location to the test wind location shall be:





 . if,
; if,
WindLonTestLonVectorV
WindLonTestLonVectorVVectorU

Equation 42

Otherwise:

;VectorCVectorN
VectorCVectorNVectorU 


Equation 43

where the auxiliary vector VectorN is:
VectorN = VectorC × VectorE.

Then, the angle formed by VectorU with respect to the reference wind direction shall be computed as:
WindAngle = PsiAngle – WindDir,
where WindDir is the reference wind direction and PsiAngle = acos( VectorU · VectorV) is the angle
between VectorU and the local parallel.
The distance between the reference wind and the test wind locations shall finally be computed as the
great-circle distance between the two wind locations:

<!-- source_page: 167 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




WindDist = EarthRadius · acos(VectorC · VectorE).
The individual quality marks shall be calculated according to the following equation:
    __)__,2/,,__max(
),(),(
tanh
__
, 

















CSCAQCBSCAQCiyixSyxSASCAQC
jyixSyxS
-1=M
DSCAQC
SWC ji
where AQC_SC_A to AQC_SC_D are set-up parameters included in the static data file.
If lc_dist_weight is false (default value) the final quality mark shall be a linear average of the
N_best_lc (nominally 2) nearest matches.
If lc_dist_weight is true the final quality mark shall be the distance-weighted average of the N_best_lc
individual marks:


Equation 44

If no wind vectors are found the quality mark M
SWC shall be set to zero.
To calculate the spatial height consistency, the AMV values shall be compared with all neighbouring
AMV vectors within the height threshold of the current segment, according to the following equation:

BHCAQCyxPAHCAQC
jyixPyxPabs - 1 = M
CHCAQC
MIN
SHC
__
__),(__
)),(),((tanh 














Equation 45

where AQC_HC_A to AQC_HC_C are set-up parameters included in the static data file.
9.3.3.1.3 Temporal Vector Consistency Test
This process shall generate the quality mark MTC which is a measure of the temporal consistency of
the AMV.
To calculate MTC, the AMV shall be compared with the AMV from the preceding Intermediate AMV
Product having the same Target ID.
For new targets within an intermediate AMV, the AMV shall be compared with the AMV from the
preceding intermediate AMV product within prev_gen_pp (nominally 50 hPa) and within the smallest
prev_gen_ell = (X/(A_p))2 + (Y/(B_p))2






 

jiSWCSWC MDISTELLDISTELL
M
,
_
1
_
1
1

<!-- source_page: 168 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




where:
A_p = A1_p + spd*(A2_p)
B_p = B1_p + spd*(B2_p)
X, Y are as for the Spatial Consistency Test, except that d_lat and d_lon are based on
the backward propagation of the target into the previous cycle.

If no preceding Intermediate AMV Product is available, the quality mark shall be computed against the
Final AMV of the previous AMV Product not older than one hour.

CTCAQCBTCAQCyxSyxSATCAQC
yxSyxS - 1 =i M
DTCAQC
N
N
TC
__
__)__,2/),(),(__ ( max
),(),( tanh)( 

















where AQC_TC_A to AQC_TC_D are set-up parameters included in the static data file.
9.3.3.1.4 Temporal Speed Consistency Test
This process shall generate the quality mark MTSC which is a measure of the speed consistency of the
AMV.
To do this, the AMV shall be compared with the AMV from the preceding Intermediate AMV Product in
the same way as the Temporal Vector Test above:

 CTSCAQCBTSCAQCyxSyxSATSCAQC
yxSyxS - 1 =M
DTSCAQC
N
N
TSC
__
__)__,2/),(),(__max(
),(),(tanh 


















where AQC_TSC_A to AQC_TSC_D are set-up parameters included in the static data file.
9.3.3.1.5 Temporal Direction Consistency Test
This process shall generate the quality mark MTDC which is a measure of the direction consistency of
the AMV.
To do this, the AMV shall be compared with the AMV from the preceding Intermediate AMV Product
in the same way as the Temporal Vector Test above:

where AQC_TSC_A to AQC_TSC_D are set-up parameters included in the static data file and

vel
Sxy S xy N

(,) (,)
2
Equation 44


DTDCAQCvelCTDCAQCeATDCAQC
yxDIRyxDIR - 1 = M
ETDCAQC
BTDCAQCvel
N
TDC
__
__/ ____)__(
),(),(tanh 















<!-- source_page: 169 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.3.3.1.6 Temporal Pressure Consistency Test
This process shall generate the quality mark MTPC which is a measure of the temporal height
consistency of the AMV.
To do this, the AMV shall be compared with the AMV from the preceding Intermediate
AMV Product in the same way as the Temporal Vector Test in 9.3.3.1.3 above:

 CTPCAQCBTPCAQCyxPATPCAQC
yxPyxP
- 1 =M
DTPCAQC
TPC
__
1
__)__,),(__max(
),(),(
tanh 
















 

where AQC_TPC_A to AQC_TPC_D are set-up parameters included in the static data file.
9.3.3.1.7 Image Correlation Test
This process shall generate the quality mark MHAC which is a measure of the correlation cc(ir,wv)
between the IR10.8 and WV6.2 channels. The quality mark shall be computed as follows:
BHAAQC
wvirccAHAAQCMAX =M
CHAAQC
HAC
__
__
)),(,__(tanh 












Equation 47
where AQC_HA_A to AQC_HA_C are set-up parameters included in the static data file.
The test is applied to mid-low level cloud winds. If the pressure of the corresponding
AMV > AQC_HA_PP, then
M =M HACHAC 1
else
M HAC = 1

The above test is also applied to clear sky winds using the above main formula for MHAC and setting
M HAC = M HAC – 1
For the WV channels, the quality mark shall be set to zero in case the pressure is above certain
prescribed threshold: 450 hPa for the 6.2 µm channel, and 650 hPa for the 7.3 µm channel.
9.3.3.1.8 Inter-Channel Consistency Check
All winds with pressure greater than ic_low_pres (default 600 hPa) and a minimum speed of
ic_min_spd (default 20 m/s) shall be compared to all winds within low_ic_check_dist (nominally 100
km). Against these vectors, if the pressure difference is greater than ic_pres_diff (nominally 100 hPa)
the following test shall be performed:
 CICAQCBICAQCyxSyxSAICAQC
yxSyxS M
DICAQC
N
N
IC
__
____,2/),(),(__max
),(),(tanh 
















<!-- source_page: 170 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





where AQC_IC_A, AQC_IC_B, AQC_IC_C and AQC_IC_D are set-up parameters.
The final quality of the low-level vectors shall be multiplied with this test value. If no suitable
collocated clear sky winds are available, the test value returned shall be 1.
Note: The inter-channel consistency check is neither applied nor evaluated in the above form, but will
be considered as a Future Enhancement.
9.3.3.1.9 Final Quality
The Final Quality Value (QI) for AMVs in the Intermediate AMV product shall be calculated as a
weighted mean of the forecast, four temporal and two spatial consistency tests, multiplied by the
image correlation test. The weights shall be defined by the set-up parameters AQC_Q_Weights_*.
This normalised value shall be the final quality indicator which is attached to the AMV. The final
quality indicator is always in the range 0 to 1, because of the way in which the individual quality
marks have been defined.
9.3.3.2 AQC for the Final AMV Product
Similar consistency tests shall be used for the AMV Final Product.
For the forecast consistency test, the vector difference between the AMV final vector and the forecast
vector interpolated to the same location and pressure level shall be computed, using the same set-up
parameters as for the Intermediate Product AQC.
The quality values for the spatial consistency tests are calculated using the surrounding AMVs in the
Final AMV Product itself, using the same set-up parameters as for the Intermediate Product AQC.
For the individual temporal consistency tests on speed, direction, vector and height, the quality values
for the AMVs in the Final AMV Product shall be based on the corresponding quality values for the
AMVs in the Intermediate AMV Products used to form the Final AMV. The Final value shall be
calculated as a weighted mean of the contributing Intermediate values. The weights shall be defined
by the corresponding set-up parameters N_Gen_AQC_Q_Weights_*(1-3), where (1-3) indicates the
intermediate AMV product. Values for the first intermediate AMV product are never used in the
averaging for the temporal tests.
For the image correlation test, the quality shall
be calculated in the same way as for the temporal tests
above, but the first intermediate AMV product value is now included in the averaging.
The Final Quality Value (QI) for AMVs in the Final AMV product is calculated in the same way as
described for AMVs in the Intermediate AMV Product above. An additional Final Quality Value
which excludes the forecast consistency shall also be calculated. This is provided for users requesting
a product as independent as possible from the input forecast.
Both quality values shall also be modified to reduce the quality of slow winds. If AMV wind speed,
wind_spd < speed_threshold (nominally 2.5 m/s), then the Final Quality Value is multiplied by the
factor, wind_spd/speed_threshold.

<!-- source_page: 171 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.3.3.2.1 AMV Encoding Filter
An encoding filter is applied to the Final AMV Product to prevent very bad products being sent to
users. The filter is tuned in such a way as to prevent dissemination only for extremely bad cases,
occurring only a few times a year, in most cases as a result of spacecraft manoeuvres or other image
deficiencies. The following values are calculated and checked against a threshold:
 Minimum average vector consistency should be > qual_vector (nominally = 50, for channel
WV6.2 = 40).
 Minimum average forecast consistency should be > qual_forecast (nominally = 30, for channel
IR10.8 = 40).
 Minimum proportion of AMVs with QI (exFC) > qual_qi (nominally 80%) should be >
qual_proportion (nominally 20%).
 Minimum number of AMVs with QI (exFC) > qual_qi (nominally 80%) should be >
qual_num_good (nominally = 500, for the VIS channels = 10, and for HRV channel = 20).
 Maximum number of AMVs with pressure < qual_pressure (nominally 130 hPa, for the VIS and
HRV channels = 10 hPa) should be < qual_num_high (nominally = 100, for the VIS and HRV
channels = 9999).
 For RSS the parameter qual_num_good is nominally set to 100 for channels WV6.2, WV7.3 and
IR10.8.
If any of the above tests fails, the number of AMVs passing AQC (per channel) is set to 0 and the
AMV channel is not encoded.
9.3.4 Recursive Filter Function AQC Scheme
The AQC scheme described in the previous section has been used as the standard EUMETSAT QI.
The Recursive Filter Function (RFF) has been developed as an alternative AQC. It was originally
developed at UW–CIMSS (University of Wisconsin - Co-operative Institute for Meteorological
Satellite Studies). It is an objective 3D recursive filter analysis of the derived AMVs. The RFF
application is described in detail by Hayden et al (1995 and 1996). A three-dimensional background
field is created and modified at regular latitude/longitude grid points and pressure levels in several
analyses using the AMV wind (velocity component) data and (for the EUMETSAT RFF) the ECMWF
forecast field. The background field is smoothed along three dimensions and each grid point/level has
a degree of local influence on the smoothing, based on the quality of the analysis at each grid point.
The quality of the analysis is essentially composed from a comparison of the AMVs with the
background field and is dependent on pre-selected error tolerances. Where the quality analysis is low,
for example where the AMV data and background field are significantly different, the local influence
is small and information from other grid points is smoothed in. Where the quality analysis is high,
smoothing from other grid points is small. Within each analysis, corrections to the background field
are built up in several passes with increasingly rigorous quality control, beginning with coarse error
tolerances and characteristic spatial scales, which are refined with successive passes. After a number
of analyses (using the AMV and forecast field data), a best-fit of each AMV to the modified
background field is carried out to provide an adjusted height. A further analysis of the background
field is subsequently carried out using the adjusted AMV heights and a final quality indicator is
assigned to the AMV based on the quality of neighbouring analysis and the fit of the AMV to the data.

<!-- source_page: 172 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The analysis field has a latitude and longitude grid spacing of rff_delta_lat and rff_delta_lon
(nominally 1 degree) and pressure levels corresponding to those used for the input forecast and RTM
data. The forecast field is sampled at nominally every fourth grid point in longitude and every second
point in latitude (rff_pseudo_density_lon = 4, rff_pseudo_density_lat = 2), and (nominally (rff_stagger
= 1)) staggered in longitude.
There are five main processing steps:
1.
Initial Analysis
2. Main Analysis
3. Height Re-adjustment
4. Final Analysis
5. Calculation of Final Quality Flag
9.3.4.1 Initial Analysis
This consists of two analyses of the wind field. It is the effective initialisation of the analysis field as
only the forecast data is used. In the first analysis the characteristic spatial scale and error tolerances
are independently set to constant values applicable at all heights (respectively
rff_initial_firstpass_radius_influence = 100 km and rff_initial_firstpass_tolerance = 9999.0 m/s).
The vertical coupling (a characteristic scaling of the vertical dimension) is set to
rff_initial_firstpass_vert_coup (nominally 50 km). There is a single iteration
(rff_initial_firstpass_no_iterations = 1) of the analysis and rff_initial_firstpass_no_smoothing_passes
(nominally 10) smoothing passes.
In the second analysis there are rff_initial_secondpass_no_iterations (nominally 5) iterations, each
with rff_initial_secondpass_no_smoothing_passes (nominally 3) smoothing passes. The characteristic
scale is larger and height dependent (rff_initial_secondpass_radius_influence = 600 km at lowest
level) and reduces with subsequent iterations (rff_initial_secondpass_radius_scale_factor = 18,
between initial and final iterations). The vertical coupling is set to rff_initial_secondpass_vert_coup
(nominally 375 km). The tolerance is as for the first analysis (i.e. very large), however reduces with
subsequent iterations.
9.3.4.2 Main Analysis
This is carried out using the AMV wind data and a down-weighted forecast field
(rff_main_fc_weight = 0.125). The initial error tolerances are based on statistical differences (height
dependent) between the AMV observations and the analysis field and constrained to lie between the
standard deviation of the difference and a pre-assigned (height dependent) tolerance
(rff_main_tolerance = 5.0 m/s at lowest level). The error tolerances are necessarily very much lower
than in the initial analysis, and are reduced over successive iterations
(rff_main_radius_scale_factor = 18). The characteristic spatial scale and vertical coupling follows the
same pattern as for the previous analysis. The number of iterations and smoothing passes are
nominally 5 and 3 (rff_main_no_iterations, rff_main_no_smoothing_passes) respectively.

<!-- source_page: 173 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.3.4.3 Height Re-Adjustment
After the Main Analysis, the AMV re-adjusted height is calculated by minimising a variation penalty
function in speed, direction, velocity, pressure, temperature between the AMV wind and the analysis
field. The weights assigned to the penalty function are as follows:
 rff_weight_speed,
 rff_weight_dirn,
 rff_weight_vel,
 rff_weight_pres
 rff_weight_temp (nominally 1000, 1000, 2100 and 10 respectively).
9.3.4.4 Final Analysis
A final analysis is carried out using the AMV wind data with the adjusted AMV heights and the downweighted forecast data. The same number of iterations and smoothing passes are used as for the main
analysis. The error tolerances are calculated as for the main analysis. The characteristic spatial scale is
calculated as for the main analysis, but the absolute values are lower:
(rff_final_radius_influence = 200 km at lowest level).
The vertical coupling is also reduced to rff_final_vert_coup (nominally 125 km).
9.3.4.5 Calculation of Final Quality Flag
On completion of the analysis, the final RFF Quality Indicator is determined by a final pass of the
quality analysis with stricter quality control. This means the quality exponent parameter (which
controls the fit of the analysis to the data) and tolerance are set to half those of the final analysis (the
characteristic spatial scale is left unchanged). The final (unsmoothed) quality value is extracted for
each AMV and forecast point, and the quality field at each grid point built up in a single iteration with
three smoothing passes. This field is then normalised to the maximum value and interpolated to each
AMV observation point. The final RFF quality value is calculated as the square root of the product of
this interpolated value and the final (unsmoothed) quality value of the wind.
9.3.5 Monitoring of the Product Quality
The quality of the final product shall
be continuously monitored. The monitoring shall be based on the
Final Quality Mark. The data shall be sorted into classes according to the Final Quality Mark, and for
each group statistics against collocated radiosondes as well as NWP vector fields shall be computed.
For this purpose certain selected variables shall be written into a database located in the facility itself.
The selection of these variables is a continuous activity which has to be based on experience.
9.3.5.1 AMV Verification
The satellite-derived AMVs shall be compared to independent measurements such as observations by
radiosondes and forecast wind profiles. The information collected by the verification shall be stored in
a database located in the facility itself. This shall include all the information described below for the
successful collocations and the corresponding AMV vector and quality information. The comparison
shall take into account all observations or forecast profiles within the MSG processing area. For each
AMV only those observations will be considered that are within a distance of 250 km (in horizontal
sense) and 50 hPa (in vertical sense) of the AMV position. For radiosonde and forecast profiles the

<!-- source_page: 174 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




best fit height level shall be derived. The best fit level shall be specified as the level at which the
following function reaches its minimum:
     
222
_
,
_
,
_
,,,





 




 




  temppr
pTyxT
prespr
pyxP
vecpr
pyxFyxSBSTFIT

Equation 45

where:
S(x,y) S(x,y) is the AMV vector
F(x,y,p) is the collocated (e.g. forecast, radiosonde) vector at height p
P(x,y) is the AMV height
p is the collocated (e.g. forecast, radiosonde) pressure
T(x,y) is the AMV temperature
T(p) is the collocated (e.g. forecast, radiosonde) temperature at height p
pr_vec, pr_pres and pr_temp are set-up parameters

For forecast data, the BSTFIT value shall be calculated at intervals of 5 hPa from the surface to the
tropopause. At levels where no forecast data are available a linear interpolation of pressure shall be
performed. The interpolation shall be done in the speed and direction domain where direction shall be
derived via the u and v components at the nearest levels above and below the missing level. For
radiosonde data the BSTFIT value shall be calculated only at the observation profile heights.
The following information shall be stored for every AMV in the verification database:
 Spacecraft number, date and time for collocation.
 The AMV vector information: band, type, latitude, longitude, speed, direction, height,
temperature and layer thickness.
 The collocated forecast information: forecast latitude, forecast longitude, forecast information at
first level below AMV and at first level above AMV comprising: forecast speed, forecast
direction, forecast pressure and forecast temperature.
 The AMV quality information: final quality mark, forecast quality mark, temporal vector
quality mark, temporal speed quality mark, temporal direction quality mark, temporal height
quality mark, spatial vector quality mark, spatial height quality mark, inter-channel quality
mark, image correlation quality mark.
 The collocated observation information: observation type, observation quality, observation time,
station identifier, latitude, longitude, pressure, temperature, speed, direction.
 The derived Best Fit information for the collocated radiosonde and forecast observations,
comprising for both: best fit speed, best fit direction, best fit height, and best fit temperature.
 Additional information such as wind method; target type; horizontal, vertical and time
separations between AMV and radiosonde; and a flag labelling the nearest observation to every
AMV.

<!-- source_page: 175 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 176 of 298

9.4 Outputs
The outputs in the following two tables shall be produced. Tables include outputs for both intermediate and final AMV product:
9.4.1 Intermediate AMV Product
Parameter Mnemonic Units Min Max Prec Acc To
Channel identifier chan_id - 1 12 1 1 AMV Intermediate Header
Processing Segment Columns Proc_width pixels 1 232-1 1 1
Processing Segment Rows Proc_height pixels 1 2 32-1 1 1
Cloud Target Area Columns Cloud_t_width pixels 1 232-1 1 1
Cloud Target Area Rows Cloud_t_height pixels 1 2 32-1 1 1
Clear sky Target Area Columns Clear_t_width pixels 1 232-1 1 1
Clear sky Target Area Rows Clear_t_height pixels 1 2 32-1 1 1
Cloud Search Area Columns Cloud_s_width pixels 1 232-1 1 1
Cloud Search Area Rows Cloud_s_height pixels 1 2 32-1 1 1
Clear sky Search Area Columns Clear_s_width pixels 1 232-1 1 1
Clear sky Search Area Rows Clear_s_height pixels 1 2 32-1 1 1
No. Vectors in Product N_vec - 0 232-1 1 1
For each AMV: AMV Intermediate Body
Target ID Tgt_Id ° - - - -
Latitude lat ° -90 90 0.001 0.001
Longitude lon ° -180 180 0.001 0.001
Vector speed spd ms -1 0 500 0.1 0.1
Direction dir ° 0 360 0.1 0.1
Temperature Uncorrected Temp_uncor K 170 300 0.1 0.1
Height Uncorrected Pres_uncor hPa 100 1050 50 1

<!-- source_page: 176 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 177 of 298

Parameter Mnemonic Units Min Max Prec Acc To
Correction Method Corr_method - 0 5 - -
Temperature temp K 170 300 0.1 0.1
Height pres hPa 100 1050 50 1
Value of best matching Match_val - -1 1 - -
Best Match Row Offset Row_Offset pixels 1 2 32-1 1 1
Best Match Column Offset Col_Offset pixels 1 232-1 1 1
Overall reliability OR - 0 100 1 1
Estimated height error pp_err hPa 0 200 1 1
Cloud target cloud_target - 0 1 - -
Applied image enhancement tar_enh - 0 1 - -
No. pixels in coldest EBBT class tar_pix pixels 0 65532 1 1
Fraction of land pixels in target area land_frac % 0 100 1 1
Results from each quality test qc_res - 0 1 - -
Height Assignment Method HA_mthd - 1 19 1 1
For each height assignment method coldest EBBT scene:
Pressure tar_press hPa 0 1100 0.1 0.1
Pressure standard deviation tar_press_sigma hPa 0 1100 0.1 0.1
Uncorrected temperature tar_uc_temp K 170 350 0.01 0.01
Corrected temperature tar_temp K 170 350 0.01 0.01
Corrected temperature standard deviation tar_temp_sigma K 0 350 0.1 0.1
Confidence of estimate (forecast consistency) height_rel - 0 100 0.01 0.01
Fraction of pixels used height_pix % 0 100 0.01 0.01
Table 32: List of required outputs for the Intermediate AMV Product

<!-- source_page: 177 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 178 of 298

9.4.2 Final AMV Product
Parameter Mnemonic Units Min Max Prec Acc To
Channel identifier chan_id - 0 12 1 1 AMV Final Header
Centre Frequency Frequency Hz 0 1011 103 103
Bandwidth Frequency Hz 0 10 11 10 3 103
Processing Segment Columns Proc_width pixels 1 232-1 1 1
Processing Segment Rows Proc_height pixels 1 2 32-1 1 1
Segment Size Columns Seg_width m 1 232-1 1 1
Segment Size Rows Seg_height m 1 2 32-1 1 1
Correlation Method Corr_method - 0 10 1 1
No. Vectors in Product N_vec - 0 2 32-1 1 1
No. Vectors passing AQC threshold N_aqc - 0 232-1 1 1
No. cycles N_cyc - 1 10 1 1
For each cycle: Cyc_time secs 0 232-1 1 1
Product Time Prod_time Year, Day, Month,
Hour
- - - -
Start Time Start_time Hour, Minute,
Sectond
- - - -
End Time End_time Hour, Minute,
Second
- - - -
For each AMV: AMV Final Body
Latitude lat ° -90 90 0.001 0.001
Longitude lon ° -180 180 0.001 0.001
Vector speed spd ms -1 0 500 0.1 0.1

<!-- source_page: 178 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 179 of 298

Parameter Mnemonic Units Min Max Prec Acc To
Direction dir ° 0 360 0.1 0.1
Temperature temp K 170 300 0.1 0.1
Height pres hPa 100 1050 50 1
Overall reliability OR - 0 100 1 1
Overall reliability excluding forecast OR_ex_fcast - 0 100 1 1
Estimated height error pp_err hPa 0 100 1 1
Results from each quality test qc_res - 0 1 - -
Channel Identifier chan_id - 1 12 1 1
RFF Quality Indicator RFF - 0 100 1 1
Satellite Zenith Sat_zen ° 0 90 0.1 0.1
Cloud target Cloud_target logical false true - -
Height consistency H_cons - 0 1 - -
Wind method Wind_mthd - 1 10 1 1
Fraction of land pixels in target area land_frac % 0 100 1 1
Land-sea flag land_sea_flag - 0 3 1 1
For each wind intermediate component:
Direction dir ° 0 360 0.1 0.1
Speed spd ms-1 0 500 0.1 0.1
For each Height Assignment method:
Pressure pres hPa 100 1050 50 1
Pressure SD pres_sd hPa 0 100 1 1
Temperature temp K 170 300 0.1 0.1
Temperature SD temp_sd K 0 100 1 1

<!-- source_page: 179 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 180 of 298

Parameter Mnemonic Units Min Max Prec Acc To
For each Height Assignment method
written to BUFR:

BUFR Code BUFR_code - 0 14 - -
Pressure pres hPa 100 1050 50 1
Temperature temp K 170 300 0.1 0.1
Table 33: List of required outputs for the Final AMV Product
Note: As mentioned in Section 9.3.2.6, the pressure value corresponding to the CCC method shall be temporarily stored in component 6 of the
array of height assignment methods to be written to the AMV BUFR file. Additionally, the pressure plus one standard deviation shall be stored
in component 8 of the mentioned array as an indication of the height error.

Note: As mentioned in Section 9.3.2.6, the pressure value corresponding to the forecast best-fit shall be stored in component 19 of the array of
height assignment methods in the AMV Intermediate Product. Besides, it shall be stored in component 10 of the array of height assignment
methods to be written to the AMV BUFR file.

Note: As mentioned in Section 9.3.2.6, the pressure value corresponding to the use of the OCA cloud-top height shall be stored in component
18 of the array of height assignment methods in the AMV Intermediate Product. Besides, it shall be stored in component 3 of the array of
height assignment methods to be written to the AMV BUFR file, as part of the AMV Final Product. Additionally, the OCA pressure plus one
standard deviation shall be stored in component 5 of the mentioned array as an indication of the height error.

Note: As mentioned in Section 9.3.2.6, the EBBT pressure of WV clear-sky and low-level cloudy AMVs shall be stored in component 17 of
the array of height assignment methods in the AMV Intermediate Product. Besides, it shall be stored in component 9 of the array of height
assignment methods to be written to the AMV BUFR file, as part of the AMV Final Product.

<!-- source_page: 180 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9.5 Future Enhancements
The following future enhancements shall be foreseen in the design of the algorithm:
 The use of the other channels, e.g. IR8.7 and IR9.7. These channels will be used in a similar
fashion to the IR10.8 channel.
 The use of ozone tracers.
 Image enhancement: The incorporation of new channels and new characteristics implies a
redefinition of the suitable algorithms. The possibility for new approaches also has to be taken
into account. The use of CLA information and the image enhancement of clear sky targets will
also be investigated.

AQC checks: Additional AQC checks may be introduced.
9.6 References
Reference Title Date Author(s)
NOAA Technical
Memorandum NESS 78
Satellite derived sea-surface
temperatures from NOAA spacecraft
6/76 Brower, Robert L.,
Gohrband, H.S., Pichel,
W.G., Signore, T.L. and
Walton, C.C.
Journal of Applied
Meteorology, Vol. 32,
No. 7
Operational Cloud-Motion Winds
from Meteosat Infrared Images
7/93 Schmetz, Johannes,
Holmlund, Kenneth et al.
Journal of Applied
Meteorology, Vol. 32,
No. 9
A comparison of Several Techniques
to Assign Heights to Cloud Tracers
9/93 Nieman, Stephen J.,
Schmetz, Johannes,
Menzel, W. Paul
Third International Wind
Workshop
Normalised Quality Indicators for
EUMETSAT Cloud-Motion Winds
6/96 Holmlund, Kenneth
Journal of Applied
Meteorology, Vol 34
Recursive Filter Objective Analysis
of Meteorological Fields:
Applications to NESDIS Operational
Processing
1/95 Hayden, Christopher M.,
Purser R. James
NOAA Technical
Memorandum NESDIS 43
A Primer for Tuning the Automated
Quality Control System and for
Verifying Satellite-Measured Drift
Winds
7/96 Hayden, Christopher M.,
Nieman, Steven J.

<!-- source_page: 181 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




10 CLOUD TOP HEIGHT PRODUCT GENERATION
10.1 Algorithm Configuration Information
10.1.1 Algorithm Name
Cloud Top Height (CTH)
10.1.2 Algorithm Identifier
EUM_MSG_CTH_A001
10.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 H.-J. Lutz CTH Baseline
1.1 24/6/97 H. K. Wilson Use of quality flag from intermediate CLA rather than final CLA.
1.2 25/7/05 G.Dew Revised description of fog indicator.
10.2 Inputs
The following data shall be available for the CTH product generation.

Parameter Mnemonic Units Min Max Prec Acc Res Source
Scenes type scenes_type - - - - pixel Intermediate CLA
product
Cloud top height cloud_top_height hPa 100 1050 50 1 pixel Intermediate CLA
product
Quality flag quality_flag - 0 255 1 1 pixel Intermediate CLA
product
Pressure levels of
ICAO standard
atmosphere
pressure hPa 100 1020 1 1 - Set-up parameters
Height of pressure
levels of ICAO
standard atmosphere
height m 0 1800
0
1 1 - Set-up parameters
Size of the CTH
processing segment
ps_size pixels 0 64 1 1 - Set-up parameter
Minimum number of
pixels
min_pixels pixels 1 25 1 1 - Set-up parameter
Coefficients to derive
height bands
a1 - 0 10 1 1 - Set-up parameter
a2 - 0 1000 50 50 - Set-up parameter
Maximum % of bad
pixels allowed in a CTH
processing segment
max_bad % 0 100 1 1 - Set-up parameter
Table 34: Data required for production of CTH Product

<!-- source_page: 182 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




10.3 Algorithm Functional Specification
10.3.1 Overview
The CTH product is an image-based GRIB Edition 2 encoded product which indicates the height of
the highest cloud on a CTH processing segment basis, as defined by ps_size. This product is intended
for use in aviation meteorology. The following requirements shall apply:
 The CTH product shall provide the height of the highest cloud for a CTH processing segment
with a vertical resolution of 300 metre height bands, hereafter called cth_height_band.
 The CTH product shall provide information about fog in the CTH processing segment.
10.3.2 Algorithm Description
10.3.2.1 Product Preparation
For the repeat cycle closest to the required extraction time of the CTH product, the scenes type and
cloud_top_height of the pixel-based intermediate CLA product output shall be used to derive the CTH
product. The data shall be grouped into CTH processing segments, which are defined by means of the
ps_size in the set-up parameters. The CTH processing segments shall cover the whole MPEF
processing area. All of the following steps shall be performed for each of the CTH processing
segments.
10.3.2.2 Extraction of the Cloud Top Height
Within each CTH processing segment, the scenes type shall be checked. If all pixels are clear, the
cth_height_band shall be set to a default value (e.g. 0) indicating ‘no cth_height_band derived, no
clouds in processing segment’. If at least min_pixels pixels in the CTH processing segment contain a
cloud, the highest cloud shall be extracted, i.e. the lowest value of the cloud_top_height (in units of
hPa) within the CTH processing segment. This value shall then be used to derive the cth_height_band
as follows:
 Using the ICAO standard atmosphere ( pressure and height) determine the pressure levels and
their corresponding heights for which the cloud_top_height values are greater than (p n and Zn)
and less than (pn+1 and Zn+1). As a Future Enhancement the ICAO standard atmosphere will be
replaced by forecast profiles.
 Using these values convert the cloud_top_height to geometrical height as follows:
ZCTH = Zn + ((ln(cloud_top_height) - ln(pn)) × (Zn+1 - Zn)) / (ln(pn+1) - ln (pn))
 To derive the final cth_height_band, use the truncated whole number of the following
expression: cth_height_band = a1 + (ZCTH / a2)
10.3.2.3 Derive the Amount of Fog in the CTH Processing Segment
One method of determining this would be to use the scenes type information to determine fog pixels,
then the CTH_quality_flag can be set indicating ‘fog/low stratus’. However, the precise method of
extracting fog information is a Future Enhancement, and hence the CTH_quality_flag shall by default
be set to 0 (i.e. no fog).
10.3.3 Automatic Quality Control (AQC)
Use the quality_flag from the intermediate CLA for the cloudy pixels identified within the CTH
processing segment, which indicates the quality of the cloud top height for these pixels. If more than

<!-- source_page: 183 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




max_bad percent of the cloudy pixels within the CTH processing segment indicate poor quality for the
cloud top height, then the CTH_quality_flag for the segment shall be set to ‘height poor quality’.
10.4 Outputs
The following data shall be produced for each CTH processing segment in the form of a GRIB
Edition 2 encoded product, a six-bit image plus two bits of quality information.

Parameter Mnemonic Units Min Max Prec Acc To
Height band of the cloud top height
of the highest cloud
cth_height_band - 0 63 1 1 CTH
product
CTH quality flag CTH_quality_fla
g
- 0 3 1 1 CTH
product
Table 35: Data produced for each CTH Processing Segment
Parameter Bit Meaning
CTH_quality_flag Bit 0:1 Fog in CTH segment
Bit 1:1 Poor Quality Height estimation

The CTH image itself has a size that is a multiple of 64, and is given by the equation:
( ( MPEF_MAX_IMG_WIDTH / CTHSetupParameters%ps_size + 63 ) / 64 )
where:
MPEF_MAX_IMG_WIDTH = 3712
CTHSetupParameters%ps_size = 3
This results in an image size of 1280 × 1280 pixels. The image area containing actual information is
given by:
MPEF_MAX_IMG_WIDTH/CTHSetupParameters%ps_size = 3712/3 = 1237.3 = 1237

This is rounded down to 1237 × 1237 pixels.
10.5 Prototyping and Testing
No prototype software and test data are available for this product.
10.6 Future Enhancements
The following Future Enhancements shall be foreseen in the algorithm design:
 The use of forecast data, pressure, temperature and specific humidity, rather than a standard
atmosphere.
 The provision of additional information, e.g. cloud type.
 The provision of height information in more than 6 bits.
10.7 References
None

<!-- source_page: 184 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




11 CLEAR SKY RADIANCES PRODUCT GENERATION
11.1 Algorithm Configuration Information
11.1.1 Algorithm Name
Clear Sky Radiances (CSR)
11.1.2 Algorithm Identifier
EUM_MSG_CSR_A001
11.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 H.-J. Lutz CSR Baseline
1.1 2/7/97 H. K. Wilson Updated to provide additional inputs for the modified
SCE algorithm.
1.2 9/12/97 H. K. Wilson Requirements Analysis clarification points added.
1.3 02/10/01 H.-J. Lutz Replaced Quality Flag by Quality Index
11.2 Inputs
11.2.1 Dynamic Application Data
As an input, level 1.5 image data of all channels for every repeat cycle shall be available for the CSR
processing in the form of radiances, or reflectances and brightness temperatures. Also the CSR product
results from the previous repeat cycle and the scenes type information from the Scenes Analysis of the
current repeat cycle shall be available.
See Table 36 that follows:

<!-- source_page: 185 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 186 of 298



Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Scenes type scenes_type - 0 255 1 1 pixel CLA int
Radiances/reflectances/
brightness temperatures
from all channels
RADchannel
REFLchannel
EBBTchannel
mWm-2sr-1(cm-1)-1 % K 0 - - - pixel Derived from Level 1.5
image data
CSR from previous repeat
cycle
prev_CSRchannel mWm -2sr-1(cm-1)-1 % K 0 - - - CSR processing
segment
CSR prev
Solar Zenith angle sol_zenith degree 0 180 0.01 0.01 pixel Derived from level 1.5 image
header data
Table 36: Dynamic Application Data required for CSR Product
11.2.2 Static Application Data
The following static application data shall be required:
Parameter Mnemonic Units Min Max Prec Acc Res Source
Size of the CSR processing segment ps_size pixel 1 64 1 1 - Set-up parameter
Day/night check threshold sol_zenith_day degree 0 180 1 1 - Set-up parameter
Number of required clear pixels threshold min_clear_pixel pixels 0 1024 1 1 - Set-up parameter
AQC temporal check threshold for channel group AQC_temporalgroup - - - - - - Set-up parameters
AQC SD check threshold for channel group AQC_SD group - - - - - - Set-up parameters
Data type for output (EBBT/REFL or radiance) OutDataType - - - - - - Set-up parameters
Coefficients A, B, C for quality index cloud fraction (array of 11 each) AFrac, BFrac, Cfrac - - - - - - Set-up parameters
Coefficients A, B, C for quality index standard deviation (array of 11
each)
AStd, BStd, CStd - - - - - - Set-up parameters
Table 37: Static Application Data required for CSR Product

<!-- source_page: 186 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




11.3 Algorithm Functional Specification
11.3.1 Overview
The Clear Sky Radiances product (CSR) provides radiances (in mWm-2sr-1(cm-1)-1), or reflectances
(in %) and brightness temperatures (in K), averaged over cloud-free pixels on a processing segment of
size as defined by ps_size, for all MSG channels except HRVIS. Within the MPEF the intermediate
CSR product which is derived for every repeat cycle is used as an input for the Scenes Analysis for
the following repeat cycle and it is used as an input for calibration monitoring. The final CSR product
is the intermediate product which was produced from the repeat cycle closest to the required
extraction time. It can be used by the end-users to derive several other meteorological products on that
scale, i.e. SST, LST, radiation budget components.
The following general requirements shall
be applied for the CSR product:
 As defined with the switch ‘Data type for output’ in the set-up data set, the CSR product shall
provide radiances (in mWm-2sr-1(cm-1)-1) or reflectances (in %), averaged over all cloud-free
pixels on a CSR processing segment basis for the solar channels VIS0.6, VIS0.8 and NIR1.6,
and for the infrared channels WV7.3, IR3.9, IR8.7, IR9.7, IR10.8, IR12.0 and IR13.4, and the
CSR product shall provide radiances (in mWm-2sr-1(cm-1)-1) or brightness temperatures (in K)
on a CSR processing segment averaged over all cloud-free pixels and all pixels covered by a
low-level cloud for channel WV6.2.

The algorithm shall be able to derive the CSR product for HRVIS; this is seen as a Future
Enhancement. The CSR product for the HRVIS shall be able to be derived on two different
processing segment scales, one which is collocated with the other solar channels (e.g.
nominally 96 × 96 HRVIS pixels) and one with e.g. 32 × 32 HRVIS pixels, to maintain the
nominal high resolution differences.
The algorithm is described in detail in the next section. The processing of the algorithm which shall
be applied to the data from every repeat cycle is as follows:

Step 1 Image segmentation: Divide the image data into CSR processing segments.

Step 2 Extraction of clear pixels within the processing segments: Use the scenes type
information from Cloud Analysis to extract the clear pixels and the pixels with lowlevel clouds within the processing segment. If the number of clear pixels, hereafter
called clear_IR_pixels, is lower than a threshold, min_clear_pixel, the following steps
will be skipped for all channels, except channel WV6.2. If the number of clear and lowlevel cloud pixels, hereafter called clear_WV6.2_pixels, is lower than the same
threshold (min_clear_pixel), then the following steps will also be skipped for channel
WV6.2.

Step 3 Solar zenith angle check: Use the solar zenith angle to determine whether the clear
pixels have day or night conditions. If the number of clear pixels under day conditions,
hereafter called clear_VIS_pixels, is smaller than min_clear_pixel the following steps
will be skipped for the solar channels.

<!-- source_page: 187 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Step 4 Determination of the CSR: Determine the CSR for each processing segment by
averaging the radiances/brightness temperatures of channel WV6.2 for all
clear_WV6.2_pixels and of the other infrared channels for all clear_IR_pixels, and by
averaging the radiances/reflectances of the solar channels
for all clear_VIS_pixels with
day conditions.

Step 5 Determination of the location of the derived CSR: Determine the centre of the clear
pixels within the processing segment. This defines the location of the derived CSR
information, for each CSR processing segment.
11.3.1.1 Algorithm Description
The above listed steps shall be performed for each repeat cycle. They are described in detail in the
following sections. All static application data used in the algorithm (i.e. static thresholds, parameters)
shall be configurable.
11.3.1.2 Step 1: Image Segmentation
For each repeat cycle the level 1.5 image data shall be divided into CSR processing segments, which
are defined by means of ps_size in the set-up parameters, hereafter called CSR processing segment.
The CSR processing segments shall cover the MPEF processing area. All of the following steps shall
be performed for each of the CSR processing segments.
11.3.1.3 Step 2: Extraction of Clear Pixels within the CSR Processing Segments
The scenes type provided by the Cloud Analysis shall be used to determine how many pixels in the
CSR processing segment are clear (clear_IR_pixels) and how many are clear or covered by a lowlevel cloud (clear_WV6.2_pixels). For all IR channels except WV6.2 the following check shall be
applied:
If clear_IR_pixels is lower than a threshold (min_clear_pixel), a default value shall be set for these
channels and the quality flag shall be set indicating ‘no CSR derived for IR channels, insufficient
number of clear pixels’ and the following steps shall be skipped.
For channel WV6.2 the following check shall be applied:
If clear_WV6.2_pixels is lower than a threshold (min_clear_pixel), a default value shall be set for this
channel and the quality flag shall be set indicating ‘no CSR derived for WV channels, insufficient
number of clear pixels’ and the following steps shall be skipped.
The percentage of the clear pixels (or clear and low-level cloud pixels for WV6.2) within the CSR
processing segment used to determine the CSR shall be calculated.
11.3.1.4 Step 3: Solar Zenith Angle Check
If the number of clear_IR_pixels is greater than min_clear_pixel, for all clear pixels within the
processing segment, the solar zenith angle data (sol_zenith) shall be used to determine whether it was
acquired during day or night, i.e. if the sol_zenith is lower than a threshold (sol_zenith_day), it is day
(clear_VIS_pixels) else it is night. If clear_VIS_pixels is smaller than a threshold (min_clear_pixel),
then the CSR shall not be derived for the solar channels. A default value shall be set for the CSR
product and the quality flag shall be set indicating ‘no CSR derived for the VIS channels, insufficient
number of clear daytime pixels’ and the following steps shall be skipped for these channels.

<!-- source_page: 188 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The percentage of the clear VIS pixels within the CSR processing segment shall be calculated.
11.3.1.5 Step 4: Determination of the CSR
For the infrared channels except channel WV6.2 the CSR shall be derived by averaging the radiances
or brightness temperatures over all pixels identified as clear_IR_pixels within the CSR processing
segment.
For channel WV6.2 the CSR shall be derived by averaging the radiances or brightness temperatures
over all pixels identified as clear_WV6.2_pixels within the CSR processing segment.
For the solar channels the CSR shall be derived by averaging the radiances or reflectances over all
pixels identified as clear_VIS_pixels within the CSR processing segment.
The standard deviation of the radiances/reflectances/brightness temperatures of all the clear pixels
contributing to the CSR in each processing segment shall be calculated for each channel.
11.3.1.6 Step 5: Determination of the Location of the CSR
Because the clear pixels in a processing segment are not uniformly distributed and they may not be
representative of the mid-point of a segment, the location of the centre of the used pixels shall be
derived for each processing segment. This shall be performed by calculating the arithmetic mean of
the line and element position of all pixels used to derive the CSR and by converting the line and
element to latitude and longitude. This latitude and longitude shall determine the location of the
derived CSR for that processing segment. This location shall be determined separately for the solar
channels, and channel WV6.2, and the other infrared channels.
The final CSR product for dissemination shall be the intermediate CSR product which is extracted
from the repeat cycle closest to the required dissemination time.
11.3.2 Automatic Quality Control (AQC)
The automatic quality control (AQC) of the CSR product consists of the Quality Index and an AQC
flag providing information about the temporal and spatial consistency of the results. The Quality
Index of the CSR product shall be determined for each channels as follows:
QIchan = ( QIFracchan * QIStdchan ) / 100.0
where:

QIFracchan = ((tanh((percentClearPixels**CFracchan) / BFracchan )) ** AFracchan ) * 100.
QIStdchan = ((tanh(BStdchan / (StandardDeviationchan ** CStdchan ))) ** AStdchan ) * 100.

In addition to the quality index, the temporal and spatial consistency of the product shall be
determined as follows:
 The temporal consistency check shall compare the CSR results of the current repeat cycle for
each processing segment and each of the channels with the results of the previous repeat cycle.
If the highest difference for each channel group between the two results exceeds a threshold,
AQC_Temporalgroup, the quality flag shall be set indicating ‘poor quality, temporal check’ for
that processing segment and channel group. The thresholds are channel group dependent.
The spatial consistency check shall consist of determining whether there are land and water pixels in
the same processing segment, using the scenes type. If there are mixed pixels in a segment, the quality
flag shall be set indicating ‘poor quality, spatial check’ for that processing.

<!-- source_page: 189 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 190 of 298

11.4 Outputs
The following list of output parameters shall be generated per CSR processing segment for both the final and the intermediate CSR products.

Parameter Mnemonic Units Min Max Prec Acc To
CSRchannel_1
CSRchannel_2

CSRchannel_N
mWm -2sr-1(cm-1)-1
mWm-2sr-1(cm-1)-1
...
mWm-2sr-1(cm-1)-1
0
0
...
0
-
-
...
-
-
-
...
-
-
-
...
-
CSR final & intermediate products
Location of the CSR for the solar
channels (lat/lon)
CSR_VIS_lat
CSR_VIS_lon
degree
degree
-90°
-180°
90°
180°
0.1
0.1
0.1
0.1
CSR final & intermediate products
Location of the CSR for channel
WV6.2 (lat/lon)
CSR_WV6.2_lat
CSR_WV6.2_lon
degree
degree
-90°
-180°
90°
180°
0.1
0.1
0.1
0.1
CSR final & intermediate products
Location of the CSR for the IR
channels (lat/lon)
CSR_IR_lat
CSR_IR_lon
degree
degree
-90°
-180°
90°
180°
0.1
0.1
0.1
0.1
CSR final & intermediate products
Quality flag CSR_qua lity_flag - - - - - CSR final & intermediate products
Percentage of clear pixels
contributing to the CSR for each
segment for each channel
frac_clear % 0 100 0.1 0.1 CSR final & intermediate products
SD of clear pixels contributing to
CSR for each segment for each
channel
sd_pixels
chan - - - - - CSR final & intermediate products
Table 38: Output parameters per CSR Processing Segment for both final and intermediate CSR products

<!-- source_page: 190 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 191 of 298

Parameter Value Meaning
CSR_quality_flag Bit 0: 1 No CSR derived for VIS channels, insufficient number of clear day pixels
Bit 1: 1 No CSR derived for WV channels, insufficient number of pixels
Bit 2: 1 No CSR derived for IR channels, insufficient number of pixels
Bit 3: 1 AQC Temporal Check failed for VIS channels
Bit 4: 1 AQC Temporal Check failed for WV channels
Bit 5: 1 AQC Temporal Check failed for IR channels
Bit 6: 1 AQC Spatial Check failed
Bit 7: 1 AQC SD Check failed for VIS channels
Bit 8: 1 AQC SD Check failed for WV channels
Bit 9: 1 AQC SD Check failed for IR channels
Table 39: CSR Quality Flags and Bit breakdown
11.5 Prototyping and Testing
No prototyping activities are foreseen for the CSR product.
11.6 Future Enhancements
The following enhancements shall be foreseen in the algorithm design:
 Derivation of CSR for HRVIS.
11.7 References
None.

<!-- source_page: 191 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




12 ALL SKY RADIANCES PRODUCT GENERATION
12.1 Algorithm Configuration Information
12.1.1 Algorithm Name
All Sky Radiances (ASR)
12.1.2 Algorithm Identifier
EUM_MSG_ASR_A001
12.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 08/04/2008 H-J. Lutz, O. Samain ASR Baseline
12.2 Inputs
12.2.1 Dynamic Application Data
As an input, level 1.5 image data of all channels for every repeat cycle shall be available for the ASR
processing in the form of brightness temperatures. Also, the ASR product results from the previous
repeat cycle and the scenes type information from the Scenes Analysis of the current repeat cycle
shall
be available.

<!-- source_page: 192 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 193 of 298


Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Scenes type scenes_type - 0 255 1 1 pixel CLA int
Reflectance, radiances and brightness
temperatures from all channels
EBBTchannel % mWm-2sr-1(cm-1)-1
or kelvin
0 - - - pixel Derived from Level 1.5
image data
ASR from previous repeat cycle prev_ASR channel % mWm -2sr-1(cm-1)-1
or kelvin
0 - - - ASR processing
segment
ASR prev
Solar Zenith angle sol_zenith degree 0 180 0.01 0.01 pixel Derived from Level 1.5
image header data
Table 40: ASR Product: Dynamic Application Data
12.2.2 Static Application Data
The following static application data shall be required:

Parameter Mnemonic Units Min Max Prec Acc Res Source
Size of the ASR processing segment ps_size Pixel 1 64 1 1 - Set-up parameter
Day/night check threshold sol_zenith_day Degree 0 180 1 1 - Set-up parameter
Minimum number of pixels under day conditions min_day_pixel % 0 100 1 1 - Set-up parameter
Minimum number of valid pixels for IR/WV
channels for ASR subproduct xy (array of 6)
Min_valid_pixel % 0 100 1 1 - Set-up parameters
Minimum number of valid pixels for VIS
channels for ASR subproduct xy (array of 6)
Min_valid_VIS_pixel % 0 100 1 1 - Set-up parameters
Coefficients A, B, C for quality index cloud
fraction (array of 11 times 6 each)
AFrac, BFrac,
Cfrac
- - - - - - Set-up parameters
Coefficients A, B, C for quality index standard
deviation (array of 11 times 6 each)
AStd, BStd, CStd - - - - - - Set-up parameters
Table 41: ASR Product Static Application Data required

<!-- source_page: 193 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





12.3 Algorithm Functional Specification
12.3.1 Overview
The All Sky Radiances product (ASR) provides brightness temperatures (in K) for the infrared
channels, averaged over the following categories:
 ASR-all using all pixels within a segment
 ASR-clear using all clear pixels within a segment
 ASR-cloudy using all cloudy pixels within a segment
 ASR-low using all low-level cloud pixels within a segment
 ASR-mid using all mid-level cloud pixels within a segment
 ASR-high using all high-level cloud pixels within a segment
The intermediate ASR product is derived for every repeat cycle and the final ASR product is the
intermediate product which was produced from the repeat cycle closest to the required extraction
time. The size of the processing segment is defined by a setup parameter ps_size. It can be used by the
end-users to derive several other meteorological products on that scale, i.e. SST, LST, radiation
budget components.
For the visible channels, the ASR product provides missing values. Radiance or reflectance values
shall be provided for these channels as a future enhancement.
The algorithm shall also be able to derive the ASR product for HRVIS; this is seen as a Future
Enhancement. The ASR product for the HRVIS shall be able to be derived on two different
processing segment scales, one which is collocated with the other solar channels (e.g. nominally
96 × 96 HRVIS pixels) and one with 32 × 32 HRVIS pixels, to maintain the nominal high resolution
differences.
The algorithm is described in detail in the next section. The processing of the algorithm which shall

be applied to the data from every repeat cycle is as follows:
Step 1 Image segmentation
Step 2 Solar zenith angle check
Step 3 Extraction of valid pixels for the ASR sub-products within the processing segments
Step 4 Determination of the ASR
Step 5 Determination of the location of the derived ASR
12.3.1.1 Algorithm Description
The above listed steps shall be performed for each repeat cycle. They are described in detail in the
following sections. All static application data used in the algorithm (i.e. static thresholds, parameters)
shall be configurable.
12.3.1.2 Step 1: Image Segmentation
For each repeat cycle the level 1.5 image data shall be divided into processing
segments, which are defined by means of ps_size in the set-up parameters, and which
are hereafter called ASR processing segments. The ASR processing segments shall
cover the MPEF Processing Area. All of the following steps shall be performed for
each of the ASR processing segments.

<!-- source_page: 194 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




12.3.1.3 Step 2: Solar Zenith Angle Check
The solar zenith angle shall be used to determine whether the clear pixels have day or
night conditions. A pixel is regarded as “under day conditions” if the solar zenith angle
is smaller than the threshold solzen_day. The number of pixels under day conditions
shall be given as a percentage of the total number of pixels. If the number of pixels
under day conditions is smaller than min_day_pixel, the following steps shall be
skipped for the VIS channels and the ASR product shall set a value stating “number of
valid pixels under day conditions in the segment smaller than min_day_pixel”.
12.3.1.4 Step 3: Extraction of valid pixels for ASR sub-products within ASR
Processing Segments
The scenes type provided by the Cloud Analysis shall be used to extract the valid
pixels for the ASR sub-products within the processing segments, as follows:
 All pixels within a segment for sub-product ASR-all
 All clear pixels within a segment for sub-product ASR-clear
 All cloudy pixels within a segment for sub-product ASR-cloudy
 All low-level cloud pixels within a segment for sub-product ASR-low
 All mid-level cloud pixels within a segment for sub-product ASR-mid
 All high-level cloud pixels within a segment for sub-product ASR-high
For each of the sub-products the number of valid pixels, hereafter called
valid_pixel_xy (xy stands for the sub-products) is calculated as a percentage (%)
of the total number of pixels. In addition to that, the solar zenith angle is used to
determine how many valid pixels have day conditions, hereafter called
valid_VIS_pixels_xy, which is also given as a percentage of the total number of
pixels.

12.3.1.5 Step 4: Determination of the ASR
If the percentage valid_pixels_xy (xy stands for the sub-products) for the IR/WV
channel is larger than or equal to the threshold min_valid_pixel_xy, the ASR
sub_product shall be calculated for all IR/WV channels. In addition, if the
percentage valid_VIS_pixels_xy is larger than or equal to the threshold
min_valid_VIS_pixels_xy, the ASR sub-product shall be calculated for the VIS
channels.
The ASR sub-products are generated for each processing segment per channel
using all pixels which are valid for the channel and the sub-product. The
following values are determined per segment and channel:
 Mean brightness temperatures
 Standard deviation of the brightness temperatures
 Brightness temperatures maximum value
 Brightness temperatures minimum value
Otherwise, if the percentage valid_pixels_xy for the IR/WV channel is smaller
than min_valid_pixel_xy, the values of the sub-product is set to a value
indicating “percentage of valid pixels in the segment is smaller than

<!-- source_page: 195 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




min_valid_pixel_xy for product xy”.
The same is applied to the VIS ch annels, i.e. if the percentage
valid_VIS_pixels_xy is smaller than min_valid_VIS_pixel_xy, the value of the
sub-product is set to a value indicating “percentage of valid pixels in the segment
is smaller than min_valid_pixel_xy for product xy”.
With the land-sea mask, the percentage of sea pixels within each segment is
determined.
12.3.1.6 Step 5: Determination of the location of the derived ASR
The centre of the processing segment shall be regarded as the location of the
ASR product. The location shall be given as latitude and longitude.
The centre of the processing segment shall be regarded as the location of the ASR product. The
location shall be given as latitude and longitude.
12.3.1.7 Automatic Quality Control (AQC)
The automatic quality control (AQC) of the ASR product consists of the Quality Index and an AQC
flag providing information about the temporal and spatial consistency of the results. The Quality
Index of the ASR product shall be determined for each channel and ASR sub-product (xy) as follows:

100/).( StdFrac QIQIQI 
Equation 46

where:


FracFrac
A
Frac
C
Frac BpixelsclearPercentTANHQI /__100 
Equation 47

Std
Std
A
C
Std
Std
eviationStandard_d
BTANHQI














 100

Equation 48
and where AFrac, BFrac, CFrac, AStd, BStd, CStd are specific for each channel.

<!-- source_page: 196 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 197 of 298

12.4 Outputs
The following list of output parameters shall be generated per ASR processing segment for both the final and the intermediate ASR products.

Parameter Mnemonic Units Min Max Prec Acc To
ASR mean values for the 11 channels and 6
sub-products
ASRchan, subproduct % mWm-2sr-1(cm-1)-1
or kelvin
0

-

-

-

ASR final and intermediate
products
Standard deviation for the 11 channels and 6
sub-products
STDchan, subproduct % mWm-2sr-1(cm-1)-1
or kelvin
0

-

-

-

ASR final and intermediate
products
Centre location of the ASR segment (lat/lon) ASR_lat
ASR_lon
degree
degree
-90
-180
90
180
0.1
0.1
0.1
0.1
ASR final and intermediate
products
Quality flags QIchan, sub-product
QIFracvchan, subproduct
QIStdchan, subproduct
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
ASR final and
intermediate products
Percentage of clear pixels in the segment ASR_clear % 0 100 0.1 0.1 ASR final and
intermediate products
Percentage of cloudy pixels in the segment ASR_cloudy % 0 100 0.1 0.1 ASR final and
intermediate products
Percentage of low-level cloud pixels in the
segment
ASR_low % 0 100 0.1 0.1 ASR final and
intermediate products
Percentage of mid-level cloud pixels in the
segment
ASR_mid % 0 100 0.1 0.1 ASR final and
intermediate products
Percentage of high-level cloud pixels in the
segment
ASR_high % 0 100 0.1 0.1 ASR final and
intermediate products
Table 42: Output parameters per ASR processing segment for both final and intermediate ASR products

<!-- source_page: 197 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




12.5 Prototyping and Testing
No prototyping activities are foreseen for the ASR product.
12.6 Future Enhancements
The following enhancements shall be foreseen in the algorithm design:
 The derivation of reflectance / radiance values for the visible channels
 The derivation of ASR for HRVIS.
12.7 References
None.

<!-- source_page: 198 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




13 CLIMATE DATA SET PRODUCT GENERATION
13.1 Algorithm Configuration Information
13.1.1 Algorithm Name
Climate Data Set (CDS)
13.1.2 Algorithm Identifier
EUM_MSG_CDS_A001
13.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 R. Schraidt CDS Baseline
1.1 24/6/97 H. K. Wilson Clarifications added and errors corrected
13.2 Inputs
13.2.1 Dynamic Application Data
See Table 43 on following page:

<!-- source_page: 199 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 200 of 298

Parameter Mnemonic Units Min Max Prec Acc Res Source
Image data (cha_tbp_CDS) image_i mWm -2sr-1(cm-1) -1 0 2 10-1 1 1 pixel Derived from level 1.5 data
Scenes Type scenes_type - - - - - pixel CLA intermediate
Semi-transparency flag st_flag - - - - - pixel CLA intermediate
Effective Cloud Amount cloud_amount % 0 100 1 1 pixel CLA intermediate
Cloud Top Temperature cloud_top_temp K 170 300 0.1 0.1 pixel CLA intermediate
Atmospheric correction tables
for channel
atm_corr_j mWm-2sr-1(cm-1)-1 0 - - - pixel RTM
Sun zenith angle sun_zen degrees 0 180 0.1 0.1 pixel Derived from level 1.5 data
Spacecraft zenith angle sat_zen degrees 0 90 0.01 0.01 pixel Derived from level 1.5 data
Sun/spacecraft azimuth
difference
sunsat_azi degrees 0 360 0.1 0.1 pixel Derived from level 1.5 data
Table 43: Climate Data Set: Dynamic Application Data inputs
13.2.2 Static Application Data
Parameter Mnemonic Units Min Max Prec Acc Res Source
CDS segment structure seg_str uct_CDS - - - - - - Set-up
CDS processing area proc_area_CDS - - - - - - Set-up
Channels to be processed cha_tbp_CDS - - - - - - Set-up
Channels to be corrected cha_tbc_CDS - - - - - - Set-up
Scene types sce_typ - - - - - - Set-up
Sunglint threshold sun_glnt_tresh  0 90 0.1 0.1 - Set-up
Minimum cluster size threshold clust_tresh pixels 1 1024 - - - Set-up
Table 44: Climate Data Set: Static Application Data inputs

<!-- source_page: 200 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




13.3 Algorithm Functional Specification
13.3.1 Overview
This algorithm is responsible for the generation of the Climate Data Set. The product contains results
of the image pixel classification process, which is performed by Scenes Analysis and Cloud Analysis,
together with calibration tables for the processed image channels, navigation information and sun and
spacecraft position angles. As a baseline all spectral channels are to be processed.
The classification process determines which scenes (sea or land surfaces, types of clouds) are likely to
have produced the radiation measured by the satellite. This is done on a pixel-by-pixel basis. To
reduce the amount of information the processed images are segmented according to the CDS
Processing Segment structure (the segments being of synoptic scale, e.g. 32 × 32 pixels) and the
pixels of a segment that are classified as belonging to the same scene type are combined into a cluster
from which statistical information is derived which is finally put into the CDS product.
13.3.2 Algorithm Description
The following steps shall
be performed in order to derive the CDS product:

Step 1 Derive CDS processing segment results.
For each CDS processing segment contained in the processing area of the CDS product
perform the following processing steps:
A. Remove all pixels of type ‘Unknown’ from further processing.
B. Using the st_flag separate the pixels of each cloud type into two sub-types, opaque
and semi-transparent.
C. For all possible surface types and all possible cloud sub-types calculate the mean and
the standard deviation in all the requested channels (cha_tbp_CDS) from the
uncorrected pixels classified (by Cloud Analysis) with the given scene type and count
the number of pixels within the cluster.
D.
Remove all clusters with the number of pixels smaller than a threshold (clust_tresh)
from further processing.
E. For each surface type and for each IR channel requested for correction
(cha_tbc_CDS), use the cluster pixel mean count to calculate the atmospheric
absorption corrected mean count as follows:
1. Derive from the TOA radiance a surface temperature by interpolating the
RTM Atmospheric Correction Table.
2. Convert the surface temperature to channel surface radiance by applying the
channel-specific Planck function..
3. Convert the channel surface radiance to an atmospheric absorption corrected
count value by inverse calibration.
4. Set mean effective cloud amount to 0.
F. For the cloud sub-types, derive from the CLA effective cloud amount the mean
effective cloud amount.

<!-- source_page: 201 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




G. For each cloud sub-type and for each IR channel requested for correction
(cha_tbc_CDS), calculate the mean count corrected for atmospheric absorption and
potentially corrected for semi-transparency as follows:
1. Calculate the mean cloud_top_temp from the intermediate CLA product.
2. Convert the cloud_top_temp to channel radiance.
3. Convert the IR channel radiance to a corrected count value.
H. Calculate the latitude and the longitude of the centre (in terms of pixels) of the
processing segment.
I. Get the zenith angles and the difference of the azimuth angles of the sun and the
spacecraft at the centre of the segment for the time when the centre is scanned.
J. Calculate whether the segment centre fulfils the sunglint condition, i.e. might be
affected by sunglint. If the following condition is satisfied, the segment may be
affected by sunglint:
sun_glnt_tresh > arccos[cos(sun_zen) * cos(sat_zen) - (sin(sun_zen) * sin(sat_zen) * cos(sunsat_azi))]
K. Store the calculated values, together with the segment row and column numbers and
the scene classification identifiers, into the CDS product.
Step 2 For the IR and WV channels used for the CDS product generation, calculate tables
that convert the IR pixel counts to temperatures by calibrating each possible pixel
count (0, ... , 210-1) to its channel TOA radiance and transforming the radiance to a
temperature by means of the channel-specific Planck function.
Note: Applying the count/temperature conversion tables to uncorrected pixel counts
provides EBBTs. Applying them to corrected counts results in surface temperatures
(sea, land or cloud top).

Step 3 Construct the CDS product header as described in the reference.
13.3.3 Automatic Quality Control (AQC)
No AQC check is required; the input data are already quality-controlled.
13.4 Outputs
The following data shall be output:
Note: The format guide given in Section 13.7 is intended as a reference only, the format information
contained within it will need to be modified to incorporate the differences between the MTP and MSG
satellites, e.g. increased number of channels, different satellite-specific information.

<!-- source_page: 202 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Parameter Mnemonic Units Min Max Prec Acc To
Count/Temp Conversion Table C_T_tables counts, K - - - - CDS
Per segment:
Segment row number row - 0 3712 1 1
Segment column number column - 0 3712 1 1
Latitude of segment centre lat  –90 90 0.1 0.1
Longitude of segment centre lon  –180 180 0.1 0.1
Sun zenith angle (segment
centre)
sun_zen_c  0 180 0.1 0.1
Spacecraft zenith angle sc_zen_c  0 90 0.1 0.1
Sun/spacecraft azimuth
difference
az_diff  0 360 0.1 0.1
Sunglint indicator sunglint - - - - -
No. of scene clusters in
segment
no_scenes - 0 64 1 1
Per scene cluster in segment:
No. of pixels in cluster no_pixs pixels 1 1024 1 1
Mean effective cloud amount mean_ec % 0 100 1 1
Per channel to be processed:
Mean pixel count mean_count counts 0 - 1 1
SD of cluster pixel counts sd_count counts 0 - - -
Per channel to be corrected:
Corrected mean pixel count c_mean_count counts 0 - 1 1
Table 45: Climate Data Set: Required outputs parameter definition
13.5 Prototyping and Testing
No prototype software and test data are available for this product.
13.6 Future Enhancements
No Future Enhancements are planned.
13.7 References
Reference Title Date Issue Author(s)
EUM FG 4 The Meteosat Archive, Format Guide No. 4,
Climate Data Set (CDS), Open MTP Format
02/96 1.0

<!-- source_page: 203 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




14 HIGH RESOLUTION PI PRODUCT GENERATION
14.1 Algorithm Configuration Information
14.1.1 Algorithm Name
High Resolution Precipitation Index (HPI)
14.1.2 Algorithm Identifier
EUM_MSG_HPI_A001
14.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 R. Schraidt GPI Baseline
1.1 12/6/97 H. K. Wilson Specification updated in line with latest GPCP
requirements, clarifications added and errors corrected.
1.2 25/7/05 A. Koch Output table split into two tables with additions.
14.2 Inputs
Parameter Mnemonic Units Min Max Prec Acc Res Source
Processing area
definition as lat/lon
boundaries
proc_area_HPI degree 40 65 1 1 - Set-up
PI segment structure
as equal angle
lat/lon areas
seg_struct_HPI degree 0 1 0.1 0.1 - Set-up
Number of EBBT
histogram classes
no_hist_HPI - 0 24 1 1 - Set-up
EBBT histogram
class thresholds
T_thresh_HPI K 180 280 1 1 - Set-up
Scaling factor scal_fact - 10000 10000 1 1 - Set-up
Backup parameter backup_HPI - 0 1 - - - Set-up
IR channel to be
processed
cha_tbp_HPI - 1 12 - - - Set-up
EBBT image data
(cha_tbp_HPI)
EBBT_ima K 180 280 0.1 0.1 pixel Derived from
level 1.5
image data
Table 46: High Resolution Precipitation Index Product Inputs

<!-- source_page: 204 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




14.3 Algorithm Functional Specification
14.3.1 Overview
This algorithm is responsible for the generation of the precipitation index data set EUMETSAT have
to provide to the Global Precipitation Climatology Project (GPCP).
The distribution of water in the atmosphere, its transport and its diurnal and seasonal change play an
important role in the Earth’s weather and climate. Precipitation is a meteorological parameter which is
important in climatological studies, general circulation studies and for the validation of numerical
weather prediction (NWP) models. Because there is rather limited information about the amount and
distribution of precipitation in many regions, the use of satellite data can provide the required
information.
The precipitation index generation is based on the relationship between the channel TOA radiance
equivalent black body temperature (EBBT) of clouds and convective rainfall. The idea of this
relationship is that clouds with cold cloud tops are convective rain-bearing clouds. This means that
cloudy pixels colder than a configurable threshold temperature are counted because they are assumed
to contribute to rainfall. The scheme is a cloud indexing method based on the pixel values of an IR
channel.
The default HPI processing area covers a box bounded by  40 of latitude and  50 of longitude
from the SSP. It is segmented into equal angle latitude/longitude areas where the default size of a
processing segment is 1
o × 1o latitude/longtitude.
Precipitation Index (HPI) values for the different HPI processing segments are currently derived from
satellite infrared image data for the synoptic hours (every three hours starting with 03:00 UTC). For
MSG, this frequency will remain unaltered. Per run of the HPI Product Generation task an HPI data
set is generated. All HPI data sets of a day are put into the Final HPI product providing a temporal and
spatial distribution of the precipitation indices of the day. The precipitation indices are based on the
black body temperatures (EBBT) being equivalent to the IR pixel counts of a particular IR channel
(nominally the IR10.8µm channel). In addition to the precipitation indices, the final HPI product
contains also per processing segment the EBBT mean for each individual run (intermediate product))
and the variance of the EBBT means of the individual runs of the day.
The precipitation indices are derived as EBBT class histograms over each processing segment by
assigning the pixels of the processing segment to the EBBT classes according to their EBBT value.
The number of pixels in the cold EBBT classes are indicative of the likelihood of precipitation.
14.3.2 Algorithm Description
The following steps shall
be performed in order to derive the HPI product:
Step 1 At the first run of the HPI product of a day (nominally 03:00 UTC, i.e. the repeat
cycle covering 02:45 to 03:00 UTC), initialise the accumulative PI product regardless
of whether an image is available for processing or not.

Step 2 At the last run of the HPI product of a day (nominally 00:00 UTC the following day),
produce the final HPI product even if no processable image or backup image is
available.

<!-- source_page: 205 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





Step 3 Process the level 1.5 image data from the processing cycle that matches the requested
image recording time. If that image is not available or of bad quality, process a backup
image as specified by the backup parameter. The backup parameter specifies the
number of images before the nominal extraction time than can be used for backup
purposes. The most recently available image should be used. If the backup image is
not available or of bad quality, mark in the product header the HPI data set as missing
and issue an error message, otherwise mark in the product header the availability of
the HPI data set with the time of the used image.

Step 4 Perform HPI product data set generation.
For each HPI processing segment contained in the processing area of the HPI product:
A. For each pixel in the processing segment increase the histogram count of
that EBBT class which corresponds to the pixel’s EBBT value.
B. Calculate the mean and the variance of the EBBT values of all pixels in
the processing segment.
C. Divide the number of pixels in each EBBT class by the total number of
pixels in the processing segment and multiply the quotient by the scaling
factor (scal_fact).

Step 5 Generate the final HPI product. After completion of the generation of the last HPI
data set of the day and even if the last accumulation was not possible:
A. Put all HPI data sets of the day into the Final HPI product.
14.3.3 Automatic Quality Control (AQC)
The header of the HPI product shall indicate which intermediate HPI products could not be produced
due to missing/bad quality images.
14.4 Outputs
The following data, for intermediate and final products, shall be output:
14.4.1 Intermediate Product
Parameter Mnemonic Units Min Max Prec Acc To
HPI Header: HPI Intermediate
Nominal Year of Product HPI_year Year 1996 2020 1 1
Nominal Day of the Year HPI_day Day 0 366 1 1
Nominal Repeat Cycle of
Product
HPI__nom_rc - 1 96 1 1
For each latitude and
longitude:

For each EBBT histogram
class as defined by the
set-up parameter:

HPI count HPI_count - - - - -

<!-- source_page: 206 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Parameter Mnemonic Units Min Max Prec Acc To
Mean of the EBBT values EBBT_mean K 170 300 0.1 0.1
SD of the EBBT values EBBT_SD K 0 - - -
Table 47: High Resolution Precipitation Index Intermediate Product outputs
14.4.2 Final Product
Parameter Mnemonic Units Min Max Prec Acc To
HPI Header: HPI Final
Nominal Year of Product HPI_year Year 1996 2020 1 1
Nominal Day of the Year HPI_day Day 0 366 1 1
Nominal Repeat Cycle of
Product
HPI__nom_rc - 1 96 1 1
Size of data records HPI_rec_size Bytes 0 50000 1 1
Number of data records
(including header)
HPI_rec_no - 0 1 1
Number of repeat cycles
collected
HPI_rc_used - 0 96 1 1
Number of repeat cycles
missing
HPI_rc_missing - 0 96 1 1
Repeat cycles collected (array
of 96 values, detailing which
rc were used, nominally 12,
24, 36, 48, 60, 72, 84, 96)
HPI_rc_missing - 1 96 - -
Per intermediate HPI
product:

For each latitude and
longitude:

For each EBBT histogram class
defined by set-up parameter:

HPI count HPI_count - - - - -
Mean of the EBBT values EBBT_mean K 170 300 0.1 0.1
SD of the EBBT values EBBT_SD K 0 - - -
Table 48: High Resolution Precipitation Index Final Product outputs
14.5 Prototyping and Testing
The MTP MPEF HPI software (currently operational) is available as a prototype.
14.6 Future Enhancements
The redefinition of the HPI product in cooperation with the GPCP may be required.
14.7 References
None

<!-- source_page: 207 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




15 ISCCP DATA SET PRODUCT GENERATION
15.1 Algorithm Configuration Information
15.1.1 Algorithm Name
ISCCP Data Set (IDS)
15.1.2 Algorithm Identifier
EUM_MSG_IDS_A001
15.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 R. Schraidt IDS Baseline
1.1 12/6/97 H. K. Wilson Clarifications added and errors corrected.
15.2 Inputs
See Table 49 on following page.

<!-- source_page: 208 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 209 of 298


Parameter Mnemonic Units Min Max Prec Acc Source
Image data (channel i) ima_dat_i 10 bit counts 0 2 10-1 1 1 Level 1.5 Image Data
Image header ima_head - - - - - Level 1.5 Image Data
Recording time (AC) rec_tim_AC UTC 0 23:59 - - Schedule
Backup image (AC) bck_up_AC - 0 6 1 1 Set-up
Channels to be processed(AC) cha_tbp_AC - 1 12 1 1 Set-up
Starting line (channel j; AC) stt_lin_j_AC - 1 max_j 1 1 Set-up
Starting pixel (channel j; AC) stt_pix_j_AC - 1 max_j 1 1 Set-up
Number of lines (channel j; AC) no_lin_j_AC - 1 max_j 1 1 Set-up
Number of pixels (channel j; AC) no_pix_j_AC - 1 max_j 1 1 Set-up
Number of pixels averaged (ch j; AC) pix_avr_j_AC - 1 - 1 1 Set-up
Averaging method (ch j; AC) avr_mth_j_AC - 0= linear 1= RMS - - Set-up
Bits per pixel (ch j; AC) bit_pix_j_AC - 8 10 1 1 Set-up
Subsampling factor (ch j; AC) spl_fac_j_AC - 1 - 1 1 Set-up
Recording time (B1) rec_tim_B1 UTC 0 23:59 - - Schedule
Backup image (B1) bck_up_B1 - 0 6 1 1 Set-up
Channels to be processed(B1) cha_tbp_B1 - 1 12 1 1 Set-up
Starting line (channel j; B1) stt_lin_j_B1 - 1 max_j 1 1 Set-up
Starting pixel (channel j; B1) stt_pix_j_B1 - 1 max_j 1 1 Set-up
Number of lines (channel j; B1) no_lin_j_B1 - 1 max_j 1 1 Set-up
Number of pixels (channel j; B1) no_pix_j_B1 - 1 max_j 1 1 Set-up
Number of pixels averaged (ch j; B1) pix_avr_j_B1 - 1 - 1 1 Set-up
Averaging method (ch j; B1) avr_mth_j_B1 - 0= linear 1= RMS - - Set-up

<!-- source_page: 209 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 210 of 298

Parameter Mnemonic Units Min Max Prec Acc Source
Bits per pixel (ch j; B1) bit_pix_j_B1 - 8 10 1 1 Set-up
Subsampling factor (ch j; B1) spl_fac_j_B1 - 1 - 1 1 Set-up
Recording time (B2) rec_tim_B2 UTC 0 23:59 - - Schedule
Backup image (B2) bck_up_B2 - 0 6 1 1 Set-up
Channels to be processed(B2) cha_tbp_B2 - 1 12 1 1 Set-up
Starting line (channel j; B2) stt_lin_j_B2 - 1 max_j 1 1 Set-up
Starting pixel (channel j; B2) stt_pix_j_B2 - 1 max_j 1 1 Set-up
Number of lines (channel j; B2) no_lin_j_B2 - 1 max_j 1 1 Set-up
Number of pixels (channel j; B2) no_pix_j_B2 - 1 max_j 1 1 Set-up
Number of pixels averaged (ch j; B2) pix_avr_j_B2 - 1 - 1 1 Set-up
Averaging method (ch j; B2) avr_mth_j_B2 - 0= linear 1= RMS - - Set-up
Bits per pixel (ch j; B2) bit_pix_j_B2 - 8 10 1 1 Set-up
Subsampling factor (ch j; B2) spl_fac_j_B2 - 1 - 1 1 Set-up
Table 49: ISCCP Data Set Input:

<!-- source_page: 210 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




15.3 Algorithm Functional Specification
15.4 Overview
This algorithm is responsible for the generation of the three data sets (AC, B1 and B2) EUMETSAT
has to provide, in its combined role of Meteosat operator and as a Sector Processing Centre (SPC), to
the International Satellite Cloud Climatology Project (ISCCP) which is part of the World Climate
Research Programme (WCRP) of the World Meteorological Organization (WMO).
The objectives of the Meteosat Sector Processing Centre are as follows:
 To obtain satellite orbital information and calibration data from Meteosat.
 To acquire the full resolution satellite digital data (A-data) from Meteosat in real-time.
 To provide samples of full IR resolution data (the AC-data) for geographical areas of about
2000 km × 2000 km. About 60 samples of these data, with navigation and calibration data
appended, are required each year for each satellite, for the purpose of periodically calculating
inter-satellite normalisation parameters (BC-data). The inter-calibration calculations are
performed at the Satellite Calibration Centre (SCC). The times and the geographical areas of the
60 samples are chosen to produce observations coincident with the overflight of polar orbiters.
The coordinates of these samples are supplied by the SCC to each SPC.
 To provide samples of reduced resolution data (the B1-data) for the full FOV disc. These data
sets, with navigation and calibration data appended, are to be produced for the synoptic hours
(every three hours starting with 00:00 UTC) and are processed at the Global Processing Centre
(GPC) and archived at the ISCCP Central Archive (ICA). The reduction of the resolution of the
data is achieved by first averaging (linear mean or RMS) the visible channel pixel counts to the
resolution of the infrared channel pixel counts and then reducing the IR channel resolution by sub
sampling the pixels to a nominal resolution of about 10 km spacing at the sub-satellite point.

To provide samples of further reduced resolution data (the B2-data) for the full FOV disc. These
data sets, with navigation and calibration data appended, are to be produced for the synoptic
hours (every three hours starting with 00:00 UTC) and are processed at the Global Processing
Centre and archived at the ISCCP Central Archive. The reduction of the resolution of the data is
achieved by further sub sampling the pixels of the B1-data to a nominal resolution of about 30
km spacing at the sub-satellite point.
15.4.1 Algorithm Description
The IDS Product Generation has to follow the rules and specifications of the International Satellite
Cloud Climatology Project. The algorithm description concentrates therefore mainly on the generic
product structure. The detailed product structure shall
be as defined in the reference document listed
below, e.g. the construction of the data header block. As a baseline all MSG channels shall be used.
The following steps shall be performed in order to derive the IDS AC, B1 or B2 Product:

<!-- source_page: 211 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Step 1 Process the level 1.5 image data from the repeat cycle that matches the requested
image recording time. If that image is not available or of bad quality, process the
backup image as specified by the backup parameter. The backup parameter
specifies the number of images before and after the extraction time than can be
used for backup purposes. The most recently available image should be used;
if this is not available the next available image (after the current time) should be
used. If the backup image(s) is not available or of bad quality, do not produce an
IDS product but issue an error message.

Step 2 Construct the Data Block Header.

Step 3 Extract for each channel to be processed the required image pixels as specified
by the starting line, starting pixel, number of lines to be processed and pixels per
line.

Step 4 Average the VIS channel pixels as specified by the number of pixels to be
averaged and the averaging method.

Step 5 Reduce the number of bits per pixels if required.

Step 6 Subsample the IR channel resolution pixels according to the specified sub
sampling factor.
15.4.2 Automatic Quality Control (AQC)
The following checks shall be performed.
15.4.2.1 Image Availability Check
If a backup image was used set bit 0 of the IDS_QB to one.
15.4.2.2 Image Quality Check
If the quality bits in the image file header indicate that the IMPF could not produce a high quality
image, e.g. due to rectification problems, bit 1 of the IDS_QB shall be set to one.
15.4.2.3 Lost Lines Check
If lines of the area to be processed are not available, bit 2 of the IDS_QB shall be set to one.

<!-- source_page: 212 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




15.5 Outputs
The following data shall be produced, as defined in the reference document or specified below.
Note: The format guide given in Section 15.8 is intended as a reference only, the format information
contained within it will need to be modified to incorporate the differences between the MTP and MSG
satellites, e.g. increased number of channels, different satellite-specific information.
Parameter Mnemonic Units Min Max Prec Acc To
IDS AC Product IDS AC Product
IDS B1 Product IDS B1 Product
IDS B2 Product IDS B2 Product
IDS Quality flag IDS_quality_flag - - - - - All IDS products
Table 50: ISCCP Data Set Outputs
Parameter Value Meaning
IDS_quality_flag Bit 0: 0 Requested image used
Bit 0: 1 Backup image used
Bit 1: 0 Image quality good
Bit 1: 1 Image quality not good
Bit 2: 0 No image lines lost
Bit 2: 1 Some image lines lost
Table 51: ISCCP Data Set parameter to Bit value
15.6 Prototyping and Testing
No prototype software and test data are available for this product.
15.7 Future Enhancements
The redefinition of the IDS product in co-operation with the ISCCP may be required.
15.8 References
Reference Title Date Issue Author(s)
EUM FG 3 The Meteosat Archive, Format Guide No. 3,
ISCCP Data Set (IDS), Open MTP Format
02/96 1.0

<!-- source_page: 213 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




16 TROPOSPHERIC HUMIDITY PRODUCT GENERATION
16.1 Algorithm Configuration Information
16.1.1 Algorithm Name
Tropospheric Humidity (TH)
16.1.2 Algorithm Identifier
EUM_MSG_TH_A001
16.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 M. Gube TH Baseline
1.1 13/3/98 H. K. Wilson Peer Group review changes added.
1.2 05/05/08 O. Samain Several parameter updates or additions
(including AR 17598).
16.2 Inputs
16.2.1 Dynamic Application Data
Parameter Mnemonic Units Min Max Prec Acc Res Source
EBBT for WV6.2
channel
EBBTWV6.2 K 170 300 0.1 0.1 pixel Derived from level
1.5 image data
EBBT for WV7.3
channel
EBBTWV7.3 K 170 300 0.1 0.1 pixel Derived from level
1.5 image data
Satellite Zenith
Angle
Satzen
Degree 0 90 10 -6 10 -6 pixel Derived from level
1.5 image data
Predicted EBBT 5%
Humidity for WV6.2
channel
EBBT5_WV6.2 K 170 300 0.1 0.1 pixel RTM
Predicted EBBT 40%
Humidity for WV6.2
channel
EBBT40_WV6.2 K 170 300 0.1 0.1 pixel RTM
Predicted EBBT 5%
Humidity for WV7.3
channel
EBBT5_WV7.3 K 170 300 0.1 0.1 pixel RTM
Predicted EBBT 40%
Humidity for WV7.3
channel
EBBT40_WV7.3 K 170 300 0.1 0.1 pixel RTM
Scenes Type scenes_type - - - - - pixel CLA
Radiosonde
Observations
rad_obs - - - - - - Observations
Table 52: Tropospheric Humidity Product: Inputs, dynamic application data

<!-- source_page: 214 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Parameter Mnemonic Units Min Max Prec Acc Res Source
EBBT Threshold EBBT_thresh K 170 300 1 1 - Set-up Parameter
TH Upper Threshold TH_u % 0 >TH_l 1 1 - Set-up Parameter
TH Lower Threshold TH_l % 0 <TH_u 1 1 - Set-up Parameter
TH Processing segment size ps_size pixels 1 - 1 1 - Set-up Parameter
TH level threshold 1 TH_level_1 hPa 100 400 50 50 - Set-up Parameter
TH level threshold 2 TH_level_2 hPa 300 700 50 50 - Set-up Parameter
TH level threshold 3 TH_level_3 hPa 600 900 50 50 - Set-up Parameter
Number of valid levels for
WV6.2
NLEV6.2 - 1 - 1 1 - Set-up Parameter
Number of valid levels for
WV7.3
NLEV7.3 - 1 - 1 1 - Set-up Parameter
Level spacing for WV6.2 DP6..2 hPa 1 - 1 1 - Set-up Parameter
Level spacing for WV7.3 DP7.3 hPa 1 - 1 1 - Set-up Parameter
Verification area ver_area pixels 1 - 1 1 Set-up Parameter
Min Number of pixels for
verification
min_ver_pix pixels 1 - 1 1 - Set-up Parameter
Table 53: Tropospheric Humidity Product: Inputs, static application data
16.3 Algorithm Functional Specification
16.3.1 Overview
The function of this algorithm is to derive a relative humidity (in %) measure for each of the two
water vapour channels on a TH processing segment scale as defined by ps_size. The WV6.2 channel
will produce an upper tropospheric humidity which is the mean layer relative humidity between
TH_level_1, nominally 300 hPa, and TH_level_2, nominally 600 hPa. The WV7.3 channel will
produce a mid-tropospheric humidity which is the mean layer relative humidity between TH_level_2,
nominally 600 hPa, and TH_level_3, nominally 850 hPa. The product is generated for the repeat cycle
closest to the required extraction time for the TH product.
The algorithm involves the following steps:
 A relative humidity measure for each of the two water vapour channels is derived on a pixel
basis. The algorithm does not use any scenes analysis type of information, i.e. it is applied in
identical fashion to cloudy and cloud-free areas. In practice, clouds are identified by the
algorithm itself, as it produces unrealistically high (>> 100%) humidities over regions of high
or medium high clouds (see Section 16.3.3.1). Also, there might be pixels where the retrieval
algorithm produces an unrealistically low (< 0%) humidity which is clearly a failure of the
algorithm and could be due to e.g. wrong input data (see Section 16.3.3.2).

The pixel humidities are used to produce an average measure of humidity, where this average
corresponds to a scale of approximately 100 km. As the small scale (pixel) based data are
always calculated first, the averaging method can be easily adjusted to consider a different
scale. It should already be noted at this point that the average humidity is a ‘clear sky’
humidity, i.e. is derived for areas which are free of medium-high and high clouds. The
algorithm also provides information concerning the number of ‘cloudy’ pixels within the

<!-- source_page: 215 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




considered area, where the term ‘cloudy’ pixel refers to a pixel where the humidity retrieval
algorithm has produced a value of greater than or equal to TH_u, nominally 100%. Also the
number of pixels where the algorithm has completely failed, i.e. has produced a relative
humidity of TH_l nominally 0% or less, are provided.
 Finally, the product verification is performed (after the product has been disseminated),
comparing the calculated humidities with radiosonde measurements.
16.3.2 Algorithm Description
The following seven steps shall be performed in order to derive the relative humidity for each of the
two channels. For each pixel:

Step 1 If EBBTWV6.2 is less than EBBT_thresh then set THWV6.2 to a default value, i.e.
TH_l, and skip the remaining processing steps for this channel.
If EBBTWV7.3 is less than EBBT_thresh then set THWV7.3 to a default value, i.e.
TH_l, and skip the remaining processing steps for this channel.

Step 2 Calculate the cosine of the satellite zenith angle:
Qs a t z e n cos

Step 3 Calculate XL5 and XL40, where log is the logarithm in base 10:
XL Q
5
5 
 
log .
XL Q
40
40 
 
log .

Step 4 Calculate A and X for each of the WV channels:




A EBBT EBBT
XL XL
A EBBT EBBT
XL XL
wv
WV WV
wv
WV WV
62
40 6 2 56 2
40 5
73
40 7 3 57 3
40 5
.
_. _.
.
_. _.
 

 




XX L EBBT EBBT
A
XX L EBBT EBBT
A
WV
WV WV
wv
WV
WV WV
wv
62 4 0
40 6 2 6 2
62
73 4 0
4 0 73 73
73
.
_. .
.
.
_. .
.
 
 

<!-- source_page: 216 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Step 5 Calculate the Tropospheric Humidity for each of the WV channels, THWV6.2 and
THWV7.3:
TH Q
TH Q
WV
X
WV
X
WV
WV
62
73
10
10
62
73
.
.
.
.




Step 6 Perform the AQC checks specified below.

Step 7 Average the pixel-based TH values for each TH processing segment as follows:
 An average clear sky humidity shall be computed according to
Uc l e a r s k y U pixel
Np i x e l() ()
()
*
* 
where U(pixel)* denotes the pixel humidity if this value is above TH_l and below
TH_u; N(pixel)* denotes the number of pixels which meet this criterion. The
summation goes over the ps_size by ps_size number of pixels.
 The percentage of ‘cloudy’ pixels shall be computed according to

2
_
100_
sizeps
humidityTHU_u withpixelscloudPercent 
The summation goes over the ps_size by ps_size number of pixels.
 The number of ‘algorithm failure’ pixels shall be computed according to
N fail number of pixels with THU l humidity() _  
The summation goes over the ps_size by ps_size number of pixels.
16.3.3 Automatic Quality Control (AQC)
For all the pixel-based values of Tropospheric Humidity which have been calculated, the following
checks shall be performed.
16.3.3.1 Upper Limit Check
If the value of Tropospheric Humidity for a channel is greater than or equal to TH_u then the value of
Tropospheric Humidity for that pixel shall be set to TH_u.
16.3.3.2 Lower Limit Check
If the value of Tropospheric Humidity for a channel is less than or equal to TH_l then the value of
Tropospheric Humidity for that pixel shall be set to TH_l.
16.3.3.3 Quality Indicators
For each processed segment, and for the two WV channels, a quality flag is calculated as follows:

Equation 49


2
_/)(100_100 sizepsfailNcloudPercentQCFlag 

<!-- source_page: 217 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





16.3.4 Verification of TH
The satellite-derived humidities THWV6.2 and THWV7.3 shall be compared to independent humidity
measurements by radiosondes. This shall be done separately for the two humidities. The information
generated by the verification shall be included in the TH product header, and shall include all the
values of mean radiosonde humidity for the successful radiosonde collocations and the corresponding
calculated TH values.
The comparison shall
take into account all radiosondes within the MSG processing area. However, in
order to be actually used for comparison any radiosonde shall fulfil the following criteria:
A. For verification of THWV6.2:
1. The radiosonde shall be at a distance of less than or equal to ver_area pixels from the centre of
the corresponding TH segment centre.
2. The radiosonde shall have valid humidity measurements in at least a number of NLEV6.2 layers
between TH_level_1 and TH_level_2.
3. The individual measurements within the layer of TH_level_1 and TH_level_2 shall be evenly
spread over that layer. In order to ensure this, individual measurements shall lay at least DP6.2
hPa apart. At least NLEV6.2 individual measurements shall meet this criterion.
4. The radiosonde shall be in an area with no high or medium high cloud. For this, a square area
shall be defined of side ver_area pixels, consisting of a fixed number of pixels, with its centre
pixel located at the pixel of the radiosonde ground station. From this square area, all pixels
which according to the scenes type from Cloud Analysis are determined as free of medium high
and high clouds shall
be selected. The total number of these cloud-free (with respect to medium
high and high clouds) pixels shall exceed min_ver_pix.
If the radiosonde meets all these requirements, it shall be considered a valid comparison target for
THWV6.2. A mean radiosonde humidity RTHWV6.2 shall then be computed as the arithmetic mean
over all humidity measurements taken between TH_level_1 and TH_level_2.
B. For verification of TH WV7.3:
1. The radiosonde shall be at a distance of less than or equal to ver_area pixels from the centre of
the corresponding TH segment centre.
2. The radiosonde shall have valid humidity measurements in at least a number of NLEV7.3 layers
between TH_level_2 and TH_level_3.
3. The individual measurements within the layer of TH_level_2 and TH_level_3 shall be evenly
spread over that layer. In order to ensure this, individual measurements shall lay at least DP7.3
hPa apart. At least NLEV7.3 individual measurements shall meet this criterion.
4. The radiosonde shall be in a cloud-free area. For this, a square area shall be defined of side
ver_area, consisting of a fixed number of pixels, defined by a set-up parameter, with its centre
pixel located at the pixel of the radiosonde ground station. From this square area, all pixels
which according to the scenes type from Cloud Analysis are determined as cloud-free shall be
selected. The total number of these cloud-free pixels shall exceed min_ver_pix.
If the radiosonde meets all these requirements, it shall be considered a valid comparison target for
THWV7.3. A mean radiosonde humidity RTHWV7.3 shall then be computed as the arithmetic mean
over all humidity measurements taken between TH_level_2 and TH_level_3.

<!-- source_page: 218 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




16.4 Outputs
Parameter Mnemonic Units Min Max Prec Acc To
Tropospheric
Humidity for WV6.2
channel, clear sky
THWV6.2 % TH_l TH_u 0.1 0.1 TH product
Tropospheric
Humidity for WV7.3
channel, clear sky
THWV7.3 % TH_l TH_u 0.1 0.1 TH product
Percentage of ‘cloudy’
pixels for WV6.2
channel
Percent_cloud
WV6.2 % 0 100 0.1 0.1 TH product
Percentage of ‘cloudy’
pixels for WV7.3
channel
Percent_cloudWV7.3 % 0 100 0.1 0.1 TH product
Number of ‘algorithm
fail’ pixels for WV6.2
channel
NFAIL
WV6.2 - 0 1024 1 1 TH product
Number of ‘algorithm
fail’ pixels for WV7.3
channel
NFAILWV7.3 - 0 1024 1 1 TH product
TH Segment Centre
Latitude
c_lat  –90 90 0.01 0.01 TH product
TH Segment Centre
Longitude
c_lon  –180 180 0.01 0.01 TH product
Quality indicator for
channel 6.2
QCFlagWV6.2 % 0 100 0.1 0.1 TH product
Quality indicator for
channel 7.3
QCFlagWV7.3 % 0 100 0.1 0.1 TH product
Verification Results TH Product
Header
Table 54: Tropospheric Humidity Product: outputs
Note: For the BUFR-encoded product, in the case that the percentage of cloud is 100, the
Tropospheric Humidity values are set to ‘missing’.
16.5 Prototyping and Testing
This section describes the prototyping activities, highlighting the major problems which were
encountered with this development.
16.5.1 Prototyping
This algorithm is simple and thus was easy to prototype. The test data used are described below.

<!-- source_page: 219 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




16.5.2 Test Data
The following files are required as test data:
Test file wvimage.dat: this is an ASCII file whic h contains one line (2500 values) of Meteosat-5 WV
channel brightness temperatures (in K), in format 10F6.1. These values correspond to EBBT WV in the
input table, where the actual channel information (6.2 or 7.3) is omitted as the same formulae apply to
either channel.

The following constants were also used:
EBBT5_WV = 258.8 K
EBBT40_WV = 240.6 K
SATZEN = 0° (i.e. Q = 1.)
EBBT_thresh = 170.0 K
TH_u = 100 %
TH_l = 0%
16.5.3 Test Results
The test results for the image files described in 16.5.2 are available as uthout.dat. This is an ASCII file
which contains the corresponding 2500 humidity values (in per cent, rounded to the next integer),
format 19I5
.
16.6 Future Enhancements
The use of the intermediate CLA for the generation of the TH is a future enhancement.
16.7 References
None

<!-- source_page: 220 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




17 SEA SURFACE TEMPERATURE PRODUCT GENERATION
17.1 Algorithm Configuration Information
17.1.1 Algorithm Name
Sea Surface Temperature (SST)
17.1.2 Algorithm Identifier
EUM_MSG_SST_A001
17.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 H.-J. Lutz SST Baseline
1.1 12/6/97 H. K. Wilson TBD resolved, errors corrected.
1.2 13/3/98 H. K. Wilson Peer Group Review changes added.
1.3 25/7/05 J. Gustafsson Parameter reset to force use of day formulae at
night as well. Added smoothing of pixel values.
17.2 Inputs
17.2.1 Dynamic Application Data
As an input, level 1.5 image data of subset of channels (as listed in the following table) for every
repeat cycle shall be available for the SST processing in the form of equivalent black body brightness
temperatures (EBBT). Also the SST product results from the previous repeat cycle and the scenes
type information from the Scenes Analysis of the current repeat cycle shall
be available.

Parameter Mnemonic Units Min Max Prec Acc Res Source
Scenes type scenes_type - 0 255 1 1 pixel Scenes Analysis
EBBT of channels
IR3.9, IR8.7,
IR10.8, IR12.0
EBBTchannel K 170 350 0.1 0.1 pixel Derived from
Level 1.5 image
data
SST from previous
repeat cycle
prev_SST K 260 350 0.1 0.1 pixel SST product from
previous repeat
cycle
Solar zenith angle sol_zenith degree 0 180 10-6 10-6 pixel Derived from level
1.5 data
Satellite zenith
angle
sat_zenith degree 0 90 10
-6 10 -6 pixel Derived from level
1.5 data
Table 55: Sea Surface Temperature Product inputs

<!-- source_page: 221 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




17.2.2 Static Application Data
Parameter Mnemonic Units Min Max Prec Acc Res Source
Day/night check
threshold
SZ_day degrees 0 90 1 1 - Set-up parameter
AQC temporal
check threshold
SST_tempo
ral
kelvin 0 20 1 1 - Set-up parameter
AQC spatial
check threshold
SST_spatial kelvin 0 20 1 1 - Set-up parameter
Minimum
allowed pixels in
segment
M - 1 1024 1 1 - Set-up parameter
AQC spatial
check area size
n - 1 32 1 1 - Set-up parameter
AQC maximum
SST threshold
SST_MAX kelvin 300 350 1 1 - Set-up parameter
AQC minimum
SST threshold
SST_MIN kelvin 260 280 1 1 - Set-up parameter
SST Parameters A0 - An - - - - - - Set-up parameters
B 0 - Bn - - - - - - Set-up parameters
C0 - Cn - - - - - - Set-up parameters
D 0 - Dn - - - - - - Set-up parameters
Table 56: Sea Surface Temperature Product: Static Application Data
17.3 Algorithm Functional Specification
17.3.1 Overview
The Sea Surface Temperature product (SST) provides a temperature estimate (in kelvin) for the skin
surface of the ocean on a pixel basis. This product will be used for calibration monitoring and product
verification purposes.
17.3.2 Algorithm Description
The following steps shall be applied for every pixel.
17.3.2.1 Scenes Type Check
The scenes type of every pixel as derived from the Scenes Analysis algorithm shall be checked. If the
scenes type is not water (ocean) the SST shall be set to a default and the SST quality flag shall be set
indicating ‘no SST derived, scenes type is not water (ocean)’ and the following steps shall be skipped
and the processing shall start with the next pixel.
17.3.2.2 Solar Zenith Angle Check
If the scenes type is water (ocean) the solar zenith angle shall be checked against a threshold. If the
solar zenith angle is larger than a threshold (SZ_day), then the pixel has night conditions, else it has
day conditions.

<!-- source_page: 222 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




17.3.2.3 SST Processing
17.3.2.3.1 Day Conditions
For pixels with day conditions the following two formulae shall be applied:
Tday-1 = A0 + A1*TIR10.8 + A2(TIR10.8 - TIR12.0) + A3(TIR10.8 - TIR12.0)*((1/COS(sat_zenith))-1)
Tday-2 = B0 + B1*TIR12.0 + B2(TIR10.8 - TIR12.0)*((1/COS(sat_zenith))-1) +
(B3 + B4*TIR10.8 + B5*TIR12.0) * (B6 + B7*TIR12.0) / (B8 + B9*TIR10.8 + B10*T IR12.0)
where TIR10.8 and TIR12.0 are the EBBT in channel IR10.8 and IR12.0
The SST itself shall be derived as follows:
TSST = C0 + C1*Tday-1 + C2*Tday-2
17.3.2.3.2 Night Conditions
For pixels with night conditions the following three formulae are applicable:
Tnight-1 = A0 + A1*TIR10.8 + A2*((1/COS(sat_zenith))-1) +
(A3 + A4*TIR10.8 + A5*TIR12.0) * (A6 + A7*TIR10.8) / (A8 + A9*TIR3.9 + A10*T IR12.0)
Tnight-2 = B0 + B1*TIR10.8 + B2*((1/COS(sat_zenith))-1) +
(B3 + B4*TIR3.9 + B5*TIR10.8) * (B6 + B7*TIR10.8) / (B8 + B9*TIR3.9 + B10*T IR10.8)
Tnight-3 = C0 + C1*TIR12.0 + C2(TIR10.8 - TIR12.0)*((1/COS(sat_zenith))-1) +
(C3 + C4*TIR10.8 + C5*TIR12.0) * (C6 + C7*TIR12.0) / (C8 + C9*TIR10.8 + C10*T IR12.0)
The SST itself may be derived as follows:
TSST = D0 + D1*Tnight-1 + D2*Tnight-2 + D3*Tnight-3
Note: The current EUMETSAT set-up does not differentiate between day and night, so the ‘day
formulae’ previously given are used also during hours of darkness.
17.3.2.3.3 Smoothing
To make the radiative noise less apparent when viewing the product, an averaging of the pixel value is
applied. Each pixel has its SST value replaced by the local mean value, calculated from the 3 × 3 pixel
segment, if the mean is made up of at least k values. The impact is that the spatial test (in 17.3.3
below) is disabled, and there is an increased risk of including pixels contaminated by land or cloud.
17.3.3 Automatic Quality Control (AQC)
The automatic quality control (AQC) of the SST product consists of three tests. The SST product shall
be quality controlled with a spatial and a temporal consistency check, and with a climatological test.
If an SST is derived for both the pixel of the current repeat cycle and of the previous repeat cycle,
then apply the temporal consistency check. This check shall compare the SST result of the current
repeat cycle for each pixel with the result of the previous repeat cycle. If the absolute difference
between the two values exceeds a threshold, SST_temporal, the quality flag shall be set indicating
‘poor quality, temporal check’ for that pixel.
If in an n × n pixel segment the SST has been derived for at least m pixels, then the spatial consistency
check shall be applied. This check shall compare the SST result of each pixel with the averaged SST
of the n × n pixel segment. If the absolute difference between the mean SST and the pixel value
exceeds a threshold, SST_spatial, the quality flag shall be set indicating ‘poor quality, spatial check’
for that pixel.

<!-- source_page: 223 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The SST shall also be checked against a minimum climatological temperature threshold (SST_MIN)
and against a maximum climatological temperature threshold (SST_MAX). If the SST is lower than the
minimum threshold, the quality flag shall be set indicating ‘bad quality, value lower than SST_MIN’.
If the SST is higher than the maximum threshold, the quality flag shall be set indicating ‘bad quality,
value higher than SST_MAX’.
17.3.4 SST Verification
No SST verification is required.
17.4 Outputs
The following list of output parameters shall be generated per pixel.

Parameter Mnemonic Units Min Max Prec Acc Res To
Sea surface
temperature
SST kelvin 270 320 0.1 0.1 pixel SST Intermediate
Product
SST Quality flag SST_quality_flag - - - - - pixel SST Intermediate
Product
Table 57: Sea Surface Temperature Product: output parameters
Parameter Value Meaning
SST_quality_flag Bit 0: 1 No SST derived, scenes type not water (ocean)
Bit 1: 1 AQC Temporal Check poor quality
Bit 2: 1 AQC Spatial Check poor quality
Bit 3: 1 SST Bad Quality - less than SST_MIN
Bit 4: 1 SST Bad Quality - SST_MAX exceeded
Table 58: Sea Surface Temperature Product: Parameter and bit value
17.5 Prototyping and Testing
This section describes the prototyping activities, highlighting the major problems which were encountered with
this development.
17.5.1 Prototyping
The prototyping activities provide information about the scientific background for the SST algorithm
and verify that the algorithm is scientifically correct. The scientific background of the prototype is
mainly based on existing algorithms.
17.5.2 Test Data
The major problem is to simulate the MSG channels. The prototype uses existing data from
GOES-8/VISSR, which helps to simulate channels IR3.9, IR10.8 and IR12.0 on a similar horizontal
resolution as MSG. The scenes type information comes from the Scenes Analysis algorithm.
17.5.3 Test Results
Tests have been performed for several slots of the GOES-8 images. The results are available for each
of these slots.
17.6 Future Enhancements
No future enhancements are currently foreseen.

<!-- source_page: 224 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




18 OPTIMAL CLOUD ANALYSIS PRODUCT GENERATION
18.1 Algorithm Configuration Information
18.1.1 Algorithm Name
Optimal Cloud Analysis (OCA)
18.1.2 Algorithm Identifier
EUM_MSG_OCA_A001
18.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 14/10/15 J. Jackson OCA baseline
18.2 Inputs
18.2.1 Dynamic Application Data
The OCA algorithm uses the Scenes actual EBBT and reflectance derived from the level 1.5 image
data, and the modelled radiance and transmittance from the radiative transfer model (RTM). As
defined in the following table, the scenes type information, forecast data, clear sky reflectance map,
satellite and solar zenith angles for the current repeat cycle shall be available.

<!-- source_page: 225 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 226 of 298


Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Actual reflectances for visible
channels.
REFLchannel % 0 150 0.1 0.1 pixel Scenes Analysis.
Actual brightness temperatures for
infrared channels.
EBBTchannel K 170 350 0.1 0.1 pixel Scene Analysis.
Atmospheric correction tables. rtm_acc_tab mWm-2sr-1(cm-1)-1 0 - - - 1 degree Derived from the RTM.
Visible 2-path transmission tables. rtm_vis_tab - 0 100 10-6 10-6 1 degree Derived from the RTM.
Forecast temperature profiles on
the RTM standard pressure levels.
for_temp K 170 350 0.1 0.1 1 degree Derived from the Forecast data.
Forecast pressure profiles on the
RTM standard pressure levels.
for_prof hPa 0 1030 1 1 1 degree Derived from the Forecast data.
Scenes type scenes_type - 0 255 1 1 pixel Scenes Analysis.
Solar zenith angle sol_zen Degrees 0 90 10-6 10-6 pixel Angles Data, derived from Level 1.5
image data.
Satellite zenith angle sat_zen Degrees 0 90 10 -6 10 -6 pixel Angles Data, derived from Level 1.5
image data.
Solar-satellite relative azimuth rel_azi Degrees 0 180 10-6 10-6 pixel Angles Data, derived from Level 1.5
image data.
Clear sky reflectance maps crm % 0 100 0.1 0.1 pixel Scenes - clear sky reflectances image,
updated multiple times per day.
Table 59: OPTIMAL CLOUD ANALYSIS Dynamic Application Data

<!-- source_page: 226 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




18.2.2 Static Application Data
All static application data and set-up data shall be configurable.

STATIC APPLICATION DATA FOR PHYSICAL RETRIEVAL SCHEME
Parameter Mnemonic Units Value Source
Surface Type surface_type_map - - Static data
Processing area mask Proc_ar ea pixels - Static data
Spectral characteristics of the
SEVIRI channels.
SEVIRI_Chan - - Static data
Cloud Radiative Properties
(Water)
CRP_water - - Static-data
Cloud Radiative Properties (Ice) CRP_ice - - Static-data
Pixel Emissivity Maps (one for
each month of the year)
Emissivity_tables - - Static-data
Run Type for OCA model RunType - 2 Set-up
Satellite ID SatID - 3 Set-up
Max. Satellite Zenith Angle MaxSatZen degrees 75.0 Set-up
Max. Solar Zenith Angle MaxSolZen degrees 80.0 Set-up
Sunset Angle Sunset degrees 90.0 Set-up
First pixel number to process IndX0 - 1 Set-up
First image line number to process IndY0 - 1 Set-up
Last pixel number to process IndX1 - 3712 Set-up
Last image line number to process IndY1 - 3712 Set-up
Temperature threshold to detect
phase change to water
PhaseTWater K 268.0 Set-up
Temperature threshold to detect
phase change to ice.
PhaseTIce K 243.0 Set-up
Equivalent Model Parameter Noise
term for surface reflectance.
EqMPNRs - 0 Set-up
Equivalent Model Parameter
Noise term for cloud homogeneity.
EqMPNHomog - 2 Set-up
Equivalent Model Parameter Noise
term for the channels spatial
alignment.
EqMPNCoReg - 2 Set-up
Cloud Type CloudType - 2 Set-up
Invert Marquardt starting value Mqstart - 0.01 Set-up
Invert Marquardt step size Mqstep - 10.0 Set-up
Max. iterations of Invert Marquardt Maxiter - 8 Set-up
Max. number of phase changes Maxphase - 3 Set-up
The size of the cost function
decrease, below which
convergence is said to occur.
Ccj - 1.0 Set-up
Table 60: Optimal Cloud Analysis Static Application Data

<!-- source_page: 227 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




18.3 Algorithm Functional Specification
18.3.1 Overview
Optimal Cloud Analysis (OCA) was so named to describe the approach taken to the estimation of
cloud properties from the MSG SEVIRI instrume nt. The approach justifies the description optimal
from two of its characteristics; firstly that all me asurements and all important cloud parameters are
dealt with simultaneously and secondly that the formal technique of optimal estimation (OE) is
employed to obtain a solution. The simultaneity charact eristic aims to ensure that all information in a
measurement is effectively extracted; the corollary of which is that all effects on a measurement are
modelled. The OE framework aims to ensure that measurements and any prior information may be
given appropriate weight in the solution depending on error characteristics whether instrumental or
from modelling sources.
18.3.2 Algorithm Description
The OCA algorithm is based on the following components:
1.
A model of a cloudy atmosphere defined by a set of variable - ‘state’ - parameters:
x = Cloud Optical Thickness (COT), Cloud Effective Radius (CRE), Cloud Top Pressure
(CTP), Cloud Fraction (CFR), Cloud Phase (CPHS), Skin Temperature (TS) and a set of fixed
- ‘model’ - parameters
b = Atmospheric temperature and gaseous constituents, surface properties etc. Uniquely, the
cloud phase, is not a continuous variable and takes one of only two values.
2. A fast radiative transfer model (RTM) which, when operated on the state and model
parameters, estimates the values of the imager measurements y. The operation is denoted by
y(x,b).
3. Models of errors in the measurements and the ‘prior to retrieval’ values of the state
parameters.
4. A penalty or ‘cost’ function, J, which describes the ‘distance’ (weighted mismatch) between
measurements, prior state and the state estimate.
5. A technique to minimise the penalty function.
The algorithm is able to alter the state parameters but the model parameters remain fixed.
A major and frequent occurance is the presence of cloud at multiple levels which corresponds poorly
to the assumed model and results in poor estimates (especially of CTP). However, put briefly, the
value minimised cost (as listed in numbers 4 and 5 above) in these cases is very often large so that
they can be identified. In identified multi-layer cloud pixels the minimisation algorithm is re-run with
altered constraints, (see Section 18.3.3) such that infrared radiative transfer appropriate to a two-layer
cloud system is approximated. Solar-affected chan nels cannot be used in these cases. The retrieved
state can then be interpreted, with help from the fi rst single layer attempt, as the parameters of a twolayer cloud system.
18.3.3 Variable Cloud State Parameters (x)
The basic (single layer) OCA model cloud consists of a single layer of zero geometric depth,
an optical depth (COT) defined at 0.55 μm and of single phase (ice or water, CPHS). The
particle size distribution within the cloud is re presented by an effective radius (CRE) and the
temperature ‘distribution’ within the cloud is the ambient temperature at the cloud top
pressure (CTP). Finally, the pixel is assumed to be fractionally cloud covered (CFR). [A
further parameter is the skin temperature (TS) of the underlying surface, not strictly part of

<!-- source_page: 228 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




the cloud, which is included because of the strong dependence of almost all TIR channels in
some cloud conditions.]

Prior to the retrieval operation we may have some information on the values of the state parameters,
known as a priori, prior or background information, xa. The OE methodology allows us to formally
include this information by defining a prior cost function using xa and the covariance of the errors in
xa, Sa. It is the nature of clouds that we actually have little prior knowledge of the state parameters in
the observed pixel. Certainly for COT, CRE and CTP there is no information available; Sa elements
for these parameters are therefore set to a high valu e (1e+8). For CFR, as discussed earlier, we make
the assumption that the cloud detection algorithm has deduced the presence of cloud accurately and
further that the cloud cover is complete. Sa for CFR is therefore set an effective zero value (1e-8).
This is tantamount to removing CFR from the state vector and is a (somewhat false) constraint that
will be revisited as the scheme becomes better tuned and/or applied to instruments with more channels
(=information, e.g. MTG-FCI). TS is currently the only variable with genuine prior information
available. For ocean pixels a relatively low error of 1.0 K is assumed, for land a higher error, ~5.0 K.
For the re-run multi-layer cloud cases COT, CRE, and CTP continue to represent optical depth,
effective radius and pressure, but now for the upper cloud layer. CFR remains constrained to unity,
but TS is given a higher prior error estimate (~20 K) and is initialised to the mid-lower troposphere
(~700 hPa) temperature. By these means it crud ely but effectively models now not the skin
temperature but the temperature of an underlying cloud layer. As said, there is no possibility of such a
simple model for the solar reflectance channels and these are disabled here. Some post-processing of
the result of this new minimisation is performed to extend the description: the original single layer
COT (=approximately upper+lower) is used with th e new value (=upper layer) to determine the COT
of the lower layer and this can be used to estimate lower layer cloud IR transparency and convert the
lower layer temperature into a cloud pressure.
18.3.4 Fixed Model Parameters (b)
Within OCA, only the cloud parameters are retrieved; therefore assumptions are made about
atmospheric humidity, temperature, aerosol concentration, ozone concentration, surface emissivity,
reflectivity etc. Values for these so called ‘model’ parameters are derived, for the quickly varying
parameters from Numerical Weather Prediction (NWP) sources and for the more static parameters
from available climatology and datasets. They are therefore of the highest quality and accuracy
available in near real time but nevertheless errors remain. Part of the ‘optimality’ of the OCA scheme
comes from appropriate weighting of the measurements in the retrieval
.
18.3.5 The Measurements (y)
The measurement vector, ym, constitutes all the single pixel measurements from the sensor; thus 11
for SEVIRI. The values are “solar angle uncorrected” reflectance for wavelengths to 3 μm and
brightness temperatures thereafter. The measurements are weighted in the retrieval by their errors,
(Sy). It is important to note that the definition of error here refers to the ability of the forward model
to reproduce the measurements since this defines how close a fit is expected. Thus the error should in
principle include:
 instrument noise
 channel co-registration effects
 effects of deviations from the OCA cloud model
 effects of errors in ancillary model parameters

<!-- source_page: 229 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





The algorithm includes of all of the measurements, however channels that are difficult to model (e.g.
3.9 µm) or visible channels during poor illumination conditions or in two-layer retrievals are removed
by the model by setting the channel error covariance value to a high level (∞).
18.3.6 Radiative Transfer Model
The RTM needs to be very fast to achieve real time processing of high resolution imagery and this is
achieved with a) the use of lookup tables (LUT s) which store computationally intensive cloud
radiative properties, b) pre-calculated atmospheric radiative effects and transmissions at NWP
forecast grid resolution and c) a simple three layer (below cloud, cloud, and above cloud) radiative
transfer integration.
18.3.7 Cost Function
The ‘cost’ or ‘distance’ function, J, which defines the OCA algorithm method is the sum of two
parts: the measurement cost (Jm) and the prior cost (Ja).

Given a current estimate of the state x, Jm is the weighted squared difference of the observed
measurements, ym, and the values y(x) (the estimated measurements). The weights are given by the
expected errors in the measurements. Formally, this is written:

Jm = (ym – y(x))T Sy
-1(ym - y(x)) Equation 50

Similarly, J a is the weighted squared difference of the prior values of the state, xa, and x; the
weights being the expected errors in the prior values.

Ja = (x - xa)T Sa
-1 (x - xa)) Equation 51

A high J value therefore indicates that the current state is in disagreement with either the
measurements or the prior information or both. At the minimum value of J, the state has been found
which gives best agreement with both the prior estimate and the measurements. This is the meaning of
the statistical ‘optimality’ of the OCA method.
18.3.8 Minimising the Cost Function
Minimisation of the cost function involves a ‘descent’ algorithm which, starting from ‘first guess’
estimates of the state parameters, x0, takes successive steps (or ‘iterations’), δx, that reduce the
cost until either the cost is acceptably small, th e cost reduction becomes insignificant, or the
iteration limit is exceeded.

Although it is not proven, experience suggests that the cost functions found with MSG SEVIRI
measurements and the OCA cloud model state definition are relatively ‘well behaved’. This means
that there are generally few instances of multiple minima or other complex features that would require
the use of sophisticated search algorithms to find the true minimum. OCA therefore operates a
straightforward Levenberg-Marquardt descent algorithm which combines steepest descent and
Newtonian methods.

<!-- source_page: 230 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Steepest descent (SD) involves stepping in the direction in x-space that is in the steepest
‘downhill’ direction, -J’ = − ∂J/ ∂x . Such steps will always be in the correct direction although
as the length of the step is not determined and may be too far (stepping past the minimum) or too
short (needing many iterations). Newtonian descent (ND) on the other hand uses a step that is
Newton’s root finding method for the equation J’=0 which is the condition expected at any
minimum. The step is thus -J′/J" and, if J is a quadratic function of x, as it would be if all errors are
purely normal and the RT is linear in x, then one step finds exactly the minimum. It is because the RT
is not in practice completely linear that these two descent methods are combined with a mechanism to
alter the balance between them. Thus the Levenberg-Marquardt step is given by

δx=-(J" + αI)-1 J’ Equation 54

where the control variable α is varied to shift between SD and ND; α very small is equivalent to ND.
Adjustment of α is made according to the success of the last step made: if the step is successful (i.e.
lowers the value of J) then α is reduced (by e.g. a factor of 10) because it is assumed the minimum is
nearer and the problem more linear. If the step is unsuccessful in that the value of J would increase,
the step is not made and α is increased.
Steps that would lead to a parameter leaving its physically valid bounds (e.g. CTP greater than surface
pressure) are generally modified so that the parameter is restricted to the bounding value (surface
pressure in this case). An exception is the bounds check on CRE where over-stepping in two of the
four possible cases is taken to imply that the current cloud phase (water or ice) is incorrect and the
phase is changed and the minimisation re-initialised . A phase change is made when a step to CRE
larger than the water phas e upper limit (e.g. ~23 microns) is taken to imply the cloud phase is more
likely to be ice and, similarly, when a step to CRE less than the ice phase lower limit (~10 microns) is
taken to imply the cloud phase is more likely to be water. Figure 13 is taken from reference document
R1 is the logic scheme used to implement the Levenburg-Marquardt. The central column is essentially
the Levenburg-Marquardt loop; the branching to the left and right sides implement phase change and
multi-layer cloud treatments respectively.

<!-- source_page: 231 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





Figure 13: The OCA cost minimisation scheme (taken from R2).

<!-- source_page: 232 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




18.3.9 Processing mask
The OCA algorithm is applied to a ll SEVIRI pixels within the processing area. The OCA algorithm is
only applied to pixels classified as clouds by the Scenes algorithm.
18.4 Outputs
18.4.1 Final Product
The following data shall be produced for the OCA product for every pixel:
Parameter Mnemonic Units Min Max Prec To
Latitude Latitude degrees –90 90 0.1 OCA Final Product
Longitude Longitude degress –180 180 0.1
Quality Flag Quality_Flag - 0 255 1
Cloud Phase Phase - 0 3 1
Cost Jm - 0 - 1
Upper Layer Cloud
Optical Depth
ULTau - –1.0 2.4 0.01
Upper Layer Cloud
Top Pressure
ULCtp hPa 50 1060 0.01
Upper Layer Cloud
Particle Size
ULCre µm 1 180 0.1
Upper Layer Error in
Calculated Optical
Depth
ULSnTau - 0 - 0.01
Upper Layer Error in
Calculated Cloud Top
Pressure
ULSnCtp hPa 0 - 0.01
Upper Layer Error in
Calculated Particle
Size
ULSnCre µm 0 - 0.1
1Lower Layer Cloud
Optical Depth
LLTau - –1.0 2.4 0.01
1Lower Layer Cloud
Top Pressure
LLCtp hPa 50 1060 0.01
1Lower Layer Error
in Calculated Optical
Depth
LLSnTau - 0 - 0.1
1Lower Layer Error
in Calculated Cloud
Top Pressure
LLSnCtp hPa 0 - 0.01
1 Lower Layer Cloud products are only present when the 2-layer re-run has been performed–when the Cloud
Phase parameter = 3.

<!-- source_page: 233 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




18.4.2 Encoded Products
The fields of the intermediate product are encoded into a single file in the GRIB 2 format. The
Latitude, Longitude, Row, Column, and Quality Fl ag values are omitted from the encoded product.
The file is compressed with complex packi ng using the NCEP GRIB2 encoder. Finally an
MPEF_PRODUCT_HEADER (of size 172 bytes) and the XRINT_NonImage_Data_Header (of size 4
bytes) is pre-appended to the encoded OCA product.

18.5 Future Enhancements
The most likely significant future enhancement will be to replace the ad hoc 2 layer cloud modelling
currently implemented with a full description – that is extension of the state vector to explicitly
include parameters from both layers and the consequent extension of the OCA fast radiative transfer
model. The latter will probably be approached in two steps with the somewhat simpler infrared
channels in the first enhancement.
18.6 References
Reference Title Date Author(s)
R1 EUM/MTG/DOC/11/0654 MTG-FCI: ATBD for Optimal
Cloud Analysis Product.
2011 Philip Watts
R2 J. Geophys. Res., 116, D16203,
doi:10.1029/2011JD015883
Retrieval of two-layer cloud
properties from multispectral
observations using optimal
estimation
2011 P. D. Watts, R. Bennartz,
and F. Fell

<!-- source_page: 234 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




19 CALIBRATION SUPPORT
19.1 Algorithm Configuration Information
19.1.1 Algorithm Name
IR and VIS Calibration Support
19.1.2 Algorithm Identifier
EUM_MSG_CAL_A001
19.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 26/11/96 S. A. Tjemkes CAL Baseline
1.1 20/5/97 H. K. Wilson TBDs resolved, bid clarification points added, editorial
errors corrected.
1.2 1/7/97 S. A. Tjemkes Descoping and simplification of Cross Satellite
Calibration.
1.3 9/12/97 H. K. Wilson Requirements Analysis clarification points added.
1.4 13/3/98 H. K. Wilson Peer Group Review changes added, algorithm
simplified.
1.5 25/7/05 T. Heinemann Updates according to ARs 9271, 9492, 10164, 11264,
11596.
1.6 15/09/08 T. Heinemann Updated according to ECP 814.
19.2 Inputs
The tables on the following pages list the input para meter specifications for th ese specific calibration
instances:

Calibration Monitoring
Absolute Calibration of Windows Channels
Absolute Calibration of Water Vapour Channels
Absolute Calibration of Ozone Channel
Determination of the Vicarious Calibration Constants
Cross-Satellite Calibration

<!-- source_page: 235 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 236 of 298

INPUT PARAMETERS FOR CALIBRATION MONITORING
Parameter Mnemonic Units Min Max Acc Prec Source
Scenes type CLDMSK - - - - - SCE
Number of pixels in the search area CMPSA - 0 1089 1 1 Set-up
Minimum number of clear sky pixels in the search area CMNCR - 0 1089 1 1 Set-up
Observed radiances OBSRAD mWm -2sr-1 (cm-1)-1 0 - - - Derived from level 1.5 data
Atmospheric Correction Table CALRAD mWm-2sr-1 (cm-1)-1 0 - - - RTM
Number of geographical regions CMNGEO - 0 - - - Set-up
Position of geographical regions CMPGEO - - - - - Set-up
Distance to nearest coastline coastdist km 0 1000 1 1 Set-up
Channel-dependent threshold parameter CMTRS - 0 100 10-1 10-2 Set-up
Mean radiance difference reference per channel cm_mean_rad chan - - - - - Set-up
Calibration Monitoring tolerance threshold per channel cm_tolchan - 0 - - - Set-up
Table 61: Input parameters for calibration monitoring
INPUT PARAMETERS FOR ABSOLUTE CALIBRATION OF WINDOWS CHANNELS
Parameter Mnemonic Units Min Max Acc Prec Source
Scenes Type CLDMSK - - - - - SCE
Number of pixels in the search area ACPSA - 0 1089 1 1 Set-up
Minimum number of clear sky pixels in the search area ACNCR - 0 1089 1 1 Set-up
Observed digital counts OBSCNT counts 0 - - - Level 1.5 data
Level 1.5 space counts SPACNT counts 0 - - - Level 1.5 data
Atmospheric Correction Table CALRAD mWm -2sr-1(cm-1)-1 0 - - - RTM
Channel-dependent threshold parameter ACTRS - 0 100 10-1 10-2 Set-up
Distance to nearest coastline coastdist km 0 1000 1 1 Set-up
Table 62: Input parameters for Absolute Calibration of windows channels

<!-- source_page: 236 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 237 of 298


INPUT PARAMETERS FOR ABSOLUTE CALIBRATION OF WATER VAPOUR CHANNELS
Parameter Mnemonic Units Min Max Acc Prec Source
Scenes type CLDMSK - - - - - SCE
Pressure p hPa 0 1050 10 -2 10 -3 Observations
Temperature T K 170 350 10-1 10-2 Observations
Water vapour relative humidity RH % 0 100 1 1 Observations
Cut-off time ACCUT hours 0 24 1 1 Set-up
Minimum relative humidity ACMINRH % 0 100 1 1 Set-up
Max. relative humidity ACMAXRH % 0 100 1 1 Set-up
Minimum observations ACMINOBS - 0 1089 1 1 Set-up
Maximum cloudiness ACMAXCLD % 0 100 1 1 Set-up
Number of pixels in the search area ACPSA - 0 1089 1 1 Set-up
Minimum number of clear sky pixels in the search area ACNCR - 0 1089 1 1 Set-up
Observed digital counts OBSCNT counts Level 1.5 data
Level 1.5 space counts SPACNT counts 0 Level 1.5 data
Vicarious Calibration Table CALRAD mWm -2sr-1(cm-1)-1 RTM
Channel-dependent threshold parameter ACTRS - 0 100 10-1 10-2 Set-up
Table 63: Input parameters for absolute calibration of water vapour channels

<!-- source_page: 237 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 238 of 298

INPUT PARAMETERS FOR ABSOLUTE CALIBRATION OF OZONE CHANNEL
Parameter Mnemonic Units Min Max Acc Prec Source
Scenes type CLDMSK - - - - - SCE
Pressure p hPa 0 1050 10 -2 10 -3 Observations
Temperature T K 170 350 10-1 10-2 Observations
Water vapour relative humidity RH % 0 100 1 10 -1 Observations
Ozone mixing ratio mo3 kg/kg 0 - - - Observations
Cut-off time ACCUT hours 0 24 1 1 Set-up
Minimum observations ACMINOBS - 0 1089 1 1 Set-up
Maximum cloudiness ACMAXCLD % 0 100 1 1 Set-up
Number of pixels in the search area ACPSA - 0 1089 1 1 Set-up
Minimum number of clear sky pixels in the search area ACNCR - 0 1089 1 1 Set-up
Observed digital counts OBSCNT counts 0 - - - Level 1.5 data
Level 1.5 space counts SPACNT counts 0 - - - Level 1.5 data
VICARIOUS CALIBRATION TABLE CALRAD mWm-2sr-1(cm-1)-1 0 - - - RTM
Channel-dependent threshold parameter ACTRS - 0 100 10 -1 10 -2 Set-up
Table 64: Input parameters for absolute calibration of ozone channel

INPUT PARAMETERS FOR INCLUSION IN PRODUCT HEADER
Parameter Mnemonic Units Min Max Acc Prec Source
On-board black body calibration data BB_CAL - - - - - LEVEL 1.5
IMAGE DATA
Table 65: Input parameters for inclusion in product header

<!-- source_page: 238 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 239 of 298

INPUT PARAMETERS FOR DETERMINATION OF THE VICARIOUS CALIBRATION CONSTANTS
Parameter Mnemonic Units Min Max Acc Prec Source
Averaging time period outside eclipse season TIMPEROUT hours 0 24 1 1 Set-up
Averaging time period inside eclipse season TIMPERIN days 0 24 1 1 Set-up
Channel-dependent threshold parameter VOCCTRS - 0 100 10-1 10-2 Set-up
Table 66: Input parameters for determination of the vicarious calibration constants
INPUT PARAMETERS FOR CROSS SATELLITE CALIBRATION
Parameter Mnemonic Units Min Max Acc Prec Source
MSG observed counts GEOOBS counts 0 - - - Level 1.5 data
MSG space counts GEOSPC counts 0 - - - Level 1.5 data
Clear Sky FSD, (LEO) radiances, geometrically corrected and absolutely
calibrated
LEOOBS mWm-2sr-1(cm-1)-1 0 - - - FSD
Minimum number of clear sky pixels in target area CCGEONCR - 0 - - - Set-up
Third degree polynomial coefficients a(0), a(1), a(2), a(3) POLCOEF - - - - - Set-up
Number of pixels in target area CCPTA - 0 4356 1 1 Set-up
Viewing angle difference VIEWDIFF  0 90 1 1 Set-up
Channel-dependent threshold parameter CCTRS1 - 0 100 10 -1 10 -2 Set-up
Channel-dependent threshold parameter CCTRS2 - 0 100 10-1 10-2 Set-up
Distance threshold DISTTHRS km 0 1000 1 1 Set-up
Observation time difference OBSTIMDIFF seconds 0 1800 1 1 Set-up
Table 67: Input parameters for cross satellite calibration

<!-- source_page: 239 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 240 of 298

INPUT PARAMETERS FOR ABSOLUTE CALIBRATION
Parameter Mnemonic Units Min Max Acc Prec Source
Weighting functions for abs_cal_wt_vicc - 0 1 - - SET-UP
Absolute calibration Calculation abs_cal_wt_xsat - 0 1 - - Set-up
Vicarious calibration tolerance threshold per channel vic_tolchan - 0 - - - Set-up
Cross-sat. calibration tolerance threshold per channel xsat_tol chan - 0 - - - Set-up
Quality flag weights per channel qf_wt_cmchan qf_wt_vicchan
qf_wt_xsatchan
- 0 1 - - Set-up
Quality flag thresholds per channel qf_upper_thr chan qf_lower_thrchan - 0 1 - - Set-up
Operational calibration coefficient per channel OCCchan - - - - - Level 1.5 data
Table 68: Input parameters for absolute calibration

INPUT PARAMETERS FROM OFF-LINE ABSOLUTE CALIBRATION OF VIS/NIR CHANNELS
Parameter Mnemonic Units Min Max Acc Prec Source
Quality flag for Level 1.5 data QFchan - - - - - Set-up
Used reference data flag rdf chan - - - - - Set-up
Absolute calibration method flag ABC_flagchan - - - - - Set-up
Absolute cal. weight (Vic. Cal) AC_wt_vic chan - - - - - Set-up
Abs calibratoin weight (Xsat. Cal) AC_wt_xsatchan - - - - - Set-up
Absolute calibration coefficients for channels VIS0.6, VIS0.8, NIR1.6, HRVIS VIS_CC chan - - - - - Set-up
Estimated accuracy of absolute calibration ACCchan - - - - - Set-up
Bias from calibration monitoring BIAS chan - - - - - Set-up
RMS from calibration monitoring RMSchan - - - - - Set-up
Space count Space_cnt chan - - - - - Set-up
Table 69: Input parameters from off-line absolute calibration of VIS/NIR channels

<!-- source_page: 240 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




19.3 Algorithm Functional Specification
19.3.1 Overview
The main task of the Calibration Support is the monitoring of the radiometric accuracy of the level 1.5
data of the eight infrared channels, namely IR3.9, WV6.2, WV7.3, IR8.7, IR9.7, IR10.8, IR12.0 and
IR13.4. A further application of the algorithm is to provide absolute calibration coefficients for the
eight infrared channels, which can be used as a backup in the event of failure of the on-board
calibration. Additionally, the VIS/NIR calibration coefficients, which are generated off-line in the
algorithm prototyping environment, are also incorporated in this algorithm. The calibration
coefficients for all the SEVIRI channels are then supplied to the IMPF.
The output of the Calibration Monitoring process is data describing the temporal evolution of the
relation between the level 1.5 data and calculated radiances. These latter radiances are calculated
using meteorological data from the forecast model. These data shall
be generated for every repeat
cycle.
The output of the Absolute Calibration task consists of the temporal evolution of the instantaneous
calibration relation between the digital counts and reference radiances. These reference radiances are
either calculated by the Radiative Transfer Model using meteorological observations or taken from
observations by instruments mounted on a space-borne platform in a Low Earth Orbit (LEO), e.g.
FSD. The generation of the Absolute Calibration shall be determined by the availability of the
required input data.
The on-board black body calibration information shall also be included in the product header for the
CAL products sent to the UMARF.
The enhancement of the calibration monitoring of the window channels using the SST product and
independent observations is a Future Enhancement.
19.3.2 Algorithm Description
19.3.2.1 Calibration Monitoring
For the Calibration Monitoring the following tasks shall be performed:
1. A valid target point shall be defined as any grid point of the forecast model not over land areas
with a minimum distance to the nearest coastline exceeding a threshold defined by a set-up
parameter, within the EMD processing area.
2.
For each valid target point, a search area shall be defined, as a square area, consisting of a fixed
number of pixels, defined by a set-up parameter, with its centre pixel located at the grid point of
the forecast model.
3.
For each of the search areas, all pixels which according to the Scenes Analysis are determined
as being clear, shall be selected.
4. If the total number of clear sky pixels in the valid target area does not exceed a threshold
specified by a set-up parameter, this target area shall be removed from further processing.
5. For each of the valid target points and each of the eight infrared channels, a local mean
observed clear sky radiance and the associated local standard deviation shall be calculated from
the level 1.5 data converted into radiances (units: mWm-2sr-1(cm-1)-1) over all clear sky pixels in
the corresponding search area.

<!-- source_page: 241 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




6. For each of the valid target areas, and each of the eight infrared channels, a calculated clear sky
radiance shall be extracted from the Atmospheric Correction Tables generated by the Radiative
Transfer Model.
7. For each of the eight IR channels and each of the valid target areas, the local radiance
difference between the local mean observed clear sky radiance and the calculated clear sky
radiance shall be calculated. For each of the eight IR channels a mean radiance difference and
its associated standard deviation shall be calculated from all local radiance differences. For
each of the eight IR channels, a reference value for the mean radiance difference shall be
defined by a set-up parameter. For each of the eight IR channels a tolerance threshold shall be
defined by a set-up parameter.
For each of the eight IR channels, the following tests shall be implemented in order to set the
radiance quality flag for that channel:
a. If the absolute difference between the mean radiance difference and the reference value is less
than or equal to the standard deviation associated with the mean radiance difference, or
b. when the mean radiance difference is smaller than the reference value and the mean radiance
difference reduced by the standard deviation associated with the mean radiance difference is
larger than the reference value reduced by the tolerance value, or
c. when the mean radiance difference is larger than the reference value and the mean radiance
difference increased by the standard deviation associated with the mean radiance difference is
smaller than the reference value increased by the tolerance value, then:
The radiance quality flag shall be set indicating that according to the Calibration Monitoring
the operational calibration produces acceptable results.
If conditions a, b and c do not apply, then:
d. When the mean radiance difference is smaller than the reference value and the absolute
difference between the mean radiance difference and the reference reduced by the tolerance
value is less than or equal to the standard deviation associated with the mean radiance
difference, or
e.
when the mean radiance difference is larger than the reference value and the absolute
difference between the mean radiance difference and the reference increased by the tolerance
value is less than or equal to the standard deviation associated with the mean radiance
difference, then:
The radiance quality flag shall be set indicating that according to the Calibration Monitoring
the operational calibration produces suspect results, but that improvements are not required.
If conditions a, b, c, d, and e do not apply, then the radiance quality flag shall be set indicating
that according to the Calibration Monitoring the operational calibration produces non-acceptable
results.
8. The implementation of the Calibration Monitoring shall be such that the comparison between the
radiance difference and the reference value can be applied to all valid target areas in geographical
areas specified by user-defined set-up parameters, over a time period specified by a user-defined
set-up parameter.

<!-- source_page: 242 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




19.3.2.2 Absolute Calibration Coefficient
This algorithm is responsible for deriving absolute calibration coefficients for the eight infrared
channels of MSG, i.e. IR3.9, WV6.2, WV7.3, IR8.7, IR9.7, IR10.8, IR12.0 and IR13.4, independently
of the on-board calibration. The output of this algorithm consists of tables which (when used as a time
series) can be used to describe the temporal evolution of the Absolute Calibration Coefficient. This
information is provided to the IMPF for further processing.
The calibration coefficients for the VIS/NIR channels are generated off-line and shall be read into this
algorithm and output together with the IR calibration coefficients.
The Absolute IR Calibration Coefficients shall be calculated as a weighted mean of the Vicarious
Operational Calibration Coefficient and the Cross Satellite Operational Calibration Coefficient using
weights determined by set-up parameters.
The implementation of the Absolute Calibration shall be such that the analysis can be applied to all
valid target areas in geographical areas specified by user-defined set-up parameters, over a time
period specified by a user-defined set-up parameter.
19.3.2.2.1 Vicarious Operational Calibration Coefficient
The determination of the Vicarious Operational Calibration Coefficient shall be done in two steps.
First the Vicarious Instantaneous Calibration Coefficient (VICC) is calculated for each channel. From
these in the second step the Vicarious Operational Calibration Coefficient (VOCC) shall be
calculated. The actual procedure to calculate the VOCC no longer depends on the eclipse season.
The monitoring VICC of all IR channels, except the IR9.7 channel, shall be based on meteorological
data from the forecast model, supplemented with Sea Surface Temperature Data. For the calculation
of the VICC of these monitoring channels the following tasks shall
be performed:
1. A valid target point shall be defined as any grid point of the forecast model not over land areas
with a minimum distance to the nearest coastline exceeding a threshold defined by a set-up
parameter, within the EMD processing area.
2. For each valid target point a search area shall be defined, as a square area, consisting of a fixed
number of pixels, defined by a set-up parameter, with its centre pixel located at the grid point of
the forecast model.
3. For each of the search areas, all pixels which according to the Scenes Analysis are determined
as being clear, shall be selected.
4. If the total number of clear sky pixels in the valid target area does not exceed a threshold
specified by a set-up parameter, this valid target area is removed from further processing.
5. For each of the valid target points, and each of the monitoring channels, the arithmetic mean
observed digital count shall be calculated from the observations given by the level 1.5 data in
digital counts of all clear sky pixels in the corresponding search area.
6. For each of the valid target areas, and each of the IR channels, the local VICC defined as the
ratio between the clear sky radiance extracted from the Atmospheric Correction Tables
generated by the Radiative Transfer Model and the mean observed clear sky digital count
corrected for the level 1.5 space count, shall be calculated.
7. For each of the monitoring channels, a first-guess VICC and its standard error shall be
calculated from the local VICC for all valid target areas.

<!-- source_page: 243 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




8. Each local VICC for which the absolute difference between the local VICC and the first-guess
VICC exceeds a threshold, shall be removed from further processing. This test shall be done
for each of the monitoring channels. The threshold shall be taken as proportional to the
standard error of the first-guess VICC; the proportional factor shall be determined by a set-up
parameter.
9. For each of the monitoring channels, the VICC shall be calculated as the arithmetic mean over
all remaining local VICCs.
In addition, VICCs of the strongly absorbing water vapour channels, WV6.2, shall be calculated
based on actual radiosonde ascents. These observations are done twice a day, at midnight and midday.
The vicarious calibration shall be based on all available observations, subject to quality control within
a cut-off time determined by a set-up parameter after the observational time. For the derivation of the
VICC of these channels the following tasks shall be performed:
1. A valid target point shall be defined as a location where an actual radiosonde observation
exists.
2. Valid target points where the corresponding radiosonde observations do not meet the following
quality control criteria shall be removed from further processing:
 Radiosonde observations shall be within the external meteorological data processing area.
 The radiosonde bulletins shall be merged in order to provide a single profile per station.
 Radiosonde observations shall have an average relative humidity in excess of a threshold
value defined by a channel-dependent set-up parameter.
 Radiosonde observations shall have a minimum number of observations within the
sensitivity
range of the channel, determined by a channel-dependent set-up parameter.

The observed cloudiness given by the associated surface observations shall not exceed a
threshold determined by a set-up parameter.
 The observed relative humidity shall not exceed a threshold defined by a set-up parameter.
3. For each valid target point a search area shall be defined, as a square area, consisting of a fixed
number of pixels, defined by a set-up parameter, with its centre pixel located at the position of
the observation.
4. For each of the search areas, all pixels which according to the Scenes Analysis are determined
as being clear, shall be selected.
5. If the total number of clear sky pixels in the target area does not exceed a threshold specified by
a set-up parameter, this target area is removed from further processing.
6. For each of the valid target points and each of the water vapour channels, the arithmetic mean
observed digital count shall be calculated from the observations given by the level 1.5 data in
digital counts of all clear sky pixels in the corresponding search area.
7. For each of the valid target areas and each of the water vapour channels, the local VICC
defined as the ratio between the clear sky radiance extracted from the Absolute Calibration
Tables for the water vapour channels generated by the Radiative Transfer Model and the mean
observed clear sky digital count corrected for the level 1.5 space count, shall be calculated.
8. For each of the water vapour channels, a first-guess VICC and its standard error shall be
calculated from the local VICC for all valid target areas.

<!-- source_page: 244 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




9. Each local VICC for which the absolute difference between the local VICC and the first-guess
VICC exceeds a threshold, shall be removed from further processing. This test shall be done
for each of the water vapour channels. The threshold shall be taken as proportional to the
standard error of the first-guess VICC; the proportional factor shall be determined by a set-up
parameter.
10. For each of the water vapour channels, the VICC shall be calculated as the arithmetic mean
over all remaining local VICCs.
The VICC of the ozone channel, IR9.7, shall be based on ozonesonde ascents. These observations are
done nominally once a week. The VICC shall be based on all available observations, subject to
quality control within a cut-off time determined by a set-up parameter after the observational time.
For the derivation of the VICC of this channel the following tasks shall be performed:
1. A target area shall be defined as any grid point where an actual ozonesonde observation exists.
2. Target areas where the corresponding ozonesonde observations do not meet the following
quality control criteria shall be removed from further processing:
 Ozonesonde observations shall be within the external meteorological data processing
area.
 Ozonesonde observations shall have a minimum number of observations within
the sensitivity range of the channel, determined by a set-up parameter.
 The observed cloudiness given by the associated surface observations shall not exceed a
threshold determined by a set-up parameter.
3. For each valid target a search area shall be defined, as a square area, consisting of a fixed
number of pixels, defined by a set-up parameter, with its centre pixel located at the position of
the observation.
4. For each of the search areas, all pixels which according to the Scenes Analysis are determined as
being clear, shall be selected.
5. If the total number of clear sky pixels in the target area does not exceed a threshold specified by
a set-up parameter, this target area is removed from further processing.
6. For each of the valid target areas, the arithmetic mean observed digital count shall be calculated
from the observations given by the level 1.5 data in digital counts of the ozone channel of all
clear sky pixels in the corresponding search area.
7. For each of the valid target areas, the local VICC defined as the ratio between the clear sky
radiance extracted from the Absolute Calibration Tables for the ozone channel generated by the
Radiative Transfer Model and the mean observed clear sky digital count corrected for the level
1.5 space count, shall be calculated.
8. A first-guess VICC and its standard error shall be calculated from the local VICC for all valid
target areas.
9. Each local VICC for which the absolute difference between the local VICC and the first-guess
VICC exceeds a threshold shall be removed from further processing. The threshold shall be
taken as proportional to the standard error of the first-guess VICC; the proportional factor shall
be determined by a set-up parameter.
10. The VICC shall be calculated as the arithmetic mean over all remaining local VICCs.
For each of the eight infrared channels, the VOCC shall be based on the VICCs.
For the channel WV6.2 the VOCC should be based only on VICCs derived from observations.

<!-- source_page: 245 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




For the channel IR3.9 the contribution of reflected sunlight to the signal at the satellite does not allow
the use of images with a daylight component for the vicarious calibration which is based on IR
radiative transfer. Therefore only the VICCs derived in the three repeat cycles around local midnight
are used to calculate the VOCC for this channel.
For each channel the following tasks shall be performed:
1. A first-guess VOCC and its standard error shall be calculated as the arithmetic mean over each
VICC within a time period determined by a set-up parameter.
2. Each VICC within this time period for which the absolute difference between the VICC and the
first-guess VOCC exceeds a threshold, shall be removed from further processing. This
threshold shall be taken as proportional to the standard error of the first-guess VOCC; the
proportional factor shall be determined by a set-up parameter. If fewer than three VICCs are
available this criterion is not applied.
3. A VOCC, i.e. the arithmetic mean over all valid VICCs and its associated standard deviation,
shall be calculated.
4. A monitoring of the operational calibration coefficient shall be implemented in a similar way
as described for the monitoring of the radiances. In particular, the following steps shall be
implemented:
For each of the eight IR channels a tolerance threshold shall be defined set by a set-up parameter. For
each of the eight IR channels, the following tests shall be implemented in order to set an Operational
Calibration Coefficient (OCC) quality flag for that channel:
a. If the absolute difference between the VOCC and the OCC is less than or equal to the
standard deviation associated with the VOCC, or
b. when the VOCC is smaller than the OCC, and the VOCC reduced by its standard deviation is
larger than the OCC reduced by the tolerance value, or
c. when the VOCC is larger than the OCC, and the VOCC increased by its standard deviation is
smaller than the OCC increased by the tolerance value, then:
A quality flag shall be set indicating that according to the vicarious calibration method the
operational calibration produces acceptable results.
If conditions a, b and c do not apply, then:
d. when the VOCC is smaller than the OCC, and the absolute difference between the VOCC and
the OCC reduced by the tolerance value is less than or equal to the standard deviation
associated with the VOCC, or
e.
when the VOCC is larger than the OCC, and the absolute difference between the VOCC and
the OCC increased by the tolerance value is less than or equal to the standard deviation
associated with the VOCC, then:
A quality flag shall be set indicating that according to the vicarious calibration method the
operational calibration produces suspect results, but that improvements are not required.
If conditions a, b, c, d and e do not apply, then a quality flag shall be set indicating that
according to the Vicarious Calibration Method the operational calibration produces nonacceptable results.

<!-- source_page: 246 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




19.3.2.2.2 Cross-Satellite Operational Calibration Coefficient
The cross satellite calibration shall be done for each foreign satellite independently.
The determination of the Cross Satellite Operational Calibration Coefficient shall be done in two
steps. First, the appropriate foreign satellite data shall be transferred to MPEF and if necessary
decoded. The most suitable foreign satellite overpass for the specified repeat cycle shall be selected
and only data from this satellite shall be used for this repeat cycle. As a second step, the Cross
Satellite Instantaneous Calibration Coefficient (CSICC) shall be calculated.
For each of the eight infrared channels, namely IR3.9, WV6.2, WV7.3, IR8.7, IR9.7, IR10.8, IR12.0
and IR13.4, for which suitable foreign satellite data are available, the following tasks shall be
performed:
1. A valid target area shall be defined as an area consisting of a finite number of foreign satellite
pixels determined by a set-up parameter.
2. For each valid target area, all pixels of the corresponding MSG channel, which meet the
following criteria, shall be selected:
 The MSG observation shall be determined as being clear according to the Scenes Analysis.
 The great circle difference between the centre of the target area and the position of the MSG
pixel shall be less than a threshold defined by a set-up parameter.
 The difference between the MSG observational time, defined by the average acquisition time
of the level 1.0 data line, and the FSD observational time shall not exceed a threshold defined
by a set-up parameter.
 The difference between the viewing angle of the MSG observation and the mean viewing
angle of the foreign satellite observations within the valid target area shall not exceed a
threshold defined by a set-up parameter.
3. If the total number of selected MSG pixels in the target area does not exceed a threshold
specified by a set-up parameter, this target area shall be removed from further processing.
4. If the standard deviation of the selected pixels exceeds a threshold defined by a set-up
parameter, this target area shall be removed from further processing.
5. For each of the valid target areas, the local mean observed MSG digital count and its standard
error shall be calculated from the instantaneous MSG observations given by the level 1.5 data
in digital counts of all clear sky pixels in the valid target area.
6. For each of the valid target areas, the local mean foreign satellite clear sky radiance observation
and its standard error shall be calculated from the individual foreign satellite clear sky
observations within the target area.
7. For each of the valid target areas, the local mean foreign satellite clear sky observations shall
be corrected for the difference in spectral response function between the foreign satellite
channel and the corresponding MSG channel, using a second order polynomial, with constants
defined by set-up parameters or an appropriate spectral convolution.
8. For each of the valid target areas, the local CSICC defined as the ratio between the local mean
foreign satellite clear sky radiance (corrected for the spectral response functions) and the local
mean MSG clear sky digital count (corrected for the level 1.5 space count) shall be calculated.
9. A first-guess CSICC and its standard error shall be calculated from the local CSICC for all
valid target areas.

<!-- source_page: 247 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




10. Each local CSICC for which the absolute difference between the local CSICC and the firstguess CSICC exceeds a threshold shall be removed from further processing. The threshold
shall be taken as proportional to the standard error of the first-guess CSICC; the proportional
factor shall be determined by a set-up parameter. The other CSICCs shall be stored as Cross
Calibration Operational Calibration Coefficients (CSOCC) in the calibration data.
11. A monitoring of the operational calibration coefficient shall be implemented in a similar way as
described for the monitoring of the radiances. In particular, the following steps shall be
implemented:
For each of the eight IR channels a tolerance threshold shall be set by a set-up parameter. For each of
the eight IR channels, the following tests shall be implemented in order to set an Operational
Calibration Coefficient (OCC) quality flag from the Cross Satellite Operational Calibration Method
for that channel:
a. If the absolute difference between the CSOCC and the OCC is less than or equal to the
standard deviation associated with the CSOCC, or
b. when the CSOCC is smaller than the OCC and the CSOCC reduced by its standard deviation
is larger than the OCC reduced by the tolerance value, or
c. when the CSOCC is larger than the OCC and the CSOCC increased by its standard deviation
is smaller than the OCC increased by the tolerance value, then:
A quality flag shall be set indicating that according to the cross-satellite calibration method
the operational calibration produces acceptable results.
If conditions a, b and c do not apply, then:
d.
When the CSOCC is smaller than the OCC and the absolute difference between the CSOCC
and the OCC reduced by the tolerance value is less than or equal to the standard deviation
associated with the CSOCC, or
e. when the CSOCC is larger than the OCC and the absolute difference between the CSOCC and
the OCC increased by the tolerance value is less than or equal to the standard deviation
associated with the CSOCC, then:
A quality flag shall be set indicating that according to the cross-satellite calibration method
the operational calibration produces suspect results, but that improvements are not required.
If conditions a, b, c, d, and e do not apply, then a quality flag shall be set indicating that according
to the cross-satellite calibration method the operational calibration produces non-acceptable
results.
The implementation of the Cross Satellite Calibration Method shall be such that for each channel a
comparison between the local CSICC and the OCC can be applied to all valid target areas in
geographical areas specified by user-defined set-up parameters, over a time period specified by a
user-defined set-up parameter.
19.3.2.2.3
Inclusion of VIS/NIR Calibration Coefficients
The solar calibration monitoring and the derivation of calibration coefficients for the three visible
SEVIRI channels will be performed outside the operational MPEF processing. The results of this
process, namely the VIS/NIR calibration coefficients, shall be input via a static data file and output
along with the IR calibration coefficients as defined above.

<!-- source_page: 248 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




19.3.3 Automatic Quality Control (AQC)
An Overall Quality Flag for each channel shall be set using the quality flags set by the cross-satellite
calibration method, the vicarious calibration method and the calibration monitoring method. This
shall be done according to the following steps. For each of the three methods, the quality flag shall be
transformed into a numerical quality equivalent, namely 0, 0.5 and 1.0 for the quality flags ‘nonacceptable’, ‘suspect’ and ‘acceptable’ respectively. The numerical equivalent of the Overall Quality
Flag shall be calculated as a linear weighted mean of the numerical quality equivalents, with the
understanding that the weights for the three methods shall be set by set-up parameters, and the linear
summation of these three weights shall be equal to unity. The Overall Quality Flag shall be set
depending on the value of its numerical equivalent according to the following rules:
a. If the numerical equivalent of the Overall Quality Flag is smaller than or equal to a lower
threshold value, set by a set-up parameter, nominal value 0.33, then the Overall Quality Flag shall
be set to ‘non-acceptable’.
b. If the numerical equivalent of the Overall Quality Flag is larger than or equal to an upper
threshold value, set by a set-up parameter, nominal value 0.66, then the Overall Quality Flag shall
be set to ‘acceptable’.
c. If condition a and condition b do not apply then the Overall Quality Flag shall be set to ‘suspect’.

<!-- source_page: 249 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 250 of 298

19.4 Outputs
The following data shall be output:

Parameter Mnemonic Units Min Max Prec Acc To
Satellite ID SAT_ID - 1 3 1 1 CAL Header
Date and Time of Repeat Cycle CAL_RC_DATE YYYYMMDDHHMMSS - - - - CAL Header
Abs Cal Performed flag per channel ABS_CAL_PERF - FALSE TRUE - - CAL Header
Applicable Date/Time for Abs Calibration per channel CAL_DATE YYYYMMDDHHMMSS - - - - CAL Header
Cal Mon Quality flag per channel CM_QF - - - - - CAL Header
Vicarious Operational Calibration Coefficient per channel VOCC - - - - - CAL Header
Vic Cal Quality flag per channel VICC_QF - - - - - CAL Header
Cross-Satellite Operational Calibration Coefficient per channel CSOCC - - - - - CAL Header
Xsat Cal Quality flag per channel XSAT_QF - - - - - CAL Header
Cal Data for IMPF, per channel:
Quality Flag for Level 1.5 data QF - - - - - CAL Header
Used Reference Data Flag rdf - - - - - CAL Header
Absolute Calibration Method Flag ABC_flag - - - - - CAL Header
Abs Cal Weight (Vic. Cal) AC_wt_vic - 0 1 - - CAL Header
Abs Cal Weight (Xsat. Cal) AC_wt_xsat - 0 1 - - CAL Header
Absolute Calibration Coefficients CC - - - - - CAL Header
Estimated Accuracy of Absolute Calibration ACC - - - - - CAL Header
Bias from Calibration Monitoring BIAS - - - - - CAL Header
RMS from Calibration Monitoring RMS - - - - - CAL Header
Space Count Space_cnt Counts 0 - - - CAL Header

<!-- source_page: 250 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 251 of 298

Parameter Mnemonic Units Min Max Prec Acc To
BB Cal Data:
On-board Black body calibration Data BB_CAL - - - - - CAL Header
VICC History Data:
VICC Calibration Time OLD_TIME YYYYMMDDHHMMSS - - - - CAL Header
VICC Calibration Type VICC_TYPE - - - - - CAL Header
Old VICCs OLD_VICC - - - - - CAL Header
Cal Mon Data, per collocation:
Collocation latitude col_lat degrees -90 90 0.01 0.01 CAL
Collocation longitude col_lon degrees -180 180 0.01 0.01 CAL
Collocation box size (N-S) col_size pixels 1 - - - CAL
Collocation box size (E-W) col_size pixels 1 - - - CAL
Collocation time C_TIME - - - - - CAL
Collocation channel C_CHAN - - - - - CAL
Mean Observed radiance (SEVIRI) OBS_RAD - - - - - CAL
Mean Calculated radiance (from RTM) CALC_RAD - - - - - CAL
Local Difference LOCAL_DIFF - - - - - CAL
Abs Cal Data, per collocation:
For all VICCs used to calculate the VOCCs, per VICC:
Collocation latitude col_lat degrees -90 90 0.01 0.01 CAL
Collocation longitude col_lon degrees -180 180 0.01 0.01 CAL
Collocation box size (N-S) col_size pixels 1 - - - CAL
Collocation box size (E-W) co l_size pixels 1 - - - CAL
Collocation time C_TIME - - - - - CAL
Collocation channel C_CHAN - - - - - CAL

<!-- source_page: 251 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 252 of 298

Parameter Mnemonic Units Min Max Prec Acc To
Mean Observed radiance (SEVIRI) OBS_RAD - - - - - CAL
Mean Calculated radiance (from Met Obs) CALC_RAD - - - - - CAL
Local VICC LOCAL_VICC - - - - - CAL
For all CSICCs used to calculate theCSOCCs, per CSICC:
Collocation latitude col_lat degrees –90 90 0.01 0.01 CAL
Collocation longitude col_lon degrees –180 180 0.01 0.01 CAL
Collocation box size (N-S) col_size pixels 1 - - - CAL
Collocation box size (E-W) col_size pixels 1 - - - CAL
Collocation time C_TIME - - - - - CAL
Collocation channel C_CHAN - - - - - CAL
Mean Observed radiance (SEVIRI) OBS_RAD - - - - - CAL
Mean Observed radiance (from FSD) FSD_RAD - - - - - CAL
Local CSICC LOCAL_CSICC - - - - - CAL
Table 70: Calibration Support required outputs
19.5 Prototyping and Testing
No prototyping activity was carried out for this algorithm.
19.6 Future Enhancements
No future enhancements are currently foreseen.
19.7 References
None.

<!-- source_page: 252 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




20 CLOUD MASK PRODUCT GENERATION
20.1 Algorithm Configuration Information
20.1.1 Algorithm Name
Cloud Mask (CLM)
20.1.2 Algorithm Identifier
EUM_MSG_CLM_A001
20.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 14/5/98 H.-J. Lutz CLM Baseline
1.1 31/8/98 H.-J. Lutz Clarification of the option of the CLM.
1.2 9/9/2002 S. S. Elliott Redefinition of CLM content, and change of format to
GRIB Edition 2. See EUM/MSG/ECP/328.
20.2 Inputs
The Cloud Mask algorithm shall use the following data:

Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Scenes type scenes_type - 0 255 1 1 pixel SCE
SCE quality flag AQC_flag % 0 100 1 1 pixel SCE

20.3 Algorithm Functional Specification
20.3.1 Overview
The purpose of the Cloud Mask Product (CLM) is to provide information about the cloud
contamination for each pixel for every repeat cycle. The CLM Product is a GRIB Edition 2 encoded
product and shall provide the following information per pixel:
Classification of pixel type as one of the following:
 clear sky over water
 clear sky over land
 cloud
 no data
The CLM Product shall be derived from the existing information produced on a pixel basis for every
repeat cycle by the Scenes Analysis (SCE) algorithm.

<!-- source_page: 253 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




20.3.2 Algorithm Description
20.3.2.1 Cloud Mask Product
The value for the cloud_mask shall be generated as follows:
 If the scenes_type is ‘cloudy’, then the cloud_mask shall be set to ‘cloud’.
 If the scenes_type is ‘clear with sunglint’, then the cloud_mask shall be set to ‘clear sky over
water’.
 If the scenes_type is ‘snow/ice over land’, then the cloud_mask shall be set to ‘clear sky over
land’.
 If the scenes_type is ‘snow/ice over water’, then the cloud_mask shall be set to ‘clear sky over
water’.
 If the scenes_type is ‘water’, then the cloud_mask shall be set to ‘clear sky over water’.
 If the scenes_type is one of the surface types, then the cloud_mask shall be set to ‘clear sky
over land’.
 If the scenes_type is ‘no scenes identified, missing input data’, then the cloud_mask shall be
set to ‘no data’.
20.3.3 Automatic Quality Control (AQC)
Not required as already performed as part of Scenes Analysis.
20.4 Outputs
The following data shall be produced for the cloud mask product for every pixel in the form of a
GRIB Edition 2 encoded product.

Parameter Mnemonic Units Min Max Prec Acc To
Cloud Mask cloud_mask - 0 3 1 1 CLM

The parameter value is defined in code table 4.217 of GRIB Edition 2. A specific entry (7) was added
to code table 4.2 (Product Discipline 3, Parameter Category 0) to specify cloud mask data.

Parameter Value Meaning
Cloud Mask 0 Clear sky over water
1 Clear sky over land
2 Cloud
3 No data
20.5 Prototyping and Testing
CLM extraction has been extensively tested during the Post-Acceptance Support phase of the project.
20.6 Future Enhancements
None
20.7 References
None

<!-- source_page: 254 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




21 TOTAL OZONE PRODUCT GENERATION
21.1 Algorithm Configuration Information
21.1.1 Algorithm Name
Total Ozone (TOZ)
21.1.2 Algorithm Identifier
EUM_MSG_TOZ_A001
21.1.3 Algorithm Specification Version History
Version Date Modified By Description
Draft A 04/01/99 F. Karcher TOZ Draft Baseline
1.0 15/01/99 H.-J. Lutz TOZ Baseline
2.0 25/07/05 R. Swifte Replacement algorithm
3.0



29/10/09



J. D. Jackson
L. van de Berg
Removed some obsolete parameters from the static
application data table, and removed the description for
the AQC (Automatic Quality Control) in the
intermediate product. See the Updated Product
Enhancement section.
4.0 02/02/11 J. D. Jackson Addition of current repeat cycle method as alternative
option for final product derivation. Final product
segment size is now 3 × 3 not 32 × 32 pixels.
5.0 17/06/11 J. D. Jackson Replacement algorithm.
21.2 Inputs
The Total Ozone generation is technically part of the Global Instability Indexing processing. For more
technical information on the processing of input data, see Chapter 22.
21.3 Algorithm Functional Specification
21.3.1 Overview
The scientific principle of the Total Ozone algorithm is described in “ATBD for the MSG GII/TOZ
Product” (see Section 21.7 for full reference). TOZ is generated as a by-product of GII using the same
algorithm, but the TOZ output is then produced as a separate product.
21.3.2 Algorithm Description of the Final TOZ Product
In the following the determination of the final TOZ product is described.
The final TOZ product shall be derived on a TOZ processing segment (nominally 3 × 3 pixels).
For each repeat cycle and each processing segment the total ozone shall be calculated.
21.3.3 Automatic Quality Control (AQC)
For each segment and each repeat cycle the following parameters shall be calculated:

<!-- source_page: 255 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




21.3.3.1 AQC for the Final Total Ozone Product
AQC Flag Quality Description
0-7 Reserved.
8 Insufficient pixels (not processed).
9 First guess good (ozone retrieval using optimal estimation is not necessary;
ozone forecast data is used to determine the total ozone).
10 High cloud (not processed).
11 Successful retrieval (ozone retrieved using the optimal estimation method).
12 Bad retrieval (unable to retrieve the ozone using the optimal estimation
method).
21.3.3.2 Processing Segment Type
Segment Type Description
0 Cloudy
1 Clear
2 Unknown
3 Insufficient pixels to classify
4 Outside processing area
21.3.3.3 Pixel Count within the Processing Segment
Pixel Count Description
0-9 The number of pixels within the segment that are used to classify the segment as
either clear, cloudy or unknown (i.e. if the segment is classified as clear, then cloudy
and unknown pixels are rejected in the processing). If the number of pixels classified
as either clear or cloudy is greater than a configurable threshold, the segment is
processed; unknown segments shall
not be processed.
21.4 Outputs
21.4.1 Output of the Final TOZ Product
The following data shall be produced for the final TOZ product for every processing segment:

FINAL TOZ PRODUCT
Parameter Mnemonic Units Min Max Prec Acc To
Total Ozone TOZfin Dobson 0 600 1 10
PixelCount Number of Pixels used 1 0 9 1 1
SegType Segment Type - 0 4 1 1
AQC Flag Quality indicator - 8 12 1 1
Seg Row No Segment Row - 1 3712 1 1
Seg Col No Segment Column - 1 3712 1 1
Latitude Lat degrees –90 90 0.001 0.001
Longitude Lon degrees –180 180 0.001 0.001
Table 71: Final TOZ Product required output

<!-- source_page: 256 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




21.5 Prototyping and Testing
A complete set of input data and output data will be available at Météo-France to be used as test data
and test results.
21.6 Future Enhancements
The following Future Enhancements shall be foreseen in the design of the algorithm:
 The resolution of the forecast data shall be improved, thereby improving the first guess of the
ozone data within the segment.
The enhancements will not change the TOZ product generation. They will be studied as tasks
designed in the framework of the Ozone SAF.
21.7 References

Reference Title Date Author(s)
Study on the exploitation of the
ozone channel on MSG for the
extraction of wind information,
report for contract
EUM/CO/96/439/MPe, p. 5-17
Review of literature on total
ozone algorithms using the nadir
emission in the 9.7 micron ozone
channel
1998 Karcher, F. and
Blaison, D.
Study on the exploitation of the
ozone channel on MSG for the
extraction of wind information,
report for contract
EUM/CO/96/439/MPe, p. 29-42
The effect of clouds on the TOVS
total ozone determination
1998 Karcher, F.
Study on the exploitation of the
ozone channel on MSG for the
extraction of wind information,
report for contract
EUM/CO/96/439/MPe, p. 43-104
Total ozone algorithms for
geostationary orbiting satellites
1998 Karcher, F,
Meyer, J.-P. and
Armand, P.
EUM/OPS/TEN/05/0266 Algorithm theoretical baseline for
the total ozone retrievals from
SEVIRI observations using
optimal estimation method
2005 Tjemkes, S. A.
EUM/MET/DOC/11/0247 ATBD for the MSG GII/TOZ
Product
2011 König, Marianne

<!-- source_page: 257 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




22 GLOBAL AND REGIONAL INSTABILITY INDICES PRODUCTS
GENERATION
22.1 Algorithm Configuration Information
The Global and Regional Instability Indices products (GII and RII respectively) are derived using the
same algorithm. In addition, the total ozone is retrieved as part of the GII Optimal Estimation (OE)
framework and is used to generate the TOZ (total ozone) product. The GII and RII products are
described together in this chapter, whilst the TOZ product is detailed in Chapter 21. The difference in
product derivation is determined by the resolution, which is a configurable parameter (segment size)
in the algorithm. RII, being regional, is computed over a configurable regional area at a higher
resolution than both GII and TOZ, which are always computed over the full disc. The TOZ product is
a by-product of the GII algorithm, and is therefore always generated at the same resolution as the GII
product.
22.1.1 Algorithm Name
Global Instability Index (GII)
Regional Instability Index (RII)
22.1.2 Algorithm Identifier
EUM_MSG_GII_A001
22.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 27/11/00 S.J. Turner GII Baseline
1.1 08/03/01 S.J. Turner Update to GII intermediate and final product averaging
methods
1.2 16/09/01 M. Koenig Complete change of output
1.3 06/12/01 S.J. Turner Minor modifications to GII section during its inclusion to ASD 2.5
1.4 14/01/02 S.J. Turner Minor corrections
1.5 01/07/05 A. Yildirim Major change in the algorithm implementation.
1.6 29/10/09 J. Jackson Addition of three LPW (Layer Precipitable Water) content
parameters to the GII intermediate and BUFR product.
Improvement to the segment scene type classification added to
improve the emissivity calculation.
1.7 17/06/11 J. Jackson The TOZ product is generated as part of the GII OE framework.
The SEVIRI ozone channel and ozone forecast data are added into
the OE framework of GII. The pixel emissivity maps are used and
replace the previous LUT method. RTTOV upgrade to handle
arbitrary number of profile levels is removed from the Future
Enhancements list. The version of RTTOV used can already handle
an arbitrary number of profiles. Addition of the “ATBD for the
MSG GII/TOZ Product” to the reference list.

<!-- source_page: 258 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




22.2 Inputs
22.2.1 Dynamic Application Data
The GII/RII algorithm uses the Scenes Actual EBBT that is derived from the level 1.5 data from every
repeat cycle from the MSG channels. As defined in the following table, the image data shall be
available in the form of equivalent black body brightness temperatures (EBBT). The scenes type
information from the Scenes Analysis of the current repeat cycle shall
also be available. It is expected
that the latitude and longitude will be derived from the pixel line and column using the geostationary
projection transformation. M and D shall be derived from the nominal repeat cycle start time in the
Level 1.5 header.

<!-- source_page: 259 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 260 of 298



Dynamic Application Data for Physical Retrieval Scheme
Parameter Mnemonic Units Min Max Prec Acc Res Source
EBBT of channels WV6.2, WV7.3, IR8.7, IR9.7,
IR10.8, IR12.0, IR13.4 from cloud-free areas (GII, RII,
and TOZ), and cloudy areas (TOZ only)
EBBTchannel K 170 350 0.1 0.1 pixel Actual EBBT data in Scenes
Analysis
Scenes type scenes_type - 0 255 1 1 pixel Scenes Analysis
Month of year M months 1 12 1 1 pixel Level 1.5 header
Day of month D days 1 31 1 1 pixel Level 1.5 header
UTC Time of day (time of line scan) H hours 0 23 1 1 pixel Level 1.5 header
M minutes 0 59 1 1 pixel Level 1.5 header
Latitude Lat degree -90 90 0.001 0.001 pixel Level 1.5 data
Longitude Long degree -180 180 0.001 0.001 pixel Level 1.5 data
Satellite zenith angle
(assuming sub-satellite position 0°N and 0°E)
sat_zenith degree 0 90 0.01 0.01 pixel Level 1.5 data
Table 72: GII and RII Product dynamic application data for physical retrieval scheme

<!-- source_page: 260 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




22.2.2 Static Application Data
The static application data in the following table shall be specified separately for each instability index
to be calculated.

Static Application Data for Physical Retrieval Scheme
Parameter Mnemonic Units Value Source
Error covariance matrix for ECMWF
forecasts for temperature, humidity and ozone
Static data
Instrument noise in the seven channels used Static data
Bias Correction for Ch5 (See Note) chan5_bias K 0.05 Set-up
Bias Correction for Ch6 chan6_bias K -0.07 Set-up
Bias Correction for Ch7 chan7_bias K 0.00 Set-up
Bias Correction for Ch8 chan8_bias K 0.00 Set-up
Bias Correction for Ch9 chan9_bias K -0.05 Set-up
Bias Correction for Ch10 chan10_bias K -0.07 Set-up
Bias Correction for Ch11 chan11_bias K 1.60 Set-up
Threshold for the cloudiness cloudthresh % 50 Set-up
Maximum iteration Max_iter 6 Set-up
Root Mean Square to define convergence Rms_thres K 2 Set-up
RTTOV coefficients for MSG Static data
Atmospheric pressure level to derive layer
precipitable water content
lpw_first_pres hPa 500 Set-up
Atmospheric pressure level to derive layer
precipitable water content
lpw_second_pres hPa 850 Set-up
Pixel Emissivity Maps Static data
Table 73: GII and RII Product Static Application Data for Physical Retrieval Scheme
Note: The channel bias correction values shown in this table are for MSG-2 (= Meteosat-9).
The values are satellite-dependent and may also vary with time.
All static application data and set-up data shall be configurable.
The imaging radiometer instrument on board the MSG satellite is known as SEVIRI (Spinning
Enhanced Visible and Infrared Imager). This instrument provides full disc Earth scans from MSG’s
nominal position over the Greenwich meridian in 11 channels of the visible, near-infrared and infrared
spectrum. The 12th channel is a high-resolution visible channel with a sampling distance which is
three times higher than that of the other 11 channels, and its images only cover a certain section of the
Earth’s disc. SEVIRI scans the full Earth disc at 15-minute intervals (or five minutes for RSS), and the
sampling rate of individual picture elements is 3 km at the sub-satellite point. The more frequent and
comprehensive data collected by MSG will also aid weather forecasters in the fast recognition and
successful prediction of dangerous weather phenomena such as thunderstorms, which is an important
contribution to the nowcasting community. As a support in this area, Air Mass Analysis has been
defined as an MSG mission, with the objective to monitor the thermodynamic characteristics of the
troposphere using the SEVIRI channels that are responsive in the atmospheric window, water vapour

<!-- source_page: 261 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




and carbon dioxide absorption bands. The GII is produced at a horizontal resolution of approximately
9 km and the RII at 3 km (at the sub-satellite point). The GII and RII products are distributed via
EUMETCast.
The spectral characteristics of the SEVIRI channels are as follows:
Channel Band Frequency at
Centre m)
Spectral Coverage
(98-99% of Energy) m)
Noise Specification
HRV High resolution visible (0.75) Broadband (peak 0.6 – 0.9) 1.07 W/m 2 sr m
VIS0.6
VIS0.8
Visible 0.635
0.81
0.56 – 0.71
0.74 – 0.88
0.53 W/m 2 sr m
0.49 W/m 2 sr m
IR1.6 Near-Infrared 1.64 1.59 – 1.78 0.25 W/m 2 sr m
IR3.9
IR8.7
IR10.8
IR12.0
Atmospheric Window 3.92
8.70
10.80
12.00
3.48 – 4.36
8.30 – 9.10
9.80 – 11.80
11.00 – 13.00
0.35 K at 300 K
0.28 K at 300 K
0.25 K at 300 K
0.37 K at 300 K
WV6.2
WV7.3
Water Vapour 6.25
7.35
5.35 – 7.15
6.85 – 7.85
0.75 K at 300 K
0.75 K at 300 K
IR9.7 Ozone 9.66 9.38 – 9.94 1.50 K at 250 K
IR13.4 CO2 13.4 12.40 – 14.40 1.80 K at 270 K
Table 74: Spectral characteristics of the SEVIRI channels
22.3 Algorithm Functional Specification
22.3.1 Overview
The Global Instability Index (GII) and Regional Instability Index (RII) products use MSG-SEVIRI
observed brightness temperatures plus some additional data to generate indices of atmospheric
instability for nowcasting of severe weather.
Two different methods exist for the generation of instability indices:
1. Statistical Retrieval method
2. Physical Retrieval method
Only the Physical Retrieval method will be described here.
The processing of the GII/RII Physical Retrieval scheme involves repeating an identical calculation
for each instability index to be calculated. The number of instability indices (n) to be calculated shall
be variable and shall be configurable via the Static Application Data. The following eight indices shall
be initially defined and set up as part of the baseline GII/RII product:
 K Index (KI)
 KO Index (KO)
 Lifted Index (LI)
 Maximum Buoyancy (MB)
 Precipitable Water Content Index (TPW)
 Layer Precipitable Water (LPW) content between the TOA and 500 hPa
 Layer Precipitable Water content between 500 hPa and 850 hPa
 Layer Precipitable Water content between 850 hPa and the surface

<!-- source_page: 262 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




For simplicity, the four instability indices (KI, KO, LI and MB), TPW and LPW will all be referred to
as ‘instability indices’.
The instability indices are defined as follows:
 Lifted Index LI = T obs - T lifted from surface at 500 hPa
 K Index KI = (T obs(850) - T obs(500) ) + TD obs(850) - (T obs(700) - TD obs(700) )
 KO Index KO = 0.5 * ( e obs(500) + e
obs(700) - e obs(850) - e
obs(1000) )
 Maximum Buoyancy MB = e obs(maximum between surface and 850) - e obs(minimum between 700 and 300)
where:
T obs is the observed temperature
TD obs is the observed dew point temperature
e obs is the observed equivalent potential temperature
 all at the indicated pressure level (in hPa)
22.3.2 Physical Retrieval Average Pixel-Based GII/RII Algorithm Description
The pixel-based GII/RII algorithm initially works independently on each pixel of the image. The
following steps shall be performed on every pixel of the image.
22.3.2.1 Scenes Type Checks
22.3.2.1.1 Clear Sky Check
Instability cannot be derived for cloudy cases because the state of the lower troposphere, which is
essential to all indices of instability, is shielded for the SEVIRI channels. Therefore, only cloud-free
pixels shall be used.
The GII/RII algorithm shall use scenes type information provided by the Scenes Analysis to check
whether it states that the pixel is clear or cloudy. All brightness temperatures for cloud-free pixels in a
segment shall be averaged. If the scene has been identified as clear, the algorithm steps in the
following sections shall be performed. Otherwise:
 If the segment is covered more than 50 % with clouds, GII/RII shall be set to a default value of
–999.
 If the scenes type is ‘no scenes identified/missing input data’ the GII/RII shall be set to a default
value of –999.
If the segment is identified as not clear the following steps shall be skipped and the processing shall
start with the next segment.
22.3.2.1.2 Land/Sea Check
The scenes type of every pixel as derived from the Scenes Analysis algorithm shall be checked.
If the scenes_type is water (ocean) the land_sea flag shall be set to 2 indicating sea. If the scenes_type
is not water (ocean) the land_sea flag shall be set to 1 indicating land.
22.3.2.1.3 Emissivity Calculations
The emissivity is read for each processed pixel w ithin the segment, from the monthly pixel emissivity
maps. The average emissivity is used for segment processing.

<!-- source_page: 263 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




22.3.2.2 Time Calculations
For every clear sky pixel, time information shall be converted into continuous and periodic phase
angles within the year and the day.
The time of year shall be calculated as a continuous phase angle year from the month (M) and day
(D). The local time of day shall be calculated as a continuous phase angle day from the longitude
(Long) and UTC (in hours (H) and minutes (m) of the exact time the respective image line was
scanned).
The following formulae shall be applied:

 DMyear 985.010.30180  

Equation 52






  mLongHday 25.0360
2415180


Equation 53

22.3.2.3 EBBT Bias Adjustment
For each channel, the EBBT bias (nominally 0) shall be added to the EBBTs for each clear sky pixel
to create bias-adjusted EBBTs as follows:

channelchannelchannel biasEBBTadjEBBT _
Equation 54

22.3.3 Physical Retrieval Method
The physical retrieval shall reconstruct a temperature, humidity and ozone profile from the satelliteobserved radiances or brightness temperatures of a given set of channels and a first-guess profile.
Within the retrieval, the profile is modified until its simulated outgoing radiance field at the top of the
atmosphere matches the satellite observations, or in practice, until its difference from the observations
is minimal. The retrieval thus needs some kind of forward model to simulate the brightness
temperatures.
The core of the retrieval is the profile adjustment step (Ma et al. 1999, or Rodgers 1976):
 )x(xTT)(xx 0nnnB,B
1
ε
T
n
1
n
-1
ε
T
n
1
x01n  
 KSKKSKS

Equation 55

<!-- source_page: 264 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




where:
x = state vector (atmospheric profile, together with a lower boundary condition)
n = iteration step; n=0 denotes background profile
TB = observed brightness temperature
TB,n = simulated brightness temperature for profile of iteration step n
Sx = error covariance matrix of background
Kn = Jacobian matrix at iteration step n
S = error covariance matrix of observed brightness temperatures and of radiation
model
22.3.4 Automatic Quality Control (AQC)
For each GII/RII processing segment, a unique quality indicator shall be defined which is applicable
to all instability indices:
AQC = 100 - (Percentage of Cloudy Pixels contained within this Segment)
The range of the AQC is 50 % to 100 %, as any segment which has more than 50% of cloudy pixels is
not processed. A segment with AQC of 100 % is of very good quality as there is no cloud
contamination, whereas an AQC of 50 % is of poor quality as the cloud contamination is at the
maximum allowed.
22.3.5 Radiation Model
The RTTOV model is used to compute brightness temperatures at the satellite level for a given
atmospheric profile. This model is also used to compute the weighting function matrix (Kn) which is
usually referred to as Jacobians. The radiation model is called rttov_direct and outputs the modelled
brightness temperatures ebbt and also the associated radiances. These two outputs are one-dimensional
arrays, containing the modelled temperatures/radiances for the seven MSG channels.
22.4 Outputs
The following data shall be produced for the GII/RII product for every pixel, except for the following
parameters which are valid for the whole image:
 Segment width (the processing segment width)
 Segment height (the processing segment height)
Note: As already mentioned, the TOZ product is generated as a by-product of GII. TOZ output is
provided as a separate product as described under Section 21.4.

<!-- source_page: 265 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Parameter Mnemonic Units Min Max Prec Acc To
KI index Ki_index °C - - - - Final GII/RII product
KO index Ko_index fin K - - - -
Lifted index Li_index fin K - - - -
Maximum Buoyancy index Mb_index K - - - -
Total Precipitable Water TotalPrepWater mm - - - -
Layer Precipitable Water
(TOA→500 hPa)
lpw1 mm - - - -
Layer Precipitable Water
(500 hPa→850 hPa)
lpw2 mm - - - -
Layer Precipitable Water
(850 hPa→BOA)
lpw3 mm - - - -
Segment quality SegQuality - - - - -
Pixel Row in product Row - 0 3712 1 1
Pixel Column in product Column - 0 3712 1 1
Latitude Latitude degrees –90 90 0.1 0.1
Longitude Longitude degrees –180 180 0.1 0.1
Satellite Zenith Angle SatZenith degrees 0 180 0.1 0.1
Table 75: GII/RII product outputs
22.5 Future Enhancements
This future enhancement shall be considered in the design of GII/RII: The generation of new
instability indices (in addition to the baseline set).
22.6 References
Reference Title Date Author(s)
EUM/MET/DOC/04/0155 GII- Physical Retrieval
Algorithm Description
June 2004 König, Marianne
EUMETSAT Technical
Memorandum No.9
Atmospheric Instability
Parameters Derived from
MSG SEVIRI Observations
January 2002 König, Marianne
EUM/CO/98/646/JKK Development of Operational
Algorithms for the Retrieval
of Instability Indices from
MSG
July 2000 Fuhrhop R., Erdmann A.,
Czekala H., Simmer C.
J. Appl. Meteor., 38,
501-513.
A nonlinear physical retrieval
algorithm – its application to the
GOES-8/9 sounder.
1999 MA, X.L., SCHMIT, T.J..
SMITH, W.L.
Rev. Geophys. Spac. Phys.,
14, 609-624.
Retrieval of atmospheric
temperature and composition
from remote measurements of
thermal radiation.
1976 Rodgers, C.D.
EUM/MET/DOC/11/0247 ATBD for the MSG GII/TOZ
Product
2011 König, Marianne

<!-- source_page: 266 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




23 CLEAR SKY REFLECTANCE MAP
23.1 Algorithm Configuration Information
23.1.1 Algorithm Name
Clear Sky Reflectance Map (CRM)
23.1.2 Algorithm Identifier
EUM_MSG_CRM_A001
23.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 25/7/05 T. Heinemann CRM Baseline
1.1 02/12/08 R. Swifte CRM now derived every 2 hours between 06 and 20
UTC, not just at noon.
23.2 Inputs
The Clear Sky Reflectance Map algorithm shall use the following data:

LEVEL 1.5 IMAGE DATA AND DATA DERIVED FROM THE IMAGE DATA
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Scenes type scenes_type - 0 255 1 1 pixel SCE
Reflectances for
channels VIS0.6,
VIS0.8, NIR1.6,
IR3.9_sol, HRVIS
REFL
channel % 0 150 0.1 0.1 pixel Derived from level
1.5 image data
Solar zenith angle sol_zenith degrees 0 90 10-6 10-6 pixel Derived from level
1.5 image data
Satellite observing
angle
sat_zenith
degrees 0 90 10 -6 10 -6 pixel Derived from level
1.5 image data
Relative azimuth
angle sun/satellite
sol_sat_azimuth degrees 0 360 0.1 0.1 pixel Derived from level
1.5 image data
23.3 Algorithm Functional Specification
23.3.1 Overview
The Clear Sky Reflectance Map describes the reflection that would be seen from the satellite in the
visible and near infrared MSG channels over a cloud-free Earth. No atmospheric correction and no
surface reflection correction according to the viewing angle is applied. Therefore, the CRM
corresponds to the so-called remote sensing reflectance. It is derived every two hours between 06:00
and 20:00 UTC for the complete visible disc except for the polar regions, and except for sun zenith
angles higher than 70 degrees.

<!-- source_page: 267 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




23.3.2 Algorithm Description
23.3.2.1 Clear Sky Reflectance Map Product
The CRM product contains the remote sensing reflectance for cloud-free pixels of the MSG channels
VIS0.6, VIS0.8, NIR1.6 and NIR3.9. In addition, the sun zenith angle and the azimuthal difference
between sun and viewing direction, as well as the number of accumulations, are given for each pixel.
If the number of accumulations is 0 the reflection values are taken from a previous CRM. The product
is encoded in the GRIB-2 data format.
23.3.2.2 Update of the Clear Sky Reflectance Map
For each pixel the reflectance value for each of channels VIS0.6, VIS0.8, NIR1.6 and IR3.9_sol for
clear scenes shall be collected for a period of seven days for each specific daily derivation time and
averaged, i.e. clear sky reflectance of channel VIS0.6, VIS0.8, NIR1.6 and IR3.9_sol for that pixel.
For each pixel the mean solar zenith angle and the mean relative azimuth angle (sun/satellite) for each
specific daily derivation time at the SSP for that seven-day period shall be determined. If a pixel has
no clear scene in that seven-day period the value of the previous seven-day period shall be used. If
that value is not available, the value shall be set to a default invalid value.
23.3.3 Automatic Quality Control (AQC)
Not required. This is already performed as part of Scenes Analysis.
23.4 Outputs
The following data shall be produced for the CRM product for every pixel in the form of a GRIB
Edition 2-encoded product.
Parameter Mnemonic Units Min Max Prec Acc To
Reflectances for channels
VIS0.6, VIS0.8, NIR1.6,
IR3.9_sol
REFLchannel % 0 150 0.1 0.1 SCE next
Solar zenith angle sol_zenith degrees 0 90 0.1 0.1 SCE next
Relative azimuth angle
sun/satellite
sol_sat_azimuth degrees 0 360 0.1 0.1 SCE next
Number of accumulations no_accum - 0 14 1 1 SCE next
Table 76: Clear Sky Reflectance Map required outputs
23.5 Prototyping and Testing
Since the Clear Sky Reflectance Map is produced as part of Scenes Analysis, details of prototyping
and testing are included in the appropriate Scenes Analysis Section 5.5.
23.6 Future Enhancements
The following future enhancements shall be foreseen in the algorithm design above:
 Increase temporal frequency of product generation.
23.7 References
None

<!-- source_page: 268 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




24 DIVERGENCE PRODUCT GENERATION
24.1 Algorithm Configuration Information
24.1.1 Algorithm Name
Divergence (DIV)
24.1.2 Algorithm Identifier
EUM_MSG_DIV_A001
24.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 21/03/07 A. de Smet DIV Baseline
1.1 27/10/09 A. de Smet Updated according to AR 19273.
24.2 Inputs
24.2.1 Data From Other MPEF Algorithms (Dynamic Application Data)
The divergence algorithm shall use the following data from the AMV Final product.

DATA FROM OTHER MPEF ALGORITHMS
Parameter Mnemonic Units Min Max Prec Acc Source
AMV latitude latitude degrees -60 60 0.01 0.01 AMV Final Product
AMV longitude longitude degrees -60 60 0.01 0.01 AMV Final Product
AMV speed speed m/s 0 100 0.01 0.01 AMV Final Product
AMV direction direction degrees 0 360 0.01 0.01 AMV Final Product
AMV pressure height hPa 100 400 0.01 0.01 AMV Final Product
AMV QI, excluding
F/C consistency
qi_excl % 0 100 1 1 AMV Final Product
Table 77: Divergence Product: dynamic application data from other MPEF algorithms
24.2.2 Static Application Data
The static application data shall define the following:
 The rectangular processing grid
 The atmospheric layer from which the AMV data should be used
 Static parameters for the mathematical expressions used in the algorithm

<!-- source_page: 269 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




STATIC APPLICATION DATA
Parameter Mnemonic Units Min Max Prec Acc Source
min latitude DIV_min_latitude degrees –60 60 0.1 0.1 Static data
max latitude DIV_max_latitude degrees –60 60 0.1 0.1 Static data
min longitude DIV_min_longitude degrees –60 60 0.1 0.1 Static data
max longitude DIV_max_longitude degrees –60 60 0.1 0.1 Static data
delta latitude DIV_delta_lat degrees 0.1 5.0 0.1 0.1 Static data
delta longitude DIV_delta_lon degrees 0.1 5.0 0.1 0.1 Static data
min pressure DIV_min_pressure hPa 100 400 0.1 0.1 Static data
max pressure DIV_max_pressure hPa 100 700 0.1 0.1 Static data
critical distance DIV_crit_distance km 0 1000 0.1 0.1 Static data
critical QI DIV_crit_QI % 0 100 1 1 Static data
minimum QI DIV_min_QI % 0 100 1 1 Static data
mode DIV_mode - 0 1 1 1 Static data
Table 78: Divergence Product: Static Application Data
The static data shall be defined in the AMV product static data files and shall be configurable.
24.3 Algorithm Functional Specification
24.3.1 Overview
The Divergence product represents the two-dimensional horizontal divergence of the atmospheric
velocity field. In Cartesian coordinates it is simply written as follows:
yxDivergence 

 VU

Equation 56


In a latitude-longitude coordinate frame, which is the basis for the algorithm, this becomes:
 





  cos.VU
cos.
1
eRDivergence

Equation 57

where:
Re = Earth’s radius
φ = latitude
λ = longitude

<!-- source_page: 270 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The algorithm generates divergence values on a latitude-longitude processing grid. It uses as input
data the Atmospheric Motion Vectors (AMVs) from the final AMV product for a prescribed
atmospheric layer. It will therefore have a frequency of one product per hour.
The product shall
be generated for the water vapour 6.2 micron channel only (channel 5). It shall in
principle be possible however to derive divergence products from any spectral channel for which
AMV data are available.
24.3.2 Algorithm Description
The algorithm breaks down into the following steps:

Step 1 Read the AMVs from the WV6.2 final AMV product. Ignore AMVs that have an
overall quality less than DIV_min_QI. Moreover, consider only those AMVs having a
final pressure in the range [DIV_min_pressure , DIV_max_pressure].

Step 2 For each remaining AMV, convert its wind speed and direction to U and V wind
components.

Step 3 Define a rectangular processing grid in a latitude-longitude coordinate frame.

Step 4 Apply a Barnes interpolation to the U and V wind components, as well as to the AMV
quality (the one excluding the forecast consistency) and the AMV wind speed. This
will map the U, V, quality and wind speed values onto the grid points. In data-sparse
areas the grid point values will remain undefined; the U, V, quality and wind speed
values shall
be set to a pre-defined ‘missing data’ value (currently 999.9) for these
cases. Refer to Borde (Section 24.7 References) for an introduction to the Barnes
interpolation scheme.

Step 5 Calculate the divergence at each grid point, applying the discrete version of
Equation 2. If one or more of the U and V components that are used in the calculation
have an undefined value, the divergence value itself shall
become undefined as well.
The value shall then be set to 999.9.

24.3.3 Automatic Quality Control (AQC)
There shall be a quality indicator for each grid point. The value of this indicator shall result from the
Barnes interpolation of the AMV quality values, as described in Section 24.3.2.

<!-- source_page: 271 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




24.4 Outputs
The data in data shall be produced for the divergence product in the form of a
GRIB Edition 2- encoded product.
Parameter Mnemonic Units Min Max Prec Acc To
min latitude DIV_min_latitude degrees –60 60 0.1 0.1 DIV
maximum latitude DIV_max_latitude degrees –60 60 0.1 0.1 DIV
minimum longitude DIV_min_longitude degrees -60 60 0.1 0.1 DIV
maximum longitude DIV_max_longitude degrees –60 60 0.1 0.1 DIV
delta latitude DIV_delta_lat degrees 0.1 5.0 0.1 0.1 DIV
delta longitude DIV_delta_lon degrees 0.1 5.0 0.1 0.1 DIV
minimum pressure DIV_min_pressure hPa 100 400 0.1 0.1 DIV
maximum pressure DIV_max_pressure hPa 100 700 0.1 0.1 DIV
critical distance DIV_crit_distance km 0 1000 0.1 0.1 DIV
critical QI DIV_crit_QI % 0 100 1 1 DIV
minimum QI DIV_min_QI % 0 100 1 1 DIV
mode DIV_mode - 0 1 1 1 DIV
minimum divergence min_divergence 10 -6 s-1 –250 250 2 1 DIV
divergence divergence 10-6 s-1 –250 250 2 1 DIV
quality quality % 0 100 1 1 DIV
wind speed windspeed m/s 0 102 0.4 0.4 DIV
Table 79: Divergence Product: Outputs
24.5 Prototyping and testing
The derivation of the Divergence product has been extensively tested with the Meteorological
Division (MET) prototype, as well as on the MPEF validation systems.
24.6 Future Enhancements
No enhancements are currently foreseen.
24.7 References
Reference Title Date Author(s)
J. Appl. Meteor., 3, 396-409 A technique for maximizing
details in numerical weather map
analysis
1964 Barnes, S.L.
EUM/MET/REP/05/0163 Upper Level Divergence Product
Algorithm Description
2005 Borde, Régis.
EUM/OPS/REP/07/0100 Product Validation Re port No. 12 2007 de Smet, Arthur.

<!-- source_page: 272 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




25 ACTIVE FIRE MONITORING PRODUCT GENERATION
25.1 Algorithm Configuration Information
25.1.1 Algorithm Name
Active Fire Monitoring Product (FIR)
25.1.2 Algorithm Identifier
EUM_MSG_FIR_A001
25.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 30/03/07 A. Yildirim FIR Baseline
2.0 1/11/08 O. Samain New FIR algorithm, as specified by EUM/MPEF/DOC/08/0195
25.2 Inputs
25.2.1 Dynamic Application Data
The main input to the Active Fire Monitoring algorithm is the Level 1.5 data from the MSG IR
channels. The image data shall be available in the form of either equivalent black body brightness
temperatures (EBBT) in kelvin (K), or radiances.

LEVEL 1.5 IMAGE DATA AND DATA DERIVED FROM THE IMAGE DATA
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
EBBT of channels
IR3.9, IR8.7, IR10.8
EBBTchannel K 170 350 0.1 0.1 pixel Derived from Level 1.5
image data
Reflectances for
channel VIS0.6
REFLchannel % 0 150 0.1 0.1 pixel Derived from level 1.5
image data
Standard deviation on
a 3 × 3 pixel segment
for channels IR3.9,
IR10.8
std_EBBT K - - - - pixel Derived from Level 1.5
image data

Solar zenith angle sol_zenith degrees 0 90 10 -6 10 -6 pixel Derived from Level 1.5
image data
Satellite zenith angle sat_zenith degrees 0 90 10-6 10-6 pixel Derived from Level 1.5
image data
Relative azimuth
angle sun/satellite
sol_sat_azimuth degrees 0 360 0.1 0.1 pixel Derived from Level 1.5
image data
Scene quality scene_quality - 0 100 1 1 pixel Scenes Analysis
Table 80: Active Fire Monitoring Product: Level 1.5 image data
Note: The scene quality is derived by the SCE algorithm (H.J. Lutz, 2007) and represents the
probability of cloudiness.

<!-- source_page: 273 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




25.2.2 Static Application Data
STATIC APPLICATION DATA - SURFACE DATA
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Surface Type Map surface_type_map - 0 99 1 1 pixel Static data
Nearest Coast Map Nearest_coast - 0 1000 1 1 pixel Static data
Emissivity Tables (for
each month of the year)
Emissivity_tables - 0 1 0.01 0.01 pixel Static data
Table 81: Active Fire Monitoring Product: static application data
The pixel-based land-sea mask /surface type map consists of 17 different land surface types and one
ocean/open water surface type. This map has been derived from the International Geosphere-
Biosphere Programme (IGBP) surface type map (Loveland and Belward, 1997).
The emissivity tables are created with data from the Global Infrared Land Surface Emissivity project,
using MODIS sensor data. The baseline fit method (Seemann et al., 2007), based on a conceptual
model developed from laboratory measurements of surface emissivity, is applied to fill in the spectral
gaps between the six emissivity wavelengths available in the MOD11 product (more information at
http://cimss.ssec.wisc.edu/iremis/). The data are then sampled spatially onto the nominal SEVIRI
rectified image grid and averaged over the individual SEVIRI spectral response functions.
25.3 Algorithm Functional Specification
25.3.1 Overview
The Active Fire Monitoring product has been developed for detecting and quantifying biomass
burning in Africa.
25.3.2 Algorithm Description
The basic principles of the FIR algorithm are similar to those already in use for other instruments like
the GOES-8 3.9 µm IR channel (Weaver and Purdom, 1995), AVHRR (Giglio et al., 1999) and
MODIS (Giglio et al., 2003).
The FIR algorithm is only applied to land surfaces with a scene quality lower than or equal to 70,
which means that off-shore oil burning fires, fires on small islands (e.g. active volcanoes which also
fall under the “hot spot” category) or fires hidden by thick clouds are not monitored by the algorithm.
Bare soil land surfaces (deserts) are also excluded from the processing.
For the remaining valid pixels, the FIR algorithm uses the following four criteria to check for potential
fire and fire pixels:
 Brightness temperature of channel IR3.9
 Standard deviation of channel IR3.9
 Brightness temperature difference of channel IR3.9 and IR10.8
 Standard deviation of channel IR10.8
The brightness temperature of channel IR3.9 picks up hot spots caused by the fire. The other MSG
channels are less sensitive to hot spots. In this test, simple fixed temperature thresholds are used,
which are different for day and night (see Section 25.3.2.2).
The standard deviation of channel IR3.9 over 3 × 3 pixels around a central hot spot is used to identify
the real hot spot versus the natural (heated) background temperature of the surface.

<!-- source_page: 274 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




As channel IR10.8 is much less sensitive to hot spots, the brightness temperature of IR10.8 will not be
as high as the brightness temperature in channel IR3.9. This means that the brightness temperature
difference of channels IR3.9 and IR10.8 is also higher than for non-fire pixels.
The reduced sub-pixel fire sensitivity of IR10.8 is furthermore used to correct for miss-classified fire
pixels. Pixels that have passed the first three of the above tests can also be missed clouds, highly
variable surface types or highly variable terrain elevation. The correction is done by using the standard
deviation of channel IR10.8, which will be relatively low in fire regions because the fire pixels have
similar brightness temperatures to the surrounding non-fire areas.
The standard deviation is calculated on a 3 × 3 pixel array around each MSG pixel. Water and cloud
pixels are excluded from the calculation of the standard deviation. The standard deviation tests are
abandoned if fewer than three pixels can be used for the calculation.
The first requirement is to select all pixels which are ‘potential’ fire pixels. This first component is
often a trade-off between computation speed/overhead and increased false detections on the one hand,
and underestimation of fire activity and biomass burning on the other. If the conditions for selecting
potential fire pixels are conservative, fewer pixels will be returned, which will reduce the prevalence
of false detections whilst benefiting from reduced processing time. On the other hand, if the conditions
are quite liberal then a greater number of pixels will be returned, which has the inverse effect by
increasing computational overhead and the likelihood of false detections.
The approach adopted in this algorithm is to identify ‘potential’ fire pixels using a liberal approach
since an earlier comparison between SEVIRI and MODIS suggests SEVIRI misses approximately
40% of the fires which MODIS detects. Given this, it was deemed more important to increase the
sensitivity of the algorithm so that smaller fires could be detected whilst attempting to reduce false
detections.
25.3.2.1 Description of the Threshold Tests
The algorithm distinguishes between potential fires and fires. Pixels with a lower confidence in their
results are defined as ‘potential fires’, those with a higher confidence are defined as ‘fires’. The main
criteria for defining potential fires and fires are different threshold settings. ‘Potential’ fires means
here that it cannot be stated with absolute certainty that there is a fire within that respective pixel. The
thresholds are day- and night-dependent for both potential fire and fire cases.
25.3.2.2 Derivation of the Thresholds
The first step is to generate the predicted clear sky brightness temperatures per channel, per repeat
cycle and per pixel from the RTM output. Because of the fact that the RTM uses emissivity values of 1
for all grid points, the given top of the atmosphere clear sky radiance has to be corrected with the
given (pixel-based) land surface emissivity. This is performed as follows:
The given top of atmosphere radiance (R
TOA), total transmittance (τs), surface skin radiance (RSFC) and
the downward radiance (RDN) at surface level have to be interpolated in space and time to the given
repeat cycle time and the pixel location. The atmospheric contribution (RATM) to the clear sky radiance
is calculated (for each channel) as follows:
RATM = RTOA - RSFC * τs

<!-- source_page: 275 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




The corrected clear sky radiance (RCOR) uses the emissivity ε at pixel location and is calculated as:
1. For channel IR3.9
RCOR = RATM + ε 3.9 * RSFC * τs
+ ( 1 - ε 3.9 ) * RDN * τs
+ ( 1 - ε 3.9 ) * RSOL * COS(MIN(90, SZEN)) * τs * τs
where RSOL is the top of atmosphere solar irradiance of channel IR3.9, which is
4.883 (mW/(m2 sr (cm)-1 )).
2. For channel IR10.8
RCOR = RATM + ε 10.8 * RSFC * τs
+ ( 1 - ε 10.8 ) * RDN * τs
The derived radiances R COR for channels IR3.9 and IR10.8 are converted to brightness temperatures
(Tpred_39 , Tpred_108). The thresholds are derived as follows:
Threshold1 = Tpred_39 + a1 + a2 ˟ SIN(MIN(szmax, sat_zenith))
Threshold2 = MAX(a3, a3 + (sat_zenith – a4) ˟ a5)
Threshold3 = (Tpred_39 - Tpred_108 ) + a6 + a7 ˟ SIN(MIN(szmax, sat_zenith))
Threshold4 = a8
Threshold5 = Tpred_39 + b1 + b2 ˟ SIN(MIN(szmax, sat_zenith))
Threshold6 = MAX(b3, b3 + (sat_zenith – b4) ˟ b5)
Threshold7 = (T pred_39 - Tpred_108 ) + b6 + b7 ˟ SIN(MIN(szmax, sat_zenith))
The coefficients used above are listed in the following table. It should be noted that the coefficients a6,
a7, b6 and b7 are set to zero and can be regarded as placeholders for later improvements.

Thresholds coefficients
Coeff Day Night
szmax 70 70
a1 5 0
a2 5 5
a3 2 2
a4 60 60
a5 0.25 0.25
a6 0 0
a7 0 0
a8 4 4
b1 10 5
b2 5 5
b3 4 4
b4 60 60
b5 0.25 0.25
b6 0 0
b7 0 0

<!-- source_page: 276 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




Note: “Day” is defined with a local solar zenith angle lower than szmax and “night” with a solar
zenith angle of higher than 90º. For solar zenith angles between szmax and 90º the thresholds are
linearly interpolated.
25.3.2.3 Application of the Threshold Tests
The FIR algorithm will be applied if the following conditions are met:
 Pixel is land
 Pixel is at least 5 km away from the nearest coastline/lake
 During day the reflectance in channel VIS0.6 is smaller than 30%
 The sunglint angle is larger than 3º
 The Scene Quality is lower than or equal to 70
The algorithm contains the following tests:
Test 1: T39 is greater than threshold1
Test 2: StdDev39 – StDev108 is greater than threshold2
Test 3: T39 – T108 is greater than threshold3
Test 4: StdDev108 is less than threshold4
Test 5: T39 is greater than threshold5
Test 6: StdDev39 – StDev108 is greater than threshold6
Test 7: T39 – T108 is greater than threshold7
where:
T39, T108 are the brightness temperatures of channels IR3.9, IR10.8
StdDev39,
StDev108
are the temperature standard deviations calculated on a 3 ˟ 3 pixels box
for the same channels, respectively.

Then the tests are applied as follows:
IF ( Test 5 AND Test 6 AND Test 7) THEN
The result is set to fir_val = probable_fire
ELSE IF (Test1 AND Test2 AND Test3 AND Test4) THEN
The result is set to fir_val = possible_fire
ELSE
The result is set to fir_val = no_fire
END
In order to provide diagnostic information on which test is true, the final value, coded on a one-byte
integer, is calculated as follows:
Fire_output = fir_val + Test1*4 + Test2*23 + Test3*24 + Test5*25 + Test6*26 + Test7*27

25.3.3 Automatic Quality Control (AQC)
There is no automatic quality control mechanism in the algorithm. The algorithm itself is based on a
simple threshold algorithm. After excluding cloudy, desert/bare soil and sea pixels, the remaining land
pixels are checked to see if they meet any of the threshold criteria and then they are assigned either

<!-- source_page: 277 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




fire-free, possible fire or probable fire status. Validation and verification of the fire pixels are done by
some users (the Met services in Portugal and Turkey) by comparison against surface observations .
25.4 Outputs
The EUMETSAT FIR product produces two types of output – one is an image-based product
generated in GRIB Edition 2 format, and the other is in ASCII format. Both output products are
disseminated to the end-users via FTP and EUMETCast. These products can be retrieved from the
following FTP address:
ftp://ftp.eumetsat.int/pub/OPS/out/simon/FIRE/
25.4.1 GRIB-2 Encoded Product
The following data shall be produced for each pixel for the FIR GRIB-2 encoded product according to
WMO FM 92-XIII GRIB Code Table 4.223 - Fire detection indicator:

Code figure Meaning
0 No fire detected
1 Possible fire detected
2 Probable fire detected
3 Missing




25.4.2 ASCII-coded Product
For the ASCII-coded text file, the following table shall be generated only for Possible Fires and
Probable Fires:

Parameter Mnemonic Units Min Max Prec Acc To
Pixel Row Row - 0 3712 1 1
Pixel Column Col - 0 3712 1 1
Latitude Lat ° –90 90 0.001 0.001
Longitude Lon ° –180 180 0.001 0.001
FIR Value ASCII - - - -
Table 82: Active Fire Monitoring Product: ASCII-Coded table requirements

<!-- source_page: 278 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





An example of a FIR ASCII text-coded file is given below:

Data from EUMETSAT, Satellite: MET09, Date: 2007/05/28 19:45Z

Row: 940 Col: 925 Lat: -26.996 Lon: 30.846 *** Probable fire ***
Row: 941 Col: 922 Lat: -26.967 Lon: 30.953 *** Probable fire ***
Row: 1527 Col: 1239 Lat: -9.070 Lon: 17.287 *** Probable fire ***
Row: 1570 Col: 994 Lat: -7.946 Lon: 24.672 *** Probable fire ***
Row: 2331 Col: 3491 Lat: 14.396 Lon: -60.969 Possible fire
Row: 2332 Col: 3492 Lat: 14.431 Lon: -61.078 Possible fire
Row: 2333 Col: 3492 Lat: 14.463 Lon: -61.099 Possible fire
Row: 2336 Col: 3491 Lat: 14.556 Lon: -61.075 Possible fire
Row: 2356 Col: 3489 Lat: 15.190 Lon: -61.340 *** Probable fire ***
Row: 2388 Col: 3479 Lat: 16.187 Lon: -61.201 *** Probable fire ***

25.5 Future Enhancements
The current fire monitoring algorithm is able to detect most of the existing active fires with a
minimum of false alarms. The validation of the algorithm is still ongoing and may lead to some further
improvements of the algorithm.
In particular, some of the remaining problems listed below need to be solved, namely:
 Mixed water (river/lake/coast) and land scenes
 Non-homogeneous land surfaces
 Dusk and dawn periods with rapidly changing IR3.9 values
An example of the limitations of fire monitoring algorithms is given by Morisette et al. (2005).

<!-- source_page: 279 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




25.6 References
Reference Title Date Author(s)
Int. J. of Remote Sensing, Vol.
20, No. 10, pp. 1947-1985
Evaluation of global fire detection
algorithms using simulated
AVHRR infrared data
1999 Giglio L., J.D. Kendall,
C.O. Justice
Remote Sensing of
Environment, Vol. 87, pp. 273-
282
An Enhanced Contextual Fire
Detection Algorithm for Modis
2003 Giglio L., J.
Descloitres, C.O.
Justice, Y.J. Kaufman
Int. Journal of Remote Sensing,
Vol. 18, No. 15, p. 3289
The IGBP-DIS global 1 km land
cover data set, DISCover: first
results
1997 Loveland T.R. and
Belward A.S.
EUMETSAT Technical
Memorandum No. 4
Cloud processing for Meteosat
Second Generation
1999 Lutz H.J.
EUMETSAT,
EUM/MET/REP/07/0132
Cloud Detection for MSG –
Algorithm Theoretical Basis
Document (ATBD)
2007 Lutz H.J.
Int. Journal of Remote Sensing,
Vol. 26, No. 19, pp. 4239-4264
Validation of the MODIS active
fire product over Southern Africa
with ASTER data
2005 Morisette J.T., L.
Giglio, I. Csiszar, C.O.
Justice
Weather and Forecasting, Vol.
10, pp. 803-808
Observing Forest Fires with the
GOES-8, 3.9 µm Imaging Channel
1995 Weaver J.F. and J.F.
Purdom
EUMETSAT,
EUM/MET/DOC/08/0195
Algorithm Implementation
Document for the Active Fire
Detection Algorithm
2008 Lutz H.J.
J. Appl. Meteor. Climatol.,
Vol. 47, 108-123
Development of a Global Infrared
Land Surface Emissivity Database
for Application to Clear Sky
Sounding Retrievals from Multispectral Satellite Radiance
Measurements
2008 Seemann, S.W., E. E.
Borbas, R. O.
Knuteson, G. R.
Stephenson, H.-L.
Huang

<!-- source_page: 280 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




26 MULTI-SENSOR PRECIPITATION ESTIMATE PRODUCT
GENERATION
26.1 Algorithm Configuration Information
26.1.1 Algorithm Name
Multi-Sensor Precipitation Estimate Product (MPE)
26.1.2 Algorithm Identifier
EUM_MSG_MPE_A001
26.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 30/11/07 T. Heinemann, O. Samain MPE Baseline
26.2 Inputs
The main inputs to the MPE algorithm are as follows (deriving from two separate satellite sources):
 Level 1.5 data from the MSG IR10.8 channel.
 Microwave imager data from the SSM/I instruments on board the polar-orbiting satellites of the
US Defense Meteorological Satellite Program (DMSP).
 Outputs from the Scenes Analysis (SCE).
26.2.1 Dynamic Application Data
As defined in the following table, the MSG IR10.8 image data shall be available in the form of
equivalent black body brightness temperatures (EBBT) in kelvin (K).

LEVEL 1.5 IMAGE DATA AND DATA DERIVED FROM THE IMAGE DATA
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
EBBT of channel
IR10.8
EBBTchannel K 170 350 0.1 0.1 pixel Derived from Level
1.5 image data
Scene type scene_type - 0 255 1 1 pixel Scenes Analysis
Table 83: Multi-Sensor Precipitation Product dynamic application data
EXTERNAL DATA
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
SSM/I rain rate R_SSMI mm/h 0 100 0.1 0.1 SSM/I pixel Derived from
SSM/I image data
Table 84: Multi-Sensor Precipitation Product external data

<!-- source_page: 281 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 282 of 298

26.2.2 Static Application Data

STATIC APPLICATION DATA – SETUP PARAMETERS
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Minimum time difference from the collocation reference time for the
retrieval of SSM/I data
Or
Minimum time difference from the rain-rate generation reference time
for the histogram accumulation
Delta_Tlf seconds 0 10000 1 1 - Static data
Maximum time difference from the collocation reference time for the
retrieval of SSM/I data
Or
Maximum time difference from the rain-rate generation reference time
for the histogram accumulation.
Delta_Tlp seconds 0 10000 1 1 - Static data
Collocation box size in latitude Dlat - 0 180 0.1 0.1 - Static data
Collocation box size in longitude Dlon - 0 180 0.1 0.1 - Static data
Processing area size in latitude Max_Lat_Diff - 0 180 0.1 0.1 - Static data
Processing area size in longitude Max_Lon_Diff - 0 180 0.1 0.1 - Static data
Maximum rain rate Max_Rainrate mm/h 0 100 0.1 0.1 - Static data
Minimum rain rate Min_Rainrate mm/h 0 100 0.1 0.1 - Static data
Minimum number of observations inside collocation box to build a LUT Minpoints - 0 100 1 1 - Static data
Rain rate histogram minimum value Rbin1 mm/h 0 100 0.1 0.1 - Static data
Rain rate histogram maximum value Rbin2 mm/h 0 100 0.1 0.1 - Static data
Rain rate histogram increment Rstep mm/h 0 100 0.1 0.1 - Static data
Brightness temperature histogram minimum value Tbin1 K 0 1000 0.1 0.1 - Static data
Brightness temperature histogram maximum value Tbin2 K 0 1000 0.1 0.1 - Static data

<!-- source_page: 282 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm Specification Document



Page 283 of 298

STATIC APPLICATION DATA – SETUP PARAMETERS
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Brightness temperature histogram increment Tstep K 0 100 0.1 0.1
Time offset between reference and the processing time Time_Delay seconds 0 10000 1 1 - Static data
Maximum brightness temperature for accepting MSG observations Tmax K 0 1000 0.1 0.1 - Static data
Threshold value for the percentage of null rain rate elements in a LUT,
before assigning a complete zero-rain LUT
Zerohist - 0 100 0.1 0.1 - Static data
Threshold below witch SSM/I rain rates are forced to zero Zerorain mm/h 0 100 0.1 0.1 - Static data
Table 85: Multi-Sensor Precipitation Product: Static application dat

<!-- source_page: 283 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




26.3 Algorithm Functional Specification
26.3.1 Overview
The MPE algorithm processes MSG data from channel IR10.8 in near real-time (or some time later in
the event of delayed processing) and derives instantaneous rain rates at full MSG pixel resolution. As
additional input, external satellite data from the SSM/I instrument on board the DMSP satellite series
shall be required from up to 24 hours before the acquisition time of the MSG image. The scientific
background of the algorithm is described in detail in the reference documents in Section 25.6
(Heinemann et al, 2002 & 2003).
26.3.2 Algorithm Description
26.3.2.1 Structure of Processing
The algorithm consists of two independent steps: the collocation of SSM/I and MSG data, and the
product generation on the basis of the collocated data sets. In the framework of MPEF these two steps
are realised by two activities of the MPE software unit, namely the ‘CoLoc’ activitiy and the
‘ProdGen’ activity. The CoLoc activity includes the acquisition and the decoding of the SSM/I data
files as well as the calculation of rain rates from the SSM/I data at the original SSM/I resolution.
26.3.2.2 Data Retrieval
SSM/I data for the period between
Delta_Tlp-x minutes and Delta_Tlf minutes before the
reference time of the CoLoc activity are retrieved via a link to an external data directory. It shall be
insured that no duplicated data are used in the processing.
The decoded and calibrated data shall be converted to rain rates using the formulae described in the
reference documents in Section 0 (Ferraro 1997, Turk et al 1999). Rain rates shall not be derived for
SSM/I pixels which are flagged as coast or degraded.
26.3.2.3 Collocation Data Retrieval
A temporal and spatial collocation shall be done in a time span from Delta_Tlp minutes to
Delta_Tlf minutes before the reference time of the CoLoc activity. In the case of delayed
processing Delta_Tlp can also be negative. In this time span the rain rates of SSM/I pixels which
are in the MPE processing area are stored together with averaged brightness temperatures (EBBT) of
MSG pixels, representing the same geographical area as the SSM/I pixel. The time difference between
the measurement of the SSM/I data and the MSG pixel shall be smaller than 10 minutes. The real
pixel sensing time and not the image time stamp of the MSG image is relevant in this context. Each
collocated data point (CDP) consists of the geographical location of the centre of the SSM/I pixel
(latitude and longitude), the rain rate derived from SSM/I data and the collocated average MSG
EBBT. The CDPs are stored in intermediate data files. The processing area is defined relative to the
rectification point by the parameters Max_Lat_Diff and Max_Lon_Diff.

<!-- source_page: 284 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




26.3.2.4 Product Generation
Definition of processing boxes: For the product generation the MSG image is divided into processing
boxes (PBs) which are equally spaced in latitude and longitude. The size of the boxes in latitude and
longitude shall be determined by the parameters Dlat and Dlon, respectively. The processing area
(see above) is filled with PBs without gaps.
Calculation of look-up tables: The CDPs from the intermediate files shall be read for the time span
from Delta_Tlp minutes to Delta_Tlf minutes before the reference time of the ProdGen
activity. For each PB the corresponding CDPs are identified. A histogram-matching technique is used
to derive look-up tables, describing the relation between MSG EBBT and SSM/I rain rate for each
single PB. The matching shall be done for the EBBT range from Tbin1 to Tbin2 with a step of
Tstep, and for the rain-rate range from Rbin1 to Rbin2 with a step of Rstep. From high to low
rain rates the cumulated histogram for rain rates is calculated at the defined rain-rate steps. In addition,
the cumulated histogram is calculated for the EBBTs from low to high temperatures at the respective
temperature steps. For each histogram value of the cumulated rain-rate histogram, the corresponding
value of the cumulated temperature histogram is searched. The corresponding EBBT is assigned to the
rain rate of the cumulated rain-rate histogram. In this way, a set of (Rbin2-Rbin1)/Rstep+1 pairs
of EBBT and rain rate are derived for each PB. These data are stored in look-up tables (LUTs).
Estimation of instantaneous rain rates: The image for channel IR10.8 is read for the reference time
of the ProdGen activity. This step can be done either in real-time or delayed. For a given pixel, the
rain-rate estimation shall be performed only if the scene type is cloudy. Otherwise, the rain rate shall
be set to zero.
For each pixel of the image, the geographical location is calculated. Then the corresponding PB and its
surrounding eight PBs are identified. At the edge of the processing area the number of surrounding
PBs can be smaller. The LUTs of the (up to nine) PBs are used to determine rain rates for the pixel
EBBTs. The final rain rate R is determined as a weighted mean of the (up to nine) pixel rain rates ri:




 9
1
9
1
i
i
i
i
i
w
rw
R

Equation 58


The weights wi are derived from the distance between the location of the pixel and the location of the
mid-points of the nine PBs:
If dlonlonlondlatlatlat pixipixi  and

<!-- source_page: 285 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




then:

  
1
22



  lonlonlatlatw pixipixii

Equation 59


else:
0wi
26.3.3 Automatic Quality Control (AQC)
For each processing box, there are two Quality Indicators (QIs): a standard deviation and a correlation
coefficient. MSG rain rates are first derived from the EBBTs using the LUTs for each CDP. These
values are then compared to the initial SSM/I rain rates, by calculating their standard deviation and
correlation coefficient.
The correlation coefficient can be used to identify areas where the confidence in the rain retrieval is
not sufficient. For instance, if the correlation is less than 0.4 then the MPE product is no longer
suitable for locating rain pattern correctly. The standard deviation is useful for estimating the accuracy
of the SSM/I rain rates themselves.
26.4 Outputs
The following data shall be output:
26.4.1 Intermediate Product
The derived rain rates for each pixel shall be written to the intermediate output files, as well as the
latest QIs (from the last collocation process), for each processing box.

Parameter Mnemonic Units Min Max Prec Acc To
Estimated rain rate R mm/h 0 100 0.1 0.1 -
Standard deviation Stdev mm/h 0 100 0.1 0.1 -
Correlation coefficient Correl - –1 1 0.1 0.1 -
26.4.2 GRIB-2 Encoded Product
The previous data shall be produced for each pixel for the MPE GRIB-2 encoded product according to
WMO FM 92-XIII GRIB Code Table 4.2.
26.5 Future Enhancements
The following future enhancements shall be foreseen in the algorithm design:
 Use of the WV6.2 channel to discriminate between cirrus (not producing rain) and high-level
cumulonimbus (producing rain).
 Replacement of core algorithm by a morphing scheme.

<!-- source_page: 286 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




26.6 References
Reference Title Date Author(s)
Proceedings of the second international
Precipitation Working Group (IPWG)
meeting, Madrid, Spain, September 2002
The Eumetsat multi-sensor
precipitation estimate (MPE)
2002 Heinemann, T.,
A. Latanzio
Proceedings of the EUMETSAT users
conference , Weimar, Germany, 2003
The EUMETSAT Multi Sensor
Precipitation Estimate (MPE):
Concept and Validation
2003 Heinemann, T.
and J. Kerényi
In: Microwave Radiometry and Remote
Sensing of the Earth's Surface and
Atmosphere, P. Pampaloni and S. Paloscia
Eds., VSP Int. Sci. Publ., 353-363
Meteorological applications of
precipitation estimation from
combined SSM/I, TRMM and
infrared geostationary satellite
data
1999 Turk, F. J., G.
D. Rohaly, J.
Hawkins, E. A.
Smith, F. S.
Marzano, A.
Mugnai and V.
Levizzani

<!-- source_page: 287 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




27 AEROSOL PROPERTIES OVER SEA PRODUCT GENERATION
27.1 Algorithm Configuration Information
27.1.1 Algorithm Name
Aerosol Properties Over Sea (AES)
27.1.2 Algorithm Identifier
EUM_MSG_AES_A001
27.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 11/05/09 O. Samain AES baseline
27.2 Inputs
27.2.1 Dynamic Application Data
The main input to the AES algorithm is the Level 1.5 data from the MSG VIS channels, in the form of
top of atmosphere reflectances.
LEVEL 1.5 IMAGE DATA AND DATA DERIVED FROM THE IMAGE DATA
Parameter Mnemonic Units Min M ax Prec Acc Resolution Source
Reflectances for
channels VIS0.6,
VIS0.8 and NIR1.6
REFLchannel % 0 150 0.1 0.1 pixel Derived from level
1.5 image data
Solar zenith angle sol_zenith degrees 0 90 10 -6 10 -6 pixel Derived from Level
1.5 image data
Satellite zenith angle sat_zenith degrees 0 90 10-6 10-6 pixel Derived from Level
1.5 image data
Relative azimuth
angle sun/satellite
sol_sat_azimuth degrees 0 360 0.1 0.1 pixel Derived from Level
1.5 image data
Scene type scene_type - 0 100 1 1 pixel Scenes Analysis
Scene quality scene_quality - 0 100 1 1 pixel Scenes Analysis
Table 86: Aerosol Properties Over Sea Product: Dynamic application data
The scene quality is derived by the SCE algorithm (H.J. Lutz, 2007) and represents the probability of
cloudiness.

<!-- source_page: 288 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




27.2.2 Static Application Data
STATIC APPLICATION DATA – SURFACE DATA
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Look-up table for
channel VIS0.6
AESLUTChan1 - - - - - - Static data
Look-up table for
channel VIS0.8
AESLUTChan2 - - - - - - Static data
Look-up table for
channel NIR1.6
AESLUTChan3 - - - - - - Static data
Nearest coast map Nearest_coast - 0 1000 1 1 pixel Static data
Table 87: Aerosol Properties Over Sea Product: Static application data-surface data
27.3 Static Application Data Setup Parameters
STATIC APPLICATION DATA – SETUP PARAMETERS
Parameter Mnemonic
Maximum scene quality MaxCloudQuality
Maximum satellite zenith angle MaxSatZen
Maximum solar zenith angle MaxSolZen
Maximum distance to coast MaxDistCoast
Maximum sunglint angle MaxSunglintAngle
Minimum valid Angström coefficient MinAngstCoeff
Maximum valid Angström coefficient MaxAngstCoeff
Size in pixels of the final product FinalSegmentSize
Maximum valid AOT value for channel 1 for the final product generation FinalMaxAOTChan1
Maximum valid AOT value for channel 2 for the final product generation FinalMaxAOTChan2
Maximum valid AOT value for channel 3 for the final product generation FinalMaxAOTChan3

27.4 Algorithm Functional Specification
27.4.1 Overview
The AES retrieval algorithm is based on the work of Alexander Ignatov from NOAA. He developed
similar algorithms for AVHRR and MODIS and also generated the look-up tables for SEVIRI. The
theoretical background of his work is described in Ignatov and Stowe, 2002. See Section 26.7.
27.4.2 Algorithm Description
After reading in the image data (channels 1, 2 and 3, i.e. VIS0.6, VIS0.8 and NIR1.6 respectively), the
related auxiliary data (latitude, longitude, solar ze nith, satellite zenith, relative azimuth, look-up
tables) and the Scene type and quality, the retrieval algorithm is applied only if:
 The Scene type is clear water and the scene quality is equal to or lower than MaxCloudQuality
 The SunglintAngle is lower than MaxSunglintAngle, where:

<!-- source_page: 289 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




 )(15.01)( eSolZenAnglCOSanglesinanglecosACOSgleSunglintAn 
with:
)()()(
)()(
SatSunAzimCOSeSatZenAnglSINeSolZenAnglSINanglesin
eSatZenAnglCOSeSolZenAnglCOSanglecos



 The solar zenith angle is lower than MaxSolZen
 The satellite viewing angle is lower than MaxSatZen

The aerosol optical thickness (AOT) for each channel is derived by a multi-dimensional interpolation
of the look-up table values from AESLUTChan1, AESLUTChan2 and AESLUTChan3 (twodimensional and one-dimensional three-point Langrangian interpolation). The table entries are the
solar zenith angle, the satellite viewing angle, the relative azimuth angle and the reflectance for the
respective channel.
The Angström coefficient (or exponent), which expresses the spectral dependence of AOT with the
wavelength of incident light, is calculated as follows:



































810.0
640.1log
08
16log
635.0
810.0log
06
08log
5.0 AOT
AOT
AOT
AOT
AngstCoeff

Equation 60

where
AOT06, AOT08 and AOT16 are the respective AOTs for channels VIS0.6, VIS0.8 and NIR1.6.
Results for which AngstCoeff is less than MinAngstCoeff or greater than MaxAngsCoeff are
discarded.
27.4.3 Final product
The intermediate product is generated every repeat cycle at pixel resolution. The final product
consists of a daily average (from 00:00 to 23:45 UTC) and a spatial average over
FinalSegmentSize × FinalSegmentSize segments.
Filtering is applied to reject noisy values and artefacts:
First, optical thickness values are rejected IF (AOT0.6 > FinalMaxAOTChan1
OR AOT0.8 > FinalMaxAOTChan2
OR AOT1.6 > FinalMaxAOTChan3 )
Secondly, the average AOTMean and standard deviation AOTStd are calculated for each
channel and segment with the values satisfying the previous criteria. The mean is then
recalculated by rejecting the data for which:
)005.0(3  AOTStdAOTMeanAOTValue

Equation 61

<!-- source_page: 290 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




27.4.4 Automatic Quality Control (AQC)
There is no automatic quality control mechanism in the algorithm. The use of look-up tables does not
allow the generation of uncertainty values. Instead, the scene_quality is provided as quality indicator
of the input data.
27.5 Outputs
27.5.1 Final Product
Parameter Mnemonic Units Min Max Prec Acc Format
Segment row number SegRowNo - 0 3712 - - Short Int
Segment column number SegColNo - 0 3712 - - Short Int
Segment latitude Latitude ° -90 90 0.01 0.01 Real
Segment longitude Longitude ° -180 180 0.01 0.01 Real
Aerosol optical thickness for
channels 0.6, 0.8 and 1.6
AOTValues - 0 10 0.1 0.1 Real(3)
Angström coefficient AngstCoeff - 0 3 0.1 0.1 Real
Quality indicator Quality % 0 100 1 1 Real
Table 88: Aerosol Properties Over Sea Product: Outputs, final product
27.5.2 Encoded Product
The AES final product is encoded in GRIB Edition 2 format. The specific GRIB codes for AES (Code
Table 4.2, Product Discipline 3, Parameter Category 1) are defined in the following table:
Code Figure Meaning
14 Aerosol optical thickness at 0.635 µm
15 Aerosol optical thickness at 0.810 µm
16 Aerosol optical thickness at 1.640 µm
17 Angström coefficient
27.6 Future Enhancements
This process also derives optical depth values over small water bodies like rivers and lakes. For an
optimal product, such non-ocean pixels should be removed from the product, which is difficult with
the existing cloud mask. We should consider the production of such an “open ocean mask” for this
product (not available in MPEF at the moment).
27.7 References
Reference Title Date Author(s)
J. Atmos. Sci., 59, 313-334 Aerosol retrievals from individual
AVHRR channels. Part I: Retrieval
algorithm, and transition from Dave to
6S RTM
2002 Ignatov and Stowe

<!-- source_page: 291 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




28 VOLCANIC ASH DETECTION AND RETRIEVAL PRODUCT
GENERATION
28.1 Algorithm Configuration Information
28.1.1 Algorithm Name
Volcanic Ash Detection (VOL)
28.1.2 Algorithm Identifier
EUM_MSG_VOL_A001
28.1.3 Algorithm Specification Version History
Version Date Modified By Description
1.0 10/05/09 O. Samain VOL baseline
2.0 5/03/12 T. Hultberg Quantitative ash properties retrieval added
28.2 Inputs
28.2.1 Dynamic Application Data
The main input to the VOL algorithm is the Level 1.5 data from the MSG channels, in the form of topof-atmosphere reflectances for VIS0.6 and IR3.9 and brightness temperatures for IR3.9, IR8.7, IR10.8
and IR12.0.

LEVEL 1.5 IMAGE DATA AND DATA DERIVED FROM THE IMAGE DATA
Parameter Mnemonic Units Min Max Prec Acc Resolution Source
Reflectances for
channels VIS0.6 and
IR3.9
REFLchannel % 0 150 0.1 0.1 pixel Derived from level
1.5 image data
Brightness
temperatures for
channels IR3.9,
IR8.7, IR10.8 and
IR12.0
EBBTchannel K 0 500 0.1 0.1 pixel Derived from SCE
processing.
Solar zenith angle sol_zen degrees 0 90 10-6 10-6 pixel Derived from Level
1.5 image data
Satellite zenith angle sat_zen degrees 0 90 10 -6 10 -6 pixel Derived from Level
1.5 image data
Table 89: Volcanic Ash Detection and Retrieval Product: Inputs, dynamic application data

<!-- source_page: 292 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




28.2.2 Static Application Data
STATIC APPLICATION DATA –THRESHOLD COEFFICIENTS AND LOOKUP TABLE
Parameter Mnemonic
Thresholds coefficients a* a{1A, 2A, 3A, 3B, 4A}
Thresholds coefficients b* b{1A, 2A, 3A, 3B}
Thresholds coefficients c* c{1A, 2A, 3A, 3B}
Ash cloud optical depth lookup table lut_aod
Ash effective particle radius lookup table lut_radius
Table 90: Volcanic Ash Detection and Retrieval Product: Static application data
28.3 Algorithm Functional Specification
28.3.1 Overview
The volcanic ash cloud detection algorithm is based on the work of the SAFNWC, and of Jochen
Kerkmann (EUMETSAT) and Fred Prata (Norwegian Institute for Air Research). It is based on a
combination of threshold tests, depending on the time of day and channel availability. For pixels
where volcanic ash is detected, a volcanic ash retrieval algorithm is applied. This algorithm is based
on the work of Fred Prata (Norwegian Institute for Air Research) under a EUMETSAT study contract.
28.3.2 Processing mask
The ash detection algorithm is applied to all SEVIRI pixels in the processing area. The ash retrieval
algorithm is only applied to pixels in which ash was detected.
28.3.3 Algorithm Description
28.3.4 Ash detection
After reading in the image data, the related auxiliary data (latitude, longitude, solar zenith and static
datasets), the processing performs the following steps for each pixel:

Step 1 Check the solar zenith angle for day (sol_zen < 80°), night (sol_zen > 90°) or
twilight (between 80° and 90°), to select the thresholds and tests.

Step 2 Calculate the following test flags:
Test1A = (T8.7 - T10.8) > a1A + b1A × TPCS,8.7 + c1A × TPCS,10.8
Test2A = (T12.0 - T10.8) > a2A + b2A × TPCS,12.0 + c2A × TPCS,10.8
Test3A = (T3.9-T10.8) > a3A + b3A × TPCS,3.9 + c3A × TPCS,10.8
Test3B = (T3.9-T10.8) < a3B + b3B × TPCS,3.9 + c3B × TPCS,10.8
Test4A = (Refl3.9 / Refl0.6) > a4A
with (TPCS,chan) denoting the predicted clear sky brightness temperature in channel
chan derived from the ECMWF forecast with the radiative transfer model.

<!-- source_page: 293 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document





Step 3 Apply the following tests:

Test Condition Test Logic Result
Night or Twilight
(sol_zen >= 80)
Test 1A AND Test2A AND Test3A AND Test3B Ash
Day
(sol_zen < 80)
Test1A AND Test2A AND Test4A Ash

Step 4 If the result of the tests is Ash and (T12.0 - T10.8) > 0.5, the pixel is considered to
be potentially ash-contaminated.

28.3.5 Ash retrieval
The ash retrieval algorithm is applied to the pixels which were classified as potentially ash
contaminated by the ash detection algorithm above. The inputs to the ash retrieval algorithm are as
follows:
 the satellite zenith angle, sat_zen
 the measured brightness temperature in channels IR10.8 and IR12.0, T10.8 and T12.0
 an estimate of the surface skin temperature, Ts = TPCS,12.0, taken as the predicted clear sky
brightness temperature in channel IR12.0
 an estimate of the ash cloud top temperature, Tc, obtained from the minimum measured
brightness temperature in channel IR12.0 of potentially ash contaminated pixels within a
neighbourhood of the current pixel, as further detailed below.
For the estimation of the ash cloud top temperature, the 3712 × 3712 image is divided into 128 × 128
blocks of size 29 × 29 pixels each.
1. Determine the minimum value of T12.0 for potentially ash contaminated pixels within each
block.
2. Within each block set Tc to the minimum value of T12.0 in a region of 15 × 15 blocks
centered around the current block
From the satellite zenith angle and T10.8 compute a water vapour correction term as
ΔTwv = min{1/cos(sat_zen), 3} × exp [6 × (T10.8/320) – 6]
The water vapour corrected T10.8 minus T12.0 difference is now computed as
TD = T10.8 – T12.0 – ΔTwv
Given the values of sat_zen, Tc, Ts, T10.8 and TD, the ash cloud optical depth, aod, and effective
particle radius, radius, are looked up in two tables dimensioned as follows:
where:
DIM1 = 12 Satellite zenith angle intervals ( ]82.97..78.98], ]78.98..7427], ..., ]13.52..0] ) degree
DIM2 = 21 Tc ( [200..205[, [205..210[, ..., [300 305[ ) K
DIM3 = 17 Ts ( ]220..225], ]225..230], ..., ]300 305] ) K
DIM4 = 200 T10.8 ( 200.5, 201, ..., 300 ) K
DIM5 = 100 TD ( –0.1, -0.2, ..., -10 ) K

<!-- source_page: 294 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




These tables have been derived by inversion of the tables of T10.8 and T12.0 for varying ash cloud
optical depth and effective particle radius provided by Fred Prata.
A further result of the VOL processing is the total ash mass loading, M, expressed in kg /m-2, which is
related to optical depth and particle radius according to the following:
M = 4/3 × rho × 1e-6 × radius × aod × cos(sat_zen)/Qext
Where rho = 2.6e + 6 g/m3 is the density of silicate and Qext is the extinction efficiency depending on
the radius via a lookup table. Finally, the ash cloud top height (in km) is derived as (Ts-Tc) / 7.
28.4 Outputs
28.4.1 Intermediate Product
The results are stored in as three floats and a one byte quality flag for every pixel, as detailed in the
following table:
Data type Value Dimension
float Volcanic_ash_height 3712 × 3712
byte Volcanic_ash_height_quality 3712 × 3712
float Volcanic_ash_loading 3712 × 3712
float Volcanic_ash_effective_radius 3712 × 3712
28.4.2 Encoded Products
28.4.2.1 NetCDF Product
The fields of the intermediate product are encoded in a single file with netCDF 3 format. The
file is compressed with bzip2 and finally an MPEF_PRODUCT_HEADER (of size 172 bytes)
is pre-appended to arrive at the VOLEncProduct.
28.4.2.2 Text Product
The VOL product is encoded in ASCII format, one line being written for each pixel for which has
been detected. In addition, Common Alert Protocol (CAP) messages are generated by identifying
areas where volcanic plumes are present. For each area, a PNG image is produced showing thick and
thin ashes. The IR channel at 8.7µm is used as background.
28.5 Future Enhancements
Refinement of the ash detection and improvements to the ash cloud top height product are anticipated.
28.6 References
Reference Title Date Author(s)
Contract
EUM/CO/10/4600000775/MK
Volcanic information derived
from satellite data
2011 Fred Prata
Technical note EVOSS products specification 2011 EVOSS project team.

<!-- source_page: 295 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




APPENDIX A: OPEN ISSUES TO BE DECIDED OR
TO BE CONFIRMED
28.7 Issues To Be Decided (TBD)
None
28.8 Issues To Be Confirmed (TBC)
None

<!-- source_page: 296 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




APPENDIX B: GLOSSARY OF TERMS USED IN
THIS DOCUMENT
Term Definition
algorithm ‘Self contained’ routine which inputs data, performs certain
processing and then outputs data, e.g. Scenes Analysis. An
algorithm may generate a product or may just generate data
required by subsequent processes.
configurable A parameter which is modifiable at run-time (by means of the static
data database management utilities) without the need for code
modifications.
dynamic Data which are updated on a regular basis, e.g. for every repeat
cycle, for a predictable time or for a predictable repeat cycle (every
sixth cycle for example).
EMD processing area Defined as a 67-degree geocentric angle around the sub-satellite
point. This is slightly larger than the area to be used to generate the
products themselves in order to allow for correct interpolation at the
edges of the MPEF processing area.
intermediate product Any product which is generated during processing which is not
disseminated to users but is required to generate another product.
MPEF processing area Defined as 65 degrees geocentric angle around the sub-satellite
point.
processing segment A ‘segment’ of size n by n level 1.5 image pixels, where n is
configurable and product-specific.
product A product may be classed as a collection of parameters which are
generated by an algorithm(s) and which are supplied to an external
facility.
static Data which are considered to be unchanging or only infrequently
requiring update (with the frequency being monthly or longer).
superpixel A processing segment made up of nominally 3 by 3 level 1.5 image
pixels.
synoptic scale Providing a horizontal accuracy of 100 km or better, this
corresponds nominally to a processing segment of between
16 × 16 and 32 × 32 level 1.5 image pixels.

<!-- source_page: 297 -->

EUM/MSG/SPE/022
v7B e-signed , 23 October 2015
MSG Meteorological Products Extraction Facility Algorithm
Specification Document




APPENDIX C: APPLICABLE DOCUMENTS NOT IN
THE PUBLIC DOMAIN
This annex lists any applicable documents listed in the Reference section of each Algorithm
Specification which are not currently available in the public domain.

Reference Title Date Author(s)
None
