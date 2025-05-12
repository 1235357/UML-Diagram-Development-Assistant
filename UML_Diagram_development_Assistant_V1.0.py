"""
# UML-Diagram-Development-Assistant

- CPS 3962: Object Orientated Analysis and Design (OOAD) Project's repository
  - Instructor: Dr. Hamza Djigal
  - Project Name: Develop a Conversational OOAD Assistant Leveraging Large Language Models
  - Project Members: Zhentong Ye (zye@kean.edu) & Yanwu Lang (langy@kean.edu)
"""

import sys
import os
import re
import time
import json
import uuid
import datetime as dt
import requests
import streamlit as st
from io import StringIO
from time import perf_counter_ns
import getopt



# Try to import optional packages with clear availability flags
try:
    import replicate
    REPLICATE_MODEL_AVAILABLE = True
except ImportError:
    REPLICATE_MODEL_AVAILABLE = False

try:
    import openai
    OPENAI_MODEL_AVAILABLE = True
except ImportError:
    OPENAI_MODEL_AVAILABLE = False

try:
    from llama_cpp import Llama
    LLAMA_CPP_MODEL_AVAILABLE = True
except ImportError:
    LLAMA_CPP_MODEL_AVAILABLE = False

try:
    from plantweb.render import render, render_file
    PLANTWEB_RENDERER_AVAILABLE = True
except ImportError:
    PLANTWEB_RENDERER_AVAILABLE = False

# Application Constants with Descriptive Names
APPLICATION_TITLE = "UML Diagram Development Assistant"
APPLICATION_VERSION = "v0.9"
SESSION_KEY_APPLICATION_INSTANCE = "CMI"
SESSION_KEY_CONVERSATION_MESSAGES = "messages"
SESSION_KEY_USER_PROMPT = "prompt/message"
SESSION_KEY_PROMPT_PREPEND_TEXT = "prompt/message/prepend"
SESSION_KEY_PROMPT_APPEND_TEXT = "prompt/message/append"
SESSION_KEY_INTERPRETER_INPUT = "int/input"
SESSION_KEY_APPLICATION_CONFIG = "configuration"

# Message Role Constants
MESSAGE_ROLE_KEY = "role"
MESSAGE_ROLE_ASSISTANT = "assistant"
MESSAGE_ROLE_USER = "user"
MESSAGE_ROLE_INTERPRETER = "interpreter"

# Message Content and Format Constants
MESSAGE_CONTENT_KEY = "message"
MESSAGE_SOURCE_KEY = "source"
MESSAGE_FORMAT_KEY = "format"
MESSAGE_FORMAT_INITIALIZATION = "in"
MESSAGE_FORMAT_USER_PROMPT = "pr"
MESSAGE_FORMAT_LLM_RESPONSE = "re/llm"
MESSAGE_FORMAT_LLM_TEXT = "re/llm/txt"
MESSAGE_FORMAT_LLM_CODE = "re/llm/code"
MESSAGE_FORMAT_INTERPRETER_RESPONSE = "re/int"
MESSAGE_FORMAT_INTERPRETER_TEXT = "re/int/txt"
MESSAGE_FORMAT_INTERPRETER_IMAGE = "re/int/img"
MESSAGE_ACTION_RERUN_LLM = "rerun/llm"
MESSAGE_ACTION_RERUN_INTERPRETER = "rerun/int"

# Default welcome message
WELCOME_MESSAGE = "How may I assist you today?"

# Avatar Icons for Different Roles
AVATAR_KEY = "avatar"
AVATAR_ASSISTANT_ICON = "🤖"  # Robot for assistant
AVATAR_USER_ICON = "👤"       # User icon for user
AVATAR_INTERPRETER_ICON = "🔄"  # Processing symbol for interpreter

# AI Model API Provider Names
API_PROVIDER_OPENAI = "OpenAI"
API_PROVIDER_REPLICATE = "Replicate"
API_PROVIDER_OLLAMA = "Ollama"
API_PROVIDER_BIGMODEL = "BigModel"  # API for GLM-4

# Selection Placeholders
MODEL_SELECTION_PLACEHOLDER = '<Select Model>'
INTERPRETER_SELECTION_PLACEHOLDER = '<Select Interpreter>'

# Interpreter Types and Options
INTERPRETER_PLANTWEB = "Plantweb"
INTERPRETER_PLANTWEB_PLANTUML = INTERPRETER_PLANTWEB + "/PlantUML"
INTERPRETER_PLANTWEB_GRAPHVIZ = INTERPRETER_PLANTWEB + "/Graphviz"

# Interpreter Default Parameters
INTERPRETER_DEFAULT_PARAMETERS = {
    INTERPRETER_PLANTWEB_PLANTUML: {
        'Output format': ['SVG', 'PNG'],
        'Use cache': False
    },
    INTERPRETER_PLANTWEB_GRAPHVIZ: {
        'Output format': ['SVG', 'PNG'],
        'Use cache': False
    },
    # Can add more interpreter options here
}

# Default API Configuration
DEFAULT_API_CONFIGURATION = {
    "api_key": {
        "value": "4c9d90ddb8a94dd79000782640b44cac.SfvIXEzfL0UaU7E5",
        "description": "Interface key, obtained from the interface platform, must be set correctly when using the online interface."
    },
    "base_url": {
        "value": "https://open.bigmodel.cn/api/paas/v4/",
        "description": "Request address, obtained from the interface platform, must be set correctly when using the online interface."
    },
    "model_name": {
        "value": "glm-4-plus",
        "description": "Model name, obtained from the interface platform, must be set correctly when using the online interface."
    }
}



# Message Format Constants
MESSAGE_FORMAT_INITIAL = "in"
MESSAGE_FORMAT_PROMPT = "pr"
MESSAGE_FORMAT_RESPONSE_LANGUAGE_MODEL = "re/llm"
MESSAGE_FORMAT_RESPONSE_LANGUAGE_MODEL_TEXT = "re/llm/txt"
MESSAGE_FORMAT_RESPONSE_LANGUAGE_MODEL_CODE = "re/llm/code"
MESSAGE_FORMAT_RESPONSE_INTERPRETER = "re/int"
MESSAGE_FORMAT_RESPONSE_INTERPRETER_TEXT = "re/int/txt"
MESSAGE_FORMAT_RESPONSE_INTERPRETER_IMAGE = "re/int/img"
INITIAL_MESSAGE = WELCOME_MESSAGE
ROLE_US = MESSAGE_ROLE_USER
ROLE_AS = MESSAGE_ROLE_ASSISTANT
ROLE_IN = MESSAGE_ROLE_INTERPRETER
MSG = MESSAGE_CONTENT_KEY
MSG_FORMAT = MESSAGE_FORMAT_KEY
SRC = MESSAGE_SOURCE_KEY
MSG_FORMAT_INIT = MESSAGE_FORMAT_INITIAL
MSG_FORMAT_RESPONSE_LLM = MESSAGE_FORMAT_RESPONSE_LANGUAGE_MODEL
MSG_FORMAT_RESPONSE_LLM_TXT = MESSAGE_FORMAT_RESPONSE_LANGUAGE_MODEL_TEXT
MSG_FORMAT_RESPONSE_INT = MESSAGE_FORMAT_RESPONSE_INTERPRETER
MSG_FORMAT_RESPONSE_INT_TXT = MESSAGE_FORMAT_RESPONSE_INTERPRETER_TEXT
MSG_FORMAT_RESPONSE_INT_IMG = MESSAGE_FORMAT_RESPONSE_INTERPRETER_IMAGE
AVATAR_ASSIST = AVATAR_ASSISTANT_ICON
INT_PLANTWEB_PLANTUML = INTERPRETER_PLANTWEB_PLANTUML



# Library availability flags
REPLICATE_LIBRARY_AVAILABLE = False
OPENAI_LIBRARY_AVAILABLE = False
LLAMA_CPP_LIBRARY_AVAILABLE = False
PLANTWEB_AVAILABLE = False

# Try to import optional libraries and update flags
try:
    import replicate
    REPLICATE_LIBRARY_AVAILABLE = True
except ImportError:
    pass

try:
    import openai
    OPENAI_LIBRARY_AVAILABLE = True
except ImportError:
    pass

try:
    from plantweb.render import render, render_file
    PLANTWEB_AVAILABLE = True
except ImportError:
    pass

# Legacy constants for backward compatibility
ROLE = "role"
AVATAR = "avatar"
AVATAR_USER = AVATAR_USER_ICON
AVATAR_INTER = AVATAR_INTERPRETER_ICON
AVATAR_ASSIST = AVATAR_ASSISTANT_ICON

# Session state keys
SESSION_KEY_USER_PROMPT_PERPEND = "prompt/message/prepend"
SESSION_KEY_USER_PROMPT_APPEND = "prompt/message/append"

# Message format aliases
MSG_FORMAT_INIT = MESSAGE_FORMAT_INITIAL
MSG_FORMAT_PROMPT = MESSAGE_FORMAT_PROMPT


