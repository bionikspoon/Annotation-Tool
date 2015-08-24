from pubmed.db import InitialData


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


