#!/usr/bin/env python
# coding=utf-8
"""
Generated Data.
"""

from . import InitialData


class DiseaseLookup(InitialData):
    choices = [

        'Adenocarcinoma Of Lung', 'Carcinoma Of Ampulla Of Vater',
        'Carcinoma Of Colon',
        'Extragastrointestinal Stromal Tumor Of Peritoneum', 'Glioma',
        'Hashimoto Thyroiditis', 'Malignant Glioma Of Brain',
        'Malignant Melanoma', 'Malignant Melanoma Of Conjunctiva',
        'Malignant Tumor Of Thyroid Gland',
        'Metastasis From Malignant Tumor Of Colon',
        'Metastasis From Malignant Tumor Of Rectum',
        'Metastatic Malignant Melanoma', 'Neoplasm Of Colon',
        'Neoplasm Of Ovary', 'Neoplastic Disease', 'Non-Small Cell Lung Cancer',
        'Papillary Thyroid Carcinoma', 'Primary Adenocarcinoma Of Pancreas',
        'Secondary Malignant Neoplasm Of Brain', 'Serous Cystadenoma Of Ovary',

    ]


class PatientOutcomesLookup(InitialData):
    choices = [

        'Disease Progression', 'Disease-Control Rate', 'Disease-Free Survival',
        'Event-Free Survival', 'Median Survival', 'Objective Response',
        'Overall Response Rate', 'Overall Survival', 'Post-Recurrence Survival',
        'Prognosis', 'Progression-Free Survival', 'Remission', 'Response Rate',
        'Time To Progression', 'Time To Relapse', 'Toxicity',

    ]


class TreatmentLookup(InitialData):
    choices = [

        '5-Fluorouracil', '5-FuLv', 'And Irinotecan', 'And Mitomycin',
        'Bevacizumab', 'Calgb 89803', 'Capecitabine',
        'Capecitabine Irinotecan Or Oxaliplatin Plus Cetuximab',
        'Capecitabine Or 5-Fluorouracil (5- Fu) Oxaliplatin', 'Carboplatin',
        'Cetuximab', 'Cetuximab Plus Chemotherapy',
        'Cetuximab With Irinotecan And', 'Cyclophosphamide', 'Dabrafenib',
        'Dabrafenib Or Dacarbazine', 'Dacarbazine',
        'Dacarbazine Cisplatin Vinblastine And Tamoxifen',
        'Docetaxel Erlotinib Or Temsirolimus', 'Fluoropirimidins',
        'Fluorouracil', 'Folfiri', 'Folfox', 'Folinic Acid', 'Fu And Lv (Ifl)',
        'FuIrinotecan', 'FuOxaliplatin', 'Imatinib', 'Ipilimumab', 'Irinotecan',
        'Irinotecan (Cpt11)', 'Irinotecan With Fluorouracil (Fu)Leucovorin',
        'Leucovorin', 'Leucovorin (FuLv)', 'Or Cetuximab',
        'Or Irinotecan And Bevacizumab', 'Oxaliplatin', 'Paclitaxel',
        'Panitumumab', 'Panitumumab And Cetuximab', 'Plx4032',
        'Radioactive Iodine Therapy', 'Radioiodine', 'Radiotherapy',
        'Selumetinib', 'Selumetinib In Combination With Dacarbazine',
        'Standard Chemotherapy', 'Standard First Line Chemo Therapy',
        'Surgical And Chemotherapy', 'Systemic Chemotherapy', 'Temozolomide',
        'Thyroidectomy', 'Trametinib', 'Vemurafenib',
        'With Interleukin 2 And Ifnα-2B',

    ]


class VariantConsequenceLookup(InitialData):
    choices = [

        'Non Synonymous Missense', 'Non Synonymous Nonsense',

    ]


class VariantTypeLookup(InitialData):
    choices = [

        'Deletion', 'Duplication', 'Indel', 'Insertion', 'Substitution',

    ]
