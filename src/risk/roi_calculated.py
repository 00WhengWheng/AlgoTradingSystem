import matplotlib.pyplot as plt
from typing import Dict, List
import numpy as np

class SophisticatedROI:
    def __init__(self):
        self.records = []  # Store historical ROI calculations

    def calculate_roi(self, revenue: float, costs: Dict[str, float]) -> float:
        """Calculate ROI based on revenue and a detailed cost breakdown."""
        total_costs = sum(costs.values())
        roi = ((revenue - total_costs) / total_costs) * 100 if total_costs != 0 else float('inf')
        print(f"Revenue: {revenue}, Costs: {costs}, ROI: {roi:.2f}%")
        return roi

    def calculate_aggregate_roi(self, revenues: List[float], costs_list: List[Dict[str, float]]) -> Dict[str, float]:
        """Calculate aggregate ROI for multiple data points."""
        total_revenue = sum(revenues)
        total_costs = sum([sum(costs.values()) for costs in costs_list])
        aggregate_roi = self.calculate_roi(total_revenue, {"total": total_costs})
        
        # Individual ROIs
        individual_rois = [
            self.calculate_roi(rev, costs) for rev, costs in zip(revenues, costs_list)
        ]
        mean_roi = np.mean(individual_rois)
        
        return {
            "aggregate_roi": aggregate_roi,
            "mean_roi": mean_roi,
            "total_revenue": total_revenue,
            "total_costs": total_costs,
            "individual_rois": individual_rois
        }

    def visualize_roi(self, individual_rois: List[float], revenues: List[float], costs_list: List[Dict[str, float]]):
        """Visualize ROI metrics using bar charts."""
        x_labels = [f"Item {i+1}" for i in range(len(individual_rois))]
        total_costs = [sum(costs.values()) for costs in costs_list]

        # Plotting
        plt.figure(figsize=(12, 6))

        plt.bar(x_labels, revenues, alpha=0.6, label="Revenues", width=0.4, align='edge')
        plt.bar(x_labels, total_costs, alpha=0.6, label="Costs", width=-0.4, align='edge')
        plt.plot(x_labels, individual_rois, marker='o', color='r', label="ROI (%)", linewidth=2)

        plt.title("ROI Metrics Visualization")
        plt.xlabel("Data Items")
        plt.ylabel("Values")
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()

        # Save and show
        plt.savefig("roi_metrics_visualization.png")
        print("ROI metrics visualization saved as 'roi_metrics_visualization.png'")
        plt.show()
