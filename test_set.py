import keras
import os
import numpy as np
import tensorflow as tf

model = keras.models.load_model('models/hai_3')

i = 0
slices = []
for fp in sorted(os.listdir('Test')):
    if fp.startswith('.'):
        continue
    for f in sorted(os.listdir(os.path.join('Test', fp))):
        if f.startswith('.'):
            continue
        with np.load(os.path.join('Test', fp, f)) as data:
            features = data['arr_0']
            label = (i, )
            sl = tf.data.Dataset.from_tensor_slices(
                (tf.expand_dims(tf.convert_to_tensor(features, dtype=tf.float32), axis=0), tf.convert_to_tensor((label, ), dtype=tf.int32)))
            slices.append(sl)
    i += 1

ds = tf.data.Dataset.from_tensor_slices(slices)
ds = ds.interleave(
    lambda x: x, cycle_length=1, num_parallel_calls=tf.data.AUTOTUNE
)
ds = ds.batch(2).shuffle(buffer_size=600)

model.compile(metrics=["accuracy"])
evaluation = model.evaluate(ds, return_dict=True)
print()

for name, value in evaluation.items():
    print(f"{name}: {value:.4f}")