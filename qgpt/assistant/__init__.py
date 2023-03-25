"""
The assistant package provides classes and functions for managing and interacting
with the GPT-powered chat interface. It includes modules for handling chat context,
completions, memory, settings, and conversation threads.
"""

from .memory import AssistantMemory
from .queue import MessageQueue
from .setting import AssistantPath, AssistantSetting
from .thread import ResponseThread
