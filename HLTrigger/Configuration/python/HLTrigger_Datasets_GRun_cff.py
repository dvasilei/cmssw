# getDatasets.py

import FWCore.ParameterSet.Config as cms


# dump of the Stream A Datasets defined in the HLT table as Stream A Datasets

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetInitialPD_selector
streamA_datasetInitialPD_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetInitialPD_selector.l1tResults = cms.InputTag('')
streamA_datasetInitialPD_selector.throw      = cms.bool(False)
streamA_datasetInitialPD_selector.triggerConditions = cms.vstring('HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p3_v1', 
    'HLT_AK8PFHT850_TrimR0p1PT0p03Mass50_v1', 
    'HLT_AK8PFJet360TrimMod_Mass30_v1', 
    'HLT_CaloJet500_NoJetID_v1', 
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_BTagCSV0p7_v1', 
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_v1', 
    'HLT_Dimuon13_PsiPrime_v1', 
    'HLT_Dimuon13_Upsilon_v1', 
    'HLT_Dimuon20_Jpsi_v1', 
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v1', 
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1', 
    'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
    'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v1', 
    'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v1', 
    'HLT_DoubleMu33NoFiltersNoVtx_v1', 
    'HLT_DoubleMu38NoFiltersNoVtx_v1', 
    'HLT_DoubleMu4_3_Bs_v1', 
    'HLT_DoubleMu4_3_Jpsi_Displaced_v1', 
    'HLT_DoubleMu4_JpsiTrk_Displaced_v1', 
    'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v1', 
    'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v1', 
    'HLT_DoublePhoton85_v1', 
    'HLT_Ele12_CaloId_TrackId_Iso_PFJet30_v1', 
    'HLT_Ele18_CaloId_TrackId_Iso_PFJet30_v1', 
    'HLT_Ele20WP60_Ele8_Mass55_v1', 
    'HLT_Ele22_eta2p1_WP85_Gsf_LooseIsoPFTau20_v1', 
    'HLT_Ele23_CaloId_TrackId_Iso_PFJet30_v1', 
    'HLT_Ele25WP60_SC4_Mass55_v1', 
    'HLT_Ele27_eta2p1_WP85_Gsf_CentralPFJet30_BTagCSV_v1', 
    'HLT_Ele27_eta2p1_WP85_Gsf_TriCentralPFJet40_v1', 
    'HLT_Ele27_eta2p1_WP85_Gsf_TriCentralPFJet60_50_35_v1', 
    'HLT_Ele27_eta2p1_WP85_Gsf_v1', 
    'HLT_Ele32_eta2p1_WP85_Gsf_CentralPFJet30_BTagCSV_v1', 
    'HLT_Ele32_eta2p1_WP85_Gsf_TriCentralPFJet40_v1', 
    'HLT_Ele32_eta2p1_WP85_Gsf_TriCentralPFJet60_50_35_v1', 
    'HLT_Ele32_eta2p1_WP85_Gsf_v1', 
    'HLT_Ele33_CaloId_TrackId_Iso_PFJet30_v1', 
    'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1', 
    'HLT_Ele95_CaloIdVT_GsfTrkIdT_v1', 
    'HLT_HT200_DiJet90_AlphaT0p57_v1', 
    'HLT_HT250_DiJet90_AlphaT0p55_v1', 
    'HLT_HT300_DiJet90_AlphaT0p53_v1', 
    'HLT_HT350_DiJet90_AlphaT0p52_v1', 
    'HLT_HT400_DiJet90_AlphaT0p51_v1', 
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1', 
    'HLT_IsoMu20_eta2p1_IterTrk02_CentralPFJet30_BTagCSV_v1', 
    'HLT_IsoMu20_eta2p1_IterTrk02_TriCentralPFJet40_v1', 
    'HLT_IsoMu20_eta2p1_IterTrk02_TriCentralPFJet60_50_35_v1', 
    'HLT_IsoMu20_eta2p1_IterTrk02_v1', 
    'HLT_IsoMu24_eta2p1_IterTrk02_CentralPFJet30_BTagCSV_v1', 
    'HLT_IsoMu24_eta2p1_IterTrk02_TriCentralPFJet40_v1', 
    'HLT_IsoMu24_eta2p1_IterTrk02_TriCentralPFJet60_50_35_v1', 
    'HLT_IsoMu24_eta2p1_IterTrk02_v1', 
    'HLT_IsoTkMu20_eta2p1_IterTrk02_v1', 
    'HLT_IsoTkMu24_eta2p1_IterTrk02_v1', 
    'HLT_JetE30_NoBPTX3BX_NoHalo_v1', 
    'HLT_JetE30_NoBPTX_v1', 
    'HLT_JetE50_NoBPTX3BX_NoHalo_v1', 
    'HLT_JetE70_NoBPTX3BX_NoHalo_v1', 
    'HLT_L1_TripleJet_VBF_v1', 
    'HLT_L2DoubleMu23_NoVertex_v1', 
    'HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v1', 
    'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_Mass10_v1', 
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu10_NoVertex_NoBPTX_v1', 
    'HLT_L2Mu20_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu30_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1', 
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v1', 
    'HLT_MET75_IsoTrk50_v1', 
    'HLT_MET90_IsoTrk50_v1', 
    'HLT_Mu17_Mu8_v1', 
    'HLT_Mu17_TkMu8_v1', 
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1', 
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1', 
    'HLT_Mu17_TrkIsoVVL_v1', 
    'HLT_Mu24_TrkIsoVVL_v1', 
    'HLT_Mu25_TkMu0_dEta18_Onia_v1', 
    'HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v1', 
    'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v1', 
    'HLT_Mu30_TkMu11_v1', 
    'HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v1', 
    'HLT_Mu34_TrkIsoVVL_v1', 
    'HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v1', 
    'HLT_Mu40_eta2p1_PFJet200_PFJet50_v1', 
    'HLT_Mu40_v1', 
    'HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL_v1', 
    'HLT_Mu8_TrkIsoVVL_v1', 
    'HLT_PFHT350_PFMET120_NoiseCleaned_v1', 
    'HLT_PFHT350_v1', 
    'HLT_PFHT550_4Jet_v1', 
    'HLT_PFHT600_v1', 
    'HLT_PFHT650_4Jet_v1', 
    'HLT_PFHT750_4Jet_v1', 
    'HLT_PFHT900_v1', 
    'HLT_PFJet140_v1', 
    'HLT_PFJet200_v1', 
    'HLT_PFJet260_v1', 
    'HLT_PFJet320_v1', 
    'HLT_PFJet400_v1', 
    'HLT_PFJet40_v1', 
    'HLT_PFJet450_v1', 
    'HLT_PFJet500_v1', 
    'HLT_PFJet60_v1', 
    'HLT_PFJet80_v1', 
    'HLT_PFMET110_PFMHT110_IDLoose_v1', 
    'HLT_PFMET120_NoiseCleaned_BTagCSV07_v1', 
    'HLT_PFMET120_NoiseCleaned_Mu5_v1', 
    'HLT_PFMET170_NoiseCleaned_v1', 
    'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon120_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon155_PFMET40_v1', 
    'HLT_Photon155_VBF_v1', 
    'HLT_Photon155_v1', 
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon250_NoHE_v1', 
    'HLT_Photon26_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon16_AND_HE10_R9Id65_Eta2_Mass60_v1', 
    'HLT_Photon300_NoHE_v1', 
    'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon18_AND_HE10_R9Id65_Mass95_v1', 
    'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v1', 
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_v1', 
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Physics_v1', 
    'HLT_QuadPFJet_BTagCSV_VBF_v1', 
    'HLT_QuadPFJet_VBF_v1', 
    'HLT_ZeroBias_v1')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetTemplates_selector
streamA_datasetTemplates_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetTemplates_selector.l1tResults = cms.InputTag('')
streamA_datasetTemplates_selector.throw      = cms.bool(False)
streamA_datasetTemplates_selector.triggerConditions = cms.vstring('HLT_IsoMu24_IterTrk02_v1', 
    'HLT_IsoTkMu24_IterTrk02_v1', 
    'HLT_ReducedIterativeTracking_v1')

