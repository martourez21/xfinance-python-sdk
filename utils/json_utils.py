import json
import uuid
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        elif hasattr(obj, 'dict'):
            return obj.dict()
        return super().default(obj)


def serialize_json(data: Any) -> str:
    """Serialize data to JSON with custom encoding"""
    return json.dumps(data, cls=CustomJSONEncoder)


def deserialize_json(json_str: str) -> Dict[str, Any]:
    """Deserialize JSON string to dictionary"""
    return json.loads(json_str)


def format_decimal(value: Decimal, precision: int = 2) -> str:
    """Format Decimal value with specified precision"""
    return f"{value:.{precision}f}"