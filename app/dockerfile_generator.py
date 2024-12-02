from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_dockerfile(language, desc):
    print(f"\n\nGenerating Dockerfile for {language} using {desc} project...")
    project_description = f"{language} project with {desc} desc"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful dockerfile generator"},
            {"role": "user", "content": f"Create the simplest Dockerfile content for a {project_description}, use latest technology, use COPY . syntax, create a Dockerfile content without any explanation"},
        ]
    )

    dockerfile_content = completion.choices[0].message.content.replace("```","#")
    print("\n\n=== Dockerfile generated successfully ===\n\n")
    print(dockerfile_content)

    return dockerfile_content