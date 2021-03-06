from box import Box


config_file_name = 'zygoat_settings.yml'

phase_function_names = [
    'create',
    'update',
    'delete',
    'deploy',
    'list',
]
project_dir_names = [
    'backend',
    'frontend',
]

Phases = Box([(t.upper(), t) for t in phase_function_names])
Projects = Box([(t.upper(), t) for t in project_dir_names])
