import jinja2

# Define the Terraform template
terraform_template = """
provider "{{ provider_name }}" {
  region = "{{ region }}"
}

resource "{{ resource_name }}" "{{ resource_type }}" {
  ami           = "{{ ami }}"
  instance_type = "{{ instance_type }}"
  {{ additional_config }}
  tags = {
    Name = "{{ name }}"
  }
}
"""

# Prompt the user for input values
provider_name = input("Enter provider name: ")
region = input("Enter region: ")
resource_name = input("Enter resource name: ")
resource_type = input("Enter resource type: ")
ami = input("Enter AMI ID: ")
instance_type = input("Enter instance type: ")
additional_config = input("Enter additional configuration (optional): ")
name = input("Enter name: ")

# Render the Terraform template with the user input values
rendered_terraform = jinja2.Template(terraform_template).render(
    provider_name=provider_name,
    region=region,
    resource_name=resource_name,
    resource_type=resource_type,
    ami=ami,
    instance_type=instance_type,
    additional_config=additional_config,
    name=name,
)

# Prompt the user for a filename and location to save the Terraform file
filename = input("Enter filename to save the Terraform file: ")
filepath = input("Enter filepath to save the Terraform file: ")

# Save the Terraform file as a text file
with open(filepath + '/' + filename + '.txt', 'w') as f:
    f.write(rendered_terraform)
    print("Terraform file saved as " + filename + ".txt at " + filepath)

