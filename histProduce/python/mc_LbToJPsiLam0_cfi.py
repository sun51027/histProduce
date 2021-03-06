import FWCore.ParameterSet.Config as cms

files = cms.vstring()
files.extend( [
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_1.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_10.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_100.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_101.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_102.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_103.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_104.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_105.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_106.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_107.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_108.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_109.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_11.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_110.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_111.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_112.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_113.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_114.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_115.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_116.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_117.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_118.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_119.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_12.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_120.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_121.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_122.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_123.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_124.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_125.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_126.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_127.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_128.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_129.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_13.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_130.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_131.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_132.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_133.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_134.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_135.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_136.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_137.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_138.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_139.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_14.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_140.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_141.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_142.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_143.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_144.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_145.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_146.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_147.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_148.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_149.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_15.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_150.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_151.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_152.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_153.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_154.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_155.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_156.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_157.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_158.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_159.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_16.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_160.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_161.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_162.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_163.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_164.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_165.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_166.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_167.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_168.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_169.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_17.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_170.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_171.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_172.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_173.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_174.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_175.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_176.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_177.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_178.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_179.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_18.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_180.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_181.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_182.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_183.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_184.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_185.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_186.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_187.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_188.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_189.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_19.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_190.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_191.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_192.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_193.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_194.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_195.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_196.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_197.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_198.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_199.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_2.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_20.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_200.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_201.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_202.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_203.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_204.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_205.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_206.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_207.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_208.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_209.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_21.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_210.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_211.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_212.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_213.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_214.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_22.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_23.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_24.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_25.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_26.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_27.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_28.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_29.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_3.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_30.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_31.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_32.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_33.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_34.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_35.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_36.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_37.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_38.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_39.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_4.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_40.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_41.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_42.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_43.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_44.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_45.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_46.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_47.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_48.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_49.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_5.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_50.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_51.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_52.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_53.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_54.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_55.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_56.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_57.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_58.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_59.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_6.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_60.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_61.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_62.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_63.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_64.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_65.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_66.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_67.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_68.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_69.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_7.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_70.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_71.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_72.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_73.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_74.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_75.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_76.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_77.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_78.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_79.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_8.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_80.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_81.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_82.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_83.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_84.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_85.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_86.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_87.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_88.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_89.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_9.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_90.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_91.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_92.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_93.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_94.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_95.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_96.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_97.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_98.root",
"/home/ltsai/Data/CRABdata/CRABdata_10_Jan_2018_LbToJPsiLam0/recoWriteSpecificDecay_99.root"
 ] )

process = cms.PSet()

process.runSetting = cms.PSet(
        #maxEvents = cms.int32(10000),
        maxEvents = cms.int32(-1),
        outEvery  = cms.uint32(5000),
        outName   = cms.string('histogram_mc_LbToJPsiLam0_13TeV_2016Generated.root'),
        )
process.inputFiles = cms.PSet( fileNames  = files )
