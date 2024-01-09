from typing import Dict, List, Optional, Sequence, Tuple, Union

from camel.agents import (
    ChatAgent,
    CriticAgent,
    TaskPlannerAgent,
    TaskSpecifyAgent,
)
from camel.generators import SystemMessageGenerator
from camel.human import Human
from camel.messages import BaseMessage
from camel.prompts import TextPrompt
from camel.responses import ChatAgentResponse
from camel.types import ModelType, RoleType, TaskType


class SalesCustomerCoach:
    """A class for the sales customer coach."""

    def __init__(
        self, 
        sales_role_name: str,
        sales_agent_kwargs: Optional[Dict[str, object]] = None,
        customer_role_name: str = "customer",
        customer_agent_kwargs: Optional[Dict[str, object]] = None,
        coach_role_name: str = "coach",
        coach_agent_kwargs: Optional[Dict[str, object]] = None,
        # task_prompt: Optional[str] = None,
        # with_task_specify: bool = False,
        # task_specify_agent_kwargs: Optional[Dict[str, object]] = None,
        # task_planner_agent_kwargs: Optional[Dict] = None,
        # sys_msg_generator_kwargs: Optional[Dict] = None,
        # extend_sys_msg_meta_dicts: Optional[List[Dict]] = None,
        # extend_task_specify_meta_dict: Optional[Dict] = None,
        # output_language: Optional[str] = None,
    ):
        self.model_type = None
        # self.task_type = task_type
        # self.task_prompt = task_prompt
        

        