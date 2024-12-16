import json
import requests
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from requests.auth import HTTPBasicAuth

# Initialize the Llama model
model = OllamaLLM(model="llama3.2:latest")

# Define the model and API token
API_TOKEN = "Replace with your actual API token"
USERNAME = "Replace with your actual username"

# Function to create a Confluence page
def create_confluence_page(title, description, body, image_url):
    url = "https://<name_of_your_workspace>.atlassian.net/wiki/api/v2/pages"
    auth = HTTPBasicAuth(USERNAME, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Prepare the body with image URL
    confluence_body = f"<h2>{description}</h2><p>{body}</p><img src='{image_url}' alt='Diagram'/>"

    payload = json.dumps({
        "spaceId": "1507360",  # Replace with your actual space ID
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": confluence_body
        }
    })

    response = requests.post(url, data=payload, headers=headers, auth=auth)

    print(json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": ")))

# Function to parse the generated response
def parse_response(response):
    # Assuming response is formatted correctly; adjust as necessary
    lines = response.splitlines()
    title = lines[0].strip()
    description = lines[1].strip()
    body = "\n".join(lines[2:]).strip()
    image_suggestion = "https://example.com/image.png"
    return title, description, body, image_suggestion

# Function to generate content using the LLM
def generate_content(user_prompt):
    # Define the template for the prompt
    template = (
        "You are a senior software architect at a technology company. You have just received a feature request for [insert feature request here]. Your task is to perform a detailed spike on this request, considering its technical feasibility, architectural impact, and potential risks. You will evaluate the following aspects:"
        "High-Level Overview : Provide a summary of the feature and its business value."
        "Current System Architecture: Describe how the current system is structured and how this new feature might integrate or impact it."
        "Technical Considerations: Analyze the potential technical challenges, dependencies, and possible solutions or approaches for implementing this feature."
        "Impact on Performance, Scalability, and Security: Assess how this feature might affect the system's performance, scalability, and security."
        "Risks and Mitigations: List potential risks and any mitigation strategies."
        "Time and Resource Estimation: Estimate the time and resources required to complete this feature, including any specific team expertise."
        "Next Steps: Outline the next steps for moving forward with this feature, including any follow-up research, design decisions, or team discussions."
        "Finally, document your analysis and conclusions in the format of a Confluence page, using appropriate headers and sections to structure the information clearly."
    )

    prompt = ChatPromptTemplate.from_template(template).format(user_prompt=user_prompt)

    # Generate the response using the model
    response = model(prompt)

    return response

# Main workflow
user_prompt = "Create a technical spike doc for an app that tracks health metrics for a person"
response = generate_content(user_prompt)

# Parse the generated content
title, description, body, image_suggestion = parse_response(response)

# Create the Confluence page
create_confluence_page(title, description, body, image_suggestion)
