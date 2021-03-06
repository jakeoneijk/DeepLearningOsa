from HParams import HParams

from MakeMetaData.SingingVoice.MakeSkMultiSingerMetaData import MakeSkMultiSingerMetaData
from MakeMetaData.SingingVoice.MakeIKalaMetaData import MakeIKalaMetaData
from MakeMetaData.SingingVoice.MakeMedlyDbVocalRawMix import MakeMedlyDbVocalRawMix

class MakeMetaData:
    def __init__(self,h_params:HParams):
        self.h_params = h_params

        self.data_mkr_dict = dict()
        self.data_mkr_dict["sk_multi_singer"] = MakeSkMultiSingerMetaData(h_params)
        self.data_mkr_dict["ikala"] = MakeIKalaMetaData(h_params)
        self.data_mkr_dict["medly_db_vocal_raw_mix"] = MakeMedlyDbVocalRawMix(h_params)
    
    def make_meta_data(self,data_type:str):
        self.data_mkr_dict[data_type].save_meta_data_list()
