#-- GAUDI jobOptions generated on Mon Apr 11 09:41:53 2016
#-- Contains event types : 
#--   10000000 - 165 files - 985338 events - 516.14 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-128251 

#--  StepId : 128251 
#--  StepName : Sim08h for Upgrade with nu = 7.6 (L=2x10^33), with spillover - MU - 2015 Baseline Geometry - Pythia8 
#--  ApplicationName : Gauss 
#--  ApplicationVersion : v47r2 
#--  OptionFiles : $APPCONFIGOPTS/Gauss/Beam7000GeV-mu100-nu7.6-HorExtAngle.py;$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py;$APPCONFIGOPTS/Conditions/IgnoreCaliboffDB_LHCBv38r7.py;$DECFILESROOT/options/@{eventType}.py;$LBPYTHIA8ROOT/options/Pythia8.py;$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py;$APPCONFIGOPTS/Gauss/Gauss-Upgrade-Baseline-20150522.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20150702 
#--  CONDDB : sim-20150716-vc-mu100 
#--  ExtraPackages : AppConfig.v3r231;DecFiles.v27r50 
#--  Visible : Y 


#--  Processing Pass Step-127608 

#--  StepId : 127608 
#--  StepName : Merge15 for Sim LDST 
#--  ApplicationName : LHCb 
#--  ApplicationVersion : v38r5 
#--  OptionFiles : $APPCONFIGOPTS/Merging/CopyDST.py 
#--  DDDB : None 
#--  CONDDB : None 
#--  ExtraPackages : AppConfig.v3r207 
#--  Visible : N 


#--  Processing Pass Step-128230 

#--  StepId : 128230 
#--  StepName : Reco15U3 for Upgrade studies - 2015 Baseline Geometry - LDST 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v48r0 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Brunel/Brunel-Upgrade-Baseline-20150522.py;$APPCONFIGOPTS/Brunel/Upgrade-RichPmt.py;$APPCONFIGOPTS/Brunel/patchUpgrade1.py;$APPCONFIGOPTS/Brunel/ldst.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r231 
#--  Visible : Y 


#--  Processing Pass Step-128288 

#--  StepId : 128288 
#--  StepName : Digi14U4 for Upgrade studies with spillover - 2015 Baseline NoRichSpillover NoNoise 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v29r8 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/Boole-Upgrade-Baseline-20150522.py;$APPCONFIGOPTS/Boole/EnableSpillover.py;$APPCONFIGOPTS/Boole/Upgrade-RichMaPMT-NoSpilloverDigi.py;$APPCONFIGOPTS/Boole/xdigi.py;$APPCONFIGOPTS/Boole/Boole-Upgrade-NoNoise.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r232 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000001_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000002_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000003_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000004_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000005_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000006_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000007_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000008_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000009_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000010_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000011_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000012_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000013_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000014_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000015_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000016_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000017_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000018_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000019_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000020_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000021_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000022_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000023_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000024_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000025_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000026_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000027_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000028_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000029_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000030_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000031_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000032_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000034_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000035_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000036_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000037_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000038_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000039_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000040_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000041_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000042_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000043_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000044_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000045_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000046_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000047_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000048_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000049_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000050_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000052_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000053_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000054_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000055_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000056_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000057_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000058_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000059_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000060_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000061_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000062_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000065_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000066_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000067_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000068_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000069_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000070_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000071_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000072_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000073_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000074_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000075_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000076_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000077_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000078_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000079_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000080_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000081_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000082_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000083_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000084_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000085_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000086_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000087_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000088_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000089_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000090_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000091_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000092_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000093_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000094_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000095_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000096_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000097_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000098_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000099_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000100_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000101_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000102_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000103_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000104_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000105_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000106_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000107_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000109_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000110_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000112_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000113_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000114_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000115_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000116_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000117_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000118_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000119_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000120_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000121_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000122_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000123_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000124_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000125_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000126_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000127_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000128_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000129_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000130_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000131_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000132_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000133_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000134_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000135_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000136_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000137_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000138_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000139_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000140_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000141_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000142_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000143_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000144_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000145_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000146_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000147_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000148_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000149_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000151_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000152_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000153_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000154_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000155_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000156_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000157_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000159_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000160_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000161_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000162_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000163_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000164_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000165_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000166_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000167_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000168_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000169_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000170_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000171_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000172_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00047160/0000/00047160_00000173_1.ldst'
], clear=True)
FileCatalog().Catalogs += [ 'xmlcatalog_file:upgrade-bbbar-up-cern-pnf.xml' ]