class ProjectionManager:
    """
    Manages different projection views for UML diagrams.

    Projections allow users to focus on specific aspects of a UML diagram
    by filtering or highlighting elements based on different criteria.
    """

    def __init__(self):
        print("Initializing Projection Manager...")
        self.available_projections = {
            "Full Diagram": "Complete diagram with all elements and details",
            "Core Classes Only": "Main classes without implementation details",
            "Inheritance Hierarchy": "Focus on class inheritance relationships",
            "Associations Only": "Focus on associations between classes",
            "Interface Implementations": "Classes and their implemented interfaces",
            "Simplified View": "Classes with minimal details for overview"
        }
        self.current_projection = "Full Diagram"

    def apply_projection(self, diagram_code, projection_name):
        """Apply the selected projection to the diagram code"""
        if projection_name == "Full Diagram":
            return diagram_code

        # Parse the PlantUML code
        lines = diagram_code.split('\n')
        result_lines = []
        class_blocks = {}
        relationships = []
        current_class = None
        in_class_def = False

        # First pass - identify elements
        for line in lines:
            stripped = line.strip()

            # Keep PlantUML directives
            if stripped.startswith('@startuml') or stripped.startswith('@enduml'):
                continue

            # Track class definitions
            if stripped.startswith('class ') or stripped.startswith('interface '):
                parts = stripped.split(' ', 2)
                if len(parts) > 1:
                    class_name = parts[1].split('{')[0].strip()
                    current_class = class_name
                    class_blocks[current_class] = []
                    in_class_def = '{' in stripped

            # Add line to current class block
            if in_class_def and current_class:
                class_blocks[current_class].append(line)
                if '}' in stripped:
                    in_class_def = False

            # Track relationships
            elif '-->' in stripped or '<--' in stripped or '--|>' in stripped or '<|--' in stripped or '--' in stripped:
                relationships.append(line)

        # Apply specific projection filters
        if projection_name == "Core Classes Only":
            return self._apply_core_classes_projection(diagram_code, class_blocks, relationships)
        elif projection_name == "Inheritance Hierarchy":
            return self._apply_inheritance_projection(diagram_code, class_blocks, relationships)
        elif projection_name == "Associations Only":
            return self._apply_associations_projection(diagram_code, class_blocks, relationships)
        elif projection_name == "Interface Implementations":
            return self._apply_interface_projection(diagram_code, class_blocks, relationships)
        elif projection_name == "Simplified View":
            return self._apply_simplified_projection(diagram_code, class_blocks, relationships)

        # Default - return original
        return diagram_code

    def _apply_core_classes_projection(self, original_code, class_blocks, relationships):
        """Filter to show only core classes with minimal details"""
        # Implementation would analyze relationships to identify central classes
        # For now, use a simple approach that keeps all classes but removes details

        result = "@startuml\n"
        result += "\n' Core Classes Projection - Showing main classes without details\n\n"

        for class_name in class_blocks:
            result += f"class {class_name} {{}}\n"

        # Keep all relationships
        for rel in relationships:
            result += f"{rel}\n"

        result += "@enduml"
        return result

    def _apply_inheritance_projection(self, original_code, class_blocks, relationships):
        """Focus on inheritance relationships"""
        result = "@startuml\n"
        result += "\n' Inheritance Hierarchy Projection - Focusing on class inheritance\n\n"

        # Keep all class declarations but simplified
        for class_name in class_blocks:
            result += f"class {class_name} {{}}\n"

        # Filter relationships to keep only inheritance
        for rel in relationships:
            if '--|>' in rel or '<|--' in rel:
                result += f"{rel}\n"

        result += "@enduml"
        return result

    def _apply_associations_projection(self, original_code, class_blocks, relationships):
        """Focus on class associations"""
        result = "@startuml\n"
        result += "\n' Associations Projection - Focusing on relationships between classes\n\n"

        # Keep all class declarations but simplified
        for class_name in class_blocks:
            result += f"class {class_name} {{}}\n"

        # Filter relationships to keep only associations (not inheritance)
        for rel in relationships:
            if '-->' in rel or '<--' in rel or '--' in rel:
                if not ('--|>' in rel or '<|--' in rel):
                    result += f"{rel}\n"

        result += "@enduml"
        return result

    def _apply_interface_projection(self, original_code, class_blocks, relationships):
        """Focus on interfaces and implementations"""
        # In a real implementation, we'd identify interfaces and implementing classes
        # For now, use a placeholder implementation
        result = "@startuml\n"
        result += "\n' Interface Implementation Projection - Focusing on interfaces\n\n"

        # Identify interfaces (simplified approach - just look for interface keyword)
        interfaces = set()
        implementing_classes = set()

        for line in original_code.split('\n'):
            if line.strip().startswith('interface '):
                interface_name = line.strip().split(' ')[1].split('{')[0].strip()
                interfaces.add(interface_name)

        # Identify implementation relationships
        for rel in relationships:
            if '..|>' in rel:  # Implementation relationship in PlantUML
                parts = rel.split('..|>')
                if len(parts) == 2:
                    class_name = parts[0].strip()
                    interface_name = parts[1].strip()
                    if interface_name in interfaces:
                        implementing_classes.add(class_name)

        # Add interfaces to result
        for interface in interfaces:
            result += f"interface {interface} {{}}\n"

        # Add implementing classes
        for class_name in implementing_classes:
            result += f"class {class_name} {{}}\n"

        # Add implementation relationships
        for rel in relationships:
            if '..|>' in rel:
                result += f"{rel}\n"

        result += "@enduml"
        return result

    def _apply_simplified_projection(self, original_code, class_blocks, relationships):
        """Show a simplified view with minimal class details"""
        result = "@startuml\n"
        result += "\n' Simplified Projection - Overview with minimal details\n\n"

        # Extract class names and add them with no details
        for class_name in class_blocks:
            result += f"class {class_name}\n"

        # Add all relationships
        for rel in relationships:
            result += f"{rel}\n"

        result += "@enduml"
        return result

    def get_available_projections(self):
        """Return list of available projection names"""
        return list(self.available_projections.keys())

    def get_projection_description(self, projection_name):
        """Return description text for the given projection"""
        return self.available_projections.get(projection_name, "No description available")


