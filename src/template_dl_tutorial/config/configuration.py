import os
from template_dl_tutorial.constants import *
from template_dl_tutorial.utils.common import read_yaml, create_directories
from template_dl_tutorial.entity.config_entity import DataIngestionConfig, EvaluationConfig, PrepareBaseModelConfig, TrainingConfig

class ConfigurationManager:
	def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
		self.config = read_yaml(config_filepath)
		self.params = read_yaml(params_filepath)

		create_directories([self.config.artifacts_root])

	def get_data_ingestion_config(self) -> DataIngestionConfig:
		config = self.config.data_ingestion
		create_directories([config.root_dir])
		return DataIngestionConfig(
			root_dir = config.root_dir,
			source_URL = config.source_URL,
			local_data_file = config.local_data_file,
			unzip_dir = config.unzip_dir
		)
	def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
		config = self.config.prepare_base_model
		create_directories([config.root_dir])
		prepare_base_model = PrepareBaseModelConfig(
			root_dir=Path(config.root_dir),
			base_model_path=Path(config.base_model_path),
			updated_base_model_path=Path(config.updated_base_model_path),
			params_image_size=self.params.IMAGE_SIZE,
			params_learning_rate=self.params.LEARNING_RATE,
			params_include_top=self.params.INCLUDE_TOP,
			params_weights=self.params.WEIGHTS,
			params_classes=self.params.CLASSES,
		)
		return prepare_base_model	
	
	def get_training_config(self):
		training = self.config.training
		prepare_base_model = self.config.prepare_base_model
		params = self.params
		training_data = os.path.join(self.config.data_ingestion.unzip_dir, 'kidney-ct-scan-image')
		create_directories([Path(training.root_dir)])

		training_config = TrainingConfig(
			root_dir=Path(training.root_dir),
			trained_model_path=Path(training.trained_model_path),
			updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
			training_data=Path(training_data),
			params_epochs=params.EPOCHS,
			params_batch_size=params.BATCH_SIZE,
			params_is_augmentation=params.AUGMENTATION,
			params_image_size=params.IMAGE_SIZE
		)

		return training_config
	
	def get_evaluation_config(self) -> EvaluationConfig:
		eval_config = EvaluationConfig(
			path_of_model = self.config.training.trained_model_path,
			training_data="artifacts/data_ingestion/kidney-ct-scan-image", # change this with configration file
			mlflow_uri=self.config.mlflow.uri, 
			all_params = self.params,
			params_image_size = self.params.IMAGE_SIZE,
			params_batch_size = self.params.BATCH_SIZE
		)

		return eval_config



