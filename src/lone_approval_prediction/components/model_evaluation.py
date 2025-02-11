import mlflow
import joblib
import pandas as pd
from urllib.parse import urlparse
from lone_approval_prediction import logger
from sklearn.metrics import accuracy_score, precision_score, f1_score

class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def eval_metrics(self, actual, pred):
        try:
            accuracy = accuracy_score(actual, pred)
            precision = precision_score(actual, pred, average='weighted')
            f1 = f1_score(actual, pred, average='weighted')
            return accuracy, precision, f1
        except Exception as e:
            logger.exception(f"Error calculating metrics: {e}")
            return 0, 0, 0

    def log_into_mlflow(self):
        try:
            test_data = pd.read_csv(self.config.x_test_data_path)
            model = joblib.load(self.config.model_path)

            test_x = test_data
            test_y = pd.read_csv(self.config.y_test_data_path)

            # Set the MLflow tracking URI and pass the access token
            mlflow.set_registry_uri(self.config.mlflow_uri)
            mlflow.set_tracking_uri(self.config.mlflow_uri)

            # Ensure the tracking URI is properly set
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            logger.info(f"Tracking URI: {mlflow.get_tracking_uri()}")

            with mlflow.start_run():
                predicted_classes = model.predict(test_x)

                accuracy, precision, f1 = self.eval_metrics(test_y, predicted_classes)
                scores = {"accuracy": accuracy, "precision": precision, "f1": f1}

                mlflow.log_params(self.config.all_params)
                mlflow.log_metrics(scores)

                # Model registry does not work with file store
                if tracking_url_type_store != "file":
                    mlflow.sklearn.log_model(model, "model", registered_model_name="LogisticRegression")
                else:
                    mlflow.sklearn.log_model(model, "model")

                return scores

        except Exception as e:
            raise e