class ConversationDataStorage:
    """
    Manages storage and logging of conversation history, model configurations, and generated diagrams.

    Responsibilities:
    - Create and maintain conversation log files
    - Record user prompts and AI responses
    - Save model configurations used in conversations
    - Store generated diagram code and output
    """

    def __init__(self):
        print("Initializing Conversation Data Storage System...")
        self.log_directory = "uml_generator_logs"
        self.conversation_log_file = None
        self.current_timestamp = None
        self.conversation_identifier = ""
        self.initial_welcome_message = ""
        self.current_message_id = 0
        self.previous_language_model = ""
        self.previous_language_model_config = ""
        self.previous_interpreter = ""
        self.previous_interpreter_config = ""


    def write_log_entry(self, key, data):
        """Write data to the JSON log file"""
        if not os.path.isfile(self.conversation_log_file):
            self.initialize_conversation_log_file()

        with open(self.conversation_log_file, 'r+') as f:
            file_data = json.load(f)
            file_data[key].append(data)
            f.seek(0)
            json.dump(file_data, f, indent=4)

    def write_content_file(self, msg_id, prefix, content, extension):
        """Write content to a file with appropriate naming"""
        filename = f"uml-gen-{self.generate_timestamp()}-{msg_id}-{prefix}{extension}"
        os.makedirs(self.log_directory, exist_ok=True)

        try:
            with open(os.path.join(self.log_directory, filename), 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file: {e}")


    def record_llm_response(self, response, execution_duration_ns):
        """Store a LLM response"""
        self.current_message_id += 1

        conversation_entry = {
            "timestamp": int(time.time()),
            "message_id": self.current_message_id,
            "execution_duration_s": execution_duration_ns/1e+9,
            "llm_response": response.strip()
        }

        self.write_log_entry("conversation", conversation_entry)
        self.write_content_file(self.current_message_id, "response", response, ".txt")


    def initialize_conversation_log_file(self):
        """Creates a new log file with basic structure for storing conversation data."""
        log_structure = {
            "llm_configurations": [],
            "int_configurations": [],
            "conversation": []
        }

        os.makedirs(self.log_directory, exist_ok=True)
        with open(self.conversation_log_file, 'w') as file:
            json.dump(log_structure, file, indent=4)

    def append_to_log_file(self, section_key, data_entry):
        """Append a new data entry to a specific section in the JSON log file."""
        if not os.path.isfile(self.conversation_log_file):
            self.initialize_conversation_log_file()

        with open(self.conversation_log_file, 'r+') as file:
            file_contents = json.load(file)
            file_contents[section_key].append(data_entry)
            file.seek(0)
            json.dump(file_contents, file, indent=4)

    def generate_timestamp(self):
        """Generate a formatted timestamp for file naming and logging."""
        return dt.datetime.now().strftime("%y%m%d-%H%M%S")

    def create_new_conversation(self, welcome_message):
        """Initialize a new conversation with a unique identifier and welcome message."""
        self.initial_welcome_message = welcome_message
        self.current_message_id = 0
        self.previous_language_model = ""
        self.previous_language_model_config = ""
        self.previous_interpreter = ""
        self.previous_interpreter_config = ""

        self.conversation_identifier = f"uml-gen-{self.generate_timestamp()}"
        self.log_directory = os.path.join(self.log_directory, self.conversation_identifier)
        self.conversation_log_file = os.path.join(self.log_directory, f"{self.conversation_identifier}.json")

    def record_language_model_configuration(self, selected_model, model_configuration):
        """Record the language model and its configuration parameters when changed."""
        if self.previous_language_model != str(selected_model) or self.previous_language_model_config != str(model_configuration):
            self.previous_language_model = str(selected_model)
            self.previous_language_model_config = str(model_configuration)
            next_message_id = self.current_message_id + 1

            configuration_entry = {
                "timestamp": int(time.time()),
                "message_id": next_message_id,
                "llm": selected_model,
                "llm_configuration": model_configuration
            }

            self.append_to_log_file("llm_configurations", configuration_entry)

    def record_interpreter_configuration(self, selected_interpreter, interpreter_configuration):
        """Record the diagram interpreter and its configuration parameters when changed."""
        if self.previous_interpreter != str(selected_interpreter) or self.previous_interpreter_config != str(interpreter_configuration):
            self.previous_interpreter = str(selected_interpreter)
            self.previous_interpreter_config = str(interpreter_configuration)
            next_message_id = self.current_message_id + 1

            configuration_entry = {
                "timestamp": int(time.time()),
                "message_id": next_message_id,
                "interpreter": selected_interpreter,
                "int_configuration": interpreter_configuration
            }

            self.append_to_log_file("int_configurations", configuration_entry)

    def record_user_prompt(self, user_prompt):
        """Store a user's prompt in the conversation history."""
        if self.current_message_id == 0:
            self.record_initial_welcome_message()

        self.current_message_id += 1

        prompt_entry = {
            "timestamp": int(time.time()),
            "message_id": self.current_message_id,
            "user_prompt": user_prompt
        }

        self.append_to_log_file("conversation", prompt_entry)
        self.save_content_to_file(self.current_message_id, "prompt", user_prompt, ".txt")

    def record_language_model_response(self, response_text, execution_time_nanoseconds):
        """Store a language model's response with execution timing information."""
        self.current_message_id += 1

        response_entry = {
            "timestamp": int(time.time()),
            "message_id": self.current_message_id,
            "execution_duration_s": execution_time_nanoseconds/1e+9,
            "llm_response": response_text.strip()
        }

        self.append_to_log_file("conversation", response_entry)
        self.save_content_to_file(self.current_message_id, "response", response_text, ".txt")

    def record_interpreter_input(self, diagram_code):
        """Store the diagram code input sent to an interpreter."""
        self.current_message_id += 1
        interpreter_input_entry = {
            "timestamp": int(time.time()),
            "message_id": self.current_message_id,
            "int_input": diagram_code
        }

        self.append_to_log_file("conversation", interpreter_input_entry)
        self.save_content_to_file(self.current_message_id, "int-input", diagram_code,
                                 self.determine_file_extension(diagram_code))

    def record_interpreter_output(self, diagram_output, execution_time_nanoseconds):
        """Store an interpreter's output diagram with execution timing information."""
        self.current_message_id += 1
        output_entry = {
            "timestamp": int(time.time()),
            "message_id": self.current_message_id,
            "execution_duration_s": execution_time_nanoseconds/1e+9,
            "int_output": diagram_output
        }

        self.append_to_log_file("conversation", output_entry)
        self.save_content_to_file(self.current_message_id, "int-output", diagram_output,
                                 self.determine_file_extension(diagram_output))

    def record_general_message(self, message_text):
        """Store a general system message in the conversation history."""
        self.current_message_id += 1
        message_entry = {
            "timestamp": int(time.time()),
            "message_id": self.current_message_id,
            "message": message_text
        }

        self.append_to_log_file("conversation", message_entry)

    def record_initial_welcome_message(self):
        """Store the initial welcome message that starts a conversation."""
        welcome_entry = {
            "timestamp": int(time.time()),
            "message_id": self.current_message_id,
            "init_message": self.initial_welcome_message
        }

        self.append_to_log_file("conversation", welcome_entry)

    def determine_file_extension(self, content):
        """Determine appropriate file extension based on content type."""
        if isinstance(content, str):
            if content.startswith("<?xml") and content.find("<svg") > -1:
                return ".svg"
            elif content.startswith("<?xml"):
                return ".xml"
        return ".txt"

    def save_content_to_file(self, message_id, content_type_prefix, content, file_extension):
        """Save message content to a separate file with appropriate naming convention."""
        filename = f"uml-gen-{self.generate_timestamp()}-{message_id}-{content_type_prefix}{file_extension}"
        os.makedirs(self.log_directory, exist_ok=True)

        try:
            with open(os.path.join(self.log_directory, filename), 'w') as file:
                file.write(content)
        except Exception as error:
            print(f"Error writing file: {error}")

    def reset_conversation_state(self, welcome_message):
        """Reset the conversation state for a new session."""
        if self.current_message_id == 0:
            self.create_new_conversation(welcome_message)
        else:
            self.previous_language_model = ""
            self.previous_language_model_config = ""
            self.previous_interpreter = ""
            self.previous_interpreter_config = ""


class DiagramInterpreterEngine:
    """
    Executes diagram generation from code using supported interpreters like PlantUML and Graphviz.

    Responsibilities:
    - Parse and validate diagram syntax
    - Execute the appropriate renderer for the diagram type
    - Apply error corrections to common syntax mistakes
    - Return the rendered diagram in the requested format
    """

    def __init__(self):
        print("Initializing Diagram Interpreter Engine...")
        self.active_interpreter = None
        self.interpreter_parameters = None
        self.external_api_endpoint = None

    def execute_diagram_generation(self, diagram_code, projection_name=None):
        """Processes diagram code through the appropriate interpreter to generate a visual diagram."""
        result = None

        # Apply projection if specified
        if projection_name and projection_name != "Full Diagram":
            projection_manager = ProjectionManager()
            diagram_code = projection_manager.apply_projection(diagram_code, projection_name)

        if self.active_interpreter == INTERPRETER_PLANTWEB_PLANTUML and PLANTWEB_RENDERER_AVAILABLE:
            formatted_code = self.format_plantuml_code(diagram_code)
            result = self.execute_plantweb_renderer(formatted_code, "plantuml")
        elif self.active_interpreter == INTERPRETER_PLANTWEB_GRAPHVIZ and PLANTWEB_RENDERER_AVAILABLE:
            formatted_code = self.format_graphviz_code(diagram_code)
            result = self.execute_plantweb_renderer(formatted_code, "graphviz")
        else:
            print(f"Interpreter {self.active_interpreter} is not available or not supported")

        if result and len(result) > 1:
            if result[1].lower() == "svg" and isinstance(result[0], bytes):
                # Convert SVG bytes to string for rendering
                return (formatted_code, result[0].decode('utf-8'))

        return (formatted_code, result[0] if result else None)

    def configure_interpreter(self, interpreter_type, configuration_parameters, api_key=None, api_endpoint=None):
        """Sets up the interpreter with specific parameters for diagram generation."""
        print(f"Configuring {interpreter_type} Interpreter...")
        self.active_interpreter = interpreter_type
        self.interpreter_parameters = configuration_parameters

        if api_endpoint:
            self.external_api_endpoint = api_endpoint

    def execute_diagram_generation(self, diagram_code):
        """Processes diagram code through the appropriate interpreter to generate a visual diagram."""
        result = None

        if self.active_interpreter == INTERPRETER_PLANTWEB_PLANTUML and PLANTWEB_RENDERER_AVAILABLE:
            formatted_code = self.format_plantuml_code(diagram_code)
            result = self.execute_plantweb_renderer(formatted_code, "plantuml")
        elif self.active_interpreter == INTERPRETER_PLANTWEB_GRAPHVIZ and PLANTWEB_RENDERER_AVAILABLE:
            formatted_code = self.format_graphviz_code(diagram_code)
            result = self.execute_plantweb_renderer(formatted_code, "graphviz")
        else:
            print(f"Interpreter {self.active_interpreter} is not available or not supported")

        if result and len(result) > 1:
            if result[1].lower() == "svg" and isinstance(result[0], bytes):
                # Convert SVG bytes to string for rendering
                return (formatted_code, result[0].decode('utf-8'))

        return (formatted_code, result[0] if result else None)

    def execute_plantweb_renderer(self, diagram_code, renderer_engine):
        """Execute diagram rendering using the Plantweb library with specified engine."""
        print(f"Executing {renderer_engine} on diagram code: {diagram_code[:20]}...")  # Log first 20 chars
        if not PLANTWEB_RENDERER_AVAILABLE:
            return None

        try:
            output_format = self.interpreter_parameters.get('Output format', 'SVG').lower()
            use_cache = self.interpreter_parameters.get('Use cache', False)

            rendering_result = render(
                diagram_code,
                engine=renderer_engine,
                format=output_format,
                cacheopts={'use_cache': use_cache}
            )
            return rendering_result
        except Exception as error:
            print(f"Error executing Plantweb renderer: {error}")
            return None

    def format_plantuml_code(self, diagram_code):
        """Format and correct PlantUML code to ensure proper syntax and rendering."""
        original_code = diagram_code
        syntax_corrections = []

        # Remove language identifiers added by code formatters
        if diagram_code.startswith("plantuml"):
            diagram_code = diagram_code[8:]
        while diagram_code.startswith("\n"):
            diagram_code = diagram_code[1:]

        # Common PlantUML syntax error corrections

        # 1. Fix incorrect inheritance syntax with label: class Child <-(Parent) : "label" {
        inheritance_pattern_with_label = r'class\s+(\w+)\s+<-\((\w+)\)\s*:\s*"([^"]+)"\s*{'
        if re.search(inheritance_pattern_with_label, diagram_code):
            matches = re.findall(inheritance_pattern_with_label, diagram_code)
            for child, parent, label in matches:
                diagram_code = re.sub(
                    r'class\s+' + child + r'\s+<-\(' + parent + r'\)\s*:\s*"' + label + r'"\s*{',
                    f'class {child} {{',
                    diagram_code
                )
                # Add proper inheritance relationship with label at the end
                if '@enduml' in diagram_code:
                    diagram_code = diagram_code.replace('@enduml', f'\n{child} --|> {parent} : "{label}"\n@enduml')
                else:
                    diagram_code += f'\n{child} --|> {parent} : "{label}"\n'
                syntax_corrections.append(f'Fixed labeled inheritance: \'class {child} <-({parent}) : "{label}"\' → \'class {child}\' with \'{child} --|> {parent} : "{label}"\'')

        # 2. Fix standard incorrect inheritance syntax
        inheritance_pattern = r'class\s+(\w+)\s+<-\((\w+)\)\s*{'
        if re.search(inheritance_pattern, diagram_code):
            matches = re.findall(inheritance_pattern, diagram_code)
            for child, parent in matches:
                diagram_code = re.sub(
                    r'class\s+' + child + r'\s+<-\(' + parent + r'\)\s*{',
                    f'class {child} {{',
                    diagram_code
                )
                # Add proper inheritance relationship at the end
                if '@enduml' in diagram_code:
                    diagram_code = diagram_code.replace('@enduml', f'\n{child} --|> {parent}\n@enduml')
                else:
                    diagram_code += f'\n{child} --|> {parent}\n'
                syntax_corrections.append(f"Fixed inheritance syntax: 'class {child} <-({parent})' → 'class {child}' with '{child} --|> {parent}'")

        # 3. Fix object/instance declarations with :upright: syntax
        upright_instance_pattern = r'(\w+)\s+(\w+)\s+:upright:\s+\"([^\"]+)\"\s+as\s+(\w+)'
        if re.search(upright_instance_pattern, diagram_code):
            matches = re.findall(upright_instance_pattern, diagram_code)
            for class_name, obj_name, label, alias in matches:
                diagram_code = re.sub(
                    r'' + class_name + r'\s+' + obj_name + r'\s+:upright:\s+\"' + label + r'\"\s+as\s+' + alias,
                    f'{class_name} "{label}" as {alias}',
                    diagram_code
                )
                syntax_corrections.append(f"Fixed instance declaration: '{class_name} {obj_name} :upright: \"{label}\" as {alias}' → '{class_name} \"{label}\" as {alias}'")

        # 4. Fix relationship syntax errors (like :upright ->)
        upright_arrow_pattern = r'(\w+)\s+o\d+\s+:upright\s+->\s+(\w+)\s+:is'
        if re.search(upright_arrow_pattern, diagram_code):
            matches = re.findall(upright_arrow_pattern, diagram_code)
            for src, dest in matches:
                diagram_code = re.sub(
                    r'' + src + r'\s+o\d+\s+:upright\s+->\s+' + dest + r'\s+:is',
                    f'{src} --> {dest}',
                    diagram_code
                )
                syntax_corrections.append(f"Fixed relationship arrow: '{src} oN :upright -> {dest} :is' → '{src} --> {dest}'")

        # 5. Fix other :upright relationships
        other_upright_pattern = r'(\w+)\s+-upright:\s+(\w+)'
        if re.search(other_upright_pattern, diagram_code):
            matches = re.findall(other_upright_pattern, diagram_code)
            for src, dest in matches:
                diagram_code = re.sub(
                    r'' + src + r'\s+-upright:\s+' + dest,
                    f'{src} --> {dest}',
                    diagram_code
                )
                syntax_corrections.append(f"Fixed upright relationship: '{src} -upright: {dest}' → '{src} --> {dest}'")

        # 6. Check and fix unbalanced braces
        open_braces = diagram_code.count('{')
        close_braces = diagram_code.count('}')
        if open_braces > close_braces:
            missing_braces = open_braces - close_braces
            if '@enduml' in diagram_code:
                diagram_code = diagram_code.replace('@enduml', '}\n' * missing_braces + '@enduml')
            else:
                diagram_code += '}\n' * missing_braces
            syntax_corrections.append(f"Added {missing_braces} missing closing braces '}}'")

        # Add start and end directives if not present
        if not '@startuml' in diagram_code:
            diagram_code = '@startuml\n' + diagram_code
            syntax_corrections.append("Added missing @startuml directive")
        if not '@enduml' in diagram_code:
            diagram_code = diagram_code + '\n@enduml'
            syntax_corrections.append("Added missing @enduml directive")

        # If errors were fixed, add a comment at the top of the diagram
        if syntax_corrections and '@startuml' in diagram_code:
            comment_header = '\n'.join([f"' {msg}" for msg in syntax_corrections])
            diagram_code = diagram_code.replace('@startuml', f'@startuml\n\n{comment_header}\n')

        return diagram_code

    def format_graphviz_code(self, diagram_code):
        """Format and prepare Graphviz code for rendering."""
        # Remove language identifiers added by code formatters
        if diagram_code.startswith("graphviz") or diagram_code.startswith("dot"):
            diagram_code = diagram_code[8:] if diagram_code.startswith("graphviz") else diagram_code[3:]
        while diagram_code.startswith("\n"):
            diagram_code = diagram_code[1:]

        # Add start and end directives if not present
        if not '@startdot' in diagram_code:
            diagram_code = '@startdot\n' + diagram_code
        if not '@enddot' in diagram_code:
            diagram_code = diagram_code + '\n@enddot'

        return diagram_code


class LanguageModelApiClient:
    """Client for interacting with various language model APIs to generate UML diagrams and explanations"""

    def __init__(self):
        print("Initializing Language Model API Client...")
        self.active_model = None
        self.active_model_api_identifier = None
        self.model_parameters = None
        self.api_authentication_key = None
        self.api_endpoint = None
        self.api_base_url = None
        self.model_name_identifier = None
        self.model_response_history = []
        self.model_generation_in_progress = False
        self.model_response_accumulator = []

    def initialize_language_model(self, selected_model, model_api_identifier, model_configuration_parameters,
                                 api_key=None, api_endpoint=None, base_url=None, model_name=None):
        """Configures the language model with specified parameters and API credentials"""
        print(f"Initializing {selected_model} Language Model...")

        self.active_model = selected_model
        self.active_model_api_identifier = model_api_identifier
        self.model_parameters = model_configuration_parameters
        self.api_authentication_key = api_key
        self.api_base_url = base_url or DEFAULT_API_CONFIGURATION["base_url"]["value"]
        self.model_name_identifier = model_name or DEFAULT_API_CONFIGURATION["model_name"]["value"]

        # Configure appropriate API endpoints based on model provider
        if api_endpoint:
            self.api_endpoint = api_endpoint
        elif selected_model.startswith(API_PROVIDER_OLLAMA):
            self.api_endpoint = "http://127.0.0.1:11434/api/generate"
        elif selected_model.startswith(API_PROVIDER_BIGMODEL):
            self.api_endpoint = self.api_base_url

        # Reset conversation context
        self.clear_conversation_history()

    def process_user_prompt(self, conversation_context, user_prompt):
        """Processes user prompt through the appropriate language model API"""
        if self.active_model.startswith(API_PROVIDER_REPLICATE):
            return self.send_prompt_to_replicate_model(conversation_context)
        elif self.active_model.startswith(API_PROVIDER_OPENAI):
            return self.send_prompt_to_openai_model(conversation_context)
        elif self.active_model.startswith(API_PROVIDER_OLLAMA):
            return self.send_prompt_to_ollama_model(user_prompt)
        elif self.active_model.startswith(API_PROVIDER_BIGMODEL):
            return self.send_prompt_to_bigmodel(conversation_context)
        return None, None

    def send_prompt_to_openai_model(self, conversation_context):
        """Sends prompt to OpenAI API with streaming response"""
        formatted_conversation = []
        for message in conversation_context:
            if "format" in message and "role" in message:
                if message["role"] == MESSAGE_ROLE_USER:
                    formatted_conversation.append({"role": "user", "content": message["message"]})
                elif message["role"] == MESSAGE_ROLE_ASSISTANT:
                    formatted_conversation.append({"role": "assistant", "content": message["message"]})

        if not openai:
            return [], lambda response: "OpenAI library not available"

        try:
            response_stream = openai.ChatCompletion.create(
                model=self.active_model_api_identifier,
                messages=formatted_conversation,
                stream=True,
                **self.model_parameters
            )
            response_parser = lambda item: item.choices[0].delta.get("content", "")
            return response_stream, response_parser
        except Exception as error:
            print(f"OpenAI API error: {error}")
            return [], lambda response: f"Error: {str(error)}"

    def send_prompt_to_replicate_model(self, conversation_context):
        """Sends prompt to Replicate API with streaming response"""
        if not REPLICATE_LIBRARY_AVAILABLE:
            return [], lambda response: "Replicate library not available"

        formatted_conversation = "You are a helpful assistant. You do not respond as 'user' or pretend to be 'user'. You only respond once as 'assistant'.\n\n"
        for message in conversation_context:
            if "format" in message and "role" in message:
                if message["role"] == MESSAGE_ROLE_USER:
                    formatted_conversation += f"user: {message['message']}\n"
                elif message["role"] == MESSAGE_ROLE_ASSISTANT:
                    formatted_conversation += f"assistant: {message['message']}\n"

        try:
            api_parameters = {
                "prompt": f"{formatted_conversation} assistant: ",
                **self.model_parameters
            }
            response_stream = replicate.stream(self.active_model_api_identifier, input=api_parameters)
            response_parser = lambda item: str(item)
            return response_stream, response_parser
        except Exception as error:
            print(f"Replicate API error: {error}")
            return [], lambda response: f"Error: {str(error)}"

    def send_prompt_to_ollama_model(self, user_prompt):
        """Sends prompt to local Ollama API with streaming response"""
        api_parameters = {
            'model': self.active_model_api_identifier,
            'prompt': user_prompt,
            'stream': True,
            'options': self.model_parameters.copy()
        }

        if self.conversation_context:
            api_parameters['context'] = self.conversation_context

        try:
            response = requests.post(self.api_endpoint, json=api_parameters, stream=True)
            response.raise_for_status()
            response_parser = lambda item: self.parse_ollama_api_response(item)
            return response, response_parser
        except Exception as error:
            print(f"Ollama API error: {error}")
            return [], lambda response: f"Error: {str(error)}"

    def parse_ollama_api_response(self, response_chunk):
        """Parses streaming response chunks from Ollama API"""
        try:
            response_text = response_chunk.decode('utf-8')
            response_data = json.loads(response_text)
            if 'context' in response_data:
                self.conversation_context = response_data['context']
            return response_data.get('response', '')
        except Exception:
            return ''

    def send_prompt_to_bigmodel(self, conversation_context):
        """Sends prompt to BigModel API (GLM-4) with streaming response"""
        formatted_conversation = []
        for message in conversation_context:
            if "format" in message and "role" in message:
                if message["role"] == MESSAGE_ROLE_USER:
                    formatted_conversation.append({"role": "user", "content": message["message"]})
                elif message["role"] == MESSAGE_ROLE_ASSISTANT:
                    formatted_conversation.append({"role": "assistant", "content": message["message"]})

        request_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_authentication_key}"
        }

        request_data = {
            "model": self.model_name_identifier,
            "messages": formatted_conversation,
            "stream": True,
            **self.model_parameters
        }

        try:
            response = requests.post(
                f"{self.api_base_url}chat/completions",
                headers=request_headers,
                json=request_data,
                stream=True
            )
            response.raise_for_status()

            def parse_bigmodel_response(chunk):
                if not chunk.strip():
                    return ""
                if chunk.startswith("data: "):
                    chunk = chunk[6:]
                if chunk == "[DONE]":
                    return ""
                try:
                    response_data = json.loads(chunk)
                    return response_data.get("choices", [{}])[0].get("delta", {}).get("content", "")
                except:
                    return ""

            return response.iter_lines(chunk_size=8192, decode_unicode=True), parse_bigmodel_response
        except Exception as error:
            print(f"BigModel API error: {error}")
            return [], lambda response: f"Error: {str(error)}"

    def clear_conversation_history(self):
        """Clears all conversation history and context"""
        self.conversation_context = []
        self.model_generation_in_progress = False
        self.model_response_accumulator = []


