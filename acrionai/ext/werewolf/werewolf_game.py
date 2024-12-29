from typing import Any, Optional

from acrionai.actions.add_requirement import UserRequirement
from acrionai.context import Context
from acrionai.environment.werewolf.werewolf_env import WerewolfEnv
from acrionai.ext.werewolf.schema import WwMessage
from acrionai.team import Team


class WerewolfGame(Team):
    """Use the "software company paradigm" to hold a werewolf game"""

    env: Optional[WerewolfEnv] = None

    def __init__(self, context: Context = None, **data: Any):
        super(Team, self).__init__(**data)
        ctx = context or Context()
        if not self.env:
            self.env = WerewolfEnv(context=ctx)
        else:
            self.env.context = ctx  # The `env` object is allocated by deserialization

    def run_project(self, idea):
        """Run a project from user instruction."""
        self.idea = idea
        self.env.publish_message(
            WwMessage(role="User", content=idea, cause_by=UserRequirement, restricted_to={"Moderator"})
        )
