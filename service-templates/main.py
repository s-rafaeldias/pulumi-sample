import jinja2
import json
from pathlib import Path
import typer

from pydantic import BaseModel

app = typer.Typer()


class DockerfileConfig(BaseModel):
    pre_install_commands: list[str]


class BuildConfig(BaseModel):
    name: str
    service_type: str
    dockerfile: DockerfileConfig


def build_dockerfile(build_config: BuildConfig):
    with open("./templates/Dockerfile", "r") as f:
        dockerfile_template = f.read()

    env = jinja2.Environment()
    template = env.from_string(dockerfile_template)
    out = template.render(build_config.dict())
    with open("output/Dockerfile", "w") as f:
        f.write(out)


def main(config: str):
    config_path = Path(config)

    with open(config_path, "r") as f:
        contents = json.load(f)

    build_config = BuildConfig(**contents)
    build_dockerfile(build_config)


if __name__ == "__main__":
    typer.run(main)