class DiagramInterpreter:
    """Interprets and renders various UML diagram formats from text descriptions"""

    def __init__(self):
        print("Initializing Diagram Interpreter...")
        self.active_interpreter = None
        self.interpreter_parameters = None
        self.service_endpoint = None


    def execute_diagram_generation(self, diagram_code, projection_name=None):
        """Processes diagram code through the appropriate interpreter with optional projection."""
        result = None

        # Apply projection if specified
        if projection_name and projection_name != "Full Diagram":
            projection_manager = ProjectionManager()
            diagram_code = projection_manager.apply_projection(diagram_code, projection_name)

        # Process using the existing method
        processed_code, rendering_result = self.process_diagram_code(diagram_code)

        return processed_code, rendering_result


    def initialize_interpreter(self, selected_interpreter, interpreter_parameters, api_key=None, api_endpoint=None):
        """Configures the diagram interpreter with specified parameters"""
        print(f"Initializing {selected_interpreter} Interpreter...")
        self.active_interpreter = selected_interpreter
        self.interpreter_parameters = interpreter_parameters

        if api_endpoint:
            self.service_endpoint = api_endpoint

    def process_diagram_code(self, diagram_code):
        """Processes diagram code through the appropriate interpreter"""
        result = None

        if self.active_interpreter == INTERPRETER_PLANTWEB_PLANTUML and PLANTWEB_AVAILABLE:
            processed_diagram_code = self.format_plantuml_code(diagram_code)
            result = self.execute_plantweb_renderer(processed_diagram_code, "plantuml")
        elif self.active_interpreter == INTERPRETER_PLANTWEB_GRAPHVIZ and PLANTWEB_AVAILABLE:
            processed_diagram_code = self.format_graphviz_code(diagram_code)
            result = self.execute_plantweb_renderer(processed_diagram_code, "graphviz")
        else:
            print(f"Interpreter {self.active_interpreter} not available")

        if result and len(result) > 1:
            if result[1].lower() == "svg" and isinstance(result[0], bytes):
                # Convert SVG binary data to UTF-8 text
                return (processed_diagram_code, result[0].decode('utf-8'))

        return (diagram_code, result[0] if result else None)

    def execute_plantweb_renderer(self, diagram_code, engine_type):
        """Executes PlantWeb renderer with the specified engine"""
        print(f"Running {engine_type} on input: {diagram_code[:20]}...")
        if not PLANTWEB_AVAILABLE:
            return None

        try:
            output_format = self.interpreter_parameters.get('Output format', 'SVG').lower()
            use_cache = self.interpreter_parameters.get('Use cache', False)

            result = render(
                diagram_code,
                engine=engine_type,
                format=output_format,
                cacheopts={'use_cache': use_cache}
            )
            return result
        except Exception as error:
            print(f"Error executing Plantweb: {error}")
            return None

    def format_plantuml_code(self, diagram_code):
        """Formats PlantUML code with error correction and syntax improvements"""
        original_code = diagram_code
        error_corrections = []

        # Remove syntax formatting instruction added by LLM
        if diagram_code.startswith("plantuml"):
            diagram_code = diagram_code[8:]
        while diagram_code.startswith("\n"):
            diagram_code = diagram_code[1:]

        # Fix common syntax errors

        # 1. Fix incorrect inheritance syntax with label: class Child <-(Parent) : "label" {
        inheritance_with_label_pattern = r'class\s+(\w+)\s+<-\((\w+)\)\s*:\s*"([^"]+)"\s*{'
        if re.search(inheritance_with_label_pattern, diagram_code):
            matches = re.findall(inheritance_with_label_pattern, diagram_code)
            for child_class, parent_class, relationship_label in matches:
                diagram_code = re.sub(
                    r'class\s+' + child_class + r'\s+<-\(' + parent_class + r'\)\s*:\s*"' + relationship_label + r'"\s*{',
                    f'class {child_class} {{',
                    diagram_code
                )
                # Add proper inheritance relationship with label at the end
                if '@enduml' in diagram_code:
                    diagram_code = diagram_code.replace('@enduml', f'\n{child_class} --|> {parent_class} : "{relationship_label}"\n@enduml')
                else:
                    diagram_code += f'\n{child_class} --|> {parent_class} : "{relationship_label}"\n'
                error_corrections.append(f'Fixed labeled inheritance: \'class {child_class} <-({parent_class}) : "{relationship_label}"\' → \'class {child_class}\' with \'{child_class} --|> {parent_class} : "{relationship_label}"\'')

        # 2. Fix standard incorrect inheritance syntax
        inheritance_pattern = r'class\s+(\w+)\s+<-\((\w+)\)\s*{'
        if re.search(inheritance_pattern, diagram_code):
            matches = re.findall(inheritance_pattern, diagram_code)
            for child_class, parent_class in matches:
                diagram_code = re.sub(
                    r'class\s+' + child_class + r'\s+<-\(' + parent_class + r'\)\s*{',
                    f'class {child_class} {{',
                    diagram_code
                )
                # Add proper inheritance relationship at the end of the diagram
                if '@enduml' in diagram_code:
                    diagram_code = diagram_code.replace('@enduml', f'\n{child_class} --|> {parent_class}\n@enduml')
                else:
                    diagram_code += f'\n{child_class} --|> {parent_class}\n'
                error_corrections.append(f"Fixed inheritance syntax: 'class {child_class} <-({parent_class})' → 'class {child_class}' with '{child_class} --|> {parent_class}'")

        # 3. Fix object/instance declarations with :upright: syntax
        upright_instance_pattern = r'(\w+)\s+(\w+)\s+:upright:\s+\"([^\"]+)\"\s+as\s+(\w+)'
        if re.search(upright_instance_pattern, diagram_code):
            matches = re.findall(upright_instance_pattern, diagram_code)
            for class_name, object_name, label_text, alias_name in matches:
                diagram_code = re.sub(
                    r'' + class_name + r'\s+' + object_name + r'\s+:upright:\s+\"' + label_text + r'\"\s+as\s+' + alias_name,
                    f'{class_name} "{label_text}" as {alias_name}',
                    diagram_code
                )
                error_corrections.append(f"Fixed instance declaration: '{class_name} {object_name} :upright: \"{label_text}\" as {alias_name}' → '{class_name} \"{label_text}\" as {alias_name}'")

        # 4. Fix relationship syntax errors (like :upright ->)
        upright_arrow_pattern = r'(\w+)\s+o\d+\s+:upright\s+->\s+(\w+)\s+:is'
        if re.search(upright_arrow_pattern, diagram_code):
            matches = re.findall(upright_arrow_pattern, diagram_code)
            for source_entity, target_entity in matches:
                diagram_code = re.sub(
                    r'' + source_entity + r'\s+o\d+\s+:upright\s+->\s+' + target_entity + r'\s+:is',
                    f'{source_entity} --> {target_entity}',
                    diagram_code
                )
                error_corrections.append(f"Fixed relationship arrow: '{source_entity} oN :upright -> {target_entity} :is' → '{source_entity} --> {target_entity}'")

        # 5. Fix other :upright relationships
        other_upright_pattern = r'(\w+)\s+-upright:\s+(\w+)'
        if re.search(other_upright_pattern, diagram_code):
            matches = re.findall(other_upright_pattern, diagram_code)
            for source_entity, target_entity in matches:
                diagram_code = re.sub(
                    r'' + source_entity + r'\s+-upright:\s+' + target_entity,
                    f'{source_entity} --> {target_entity}',
                    diagram_code
                )
                error_corrections.append(f"Fixed upright relationship: '{source_entity} -upright: {target_entity}' → '{source_entity} --> {target_entity}'")

        # 6. Check and fix unbalanced braces
        open_braces = diagram_code.count('{')
        close_braces = diagram_code.count('}')
        if open_braces > close_braces:
            missing_braces = open_braces - close_braces
            if '@enduml' in diagram_code:
                diagram_code = diagram_code.replace('@enduml', '}\n' * missing_braces + '@enduml')
            else:
                diagram_code += '}\n' * missing_braces
            error_corrections.append(f"Added {missing_braces} missing closing braces '}}'")

        # Add start and end directives if not present
        if not '@startuml' in diagram_code:
            diagram_code = '@startuml\n' + diagram_code
            error_corrections.append("Added missing @startuml directive")
        if not '@enduml' in diagram_code:
            diagram_code = diagram_code + '\n@enduml'
            error_corrections.append("Added missing @enduml directive")

        # If errors were fixed, add a comment at the top of the diagram
        if error_corrections and '@startuml' in diagram_code:
            correction_comments = '\n'.join([f"' {correction}" for correction in error_corrections])
            diagram_code = diagram_code.replace('@startuml', f'@startuml\n\n{correction_comments}\n')

        return diagram_code

    def format_graphviz_code(self, diagram_code):
        """Formats Graphviz code for proper interpretation"""
        # Remove syntax formatting instruction added by LLM
        if diagram_code.startswith("graphviz") or diagram_code.startswith("dot"):
            diagram_code = diagram_code[8:] if diagram_code.startswith("graphviz") else diagram_code[3:]
        while diagram_code.startswith("\n"):
            diagram_code = diagram_code[1:]

        # Add start and end directives if not present
        if not '@startdot' in diagram_code:
            diagram_code = '@startdot\n' + diagram_code
        if not '@enddot' in diagram_code:
            diagram_code = diagram_code + '\n@enddot'

        return diagram_code


