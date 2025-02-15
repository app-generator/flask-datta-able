import importlib
from sqlalchemy import inspect
from sqlalchemy import or_

def get_model_fk_values(model):
    mapper = inspect(model)
    foreign_keys = []

    for column in mapper.columns:
        if column.foreign_keys:
            foreign_keys.append(column.name)

    return foreign_keys

def get_model_field_names(model, field_type):
    """Returns a list of field names based on the given field type in SQLAlchemy."""
    return [
        column.name for column in model.__table__.columns
        if isinstance(column.type, field_type)
    ]

def name_to_class(name: str):
    try:
        module_name = '.'.join(name.split('.')[:-1])
        class_name = name.split('.')[-1]

        module = importlib.import_module(module_name)
        return getattr(module, class_name)
    except Exception as e:
        print(f"Error importing {name}: {e}")
        return None


def user_filter(request, query, fields, fk_fields=[]):
    value = request.args.get('search')

    if value:
        dynamic_filter = []

        for field in fields:
            if field not in fk_fields:
                dynamic_filter.append(getattr(query.column_descriptions[0]['entity'], field).ilike(f"%{value}%"))

        query = query.filter(or_(*dynamic_filter))

    return query