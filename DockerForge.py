import streamlit as st

# Initialize the Dockerfile content
dockerfile_content = []

st.title("Dockerfile Generator")

# Base Image
st.header("Step 1: Base Image Selection")
base_image = st.selectbox(
    "Choose a base image", ["ubuntu", "alpine", "python", "node", "ruby"]
)
base_version = st.text_input("Base Image Version (e.g., latest, 3.8)", "latest")
dockerfile_content.append(f"FROM {base_image}:{base_version}")

# System Dependencies
st.header("Step 2: System Dependencies")
sys_dependencies = st.multiselect(
    "Select common system packages", ["git", "curl", "vim", "wget", "build-essential"]
)
custom_sys_dependencies = st.text_input(
    "Additional system packages (comma-separated)", ""
)
if sys_dependencies or custom_sys_dependencies:
    dockerfile_content.append(
        f"RUN apt-get update && apt-get install -y {' '.join(sys_dependencies + custom_sys_dependencies.split(','))}"
    )

# Programming Language & Dependencies
st.header("Step 3: Programming Language & Dependencies")
language = st.radio("Choose a programming language", ["Python", "Node.js", "Ruby"])
version = st.text_input(f"{language} Version", "latest")
if language:
    if language == "Python":
        dockerfile_content.append(f"RUN apt-get install -y python{version} python3-pip")
        dependency_file = st.file_uploader(
            "Upload Python requirements.txt", type=["txt"]
        )
        if dependency_file:
            dockerfile_content.append("COPY requirements.txt .")
            dockerfile_content.append("RUN pip install -r requirements.txt")
    elif language == "Node.js":
        dockerfile_content.append("RUN apt-get install -y nodejs npm")
        dependency_file = st.file_uploader("Upload Node.js package.json", type=["json"])
        if dependency_file:
            dockerfile_content.append("COPY package.json .")
            dockerfile_content.append("RUN npm install")

# Environment Variables
st.header("Step 4: Environment Variables")
env_vars = st.text_area("Add environment variables (KEY=VALUE, one per line)")
if env_vars:
    for line in env_vars.split("\n"):
        if "=" in line:
            dockerfile_content.append(f"ENV {line.strip()}")

# Working Directory & File Management
st.header("Step 5: Working Directory & File Management")
work_dir = st.text_input("Working directory", "/app")
dockerfile_content.append(f"WORKDIR {work_dir}")

uploaded_files = st.file_uploader("Upload files to copy", accept_multiple_files=True)
if uploaded_files:
    dockerfile_content.append("COPY . /app")

# Commands & Entrypoint
st.header("Step 6: Commands & Entrypoint")
build_commands = st.text_area(
    "Commands to run during build (one per line)", "RUN echo 'Build complete'"
)
entrypoint = st.text_input("Entrypoint command", "")
cmd = st.text_input("Default command (CMD)", "")
if build_commands:
    dockerfile_content.extend(
        [f"{cmd.strip()}" for cmd in build_commands.split("\n") if cmd.strip()]
    )
if entrypoint:
    dockerfile_content.append(f"ENTRYPOINT {entrypoint}")
if cmd:
    dockerfile_content.append(f"CMD {cmd}")

# Dockerfile Preview & Download
st.header("Dockerfile Preview")
dockerfile_preview = "\n".join(dockerfile_content)
st.text_area("Dockerfile Content", dockerfile_preview, height=400)

st.download_button("Download Dockerfile", dockerfile_preview, file_name="Dockerfile")
