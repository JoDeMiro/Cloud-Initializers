'''Joe De Miro oficial Nespresso advocate and associated partner °˛°'''

import numpy as np
print(np.__version__)

import tensorflow as tf
print(tf.__version__)

print('°˛° ne nézz hülyén úgy sem segít')

# Start Jupyter
# jupyter notebook --ip=0.0.0.0 --port=8888 --no-browse
# jupyter notebook --ip=0.0.0.0 --port=8888 --no-browse &> /dev/null &

print(tf.config.list_physical_devices('GPU'))

print(tf.test.is_gpu_available())

print(tf.test.is_gpu_available(cuda_only=True))


from tensorflow.python.client import device_lib

def get_available_devices():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]

print(get_available_devices())

