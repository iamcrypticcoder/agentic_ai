import subprocess
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


def run_shell(command: str):
    """Run a shell command on the local machine"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {"stdout": result.stdout, "stderr": result.stderr}

git_agent = Agent(
    name="git_agent",
    model=LiteLlm(
        api_base="http://localhost:11434/v1",
        model="openai/ministral-3",
        api_key="ollama"
    ),
    description="""
        A simple agent that is capable to run git commands.
    """,
    instruction="""
    1. You are a helpful assistant who can perform git and perforce version control tasks.
    You will find a commit in GIT repo and then apply the change in perforce repo.
    Folder structure of GIT repo and perforce repo is similar.
    Your GIT repository directory is: `/home/mahbub/MERLOT/WearServices`
    You Perforce repository directory is : `/home/mahbub/PERFORCE/MAHBUB_KR_UBUNTU_TEMPLATE_D4_FRESH9US_USA_OPEN_WATCH_C/android/vendor/google_clockwork_partners/packages/WearServices`
    
    2. You will run any shell commands by the tool `run_shell`.
    You will be able to run only these git commands: `git status`, `git fetch`, `git pull`, `git show [COMMIT_ID]`
    
    3. When analyzing diff in a commit omit all test files ending "Test.java".
    User prompt will provide you a commit of Git repo and you will apply the change in perforce repo.
    """,
    tools=[run_shell]
)
