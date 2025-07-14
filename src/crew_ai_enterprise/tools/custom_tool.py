try:
    from crewai_tools import tool
except ImportError:
    try:
        from crewai.tools import tool
    except ImportError as e:
        print(f"Error importing tool: {e}")
        print("Please ensure crewai is installed in the current Python environment")
        print("Try running: pip install crewai")
        import sys
        sys.exit(1)

from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(description="Description of the argument.")

@tool("Name of my tool")
def my_custom_tool(argument: str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    try:
        # Implementation goes here
        # Process the argument and return meaningful output
        processed_result = f"Processed: {argument}"
        return processed_result
    except Exception as e:
        return f"Error processing argument: {str(e)}"

# Class-based approach for compatibility with the crew
class MyCustomTool:
    def __init__(self):
        self.name = "Name of my tool"
        self.description = "Clear description for what this tool is useful for, your agent will need this information to use it."
        self.tool_instance = my_custom_tool
    
    def run(self, argument: str) -> str:
        try:
            processed_result = f"Processed: {argument}"
            return processed_result
        except Exception as e:
            return f"Error processing argument: {str(e)}"

if __name__ == "__main__":
    import sys
    # Test the custom tool
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    
    # Test the decorator-based tool by accessing its run method
    print(f"Tool type: {type(my_custom_tool)}")
    print(f"Tool name: {my_custom_tool.name}")
    test_result = my_custom_tool.run("test argument")
    print(f"Test Result: {test_result}")
    
    # Test the class-based tool
    tool_instance = MyCustomTool()
    print(f"Tool Name: {tool_instance.name}")
    print(f"Tool Description: {tool_instance.description}")
    test_result2 = tool_instance.run("test argument")
    print(f"Test Result 2: {test_result2}")
