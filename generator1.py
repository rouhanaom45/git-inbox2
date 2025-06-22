import random
import string
import ast
import os
import astor
import re

# Utility to generate random ML-related names
def random_name(prefixes=["data", "model", "train", "net", "process", "config", "learn", "eval"], length=6):
    prefix = random.choice(prefixes)
    letters = string.ascii_lowercase
    suffix = ''.join(random.choice(letters) for _ in range(length))
    return f"{prefix}_{suffix}_{random.randint(100, 999)}"

# Utility to generate ML-related comments
def random_comment():
    comments = [
        "# Initializing neural network training pipeline",
        "# Configuring hyperparameters for model optimization",
        "# Simulating gradient descent with stochastic updates",
        "# Visualizing performance metrics for analysis",
        "# Applying data augmentation to enhance model robustness",
        "# Setting up GPU-accelerated computation",
        "# Preprocessing input features for training",
        "# Monitoring convergence during training loop",
        "# Generating confusion matrix for evaluation",
        "# Adjusting learning rate dynamically",
    ]
    return random.choice(comments)

# Utility to paraphrase print messages
def random_print_message(original):
    message_map = {
        "Setting up input data pipeline...": [
            "Configuring dataset preprocessing module...",
            "Initializing data transformation pipeline...",
            "Preparing feature extraction workflow...",
            "Setting up input data pipeline...",
            "Starting dataset preprocessing...",
        ],
        "Normalizing feature distributions...": [
            "Normalizing feature distributions...",
            "Scaling input features for consistency...",
            "Standardizing dataset attributes...",
            "Transforming features for model input...",
            "Applying feature normalization...",
        ],
        "Adjusting loss for dataset skew...": [
            "Balancing classes with weight adjustments...",
            "Calculating weights for imbalanced classes...",
            "Adjusting loss for dataset skew...",
            "Compensating for class imbalance...",
            "Configuring weights for class balancing...",
        ],
        "Initializing model architecture...": [
            "Constructing neural network architecture...",
            "Setting up model layers and parameters...",
            "Initializing deep learning model structure...",
            "Building network topology for training...",
            "Preparing model architecture...",
        ],
        "\nVisualizing model training metrics...": [
            "\nGenerating training performance plots...",
            "\nVisualizing model training metrics...",
            "\nCreating plots for training analysis...",
            "\nRendering performance visualization...",
            "\nPlotting training metrics...",
        ],
        "\nGenerating final performance visualizations...": [
            "\nGenerating final performance visualizations...",
            "\nRendering conclusive training metrics...",
            "\nCreating plots for model evaluation...",
            "\nVisualizing final training outcomes...",
            "\nPlotting final model metrics...",
        ],
        "Warning: Metadata retrieval error:": [
            "Warning: Unable to retrieve metadata:",
            "Warning: Metadata loading failed:",
            "Warning: Error accessing metadata:",
            "Warning: Failed to fetch metadata:",
            "Warning: Metadata retrieval error:",
        ],
    }
    for key in message_map:
        if original.startswith(key):
            new_prefix = random.choice(message_map[key])
            return new_prefix + original[len(key):]
    return original

# AST visitor to collect and replace names
class NameReplacer(ast.NodeTransformer):
    def __init__(self, name_map):
        self.name_map = name_map

    def visit_Name(self, node):
        if node.id in self.name_map:
            return ast.Name(id=self.name_map[node.id], ctx=node.ctx)
        return node

    def visit_FunctionDef(self, node):
        if node.name in self.name_map:
            node.name = self.name_map[node.name]
        self.generic_visit(node)
        return node

# AST visitor to replace string literals (print messages)
class StringReplacer(ast.NodeTransformer):
    def visit_Str(self, node):
        if isinstance(node.s, str) and node.s.strip():
            # Skip strings that look like URLs (starting with http:// or https://)
            if node.s.startswith(('http://', 'https://')):
                return node
            return ast.Str(s=random_print_message(node.s))
        return node

# Function to read and parse the principal script
def read_principal_script(filepath):
    try:
        with open(filepath, "r") as f:
            script_content = f.read()
        return ast.parse(script_content)
    except FileNotFoundError:
        raise FileNotFoundError(f"Principal script file '{filepath}' not found")
    except SyntaxError as e:
        raise SyntaxError(f"Invalid syntax in principal script: {str(e)}")

