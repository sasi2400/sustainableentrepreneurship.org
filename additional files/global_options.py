"""Global options for analysis
"""
import os
from pathlib import Path
from typing import Dict, List, Optional, Set

# Hardware options
N_CORES: int = 8  # max number of CPU cores to use
RAM_CORENLP: str = "27G"  # max RAM allocated for parsing using CoreNLP; increase to speed up parsing
PARSE_CHUNK_SIZE: int = 400 # number of lines in the input file to process uing CoreNLP at once. Increase on workstations with larger RAM (e.g. to 1000 if RAM is 64G)  

# Directory locations
os.environ[
    "CORENLP_HOME"
] = "./stanford-corenlp-full-2018-10-05/"  # location of the CoreNLP models; use / to seperate folders
DATA_FOLDER: str = "data/"
MODEL_FOLDER: str = "models/" # will be created if does not exist
OUTPUT_FOLDER: str = "outputs/" # will be created if does not exist; !!! WARNING: existing files will be removed !!!

# Parsing and analysis options
STOPWORDS: Set[str] = set(
    Path("resources", "StopWords_Generic.txt").read_text().lower().split()
)  # Set of stopwords from https://sraf.nd.edu/textual-analysis/resources/#StopWords
PHRASE_THRESHOLD: int = 10  # threshold of the phraser module (smaller -> more phrases)
PHRASE_MIN_COUNT: int = 10  # min number of times a bigram needs to appear in the corpus to be considered as a phrase
W2V_DIM: int = 300  # dimension of word2vec vectors
W2V_WINDOW: int = 5  # window size in word2vec
W2V_ITER: int = 20  # number of iterations in word2vec
N_WORDS_DIM: int = 500  # max number of words in each dimension of the dictionary
DICT_RESTRICT_VOCAB = None # change to a fraction number (e.g. 0.2) to restrict the dictionary vocab in the top 20% of most frequent vocab

# Inputs for constructing the expanded dictionary
DIMS: List[str] = ["E","S","G"]
SEED_WORDS: Dict[str, List[str]] = {
    "E": [
	'climate_change',
	'green_bonds',
	'fossil_fuel',
	'green_bond',
	'carbon_emission',
	'carbon_footprint',
	'renewable_energy',
	'global_warming',
	'greenhouse_gas',
	'climate_risk',
	'energy_source',
	'green_finance',
	'greenhouse_gas_emissions',
	'carbon_footprint',
	'paris_climate',
	'climate_change_meets',
	'paris_agreement',
	'fuel_companies',
	'fossil_fuel_companies',
	'climate_crisis',
	'natural_gas',
	'environmental_impact',
	'thermal_coal',
	'force_climaterelated_disclosures',
	'green_bond_market',
	'climaterelated_risks',
	'green_energy',
	'low_carbon',
	'oil_gas_companies',
	'environmental_issues',
	'carbon_dioxide',
	'zero_emissions',
	'indispensable_energy',
	'bn_green',
	'carbon_pricing',
	'green_deal',
	'carbon_neutral',
	'fight_climate_change',
	'carbon_price',
	'coal_power',
	'green_bonds',
	'fossil_fuel',
	'tackle_climate',
	'lowcarbon_economy',
	'co_emissions',
	'risks_climate',
	'zero_carbon',
	'green_investment',
	'risks_climate_change',
	'green_credentials',
	'reduce_carbon',
	'action_climate',
	'save_planet',
	'green_debt',
	'greenhouse_gases',
	'coal_projects',
	'away_fossil',
	'climate_accord',
	'carbon_credits',
	'first_green',
	'environmental_standards',
	'un_climate',
	'new_green',
	'netzero_carbon',
	'solar_wind',
	'renewable_energy',
	'global_warming',
	'sustainable_investing',
	'sustainable_investment',
	'sustainable_development'
    ],
    "S": [
	'moral_money',
	'responsible_investing',
	'development_goals',
	'sustainable_development_goals',
	'impact_investment',
	'social_issues',
	'uns_sustainable',
	'social_impact',
	'positive_impact',
	'essential_forward_thinking',
	'gender_diversity',
	'developing_countries',
	'decentralized',
	'defi',
	'democratize',
	'democratization',
	'disintermediation',
	'africa',
	'poor',
	'catching_up',
	'india',
	'mobile',
	'mobility',
	'cell_phone',
	'smart_phone',
	'access',
	'geography',
	'dispersion',
	'microfinance',
	'micro_finance',
	'impact_investing',
	'equality',
	'inequality',
	'care',
	'income',
	'responsible_investment',
	'csr'
    ],   
    "G": [
	'pension_funds',
	'investment_management',
	'supply_chain',
	'task_force',
	'investment_managers',
	'chief_investment_officer',
	'governance_issues',
	'private_sector',
	'hedge_funds',
	'managing_director',
	'shareholder_proposals',
	'due_diligence',
	'stakeholder_capitalism',
	'retail_investors',
	'annual_meetings',
	'esg_disclosure',
	'law_firm',
	'global_advisors',
	'board_members',
	'investors_looking',
	'passive_managers',
	'institutional_investors',
	'advisors',
	'bounty',
	'kyc',
	'whitelist',
	'blockchain',
	'utility',
	'security_token',
	'token_distribution',
	'intermediary',
	'law',
	'regulation',
	'policy',
	'regulator',
	'token_retention',
	'airdrop',
	'founder',
	'partner',
	'compliance',
	'howey_test',
	'sec',
	'equity',
	'venture_capital',
	'vc',
	'incubator'
    ],
}



# Create directories if not exist
Path(DATA_FOLDER, "processed", "parsed").mkdir(parents=True, exist_ok=True)
Path(DATA_FOLDER, "processed", "unigram").mkdir(parents=True, exist_ok=True)
Path(DATA_FOLDER, "processed", "bigram").mkdir(parents=True, exist_ok=True)
Path(DATA_FOLDER, "processed", "trigram").mkdir(parents=True, exist_ok=True)
Path(MODEL_FOLDER, "phrases").mkdir(parents=True, exist_ok=True)
Path(MODEL_FOLDER, "phrases").mkdir(parents=True, exist_ok=True)
Path(MODEL_FOLDER, "w2v").mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER, "dict").mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER, "scores").mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER, "scores", "temp").mkdir(parents=True, exist_ok=True)
Path(OUTPUT_FOLDER, "scores", "word_contributions").mkdir(parents=True, exist_ok=True)
