from jinja2 import Template

# Read the HTML template
with open("jinja_challenge_template.html") as file:
    template = Template(file.read())

# Render the template with the context
output = template.render(context)

# Save or display output
with open("rendered_output.html", "w") as f:
    f.write(output)