# Generate a unique script
def generate_script(principal_filepath):
    # Read and parse the principal script
    tree = read_principal_script(principal_filepath)
    used_names = set()

    # Collect original variable and function names
    original_names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, (ast.Store, ast.Param)):
            original_names.add(node.id)
        elif isinstance(node, ast.FunctionDef):
            original_names.add(node.name)

    # Create mapping for new names
    name_map = {}
    for name in original_names:
        new_name = random_name()
        while new_name in used_names or new_name in name_map.values():
            new_name = random_name()
        name_map[name] = new_name
        used_names.add(new_name)

    # Apply name replacements
    name_replacer = NameReplacer(name_map)
    modified_tree = name_replacer.visit(tree)

    # Apply string replacements (print messages)
    string_replacer = StringReplacer()
    modified_tree = string_replacer.visit(modified_tree)

    # Add a comment at the top
    modified_tree.body.insert(0, ast.Expr(value=ast.Str(s=random_comment())))

    # Add minimal dummy code after imports
    dummy_code = []
    if random.random() > 0.5:
        dummy_var = random_name()
        dummy_code.append(ast.Assign(
            targets=[ast.Name(id=dummy_var, ctx=ast.Store())],
            value=ast.Call(
                func=ast.Attribute(value=ast.Name(id='np', ctx=ast.Load()), attr='random.randn', ctx=ast.Load()),
                args=[ast.Num(n=random.randint(10, 50)), ast.Num(n=random.randint(5, 10))],
                keywords=[]
            )
        ))
        dummy_code.append(ast.Expr(value=ast.Str(s=random_comment())))

    # Find the last import statement
    last_import_index = 0
    for i, node in enumerate(modified_tree.body):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            last_import_index = i
    insert_index = last_import_index + 1

    # Insert dummy code after the last import
    if dummy_code:
        modified_tree.body[insert_index:insert_index] = dummy_code

    # Check if the script already has a for loop with range(1, 1000000)
    loop_converted = False
    epoch_var = name_map.get('train_yjoucw_593', 'epoch')  # Adjust to the provided model.py's epoch variable
    for node in ast.walk(modified_tree):
        if isinstance(node, ast.For) and isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == 'range':
            args = node.iter.args
            if len(args) == 2 and isinstance(args[0], ast.Num) and args[0].n == 1 and isinstance(args[1], ast.Num) and args[1].n == 1000000:
                loop_converted = True
                break

    # Convert while True to for loop only if not already converted
    if not loop_converted and random.random() > 0.5:
        for node in ast.walk(modified_tree):
            if isinstance(node, ast.While) and isinstance(node.test, ast.Num) and node.test.n == 1:
                node.test = ast.Num(n=1)  # Dummy to bypass while
                node.body = [
                    ast.For(
                        target=ast.Name(id=epoch_var, ctx=ast.Store()),
                        iter=ast.Call(
                            func=ast.Name(id='range', ctx=ast.Load()),
                            args=[ast.Num(n=1), ast.Num(n=1000000)],
                            keywords=[]
                        ),
                        body=node.body,
                        orelse=node.orelse
                    )
                ]
                # Remove epoch += 1 if present
                for body_node in node.body[0].body:
                    if (isinstance(body_node, ast.AugAssign) and
                        isinstance(body_node.target, ast.Name) and
                        body_node.target.id == epoch_var):
                        body_node.op = ast.Pass()
                        body_node.value = ast.Pass()
                        break
                break

    # Convert AST back to code
    modified_code = astor.to_source(modified_tree)

    # Post-process to ensure requests.get line is single-line
    pattern = r"(\w+\s*=\s*requests\.get\()\s*('https?://[^']+',\s*timeout=\d+\))"
    replacement = r"\1\2"
    modified_code = re.sub(pattern, replacement, modified_code, flags=re.MULTILINE)

    # Validate syntax
    try:
        ast.parse(modified_code)
    except SyntaxError as e:
        raise SyntaxError(f"Generated script has invalid syntax: {str(e)}")

    return modified_code

# Generate and save script
def main():
    principal_script = "model.py"
    output_filename = "copy-zara.py"

    try:
        script_content = generate_script(principal_script)
        with open(output_filename, "w") as f:
            f.write(script_content)
        print(f"Generated script: {output_filename}")
    except Exception as e:
        print(f"Error generating script: {str(e)}")

if __name__ == "__main__":
    main()
