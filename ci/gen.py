import json
import pathlib

THIS_FILE = pathlib.PurePosixPath(
    pathlib.Path(__file__).relative_to(pathlib.Path().resolve())
)
ACTIONS_CHECKOUT = {"name": "Check out repository", "uses": "actions/checkout@v5"}


def gen(content: dict, target: str):
    pathlib.Path(target).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(target).write_text(
        json.dumps(content, indent=2, sort_keys=True), newline="\n"
    )


def gen_dependabot():
    target = ".github/dependabot.yaml"
    content = {
        "version": 2,
        "updates": [
            {
                "package-ecosystem": e,
                "allow": [{"dependency-type": "all"}],
                "directory": "/",
                "schedule": {"interval": "daily"},
            }
            for e in ["github-actions"]
        ],
    }
    gen(content, target)


def gen_rate_workflow():
    target = ".github/workflows/rw-rate-all.yaml"
    content = {
        "env": {
            "description": f"This workflow ({target}) was generated from {THIS_FILE}",
        },
        "name": "Rate all songs on Rainwave",
        "on": {
            "schedule": [{"cron": "0 0 * * *"}],
            "workflow_dispatch": {},
        },
        "jobs": {
            "rate-all": {
                "name": "Rate all songs on Rainwave",
                "runs-on": "ubuntu-latest",
                "steps": [
                    ACTIONS_CHECKOUT,
                    {"name": "Install uv", "run": "sh ci/install-uv.sh"},
                    {
                        "name": "Rate all songs",
                        "run": "uv run rw-rate-all.py 3 ${{ secrets.rainwave_key }} >> $GITHUB_STEP_SUMMARY",
                    },
                ],
            }
        },
    }
    gen(content, target)


def gen_ruff_workflow():
    target = ".github/workflows/ruff.yaml"
    content = {
        "name": "Ruff",
        "on": {
            "pull_request": {"branches": ["master"]},
            "push": {"branches": ["master"]},
        },
        "permissions": {"contents": "read"},
        "env": {
            "description": f"This workflow ({target}) was generated from {THIS_FILE}",
        },
        "jobs": {
            "ruff": {
                "name": "Run ruff linting and formatting checks",
                "runs-on": "ubuntu-latest",
                "steps": [
                    ACTIONS_CHECKOUT,
                    {
                        "name": "Run ruff check",
                        "uses": "astral-sh/ruff-action@v3",
                        "with": {"args": "check --output-format=github"},
                    },
                    {
                        "name": "Run ruff format",
                        "uses": "astral-sh/ruff-action@v3",
                        "with": {"args": "format --check"},
                    },
                ],
            }
        },
    }
    gen(content, target)


def main():
    gen_dependabot()
    gen_rate_workflow()
    gen_ruff_workflow()


if __name__ == "__main__":
    main()
