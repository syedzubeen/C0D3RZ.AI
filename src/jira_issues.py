import json
import requests
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from requests.auth import HTTPBasicAuth

# Initialize the Llama model
model = OllamaLLM(model="llama3.2:latest")

# Define the template for the prompt
template = (
    "Generate a summary and description for a Jira ticket based on the following user prompt:\n\n"
    "User Prompt: \"{user_prompt}\"\n\n"
    "Please provide:\n"
    "1. A brief summary (1-2 sentences).\n"
    "2. A detailed description (3-5 sentences) including steps to reproduce, expected outcome, and actual outcome."
)

# Function to generate summary and description
def generate_jira_payload(user_prompt):
    # Create the prompt using the template
    prompt = ChatPromptTemplate.from_template(template).format(user_prompt=user_prompt)
    # Generate the response using the model
    response = model(prompt)
    # Split the response into lines
    lines = response.split("\n")
    summary = lines[0].replace("1. ", "").strip()
    description = "\n".join(lines[1:]).replace("2. ", "").strip()
    return summary, description

# Function to create a Jira ticket
def create_jira_ticket(project_id, summary, description, issue_type_id):
    url = "https://<your_workspace>.atlassian.net/rest/api/2/issue"
    auth = HTTPBasicAuth("Your username goes here...", "Your token goes here...")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "fields": {
            "project": {
                "id": f"{project_id}"
            },
            "summary": summary,
            "description": description,
            "issuetype": {
                "id": f"{issue_type_id}"
            }
        }
    })
    response = requests.post(url, data=payload, headers=headers, auth=auth)
  
    # Print the response from Jira
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
  

if __name__ == "__main__":
    user_prompt = "I need to report a bug in the login feature where users cannot access their accounts after multiple failed attempts."
    project_id = "Replace with your actual project ID"
    issue_type_id = "Replace with your actual issue type ID"
    summary, description = generate_jira_payload(user_prompt)
    create_jira_ticket(project_id, summary, description, issue_type_id)
