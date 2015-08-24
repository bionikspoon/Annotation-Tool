from .initial_data import InitialData

class AssessedPatientOutcomeLookup(InitialData):
    choices = [
        'Disease Progression',
        'Disease-Control Rate',
        'Disease-Free Survival',
        'Event-Free Survival',
        'Median Survival',
        'Objective Response',
        'Overall Response Rate',
        'Overall Survival',
        'Post-Recurrence Survival',
        'Prognosis',
        'Progression-Free Survival',
        'Remission',
        'Response Rate',
        'Time To Progression',
        'Time To Relapse',
        'Toxicity',
        'Treatment-Related Mortality',
    ]


class DiseaseLookup(InitialData):
    choices = [
        'Adenocarcinoma Of Lung',
        'Carcinoma Of Ampulla Of Vater',
        'Carcinoma Of Colon',
        'Extragastrointestinal Stromal Tumor Of Peritoneum',
        'Glioma',
        'Hashimoto Thyroiditis',
        'Malignant Glioma Of Brain',
        'Malignant Melanoma',
        'Malignant Melanoma Of Conjunctiva',
        'Malignant Tumor Of Thyroid Gland',
        'Metastasis From Malignant Tumor Of Colon',
        'Metastasis From Malignant Tumor Of Rectum',
        'Metastatic Malignant Melanoma',
        'Neoplasm Of Colon',
        'Neoplasm Of Ovary',
        'Neoplastic Disease',
        'Non-Small Cell Lung Cancer',
        'Papillary Thyroid Carcinoma',
        'Primary Adenocarcinoma Of Pancreas',
        'Secondary Malignant Neoplasm Of Brain',
        'Serous Cystadenoma Of Ovary',
    ]


class SignificantPatientOutcomeLookup(InitialData):
    choices = [
        'Disease Progression',
        'Disease-Control Rate',
        'Disease-Free Survival',
        'Event-Free Survival',
        'Median Survival',
        'Objective Response',
        'Overall Response Rate',
        'Overall Survival',
        'Post-Recurrence Survival',
        'Prognosis',
        'Progression-Free Survival',
        'Remission',
        'Response Rate',
        'Time To Progression',
        'Time To Relapse',
        'Toxicity',
    ]


class VariantConsequenceLookup(InitialData):
    choices = [
        'Non Synonymous Missense',
        'Non Synonymous Nonsense',
    ]


class VariantTypeLookup(InitialData):
    choices = [
        'Deletion',
        'Duplication',
        'Indel',
        'Insertion',
        'Substitution',
    ]


