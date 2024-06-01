from template_dl_tutorial.components.model_training import Training
from template_dl_tutorial.config.configuration import ConfigurationManager
from template_dl_tutorial import logger

STAGE_NAME = "Train model stage"

class TrainModelPipeline:
	def __init__(self):
		pass

	def main(self):
		config = ConfigurationManager()
		training_config = config.get_training_config()
		training = Training(config = training_config)
		training.get_base_model()
		training.train_valid_generator()
		training.train()
		
if __name__ == "__main__":
	try:
		logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
		obj = TrainModelPipeline()
		obj.main()
		logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")

	except Exception as e:
		logger.exception(f"stage {STAGE_NAME} failed with exception {e}")
		raise e