class UMLDiagramGenerationApp:
    """Main application class that coordinates language models, interpreters, and user interface"""

    def __init__(self):
        print("Initializing UML Diagram Development Assistant...")
        self.conversation_store = ConversationDataStorage()
        self.language_model_client = LanguageModelApiClient()
        self.diagram_interpreter = DiagramInterpreter()
        self.active_language_model = MODEL_SELECTION_PLACEHOLDER
        self.active_interpreter = INTERPRETER_SELECTION_PLACEHOLDER
        self.model_parameters = {}
        self.interpreter_parameters = {}
        self.application_configuration = DEFAULT_API_CONFIGURATION.copy()

    def load_user_configuration(self):
        """Loads user configuration from session state or sets defaults"""
        if SESSION_KEY_APPLICATION_CONFIG in st.session_state:
            self.application_configuration = st.session_state[SESSION_KEY_APPLICATION_CONFIG]
        else:
            st.session_state[SESSION_KEY_APPLICATION_CONFIG] = self.application_configuration

    def save_user_configuration(self):
        """Saves configuration to session state for persistence"""
        st.session_state[SESSION_KEY_APPLICATION_CONFIG] = self.application_configuration

    def select_language_model(self, model_id):
        """Selects a language model and initializes appropriate parameters"""
        if self.active_language_model != model_id:
            self.active_language_model = model_id
            if model_id.startswith(API_PROVIDER_OPENAI):
                self.model_parameters = INTERPRETER_DEFAULT_PARAMETERS[API_PROVIDER_OPENAI].copy()
            elif model_id.startswith(API_PROVIDER_REPLICATE):
                self.model_parameters = INTERPRETER_DEFAULT_PARAMETERS[API_PROVIDER_REPLICATE].copy()
            elif model_id.startswith(API_PROVIDER_OLLAMA):
                self.model_parameters = INTERPRETER_DEFAULT_PARAMETERS[API_PROVIDER_OLLAMA].copy()
            elif model_id.startswith(API_PROVIDER_BIGMODEL):
                self.model_parameters = {
                    "temperature": 0.2,
                    "top_p": 0.9
                }
            self.initialize_language_model()
            return True
        return False

    def select_diagram_interpreter(self, interpreter_id):
        """Selects a diagram interpreter and initializes appropriate parameters"""
        if self.active_interpreter != interpreter_id:
            self.active_interpreter = interpreter_id
            if interpreter_id == INTERPRETER_PLANTWEB_PLANTUML:
                self.interpreter_parameters = {
                    "Output format": "SVG",
                    "Use cache": False
                }
            elif interpreter_id == INTERPRETER_PLANTWEB_GRAPHVIZ:
                self.interpreter_parameters = {
                    "Output format": "SVG",
                    "Use cache": False
                }
            self.initialize_interpreter()
            return True
        return False

    def initialize_language_model(self):
        """Initializes the selected language model with current configuration"""
        if self.active_language_model != MODEL_SELECTION_PLACEHOLDER:
            api_key = self.application_configuration["api_key"]["value"]
            base_url = self.application_configuration["base_url"]["value"]
            model_name = self.application_configuration["model_name"]["value"]

            self.language_model_client.initialize_language_model(
                self.active_language_model,
                model_name,
                self.model_parameters,
                api_key=api_key,
                base_url=base_url,
                model_name=model_name
            )

    def initialize_interpreter(self):
        """Initializes the selected diagram interpreter with current parameters"""
        if self.active_interpreter != INTERPRETER_SELECTION_PLACEHOLDER:
            self.diagram_interpreter.initialize_interpreter(
                self.active_interpreter,
                self.interpreter_parameters
            )

    def process_user_prompt(self, conversation_context, user_prompt):
        """Processes a user prompt through the selected language model"""
        if self.active_language_model == MODEL_SELECTION_PLACEHOLDER:
            return None, None, None

        self.conversation_store.record_user_prompt(user_prompt)
        processing_start_time = perf_counter_ns()

        response_stream, response_parser = self.language_model_client.process_user_prompt(conversation_context, user_prompt)

        return response_stream, response_parser, processing_start_time


    def record_llm_response(self, response, execution_duration_ns):
        """Record an LLM response for logging"""
        # Delegate message handling to conversation_store instead of managing message ID directly
        self.conversation_store.record_llm_response(response, execution_duration_ns)


    def extract_diagram_code(self, model_response):
        """Extracts diagram code from model response"""
        if not self.active_interpreter or self.active_interpreter == INTERPRETER_SELECTION_PLACEHOLDER:
            return None

        # Search for code blocks with PlantUML content
        code_pattern = re.compile(r'```(?:plantuml|uml)?\s*((?:@startuml[\s\S]*?@enduml)|(?:[\s\S]*?))```', re.DOTALL)
        matches = code_pattern.findall(model_response)

        if matches and len(matches) > 0:
            # Select the longest match which is likely the complete diagram
            best_match = max(matches, key=len)

            # Ensure it has proper PlantUML delimiters
            if '@startuml' not in best_match:
                best_match = '@startuml\n' + best_match
            if '@enduml' not in best_match:
                best_match = best_match + '\n@enduml'

            return best_match.strip()

        # Fallback: try to find @startuml...@enduml directly
        direct_pattern = re.compile(r'@startuml[\s\S]*?@enduml', re.DOTALL)
        direct_matches = direct_pattern.findall(model_response)
        if direct_matches:
            return direct_matches[0].strip()

        return None



    def render_diagram(self, diagram_code, projection_name=None):
        """Renders diagram using the selected interpreter with optional projection"""
        if not self.active_interpreter or self.active_interpreter == INTERPRETER_SELECTION_PLACEHOLDER:
            return None, None

        processing_start_time = perf_counter_ns()
        processed_code, rendering_output = self.diagram_interpreter.execute_diagram_generation(
            diagram_code, projection_name
        )
        processing_end_time = perf_counter_ns()

        execution_duration = processing_end_time - processing_start_time

        if rendering_output:
            self.conversation_store.record_interpreter_input(processed_code)
            self.conversation_store.record_interpreter_output(rendering_output, execution_duration)

        return processed_code, rendering_output



    def clear_conversation_history(self):
        """Clears conversation history and starts a new conversation"""
        self.language_model_client.clear_conversation_history()
        self.conversation_store.create_conversation(INITIAL_MESSAGE)



