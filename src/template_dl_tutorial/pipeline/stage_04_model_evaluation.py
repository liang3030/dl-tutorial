from template_dl_tutorial.components.model_evaluation import Evaluation
from template_dl_tutorial.config.configuration import ConfigurationManager
from template_dl_tutorial import logger


STAGE_NAME = "Evaluate model stage"

class ModelEvaluationPipeline:
	def __init__(self):
		pass

	def main(self):
		config = ConfigurationManager()
		eval_config = config.get_evaluation_config()
		evaluation = Evaluation(eval_config)
		evaluation.evaluation()
		evaluation.save_score()
		# uncomment this when you have to train model. Otherwise it will be commented.
		# evaluation.log_into_mlflow() 
		
if __name__ == "__main__":
	try:
		logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
		obj = ModelEvaluationPipeline()
		obj.main()
		logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")

	except Exception as e:
		logger.exception(f"stage {STAGE_NAME} failed with exception {e}")
		raise e
