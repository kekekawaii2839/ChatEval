from __future__ import annotations

import re
from typing import Union

from agentverse.parser import OutputParser, LLMResult

from agentverse.utils import AgentAction, AgentFinish

from agentverse.parser import OutputParserError, output_parser_registry


@output_parser_registry.register("llm_eval/single_role/medical_report/base_abnormality")
class LLMEvalParser(OutputParser):
    def parse(self, output: LLMResult) -> Union[AgentAction, AgentFinish]:
        text = output.content
        cleaned_output = text.strip()
        cleaned_output = re.sub(r"\n+", "\n", cleaned_output)
        cleaned_output = cleaned_output.split("\n")

        # TODO chimin modify here

        if cleaned_output[0] != "### Output begin" or cleaned_output[-1] != "### Output end":
            raise OutputParserError(text)

        return AgentFinish({"output": text}, text)
