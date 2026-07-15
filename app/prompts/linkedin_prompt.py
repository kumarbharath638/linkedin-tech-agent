def generate_post_prompt(topic: str) -> str:
    """
    Create a prompt for generating a LinkedIn post.

    Args:
        topic: Technology topic for the LinkedIn post.

    Returns:
        Formatted prompt string.
    """
    return f"""
You are an experienced technology content writer.

Write a professional LinkedIn post about "{topic}".

The post should:
- Be informative and engaging.
- Be suitable for software and data professionals.
- Explain the topic clearly.
- End with a thought-provoking question.
"""