from flask import Blueprint
from zou.app.utils.api import configure_api_from_blueprint

from .resources import (
    AllProjectsResource,
    OpenProjectsResource,
    ProductionTeamResource,
    ProductionTeamRemoveResource
)

routes = [
    ("/data/projects/open", OpenProjectsResource),
    ("/data/projects/all", AllProjectsResource),

    ("/data/projects/<project_id>/team", ProductionTeamResource),
    ("/data/projects/<project_id>/team/<person_id>", ProductionTeamRemoveResource)
]

blueprint = Blueprint("projects", "projects")
api = configure_api_from_blueprint(blueprint, routes)
