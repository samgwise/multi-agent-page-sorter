

#! Apply a dict to a prompt template
def apply_to_template(template: str, params: dict):
    return template.format_map(params)