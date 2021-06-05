import numpy as np
import torch

from HParams import HParams

class Tester():
    def __init__(self,h_params:HParams):
        self.h_params = h_params
        self.device = h_params.resource.device
        self.model = None

    def test_one_sample(self,input_path):
        self.set_output_path()
        input = self.read_input(input_path)
        self.pretrained_load("")
        batch_input = self.make_batch(input)
        output = self.make_output(batch_input)
        self.post_processing(output)

    
    def set_output_path(self):
        pass

    def pretrained_load(self,pretrain_path):
        best_model_load = torch.load(pretrain_path,map_location='cpu')
        self.model.load_state_dict(best_model_load)
        self.model.to(self.device)

    def make_batch(self,input:dict,segment_size:int):
        batch_data = dict()
        for feature in input:
            batch_data[feature]=None

        total_size = None

        for start_idx in range(0,total_size,segment_size):
            end_idx = start_idx + segment_size

            for feature in input:
                feature_seg = input[feature][...,start_idx:end_idx]
            
                if feature_seg.shape[-1] != segment_size:
                    padding = segment_size - feature_seg.shape[-1]
                    if len(feature_seg.shape) == 1:
                        feature_seg =  np.pad(feature_seg,(0,padding),'constant', constant_values=0)
                    elif len(feature_seg.shape) == 2:
                        feature_seg =  np.pad(feature_seg,((0,0),(0,padding)),'constant', constant_values=0)
                    else:
                        continue
                    
                feature_seg = np.expand_dims(feature_seg,axis=0)
                batch_data[feature] = feature_seg if batch_data[feature] is None else np.vstack((batch_data[feature],feature_seg))

        return batch_data
    
    def unzip_batch(self,batch_data,unzip_data):
        numpy_batch = batch_data.detach().cpu().numpy()
        for i in range(0,numpy_batch.shape[0]):
            unzip_data = numpy_batch[i] if unzip_data is None else np.concatenate((unzip_data,numpy_batch[i]),axis=-1)
        return unzip_data
    
    def make_output(self,batch_input):
        pass
    
    def post_processing(self,model_output):
        pass
    