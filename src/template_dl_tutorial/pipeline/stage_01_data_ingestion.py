from template_dl_tutorial.config.configuration import ConfigurationManager
from template_dl_tutorial.components.data_ingestion import DataIngestion
from template_dl_tutorial import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
	def __init__(self):
		pass

	def main(self):
		config = ConfigurationManager()
		data_ingestion_config = config.get_data_ingestion_config()
		data_ingestion = DataIngestion(data_ingestion_config)
		data_ingestion.download_file()
		data_ingestion.extract_zip_file()
		
if __name__ == "__main__":
	try:
		logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
		obj = DataIngestionTrainingPipeline()
		obj.main()
		logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")

	except Exception as e:
		logger.exception(f"stage {STAGE_NAME} failed with exception {e}")
		raise e
