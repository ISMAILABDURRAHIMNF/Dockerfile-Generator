from openai import OpenAI

client = OpenAI()

def generate_dockerfile(choice, version):
    print(f"\n\nGenerating Dockerfile for {choice} using {version} project...")
    project_description = f"{choice} project with {version} version"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful dockerfile generator"},
            {"role": "user", "content": f"Create Dockerfile content for a {project_description}, use latest technology, create a Dockerfile content without any explanation"},
        ]
    )

    dockerfile_content = completion.choices[0].message.content
    print("\n\n=== Dockerfile generated successfully ===\n\n")
    print(dockerfile_content)

    return dockerfile_content