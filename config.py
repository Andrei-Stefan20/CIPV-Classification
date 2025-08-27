import os

# Path of the main project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for data folders
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')

DATASET = "dataset.json"

# Input file names for training
TRAIN_FILE = 'train.JSON'
VAL_FILE = 'val.JSON'
TEST_FILE = 'test.JSON'

# File path for merged train and test data
TRAIN_MERGED_FILE = "train_merged.json"
VAL_MERGED_FILE = "val_merged.json"
TEST_MERGED_FILE = "test_merged.json"

# Parameters for reproducibility
RANDOM_STATE = 42

# Important columns in the datasets
TEXT_COLUMN = 'conversation'
PERSON_COUPLE_COLUMN = 'person_couple'

# Parameters for dataset splitting
TEST_SIZE = 0.15  # Percentage for test set
VAL_SIZE = 0.15   # Percentage for validation set from the remaining (or total)
RANDOM_STATE = 42 # For reproducibility

# Rules for text cleaning
REMOVE_PUNCTUATION = False
TO_LOWERCASE = False
REMOVE_NUMBERS = False
REMOVE_STOPWORDS = False
