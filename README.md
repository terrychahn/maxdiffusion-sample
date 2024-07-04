# MaxDiffusion Sample - Stable Diffusion XL Lightning on TPU v5e

The project provides sample code for inferencing with the Stable Diffusion XL Lightning model on TPU v5e using MaxDiffusion. For more details, please refer to [Medium blog post](https://medium.com/p/3f7be638f2b9) (in Korean).

### Stable Diffusion XL Lightning + MaxDiffusion Inference Server

    python server/main_lightning.py

It requires [FastAPI](https://fastapi.tiangolo.com). Run on TPU VM.


### Web Frontend App

    export MAXDIFFUSION_SERVER_URL="http://[SERVER_IP]:8000"
    streamlit run src/frontend/clientapp.py

It requires [Streamlit](https://streamlit.io). Replace SERVER_IP with MaxDiffusion Server IP and run on local. 

## References

[google/maxdiffusion](https://github.com/google/maxdiffusion)

: MaxDiffusion is a collection of reference implementations of various latent diffusion models written in pure Python/Jax that run on XLA devices.

[llm-on-gke/sdxl-tpu](https://github.com/llm-on-gke/sdxl-tpu) 

: A repository for SDXL inference on GKE and TPU.