# User Interface Component Classes
class SessionStateManager:
    """Manages application state persistence across page reloads in the Streamlit application"""

    @staticmethod
    def initialize_application_state():
        """Sets up initial state variables if they don't already exist"""
        if SESSION_KEY_CONVERSATION_MESSAGES not in st.session_state:
            st.session_state[SESSION_KEY_CONVERSATION_MESSAGES] = []

        if SESSION_KEY_USER_PROMPT not in st.session_state:
            st.session_state[SESSION_KEY_USER_PROMPT] = ""

        if SESSION_KEY_USER_PROMPT_PERPEND not in st.session_state:
            st.session_state[SESSION_KEY_USER_PROMPT_PERPEND] = ""

        if SESSION_KEY_USER_PROMPT_APPEND not in st.session_state:
            st.session_state[SESSION_KEY_USER_PROMPT_APPEND] = ""

        if SESSION_KEY_INTERPRETER_INPUT not in st.session_state:
            st.session_state[SESSION_KEY_INTERPRETER_INPUT] = ""

    @staticmethod
    def add_message_to_conversation(role_type, message_content, message_format_type, source_info=None):
        """Adds a formatted message to the conversation history"""
        message_object = {
            ROLE: role_type,
            MSG: message_content,
            MSG_FORMAT: message_format_type
        }

        if source_info:
            message_object[SRC] = source_info

        # Add appropriate avatar based on role
        if role_type == ROLE_AS:
            message_object[AVATAR] = AVATAR_ASSIST
        elif role_type == ROLE_US:
            message_object[AVATAR] = AVATAR_USER
        elif role_type == ROLE_IN:
            message_object[AVATAR] = AVATAR_INTER

        st.session_state[SESSION_KEY_CONVERSATION_MESSAGES].append(message_object)
        return message_object


class LanguageModelProcessor:
    """Processes user prompts through language models and manages response handling"""

    @staticmethod
    def process_user_prompt_with_model(prompt_text, application_instance):
        """Sends user prompt to language model and handles streaming response"""
        if not prompt_text:
            return False

        # Determine if we're in diagram revision mode
        is_diagram_revision_request = prompt_text.startswith("Please review and improve the following UML class diagram:")

        # Create appropriate context based on the mode
        if is_diagram_revision_request:
            system_context_message = {
                ROLE: ROLE_AS,
                MSG: "You are a UML diagram expert focusing on analyzing and improving existing PlantUML code. Provide detailed analysis, identify issues, and suggest improvements to make the diagram more clear, complete, and conforming to best practices.",
                MSG_FORMAT: MSG_FORMAT_INIT
            }
        else:
            system_context_message = {
                ROLE: ROLE_AS,
                MSG: "You are a UML diagram generation assistant. Focus on the conversation history to understand the user's requirements. Generate accurate PlantUML code to assist in their Object-Oriented Analysis and Design development process.",
                MSG_FORMAT: MSG_FORMAT_INIT
            }

        # Build conversation context with appropriate system message
        conversation_context = st.session_state[SESSION_KEY_CONVERSATION_MESSAGES].copy()
        if conversation_context and len(conversation_context) > 0:
            conversation_context.insert(0, system_context_message)

        # Process the user prompt with the language model
        response_stream, response_parser, processing_start_time = application_instance.process_user_prompt(
            conversation_context, prompt_text)

        if not response_stream or not response_parser:
            SessionStateManager.add_message_to_conversation(
                ROLE_AS,
                "Failed to process your request. Please check your model configuration.",
                MSG_FORMAT_RESPONSE_LLM_TXT
            )
            return False

        # Process streaming response from language model
        complete_model_response = ""
        response_placeholder = st.empty()
        message_object = SessionStateManager.add_message_to_conversation(
            ROLE_AS, "", MSG_FORMAT_RESPONSE_LLM)

        # Accumulate response chunks
        for response_chunk in response_stream:
            text_fragment = response_parser(response_chunk)
            if text_fragment:
                complete_model_response += text_fragment
                message_object[MSG] = complete_model_response
                response_placeholder.markdown(complete_model_response)

        # Record the final response timing
        if processing_start_time:
            processing_end_time = perf_counter_ns()
            execution_duration = processing_end_time - processing_start_time
            application_instance.record_llm_response(complete_model_response, execution_duration)

        # Extract diagram code and handle diagram generation
        LanguageModelProcessor.handle_diagram_code_detection(
            complete_model_response,
            response_placeholder,
            application_instance
        )

        return True

    @staticmethod
    def handle_diagram_code_detection(model_response, placeholder_element, application_instance):
        """Detects and processes PlantUML diagram code in model responses"""
        # Look for PlantUML code patterns
        plantuml_pattern = r'@startuml[\s\S]*?@enduml'
        code_block_pattern = r'```(?:plantuml|uml)?([\s\S]*?)```'

        # First try code blocks with explicit markup
        code_blocks = re.findall(code_block_pattern, model_response)
        detected_diagram_code = None

        for block in code_blocks:
            if '@startuml' in block and '@enduml' in block:
                detected_diagram_code = block.strip()
                break

        # If not found in code blocks, try direct pattern
        if not detected_diagram_code:
            direct_matches = re.findall(plantuml_pattern, model_response)
            if direct_matches:
                detected_diagram_code = direct_matches[0].strip()

        # Handle the detected diagram code
        if detected_diagram_code and "previous_page" not in st.session_state:
            # Notify user that diagram code was detected
            with placeholder_element.container():
                st.success("PlantUML code detected! You can open it in the Diagram Editor.")

                # Configure the interpreter automatically
                application_instance.select_diagram_interpreter(INT_PLANTWEB_PLANTUML)

                # Save diagram code for the editor
                st.session_state["editor_code"] = detected_diagram_code


