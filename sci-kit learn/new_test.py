from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

## ======== YOUR CODE HERE ======== ##

# 1. Calculate FPR and TPR
fpr, tpr, thresholds = roc_curve(y_val, y_probs)

# 2. Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {auc_score:.2f})')

# 3. Plot the random baseline (diagonal line)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')

## Set appropriate X Label, Y Label and Title for the graph
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.grid(True)

plt.show()  