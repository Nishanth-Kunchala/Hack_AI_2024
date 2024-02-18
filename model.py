import tensorflow as tf
import numpy as np
import keras
from keras import layers
from keras.src.optimizers import Adam
from sklearn.model_selection import train_test_split
import os

im_width = 124
im_height = 62

i = 0
slices = []
for fp in sorted(os.listdir('Stacks2')):
    if fp.startswith('.'):
        continue
    for f in sorted(os.listdir(os.path.join('Stacks2', fp))):
        if f.startswith('.'):
            continue
        with np.load(os.path.join('Stacks2', fp, f)) as data:
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

batch_size = 2
ds = ds.batch(batch_size)
ds = ds.shuffle(buffer_size=800)

inputs = layers.Input(shape=(im_height, im_width, 61, 1))

x = layers.Conv3D(filters=32, kernel_size=3, activation='relu')(inputs)
x = layers.MaxPool3D(pool_size=2)(x)
x = layers.BatchNormalization()(x)

x = layers.Conv3D(filters=64, kernel_size=3, activation='relu')(x)
x = layers.MaxPool3D(pool_size=2)(x)
x = layers.BatchNormalization()(x)

x = layers.Conv3D(filters=128, kernel_size=3, activation='relu')(x)
x = layers.MaxPool3D(pool_size=2)(x)
x = layers.BatchNormalization()(x)

x = layers.Conv3D(filters=128, kernel_size=3, activation='relu')(x)
x = layers.MaxPool3D(pool_size=2)(x)
x = layers.BatchNormalization()(x)

x = layers.GlobalAveragePooling3D()(x)
x = layers.Dense(units=256, activation='relu')(x)
#x = layers.Dropout(0.2)(x)

outputs = layers.Dense(units=4, activation='sigmoid')(x)

model = keras.Model(inputs, outputs)
model.summary()

model.compile(optimizer=Adam(learning_rate=.01), loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])
history = model.fit(ds, epochs=10, class_weight={0: 2.35, 1: 3.011, 2: 0.48, 3: 0.86})
model.save('models/hai_3')