class DiagramInterpreterProcessor:
    """Processes diagram code through interpreters and handles rendering results"""

    @staticmethod
    def process_diagram_with_interpreter(application_instance):
        """Processes diagram code through the selected interpreter"""
        diagram_code = st.session_state[SESSION_KEY_INTERPRETER_INPUT]
        if not diagram_code:
            return

        # Clear input after retrieving
        st.session_state[SESSION_KEY_INTERPRETER_INPUT] = ""

        # Create placeholder for displaying results
        result_placeholder = st.empty()
        message_object = SessionStateManager.add_message_to_conversation(
            ROLE_IN, "", MSG_FORMAT_RESPONSE_INT)

        # Preprocess PlantUML code before sending to interpreter
        if application_instance.active_interpreter == INT_PLANTWEB_PLANTUML:
            # Ensure code has proper start/end tags
            if not diagram_code.strip().startswith("@startuml"):
                diagram_code = "@startuml\n" + diagram_code
            if not diagram_code.strip().endswith("@enduml"):
                diagram_code = diagram_code + "\n@enduml"

        # Process the diagram code with interpreter
        processed_diagram_code, rendering_result = application_instance.render_diagram(diagram_code)

        # Display the results
        if rendering_result:
            # For SVG output
            if isinstance(rendering_result, str) and rendering_result.startswith("<?xml") and "<svg" in rendering_result:
                message_object[MSG] = rendering_result
                message_object[MSG_FORMAT] = MSG_FORMAT_RESPONSE_INT_IMG
                with result_placeholder.container():
                    st.components.v1.html(rendering_result, height=500)
            else:
                # For text output
                message_object[MSG] = str(rendering_result)
                message_object[MSG_FORMAT] = MSG_FORMAT_RESPONSE_INT_TXT
                with result_placeholder.container():
                    st.code(str(rendering_result))
        else:
            message_object[MSG] = "Failed to generate diagram."
            message_object[MSG_FORMAT] = MSG_FORMAT_RESPONSE_INT_TXT
            with result_placeholder.container():
                st.warning("Failed to generate diagram.")




