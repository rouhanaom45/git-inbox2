import random
import string
import os
import sys
from io import StringIO
from ruamel.yaml import YAML
import copy
import logging
from collections import Counter
from ruamel.yaml.comments import CommentedMap, CommentedSeq
from ruamel.yaml.scalarstring import LiteralScalarString

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def random_name(prefixes=['setup', 'run', 'config', 'install', 'log', 'trigger', 'find', 'cache'], length=6):
    prefix = random.choice(prefixes)
    letters = string.ascii_lowercase
    suffix = ''.join(random.choice(letters) for _ in range(length))
    return f"{prefix}_{suffix}_{random.randint(100, 999)}"

def random_comment():
    comments = [
        "Initializing workflow for model training",
        "Configuring CI/CD pipeline for ML tasks",
        "Setting up environment for neural network training",
        "Managing dependencies for data processing",
        "Logging workflow execution details",
        "Executing training script with GPU support",
        "Monitoring workflow progress",
        "Generating performance analysis artifacts",
        "Preparing model training environment",
        "Optimizing training pipeline execution",
    ]
    return random.choice(comments)

def random_training_message():
    messages = [
        "echo 'Starting next model training iteration'",
        "echo 'Initiating subsequent training cycle'",
        "echo 'Launching new AI model training run'",
        "echo 'Continuing with next training phase'",
        "echo 'Executing additional model training'",
        "echo 'Proceeding with further training iterations'",
        "echo 'Running next neural network training loop'",
        "echo 'Advancing to subsequent model optimization'",
    ]
    return random.choice(messages)

def read_workflow_file(filepath):
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File '{filepath}' does not exist")
        logging.debug(f"Reading file from: {os.path.abspath(filepath)}")
        yaml = YAML()
        yaml.preserve_quotes = True
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.load(f)
        if not isinstance(data, (CommentedMap, dict)):
            raise ValueError("Parsed YAML is not a dictionary")
        if True in data:
            data['on'] = data.pop(True)
            logging.info("Renamed 'true' to 'on' in parsed data")
        logging.info(f"Successfully read workflow file: {filepath}")
        output_buffer = StringIO()
        yaml.dump(data, output_buffer)
        logging.debug(f"Parsed workflow data:\n{output_buffer.getvalue()}")
        logging.debug(f"Top-level keys: {list(data.keys())}")
        return data
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {e}")
        raise
    except UnicodeDecodeError as e:
        logging.error(f"Encoding error in '{filepath}': {e}")
        raise
    except Exception as e:
        logging.error(f"Error reading workflow file: {e}")
        raise

def validate_yaml_structure(data, context="input"):
    errors = []
    if 'on' not in data:
        errors.append("Missing 'on' key")
        output_buffer = StringIO()
        yaml = YAML()
        yaml.dump(data, output_buffer)
        logging.error(f"{context} data lacks 'on' key. Parsed data:\n{output_buffer.getvalue()}")
    if 'true' in data or True in data:
        errors.append("Invalid 'true' key found")
    if 'jobs' not in data or 'run-model' not in data['jobs']:
        errors.append("Missing 'jobs' or 'run-model'")
    if 'steps' not in data['jobs']['run-model'] or len(data['jobs']['run-model']['steps']) != 10:
        errors.append(f"Expected 10 steps, found {len(data['jobs']['run-model'].get('steps', []))}")
    if errors:
        raise ValueError(f"{context} validation errors: {', '.join(errors)}")
    if data['on'].get('workflow_dispatch') != {}:
        data['on']['workflow_dispatch'] = {}
        logging.info(f"Set workflow_dispatch to empty mapping in {context}")

def check_duplicate_keys(data):
    keys = list(data.keys())
    duplicates = [key for key, count in Counter(keys).items() if count > 1]
    if duplicates:
        raise ValueError(f"Duplicate top-level keys found: {duplicates}")

def generate_workflow(workflow_filepath):
    workflow_data = read_workflow_file(workflow_filepath)
    workflow_data = copy.deepcopy(workflow_data)
    
    check_duplicate_keys(workflow_data)
    validate_yaml_structure(workflow_data, context="input")
    
    used_names = set()
    steps = workflow_data['jobs']['run-model']['steps']
    for step in steps:
        if 'name' in step:
            new_name = random_name()
            while new_name in used_names:
                new_name = random_name()
            step['name'] = new_name
            used_names.add(new_name)
        if 'run' in step and isinstance(step['run'], str) and '\n' in step['run']:
            step['run'] = LiteralScalarString(step['run'])
    logging.info(f"Randomized {len(used_names)} step names")
    
    if len(steps) >= 9 and 'run' in steps[8]:
        new_sleep = random.randint(18000, 18300)
        new_message = random_training_message()
        steps[8]['run'] = LiteralScalarString(f"sleep {new_sleep}\n{new_message}")
        logging.info(f"Modified sleep step: sleep {new_sleep}, message: {new_message}")
    
    if len(steps) >= 2 and 'with' in steps[1] and 'restore-keys' in steps[1]['with']:
        steps[1]['with']['restore-keys'] = LiteralScalarString("${{ runner.os }}-pip-\n")
        logging.info("Fixed 'restore-keys' in cache step")
    
    # Add comments
    output_data = CommentedMap(workflow_data)
    output_data.yaml_set_start_comment(random_comment())
    
    step_comments = [random_comment() if i == 8 or random.random() > 0.5 else None for i in range(len(steps))]
    commented_steps = CommentedSeq()
    for i, step in enumerate(steps):
        if step_comments[i]:
            commented_steps.append(CommentedMap(step))
            commented_steps.yaml_set_comment_before_after_key(len(commented_steps) - 1, before=step_comments[i], indent=4)
        else:
            commented_steps.append(CommentedMap(step))
    
    output_data['jobs']['run-model']['steps'] = commented_steps
    
    # Serialize YAML
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.explicit_start = False  # Omit ---
    yaml.preserve_quotes = True
    
    # Validate output
    output_buffer = StringIO()
    yaml.dump(output_data, output_buffer)
    output_yaml = output_buffer.getvalue()
    logging.debug(f"Generated YAML:\n{output_yaml}")
    
    try:
        yaml_data = yaml.load(output_yaml)
        validate_yaml_structure(yaml_data, context="output")
        check_duplicate_keys(yaml_data)
        logging.info("Generated YAML is valid")
    except Exception as e:
        logging.error(f"Invalid YAML generated: {e}")
        raise
    
    return output_yaml

def main():
    workflow_file = "workflow.yml"
    output_filename = "copy-workflow.yml"
    
    try:
        workflow_content = generate_workflow(workflow_file)
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(workflow_content)
        logging.info(f"YAML Workflow Generated: {output_filename}")
        print(f"YAML {output_filename} Generated")
    except Exception as e:
        logging.error(f"Error generating YAML workflow: {e}")
        raise

if __name__ == "__main__":
    main()
