import CombineHarvester.CombineTools.ch as ch

def AddCommonSystematics(cb, year):
  backgrounds = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  bbhsignals = ['bbH_htt','bbH_nobb_htt','bbH_hww','bbH_nobb_hww']
  mc_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH_hww','bbH_nobb_hww','ggH_bb_hww','ggH_hww','ZL','TTL','VVL','qqH125','WH125','ZH125','qqHWW125','WHWW125','ZHWW125','WH','TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT']
  nojetfakes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH_hww','bbH_nobb_hww','ggH_bb_hww','ggH_hww','ZL','TTL','VVL','qqH125','WH125','ZH125','qqHWW125','WHWW125','ZHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','EMB','W','ZTT']
  httprocs = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','ZH','VBF','qqH125','WH125','ZH125']
  hwwprocs = ['bbH_hww','bbH_nobb_hww','ggH_bb_hww','ggH_hww','qqHWW125','WHWW125','ZHWW125']

  #Signal theory uncertainties
  cb.cp().process(bbhsignals).AddSyst(cb,'QCDscale_bbH','lnN', ch.SystMap()((0.76,1.201)))
  cb.cp().process(['ggH125','ggHWW125','bbH125_yb2','bbH125_yt2','ggH_bb_htt','ggH_htt']).AddSyst(cb,'QCDscale_ggH','lnN', ch.SystMap()((0.93,1.046)))
  cb.cp().process(['ggH125','ggHWW125','bbH125_yb2','bbH125_yt2','ggH_bb_htt','ggH_htt']).AddSyst(cb,'pdf_Higgs_ggH','lnN', ch.SystMap()(1.032))
  #Additional uncertainty for ggH+2b 
  cb.cp().process(['ggH_bb_htt']).AddSyst(cb,'QCDscale_ggHbb','lnN',ch.SystMap()(1.40))

  #Need to double check these ones 
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_THU','lnN', ch.SystMap()(1.017))
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_PU_mq','lnN', ch.SystMap()(1.0099))
  cb.cp().process(httprocs).AddSyst(cb,'BR_htt_PU_alphas','lnN', ch.SystMap()(1.0062))

  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_THU','lnN', ch.SystMap()(1.0099))
  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_PU_mq','lnN', ch.SystMap()(1.0099))
  cb.cp().process(hwwprocs).AddSyst(cb,'BR_hww_PU_alphas','lnN', ch.SystMap()(1.0066))

  cb.cp().process(['ZH125','ZH','ZH1','ZHWW125']).AddSyst(cb,'QCDscale_VH','lnN',ch.SystMap()(1.009))
  cb.cp().process(['ZH125','ZH','ZH1','ZHWW125']).AddSyst(cb,'pdf_Higgs_VH','lnN',ch.SystMap()(1.013))
  cb.cp().process(['WH125','WH','WH1','WHWW125']).AddSyst(cb,'QCDscale_VH','lnN',ch.SystMap()(1.008))
  cb.cp().process(['WH125','WH','WH1','WHWW125']).AddSyst(cb,'pdf_Higgs_VH','lnN',ch.SystMap()(1.018))
  cb.cp().process(['ttH125']).AddSyst(cb,'QCDscale_ttH','lnN',ch.SystMap()(1.08))
  cb.cp().process(['ttH125']).AddSyst(cb,'pdf_Higgs_ttH','lnN',ch.SystMap()(1.036))
  cb.cp().process(['VBF','qqH125','qqHWW125']).AddSyst(cb,'QCDscale_qqH','lnN',ch.SystMap()(1.005))
  cb.cp().process(['VBF','qqH125','qqHWW125']).AddSyst(cb,'pdf_Higgs_qqbar','lnN',ch.SystMap()(1.021))


  #Tau trigger efficiency 
  tautriggerdmbins = ["0","1","10","11"]
  for taubin in tautriggerdmbins:
     cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))
     cb.cp().process(["EMB"]).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_emb_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))
     cb.cp().process(["EMB"]).channel(['tt']).AddSyst(cb,'CMS_eff_xtrigger_t_tt_dm'+taubin+'_'+year,'shape',ch.SystMap()(1.0))

  #Tau ID
  cb.cp().process(nojetfakes).channel(['mt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.03))
  cb.cp().process(['bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ggH125','qqH125','WH125','ZH125','EMB','ZTT','TTT','VVT','TT','VV','ST']).channel(['tt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.06))
  cb.cp().process(['TTL','VVL']).channel(['tt']).AddSyst(cb,'CMS_eff_t_wp_'+year,'lnN',ch.SystMap()(1.03))

  #Electron ID
  cb.cp().process(mc_processes).channel(['et','em']).AddSyst(cb,"CMS_eff_e","lnN",ch.SystMap()(1.02))

  #Muon ID
  cb.cp().process(mc_processes).channel(['mt','em']).AddSyst(cb,"CMS_eff_m","lnN",ch.SystMap()(1.02))
  
  for taubin in tautriggerdmbins:
    #cb.cp().process(mc_processes).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_dm'+taubin+"_"+year,'shape',ch.SystMap()(1.0))
    cb.cp().process(mc_processes).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_$CHANNEL'+'_'+year,'lnN',ch.SystMap()(1.01))
    cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_t_dm'+taubin+'_'+year, 'shape', ch.SystMap()(1.0))
    cb.cp().process(mc_processes).channel(['tt']).AddSyst(cb,'CMS_eff_t_$CHANNEL'+'_'+year, 'lnN', ch.SystMap()(1.014))
  
  #EMB lepton ID
  cb.cp().process(['EMB']).channel(['et','em']).AddSyst(cb,'CMS_eff_e_emb','lnN',ch.SystMap()(1.017))
  cb.cp().process(['EMB']).channel(['et','em']).AddSyst(cb,'CMS_eff_e','lnN',ch.SystMap()(1.01))
  cb.cp().process(['EMB']).channel(['mt','em']).AddSyst(cb,'CMS_eff_m_emb', 'lnN',ch.SystMap()(1.017))
  cb.cp().process(['EMB']).channel(['mt','em']).AddSyst(cb,'CMS_eff_m', 'lnN',ch.SystMap()(1.01))
  for taubin in tautriggerdmbins:
    cb.cp().process(['EMB']).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_emb_dm'+taubin+'_'+year,'shape',ch.SystMap()(0.866))
    cb.cp().process(['EMB']).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_dm'+taubin+'_'+year,'shape',ch.SystMap()(0.5))
    cb.cp().process(['EMB']).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_emb_dm_$CHANNEL_'+year,'lnN',ch.SystMap()(1.0087))
    cb.cp().process(['EMB']).channel(['et','mt']).AddSyst(cb,'CMS_eff_t_dm_$CHANNEL_'+year,'lnN',ch.SystMap()(1.005))
    cb.cp().process(['EMB']).channel(['tt']).AddSyst(cb,'CMS_eff_t_emb_dm'+taubin+'_'+year,'shape',ch.SystMap()(0.866))
    cb.cp().process(['EMB']).channel(['tt']).AddSyst(cb,'CMS_eff_t_dm'+taubin+'_'+year,'shape',ch.SystMap()(0.5))
    cb.cp().process(['EMB']).channel(['tt']).AddSyst(cb,'CMS_eff_t_emb_dm_$CHANNEL_'+year,'lnN',ch.SystMap()(1.012))
    cb.cp().process(['EMB']).channel(['tt']).AddSyst(cb,'CMS_eff_t_dm_$CHANNEL_'+year,'lnN',ch.SystMap()(1.007))
  
  #Ele ES  
  #  cb.cp().channel(['em']).process(mc_processes).AddSyst(cb,'CMS_scale_e','shape',ch.SystMap()(1.0)) #Maybe also apply to et but don't have it at the moment
  cb.cp().channel(['em','et']).process('EMB').AddSyst(cb,'CMS_scale_e_emb','shape',ch.SystMap()(1.0)) #Maybe also apply to et but don't have it at the moment

  #Missing: btag, JES, MET, etc.

  #Bkg normalisations
  cb.cp().channel(['et','mt','tt','em']).process(['VVT','VVJ','VVL','VV','ST']).AddSyst(cb,'CMS_htt_vvXsec','lnN',ch.SystMap()(1.05))
  cb.cp().channel(['et','mt','tt','em']).process(['TTT','TTL','TTJ','TT']).AddSyst(cb,'CMS_htt_tjXsec','lnN',ch.SystMap()(1.06))
  cb.cp().channel(['et','mt','tt','em']).process(['W','WJets']).AddSyst(cb,'CMS_htt_wjXsec','lnN',ch.SystMap()(1.04))
  cb.cp().channel(['et','mt','tt','em']).process(['ZTT','ZL','ZJ','DYJets']).AddSyst(cb,'CMS_htt_zjXsec','lnN',ch.SystMap()(1.02))

  #emu QCD  
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_0jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_0jet_shape_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_0jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_1jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_1jet_shape_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_1jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_2jet_rate_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_2jet_shape_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_2jet_shape2_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_iso_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_nonClosure_'+year,'shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['em']).process(['QCD']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_extrap','lnN',ch.SystMap()(1.15)) 
  cb.cp().channel(['em']).process(['W']).AddSyst(cb,'CMS_htt_fake_em_'+year,'lnN',ch.SystMap()(1.15)) 
  cb.cp().channel(['em']).process(['ZL']).AddSyst(cb,'CMS_htt_ZL_fake_em_'+year,'lnN',ch.SystMap()(1.2)) 

   
  cb.cp().channel(['tt','em']).process(['TTT','TTL','TTJ','TT']).AddSyst(cb,'CMS_htt_ttbarShape','shape',ch.SystMap()(1.0))  #Not present in et,mt

  #cb.cp().channel(['mt']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['mt']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong1pizero_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['et']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong_barrel_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['et']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong1pizero_barrel_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['et']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong_endcap_'+year,'shape',ch.SystMap()(1.0)) 
  #cb.cp().channel(['et']).process(['ZL']).AddSyst(cb,'CMS_ZLShape_$CHANNEL_1prong1pizero_endcap_'+year,'shape',ch.SystMap()(1.0)) 


  cb.cp().process(['EMB']).AddSyst(cb,'CMS_htt_doublemutrg_'+year,'lnN',ch.SystMap()(1.04)) 
  cb.cp().process(['EMB']).AddSyst(cb,'CMS_htt_emb_ttbar_'+year,'shape',ch.SystMap()(1.00)) 
  #cb.cp().channel(['et','mt','tt']).process(['EMB']).AddSyst(cb,'CMS_3ProngEff_'+year,'shape',ch.SystMap()(1.00)) 
  #cb.cp().channel(['et','mt','tt']).process(['EMB']).AddSyst(cb,'CMS_1ProngPi0Eff_'+year,'shape',ch.SystMap()(1.00)) 

  #jetFake uncs
  #  jetbins = ['njets0','njets1','njets2']
  #  dmbins = ['dm0','dm1','dm10']
  #  qcduncs = ['unc1','unc2']

  #  for jbin in jetbins:
  #    for unc in qcduncs:
  #      for dm in dmbins:
  #        cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_ff_total_qcd_stat_'+unc+'_'+jbin+'_'+dm+'_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
  
  variables = ['dR','pt']
  qcduncs = ['unc1','unc2']
  for variable in variables:
    for unc in qcduncs:
      cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_stat_'+variable+'_'+unc+'_'+year,'shape',ch.SystMap()(1.0))

  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_fakes_subtr_syst_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))
#  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_syst_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_syst_dr_closure_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_$CHANNEL_qcd_syst_pt_2_closure_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['jetFakes']).AddSyst(cb,'CMS_htt_tt_qcd_syst_met_closure_'+year,'shape',ch.SystMap()(1.0))
  cb.cp().channel(['tt']).process(['wFakes']).AddSyst(cb,'CMS_htt_$CHANNEL_wFakes_syst_'+year,'lnN',ch.SystMap()(1.3))

  cb.cp().channel(['tt']).process(['TT','VV','ZL','ST']).AddSyst(cb,'CMS_htt_fake_m_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))

# absent at the moment should be added later
#  cb.cp().channel(['tt']).process(['TT','VV','ZL','ST']).AddSyst(cb,'CMS_htt_fake_e_$CHANNEL_'+year,'shape',ch.SystMap()(1.0))


def AddSystematics2018(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  mc_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ZL','TTL','VVL','ggH125','qqH125','WH125','ZH125','ggHWW125','qqHWW125','WHWW125','ZHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT']

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2018','lnN', ch.SystMap()(1.015))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.02))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.002))

  cb.cp().process(['ZTT','ZL','ZJ']).channel(["tt","em"]).AddSyst(cb, 'CMS_htt_dyShape', 'shape', ch.SystMap()(0.20)) #FIXME not present in mt,et
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_lf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_hf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_cferr1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2018_cferr2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'jesTotal2018', 'shape', ch.SystMap()(1.0))
  #cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_qcd', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_w', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_tt', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_qcdfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_qcdfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_wfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_wfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_wfitpar3', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_wfitpar4', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_ttfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2018_ttfitpar2', 'shape', ch.SystMap()(1.0))

def AddSystematics2017(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  mc_processes = ['bbH_htt','bbH_nobb_htt','ggH_bb_htt','ggH_htt','bbH125_yb2','bbH125_yb2_nobb','bbH125_yt2','ZL','TTL','VVL','ggH125','qqH125','WH125','ZH125','ggHWW125','qqHWW125','WHWW125','ZHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF','W','ZTT']

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2017','lnN', ch.SystMap()(1.020))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.009))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.006))

  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'CMS_prefiring', 'shape', ch.SystMap()(1.0))

  cb.cp().process(['ZTT','ZL','ZJ']).channel(["tt","em"]).AddSyst(cb, 'CMS_htt_dyShape', 'shape', ch.SystMap()(0.20)) #FIXME not present in mt,et
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_lf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_hf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_cferr1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2017_cferr2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'jesTotal2017', 'shape', ch.SystMap()(1.0))
  #cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_qcd', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_w', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_tt', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_qcdfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_qcdfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_wfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_wfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_wfitpar3', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_wfitpar4', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_ttfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2017_ttfitpar2', 'shape', ch.SystMap()(1.0))

def AddSystematics2016(cb):
  backgrounds  = cb.cp().backgrounds().process_set()
  signals = cb.cp().signals().process_set()
  mc_processes = ['bbH_htt','bbH125','bbHWW125','bbH_nobb_htt','ggH_bb_htt','ggH_htt','ggH125','ZL','TTL','VVL','ggH125','qqH125','ggHWW125','qqHWW125','TT','ST','WJets','DYJets','VV','ZH','VBF']

  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV_2016','lnN', ch.SystMap()(1.010))
  cb.cp().process(mc_processes).AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.006))

  cb.cp().process(mc_processes).channel(["tt","em"]).AddSyst(cb, 'CMS_prefiring', 'shape', ch.SystMap()(1.0))
  cb.cp().process(['ZTT','ZL','ZJ']).channel(["tt","em"]).AddSyst(cb, 'CMS_htt_dyShape_2016', 'shape', ch.SystMap()(0.20)) #FIXME not present in mt,et
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_jes', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_lf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_hf', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_hfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_hfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_lfstats1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_lfstats2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_cferr1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'btag2016_cferr2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'jesTotal2016', 'shape', ch.SystMap()(1.0))
  #cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_qcd', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_w', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_tt', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_qcdfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_qcdfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_wfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_wfitpar2', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_wfitpar3', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_wfitpar4', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_ttfitpar1', 'shape', ch.SystMap()(1.0))
  cb.cp().process(mc_processes).channel(["mt","et"]).AddSyst(cb, 'ff2016_ttfitpar2', 'shape', ch.SystMap()(1.0))