class ApplicationPages:
    """Contains all page definitions for the Streamlit application"""

    @staticmethod
    def render_about_info():
        """Renders the author and project information"""
        with st.expander("About this Project"):
            st.markdown("""
            ### UML-Diagram-Development-Assistant
            
            **CPS 3962**: Object Orientated Analysis and Design (OOAD) Project
            
            **Instructor**: Dr. Hamza Djigal
            
            **Project Name**: Develop a Conversational OOAD Assistant Leveraging Large Language Models
            
            **Project Members**:
            - Zhentong Ye (zye@kean.edu)
            - Yanwu Lang (langy@kean.edu)
            
            **Version**: {0}
            """.format(APPLICATION_VERSION))

    @staticmethod
    def render_configuration_page():
        """Renders the configuration page for API settings"""
        st.title("API Configuration")

        # Add the about info to the sidebar
        with st.sidebar:
            ApplicationPages.render_about_info()

        application_instance = st.session_state.get(SESSION_KEY_APPLICATION_INSTANCE)
        if not application_instance:
            st.error("Application not initialized")
            return

        with st.form("api_configuration_form"):
            st.subheader("API Settings")

            api_key = st.text_input(
                "API Key",
                value=application_instance.application_configuration["api_key"]["value"],
                help=application_instance.application_configuration["api_key"]["description"],
                type="password"
            )

            base_url = st.text_input(
                "Base URL",
                value=application_instance.application_configuration["base_url"]["value"],
                help=application_instance.application_configuration["base_url"]["description"]
            )

            model_name = st.text_input(
                "Model Name",
                value=application_instance.application_configuration["model_name"]["value"],
                help=application_instance.application_configuration["model_name"]["description"]
            )

            submit_button = st.form_submit_button("Save Configuration")
            if submit_button:
                application_instance.application_configuration["api_key"]["value"] = api_key
                application_instance.application_configuration["base_url"]["value"] = base_url
                application_instance.application_configuration["model_name"]["value"] = model_name
                application_instance.save_user_configuration()

                # Re-initialize if a model is already selected
                if application_instance.active_language_model != MODEL_SELECTION_PLACEHOLDER:
                    application_instance.initialize_language_model()

                st.success("Configuration saved!")

        st.divider()
        with st.expander("Default Configuration"):
            st.json(DEFAULT_API_CONFIGURATION)

    @staticmethod
    def render_chat_page():
        """Renders the main chat interface page"""
        st.title("UML Diagram Development Assistant")

        # Add the about info to the sidebar
        with st.sidebar:
            ApplicationPages.render_about_info()


        # Initialize application if needed
        if SESSION_KEY_APPLICATION_INSTANCE not in st.session_state:
            application_instance = UMLDiagramGenerationApp()
            application_instance.load_user_configuration()
            st.session_state[SESSION_KEY_APPLICATION_INSTANCE] = application_instance
            application_instance.conversation_store.create_new_conversation(INITIAL_MESSAGE)
            # Set default model automatically
            application_instance.select_language_model(f"{API_PROVIDER_BIGMODEL}/glm-4-plus")
        else:
            application_instance = st.session_state[SESSION_KEY_APPLICATION_INSTANCE]

        # Initialize session state
        SessionStateManager.initialize_application_state()

        # Handle revision prompt if coming from Diagram Editor
        if SESSION_KEY_USER_PROMPT in st.session_state and st.session_state[SESSION_KEY_USER_PROMPT]:
            prompt_text = st.session_state[SESSION_KEY_USER_PROMPT]
            st.session_state[SESSION_KEY_USER_PROMPT] = ""  # Clear the prompt

            # Add user message to chat
            SessionStateManager.add_message_to_conversation(ROLE_US, prompt_text, MSG_FORMAT_PROMPT)

            # Process with language model if model is selected
            if application_instance.active_language_model != MODEL_SELECTION_PLACEHOLDER:
                LanguageModelProcessor.process_user_prompt_with_model(prompt_text, application_instance)
            else:
                SessionStateManager.add_message_to_conversation(
                    ROLE_AS,
                    "Please select a language model first.",
                    MSG_FORMAT_RESPONSE_LLM_TXT
                )

        # Sidebar for model selection and parameters
        with st.sidebar:
            st.header("Model Selection")

            # Language model selection with default value
            selected_model = st.selectbox(
                "Select Language Model",
                options=[MODEL_SELECTION_PLACEHOLDER,
                         f"{API_PROVIDER_BIGMODEL}/glm-4-plus",
                         f"{API_PROVIDER_OPENAI}/gpt-4",
                         f"{API_PROVIDER_REPLICATE}/llama3-70B-Chat",
                         f"{API_PROVIDER_OLLAMA}/llama3"],
                index=1  # Default to BigModel option
            )

            if application_instance.select_language_model(selected_model):
                st.success(f"Selected model: {selected_model}")

            # Model parameters
            if application_instance.active_language_model != MODEL_SELECTION_PLACEHOLDER:
                st.subheader("Model Parameters")

                temperature_value = st.slider(
                    "Temperature",
                    min_value=0.0,
                    max_value=1.0,
                    value=application_instance.model_parameters.get("temperature", 0.2),
                    step=0.1,
                    help="Higher values make output more random, lower values more deterministic"
                )
                application_instance.model_parameters["temperature"] = temperature_value

                top_p_value = st.slider(
                    "Top P",
                    min_value=0.0,
                    max_value=1.0,
                    value=application_instance.model_parameters.get("top_p", 0.9),
                    step=0.1,
                    help="Controls diversity via nucleus sampling"
                )
                application_instance.model_parameters["top_p"] = top_p_value

            # Actions section
            st.header("Actions")
            # if st.button("New Conversation"):
            #     st.session_state[SESSION_KEY_CONVERSATION_MESSAGES] = []
            #     application_instance.clear_conversation_history()
            #     st.rerun()

            # Add button to return to Diagram Editor if we came from there
            if "previous_page" in st.session_state and st.session_state["previous_page"] == "Diagram Editor":
                if st.button("Return to Diagram Editor"):
                    st.session_state["current_page"] = "Diagram Editor"
                    st.session_state["previous_page"] = "Chat"
                    st.rerun()


            with st.expander("About Projections"):
                st.markdown("""
                **What are Diagram Projections?**
                
                Projections allow you to view your UML diagram from different perspectives, 
                highlighting specific aspects while hiding others.
                
                **When to use projections:**
                
                - **Full Diagram**: Complete view with all details
                - **Core Classes**: Focus on main classes without implementation details
                - **Inheritance Hierarchy**: Understand class hierarchy and inheritance
                - **Associations Only**: See how classes relate to each other
                - **Interface Implementations**: Focus on interfaces and implementations
                - **Simplified View**: Get a high-level overview of the system
                
                Use projections to better understand complex systems by focusing on one aspect at a time.
                """)

        # Display chat messages
        for message_index, message in enumerate(st.session_state[SESSION_KEY_CONVERSATION_MESSAGES]):
            role_type = message[ROLE]
            message_content = message[MSG]
            message_format = message[MSG_FORMAT]

            with st.chat_message(role_type):
                st.markdown(message_content)

                # Check for PlantUML code in assistant messages to add convenience buttons
                if role_type == ROLE_AS:
                    code_block_pattern = r'```(?:plantuml|uml)?([\s\S]*?)```'
                    code_blocks = re.findall(code_block_pattern, message_content)

                    for block in code_blocks:
                        if '@startuml' in block and '@enduml' in block:
                            diagram_code = block.strip()
                            if st.button(f"Open in Diagram Editor", key=f"open_editor_{message_index}"):
                                st.session_state["editor_code"] = diagram_code
                                st.session_state["current_page"] = "Diagram Editor"
                                st.session_state["previous_page"] = "Chat"
                                st.rerun()
                            break

        # Chat input
        user_prompt = st.chat_input("Type your message here...")
        if user_prompt:
            # Add user message to chat
            SessionStateManager.add_message_to_conversation(ROLE_US, user_prompt, MSG_FORMAT_PROMPT)

            # Process with language model if model is selected
            if application_instance.active_language_model != MODEL_SELECTION_PLACEHOLDER:
                LanguageModelProcessor.process_user_prompt_with_model(user_prompt, application_instance)
            else:
                SessionStateManager.add_message_to_conversation(
                    ROLE_AS,
                    "Please select a language model first.",
                    MSG_FORMAT_RESPONSE_LLM_TXT
                )









    @staticmethod
    def render_diagram_editor_page():
        """Renders the interactive diagram editor page"""
        st.title("UML Diagram Editor")

        # Add the about info to the sidebar
        with st.sidebar:
            ApplicationPages.render_about_info()


        # Initialize application if needed
        if SESSION_KEY_APPLICATION_INSTANCE not in st.session_state:
            application_instance = UMLDiagramGenerationApp()
            application_instance.load_user_configuration()
            st.session_state[SESSION_KEY_APPLICATION_INSTANCE] = application_instance
        else:
            application_instance = st.session_state[SESSION_KEY_APPLICATION_INSTANCE]

        # Initialize the diagram interpreter with PlantUML if not already selected
        if application_instance.active_interpreter == INTERPRETER_SELECTION_PLACEHOLDER:
            application_instance.select_diagram_interpreter(INT_PLANTWEB_PLANTUML)

        # Add projection controls to sidebar
        with st.sidebar:
            st.header("Diagram Projections")

            # Get available projections
            projection_manager = ProjectionManager()
            projections = projection_manager.get_available_projections()

            # Current projection selection
            if "current_projection" not in st.session_state:
                st.session_state.current_projection = "Full Diagram"

            selected_projection = st.selectbox(
                "Select Projection View",
                options=projections,
                index=projections.index(st.session_state.current_projection),
                help="Choose different ways to visualize your UML diagram"
            )

            # Update the current projection
            st.session_state.current_projection = selected_projection

            # Display projection description
            projection_description = projection_manager.get_projection_description(selected_projection)
            st.info(projection_description)

            with st.expander("About Projections"):
                st.markdown("""
                **What are Diagram Projections?**
                
                Projections allow you to view your UML diagram from different perspectives,
                highlighting specific aspects while hiding others.
                
                **When to use projections:**
                
                - **Full Diagram**: Complete view with all details
                - **Core Classes**: Focus on main classes without implementation details
                - **Inheritance Hierarchy**: Understand class hierarchy and inheritance
                - **Associations Only**: See how classes relate to each other
                - **Interface Implementations**: Focus on interfaces and implementations
                - **Simplified View**: Get a high-level overview of the system
                
                Use projections to better understand complex systems by focusing on one aspect at a time.
                """)

        # Create a two-column layout
        code_column, preview_column = st.columns([1, 1])




        with code_column:
            st.subheader("PlantUML Code")

            # Get stored code or use a default example
            if "editor_code" not in st.session_state:
                st.session_state.editor_code = """@startuml
    class User {
      -String name
      -String email
      +void login()
      +void logout()
    }
    
    class Product {
      -String name
      -double price
      +void setPrice(price: double)
      +double getPrice()
    }
    
    User --> Product: browses
    @enduml"""

            # Code editor
            plant_uml_code = st.text_area(
                "Edit your PlantUML code here:",
                st.session_state.editor_code,
                height=400
            )
            st.session_state.editor_code = plant_uml_code

            button_column1, button_column2, button_column3 = st.columns(3)

            # Render button that stays on this page
            with button_column1:
                if st.button("Render Diagram"):
                    with st.spinner("Rendering..."):
                        # Process the diagram code with the selected projection
                        processed_code, diagram_result = application_instance.render_diagram(
                            plant_uml_code, st.session_state.current_projection
                        )

                        # Store results
                        if diagram_result:
                            st.session_state["current_diagram"] = diagram_result
                            st.session_state["last_processed_code"] = processed_code
                            st.session_state["last_successful_code"] = plant_uml_code
                        else:
                            st.error("Failed to generate diagram")

            # Add Revise UML button
            with button_column2:
                if st.button("Revise UML"):
                    # Store the code to be sent to the language model
                    st.session_state["revise_uml_code"] = plant_uml_code

                    # Switch to Chat page
                    st.session_state["current_page"] = "Chat"
                    st.session_state["previous_page"] = "Diagram Editor"

                    # Add system prompt and the code as a user message
                    uml_revision_prompt = f"""Please review and improve the following UML class diagram:
    
    ```plantuml
    {plant_uml_code}
    ```
    
    Focus on:
    1. Fixing any syntax errors
    2. Improving class relationships
    3. Enhancing readability
    4. Following UML best practices
    
    Please explain your changes and provide the improved diagram code.
    """
                    # Insert message in session state for next page load
                    st.session_state[SESSION_KEY_USER_PROMPT] = uml_revision_prompt
                    st.rerun()

            # Add this in the button_column3 section where the Apply Projection button is defined
            with button_column3:
                if st.button("Apply Projection"):
                    with st.spinner("Applying projection..."):
                        # Get current projection from session state
                        projection_name = st.session_state.current_projection

                        # Render the diagram with the selected projection
                        processed_code, svg_content = application_instance.render_diagram(
                            plant_uml_code,
                            projection_name=projection_name
                        )

                        # Store the results in session state
                        st.session_state.current_diagram = svg_content
                        st.session_state.last_processed_code = processed_code

                        # If successful, store as last successful code
                        if svg_content:
                            st.session_state.last_successful_code = plant_uml_code

                        # Use rerun to refresh the page and show the updated diagram
                        st.rerun()

        with preview_column:
            st.subheader("Diagram Preview")
            # Display the currently active projection name
            if "current_projection" in st.session_state and st.session_state.current_projection != "Full Diagram":
                st.caption(f"Current View: {st.session_state.current_projection}")

            # Render the SVG diagram if available
            if "current_diagram" in st.session_state:
                svg_content = st.session_state.current_diagram

                if isinstance(svg_content, str) and "<svg" in svg_content:
                    # Create scrollable container with CSS
                    scroll_container_style = """
                        <style>
                            .svg-container {
                                max-height: 500px;
                                overflow-y: auto;
                                border: 1px solid #ddd;
                                padding: 10px;
                                background-color: white;
                            }
                        </style>
                    """

                    # Wrap SVG content in a scrollable div
                    scrollable_svg = f"""
                        {scroll_container_style}
                        <div class="svg-container">
                            {svg_content}
                        </div>
                    """

                    # Display with scrolling capability
                    st.components.v1.html(scrollable_svg, height=520)

                else:
                    # Display text or other format
                    st.code(str(svg_content))
            else:
                st.info("Click 'Render Diagram' to see the preview")

            # Export options if we have a diagram
            if "current_diagram" in st.session_state:
                export_col1, export_col2 = st.columns(2)

                with export_col1:
                    svg_content = st.session_state.current_diagram
                    if isinstance(svg_content, str) and "<svg" in svg_content:
                        st.download_button(
                            label="Download SVG",
                            data=svg_content,
                            file_name="uml_diagram.svg",
                            mime="image/svg+xml"
                        )

                with export_col2:
                    if "last_processed_code" in st.session_state:
                        download_code = st.session_state.last_processed_code
                    elif "last_successful_code" in st.session_state:
                        download_code = st.session_state.last_successful_code
                    else:
                        download_code = plant_uml_code

                    st.download_button(
                        label="Download PlantUML Code",
                        data=download_code,
                        file_name="uml_diagram.puml",
                        mime="text/plain"
                    )


class ApplicationMain:
    """Main application class responsible for setup and execution"""

    @staticmethod
    def configure_application():
        """Configures the Streamlit application settings"""
        st.set_page_config(
            page_title=APPLICATION_TITLE,
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="expanded"
        )

    @staticmethod
    def execute_application():
        """Main application entry point that handles navigation and renders pages"""
        ApplicationMain.configure_application()

        # Define available application pages
        application_pages = {
            "Chat": ApplicationPages.render_chat_page,
            "Diagram Editor": ApplicationPages.render_diagram_editor_page,
            "Settings": ApplicationPages.render_configuration_page
        }

        # Navigation sidebar
        with st.sidebar:
            st.title(f"{APPLICATION_TITLE} {APPLICATION_VERSION}")
            current_page = st.session_state.get("current_page", "Chat")
            selected_page = st.radio(
                "Navigation",
                list(application_pages.keys()),
                index=list(application_pages.keys()).index(current_page)
            )
            st.session_state["current_page"] = selected_page

        # Display the selected page
        application_pages[selected_page]()


# Application entry point
if __name__ == "__main__":
    try:
        # Handle command line arguments
        if "--help" in sys.argv or "-h" in sys.argv:
            print(f"{APPLICATION_TITLE} {APPLICATION_VERSION}")
            print("Usage: python UML_Diagram_Generator.py [options]")
            print("\nOptions:")
            print("  -h, --help  Show this help message")
            sys.exit(0)

        # Start the application
        ApplicationMain.execute_application()
    except Exception as error:
        st.error(f"An error occurred: {str(error)}")
        raise error
