from Configurables import Brunel

from Configurables import GaudiSequencer
from Configurables import PatPV3D, PVOfflineTool, LSAdaptPV3DFitter
from Configurables import PatPVOffline, LSAdaptPVFitter, PVSeed3DOfflineTool,  VertexCompare
from Gaudi.Configuration import *
from Configurables import LHCbApp
from Configurables import Brunel
from Configurables import RecSysConf, RecMoniConf
from Configurables import L0Conf
from Configurables import TrackAssociator
from Brunel.Configuration import  *
import GaudiKernel.SystemOfUnits as Units

#Brunel().CondDBtag = 'sim-20131023-vc-md100' # use the mu100 for MagUp data
#Brunel().DDDBtag = 'dddb-20130929-1'
from GaudiConf import IOHelper

Brunel().InputType = "DST"
Brunel().WithMC    = True
Brunel().WriteFSR = False
Brunel().WriteLumi = False 
Brunel().OutputType  = "LDST"
Brunel().EvtMax = 10
Brunel().SkipEvents = 0
Brunel().Simulation = True
part = str(int(Brunel().SkipEvents))

Brunel().MCCheckSequence = ["MyChecks"]
#Brunel().MCLinksSequence =  ['Unpack']

from Configurables import Brunel, CondDB
CondDB().Upgrade = True

Brunel().Detectors = ['VP', 'UT', 'FT', 'Tr']
Brunel().DataType     = "Upgrade"

LHCbApp().DDDBtag = "dddb-20150702"
LHCbApp().CondDBtag = "sim-20150716-vc-mu100"
LHCbApp().DataType = "Upgrade"
#LHCbApp().Detectors = ['VP', 'UT', 'FT', "Tr"]

L0Conf().EnsureKnownTCK=False

from Configurables import RootCnvSvc
RootCnvSvc().GlobalCompression = "ZLIB:1"

#from Configurables import MCFTDigitCreator
#MCFTDigitCreator().SimulateNoise = False

from Configurables import DecodeRawEvent
DecodeRawEvent().setProp("OverrideInputs",4.2)


from Configurables import RichRecSysConf,  RichRecQCConf
rConf = RichRecSysConf("RichOfflineRec")
# No Aerogel                                                                                                                                                                                 
rConf.Radiators = [ "Rich1Gas", "Rich2Gas" ]
# no photon sel cuts (need optimising)                                                                                                                                                       
rConf.photonConfig().SelectionMode = "All"
# Corrections to CK theta                                                                                                                                                                    
rConf.richTools().photonReco().CKThetaQuartzRefractCorrections = [ -0.00625,  0.00010,  2.9e-5 ]


RecMoniConf().Detectors = ["Tr"]
RecMoniConf().MoniSequence = ["Tr"]

ApplicationMgr().ExtSvc += ["DataOnDemandSvc"]


