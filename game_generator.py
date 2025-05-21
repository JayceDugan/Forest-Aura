from pydantic import BaseModel, Field
from prompts import GENERATE_FOREST_LOCATIONS_PROMPT, GENERATE_FOREST_ITEMS_PROMPT, GENERATE_FOREST_HINTS_PROMPT, GENERATE_FOREST_BLOCKED_PATHS_PROMPT
from openai import OpenAI

client = OpenAI()
model="gpt-4o-mini"

class LocationsResponse(BaseModel):
    locations: list[str] = Field(..., min_items=10, max_items=10)

def generateLocations():
    print("Generating locations...")

    locations = client.responses.parse(
        model=model,
        input=[
            { "role": "system", "content": GENERATE_FOREST_LOCATIONS_PROMPT }
        ],
        text_format=LocationsResponse
    )

    return locations.output_parsed.locations

class ItemsResponse(BaseModel):
    items: list[str] = Field(..., min_items=10, max_items=10)
    itemLocations: list[int] = Field(..., min_items=10, max_items=10)

def generateItems():
    print("Generating items...")

    languageModelResponse = client.responses.parse(
        model=model,
        input=[
            { "role": "system", "content": GENERATE_FOREST_ITEMS_PROMPT }
        ],
        text_format=ItemsResponse
    )

    return languageModelResponse.output_parsed.items, languageModelResponse.output_parsed.itemLocations;

class HintsResponse(BaseModel):
    hints: list[str] = Field(..., min_items=10, max_items=10)

def generateHints():
    print("Generating hints...")

    languageModelResponse = client.responses.parse(
        model=model,
        input=[
            { "role": "system", "content": GENERATE_FOREST_HINTS_PROMPT }
        ],
        text_format=HintsResponse
    )

    return languageModelResponse.output_parsed.hints;

class BlockedPathsResponse(BaseModel):
    blockedPathMessages: list[str] = Field(..., min_items=10, max_items=10)

def generateBlockedPaths():
    print("Generating blocked paths...")

    languageModelResponse = client.responses.parse(
        model=model,
        input=[
            { "role": "system", "content": GENERATE_FOREST_BLOCKED_PATHS_PROMPT }
        ],
        text_format=BlockedPathsResponse
    )

    return languageModelResponse.output_parsed.blockedPathMessages