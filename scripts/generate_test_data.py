"""
Generate dummy patient report data for testing NSCLC classification pipeline.
Not required for production use.
"""
import pandas as pd

# Create dummy patient text reports for testing
dummy_data = pd.DataFrame({
    "PatientID_Masked": ["P001", "P002", "P003"],
    "Full_Text_Report": [
        """CT scan reveals a suspicious 3.5cm mass in the right upper lobe with mediastinal lymphadenopathy. Biopsy confirms adenocarcinoma. EGFR mutation testing pending.""",
        """Chest X-ray shows patchy infiltrates. No prior history of smoking. Symptoms include cough and mild weight loss. No mass or nodule detected on follow-up imaging.""",
        """Follow-up PET-CT scan indicates metabolic activity in the left lower lobe. Prior scans inconclusive. Further bronchoscopy and histopathology scheduled."""
    ]
})

# Save for reuse
dummy_data.to_excel("./data/dummy_nsclc_reports.xlsx", index=False)
print("Dummy data saved to './data/dummy_nsclc_reports.xlsx'")
