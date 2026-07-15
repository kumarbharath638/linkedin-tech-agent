from app.llm.base_llm import BaseLLM
from app.prompts.linkedin_prompt import generate_post_prompt


class LinkedInService:
    """
    Business service responsible for LinkedIn content generation.
    """

    def __init__(self, llm: BaseLLM):
        """
        Initialize the LinkedIn service.

        Args:
            llm: An implementation of the BaseLLM contract.
        """
        self.llm = llm
        self.generate_post_prompt=generate_post_prompt

    def generate_post(self, topic: str) -> str:
        """
        Generate a LinkedIn post for the given topic.
        """
        prompt = generate_post_prompt(topic)

        #print(prompt)

        response = self.llm.generate_text(prompt)

        return response

    '''def generate_post(self, topic: str) -> str:
        prompt = generate_post_prompt(topic)

        return self._llm.generate_text(prompt) '''
    
    
    '''def _build_prompt(self, topic: str) -> str:
        """
        Build the prompt to send to the LLM.

        This method is private because prompt construction is an
        internal implementation detail of LinkedInService.
        """
        return (
            f"Write a professional LinkedIn post about "
            f"{topic}."
        )'''