# C0D3RZ.AI


## Automating Agile Scrum with Generative AI

This project automates the Agile Scrum process using Generative AI, leveraging Large Language Models (LLMs) to handle key tasks throughout the software development lifecycle. Key tasks such as Feature Spiking, Story Breakdown, Code Evaluation, and Feature Deployment are automated in a seamless pipeline.

By automating these manual workflows, this solution drastically reduces time and effort, improves consistency, and enhances the overall efficiency of the development process. The transition from manual tasks to automated, review-driven processes accelerates development timelines and minimizes human errors, transforming the Agile workflow into a more streamlined and reliable system.

## Why It Matters?

Manual workflows in software development slow down feature delivery, consume significant resources, and increase the risk of human error. Automation is crucial to streamline these processes, improve efficiency, and enable teams to innovate faster. By automating the Agile Scrum process, teams can focus more on value-added tasks rather than repetitive manual work.

## Key Features

- **Automated Feature Spiking**: Automatically generates high-level feature proposals and estimates for better planning.
- **Automated Story Breakdown**: Breaks down complex features into manageable user stories and tasks.
- **Code Evaluation**: Uses AI models to assess and evaluate code quality, suggesting improvements and highlighting issues.
- **Feature Deployment**: Automates deployment tasks to ensure seamless, error-free releases.

## Key Benefits

- **Drastically Reduces Manual Effort**: Automates tasks across planning, development, testing, and deployment stages.
- **Speeds Up Development Timelines**: Reduces delays in development processes, enabling faster feature delivery.
- **Improves Consistency and Quality**: Ensures standardization of tasks and minimizes human errors.
- **Transforms Workflows**: Turns traditional workflows into review-driven processes, increasing collaboration and quality control.

## Tech Stack

### Gen-AI Specific Components:

- **AWS Bedrock**: Provides the foundation for scalable AI applications with fully managed AI and machine learning models.
- **Ollama**: Powers the generative AI capabilities, enabling LLM-based tasks across the development pipeline.
- **Prompt Engineering**: Utilizes fine-tuned AI prompts to maximize task automation effectiveness.

### Web Framework:

- **Flask**: Lightweight web framework to manage API endpoints and automate various processes in the pipeline.

### APIs Leveraged:

- **Confluence REST APIs**: To integrate with Confluence for documentation management.
- **GitHub REST APIs**: For interacting with code repositories, automating pull requests, and managing commits.
- **JIRA REST APIs**: For task management, issue tracking, and user story breakdowns.

### CI/CD Tools:

- **GitHub Actions**: Automates the CI/CD pipeline to deploy code changes efficiently and consistently.

## Getting Started

### Prerequisites

1. Install the following software:
   - Python 3.x
   - Flask
   - AWS CLI
   - GitHub Actions (configured with your repository)

2. Set up the necessary API integrations:
   - Generate API tokens for **Confluence**, **GitHub**, and **JIRA** to enable seamless API interactions.

3. Set up **AWS Bedrock** and **Ollama** credentials for generative AI tasks.

### Installation

Clone the repository:

```bash
git clone [<repository_url>](https://github.com/syedzubeen/C0D3RZ.AI.git)
cd src
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

Set up environment variables for the necessary APIs and tools:

```bash
export CONFLUENCE_API_TOKEN=<your_confluence_api_token>
export GITHUB_API_TOKEN=<your_github_api_token>
export JIRA_API_TOKEN=<your_jira_api_token>
export AWS_BEDROCK_API_KEY=<your_aws_bedrock_api_key>
```

### Running the Application

Start the Flask web server:

```bash
flask run
```

## Usage

1. **Automating Feature Spiking**: Automatically generate feature spikes from high-level requirements by sending a request to the API endpoint.

2. **Story Breakdown**: Break down user stories into smaller tasks by interacting with the JIRA API through the system.

3. **Code Evaluation**: Use the integrated GitHub API to analyze code quality and receive AI-powered recommendations.

4. **Feature Deployment**: Once code changes are evaluated and reviewed, automatically deploy features using GitHub Actions.

## Contributing

We welcome contributions to this project! If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Open a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License.
