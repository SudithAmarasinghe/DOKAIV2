Do the following steps befor run the main.py
######################################################

01. First run the following in the console to install the required packages.
pip install -r requirements.txt
pip install -r model/deep_seek/DeepSeek_VL/requirements.txt

If you receive the following error do the step 02.
RuntimeError: "triu_tril_cuda_template" not implemented for 'BFloat16'
02. Change the modelling_llama.py in the following path.
"/usr/local/lib/python3.10/dist-packages/transformers/models/llama/modeling_llama.py"
In line 1076, in _update_causal_mask.
Currently only following code part is there.
    "causal_mask = torch.triu(causal_mask, diagonal=1)"
Change it to:
    causal_mask = causal_mask.to(torch.float32)
    causal_mask = torch.triu(causal_mask, diagonal=1)
    causal_mask = causal_mask.to('cuda', dtype=torch.bfloat16)
Note: Do this only if it is not changed already.
