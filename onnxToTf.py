import onnx
from onnx_tf.backend import prepare

# Charger le modèle ONNX
onnx_model = onnx.load("best_model/best.onnx")

# Convertir en modèle TensorFlow
tf_rep = prepare(onnx_model)

# Sauvegarder le modèle TensorFlow
tf_rep.export_graph("model_tf")

