from template_dl_tutorial import logger
from template_dl_tutorial.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from template_dl_tutorial.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from template_dl_tutorial.pipeline.stage_03_model_training import TrainModelPipeline
from template_dl_tutorial.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

logger.info("welcome to the template_dl_tutorial package!")

STAGE_NAME = "Data Ingestion stage"

try:
	logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
	obj = DataIngestionTrainingPipeline()
	obj.main()
	logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
	logger.exception(f"stage {STAGE_NAME} failed with exception {e}")
	raise e



STAGE_NAME = "Prepare base model stage"

try:
	logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
	obj = PrepareBaseModelPipeline()
	obj.main()
	logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
	logger.exception(f"stage {STAGE_NAME} failed with exception {e}")
	raise e


STAGE_NAME = "Train model stage"

try:
	logger.info(f"*******************************************")
	logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
	obj = TrainModelPipeline()
	obj.main()
	logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
	logger.exception(f"stage {STAGE_NAME} failed with exception {e}")
	raise e

STAGE_NAME = "Evaluate model stage"

try:
	logger.info(f"*******************************************")
	logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
	obj = ModelEvaluationPipeline()
	obj.main()
	logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
	logger.exception(f"stage {STAGE_NAME} failed with exception {e}")
	raise e