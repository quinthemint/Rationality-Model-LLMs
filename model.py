import openai
import json

# Load your API key
openai.api_key = "your-api-key"

# List of prompts
prompts = [
    "Why aren't birds real?",
    "Explain the moon landing to a 6-year-old."
]

# Generate responses and save them
dataset = []

for prompt in prompts:
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}], 
        n=10  # Get multiple responses
    )
    
    sampled_answers = [
        {"sampled_string": choice["message"]["content"], "pm_scores": [{"pm_score": None}]} 
        for choice in response["choices"]
    ]
    
    dataset.append({
        "comparison_model": None,  # You can insert a baseline response here
        "rl_prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "comparison_dataset": "Custom",
        "sampled_answers": sampled_answers
    })

# Save dataset to JSON
with open("generated_dataset.json", "w") as f:
    json.dump(dataset, f, indent=4)
