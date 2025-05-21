# Only export prompts for usage
__all__ = ['GENERATE_A_BLOCKED_PATH_MESSAGE_PROMPT', 'GENERATE_A_CONTEXTUAL_HINT_PROMPT', 'GENERATE_FOREST_LOCATION_PROMPT', 'GENERATE_A_NEW_ITEM_PROMPT'];

def readFile(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            return content;
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")

GENERATE_FOREST_LOCATIONS_PROMPT = readFile("./prompts/GENERATE_FOREST_LOCATIONS.txt")
GENERATE_FOREST_ITEMS_PROMPT = readFile("./prompts/GENERATE_FOREST_ITEMS.txt")
GENERATE_FOREST_HINTS_PROMPT = readFile("./prompts/GENERATE_FOREST_HINTS.txt")
GENERATE_FOREST_BLOCKED_PATHS_PROMPT = readFile("./prompts/GENERATE_FOREST_BLOCKED_PATHS.txt")
