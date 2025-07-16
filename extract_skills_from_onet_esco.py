"""
Script to extract and combine skills from O*NET Technology Skills (Excel) and ESCO Skills (CSV) into skills_list.txt.

Instructions:
1. Download O*NET Technology Skills Excel file from:
   https://www.onetcenter.org/dictionary/24.3/excel/Technology%20Skills.xlsx
2. Download ESCO Skills CSV file from:
   https://esco.ec.europa.eu/en/use-esco/download (choose Skills & Competences, English, CSV)
3. Place both files in the same directory as this script, named:
   - Technology_Skills.xlsx
   - ESCO_Skills.csv
4. Run this script:
   python extract_skills_from_onet_esco.py
5. The combined, deduplicated skills will be written to skills_list.txt
"""

import pandas as pd
import csv

# Read O*NET Technology Skills Excel
onet_file = 'Technology_Skills.xlsx'
onet_skills = set()
try:
    df_onet = pd.read_excel(onet_file)
    if 'Example' in df_onet.columns:
        onet_skills = set(df_onet['Example'].dropna().astype(str).str.strip())
    else:
        print('Could not find "Example" column in O*NET file.')
except Exception as e:
    print(f'Error reading O*NET file: {e}')

# # Read ESCO Skills CSV
# esco_file = 'ESCO_Skills.csv'
# esco_skills = set()
# try:
#     with open(esco_file, encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         # Try common column names for skill label
#         for row in reader:
#             label = row.get('preferredLabel') or row.get('Skill/competence') or row.get('label')
#             if label:
#                 esco_skills.add(label.strip())
# except Exception as e:
#     print(f'Error reading ESCO file: {e}')

# Combine and deduplicate
all_skills = sorted(onet_skills )

# Write to skills_list.txt
with open('skills_list.txt', 'w', encoding='utf-8') as f:
    for skill in all_skills:
        f.write(skill + '\n')

print(f'Wrote {len(all_skills)} unique skills to skills_list.txt') 