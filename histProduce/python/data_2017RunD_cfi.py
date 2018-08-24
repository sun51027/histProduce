import FWCore.ParameterSet.Config as cms

files = cms.vstring()
files.extend( [
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-1.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-10.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-11.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-12.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-13.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-14.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-15.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-16.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-17.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-18.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-19.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-2.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-20.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-21.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-22.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-23.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-24.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-25.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-26.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-27.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-28.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-29.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-3.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-30.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-31.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-32.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-33.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-34.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-35.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-36.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-37.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-38.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-4.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-5.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-6.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-7.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-8.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1-9.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_1.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_10.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_11.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_12.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_13.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_14.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_15.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_16.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_17.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_18.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_19.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_2.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_20.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_21.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_22.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_23.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_24.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_25.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_26.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_27.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_28.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_29.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_3.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_30.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_31.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_33.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_34.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_35.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_36.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_37.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_38.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_39.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_4.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_40.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_41.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_42.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_43.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_44.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_45.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_46.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_47.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_48.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_49.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_5.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_50.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_51.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_52.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_53.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_54.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_55.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_56.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_57.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_58.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_59.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_6.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_60.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_61.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_62.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_63.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_64.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_65.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_66.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_67.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_68.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_69.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_7.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_70.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_71.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_72.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_73.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_74.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_75.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_76.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_77.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_78.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_79.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_8.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_80.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_81.root",
"/home/ltsai/Data/CRABdata/CRABdata_20_Aug_2018_2017RunD/recoBPHanalysis_withFilter_9.root",

 ] )

process = cms.PSet()

process.runSetting = cms.PSet(
        #maxEvents = cms.int32(500000),
        maxEvents = cms.int32(-1),
        outEvery  = cms.uint32(5000),
        outName   = cms.string('tree_2017RunX_testData_07Aug2017ReReco.root'),
        )
process.inputFiles = cms.PSet( fileNames  = files )
