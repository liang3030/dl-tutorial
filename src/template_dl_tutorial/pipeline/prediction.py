import numpy as np
import tensorflow as tf
import os

class PredictionPipeline:
	def __init__(self, file_name):
		self.filename = file_name

	def predict(self):
		# load model
		# because artifacts is not saved in github
		# we need to create a model file and store trained model in it.
		model = tf.keras.models.load_model(os.path.join( "model", "model.h5"))

		imagename = self.filename
		
		test_image = tf.keras.preprocessing.image.load_img(imagename, target_size=(224, 224))
		test_image = tf.keras.preprocessing.image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis=0)
		prediction = np.argmax(model.predict(test_image), axis=1)
		print(prediction)

		if prediction[0] == 1:
			prediction = "Tumor"
			return [{"image": prediction}]
		else:
			prediction = "Normal"
			return [{"image": prediction}]
