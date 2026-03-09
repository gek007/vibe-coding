from collections import deque


def list_example(items: list[int]) -> int:
    labels_tuple = ("sum", "count")
    seen_set = set(items)
    info_dict = {"total": sum(items), "unique": len(seen_set), "label_count": len(labels_tuple)}
    return info_dict["total"]


def tuple_example(items: tuple[int, ...]) -> int:
    items_list = list(items)
    index_map = {idx: value for idx, value in enumerate(items)}
    even_set = {value for value in items if value % 2 == 0}
    return len(items_list) + len(index_map) - len(even_set)


def set_example(items: set[str]) -> bool:
    target_tuple = ("python", "java")
    normalized_list = [value.lower() for value in items]
    normalized_set = set(normalized_list)
    meta_dict = {"size": len(items), "has_python": target_tuple[0] in normalized_set}
    return meta_dict["has_python"]


def dict_example(items: dict[str, int]) -> list[str]:
    keys_list = list(items.keys())
    values_tuple = tuple(items.values())
    positive_values = {value for value in values_tuple if value > 0}
    stats = {"key_count": len(keys_list), "positive_count": len(positive_values)}
    return keys_list if stats["key_count"] >= stats["positive_count"] else []


def string_example(text: str) -> int:
    chars_list = list(text)
    unique_chars = set(chars_list)
    edges_tuple = (text[:1], text[-1:] if text else "")
    info_dict = {"length": len(chars_list), "unique": len(unique_chars), "has_edges": any(edges_tuple)}
    return info_dict["length"]


def deque_example(items: deque[int]) -> int | None:
    snapshot_list = list(items)
    snapshot_set = set(snapshot_list)
    position_map = {idx: value for idx, value in enumerate(snapshot_list)}
    return position_map.get(0) if snapshot_set else None


def bytes_example(data: bytes) -> int:
    values_list = list(data)
    values_set = set(values_list)
    header_tuple = (values_list[0],) if values_list else tuple()
    summary = {"len": len(values_list), "unique": len(values_set), "has_header": bool(header_tuple)}
    return summary["len"]


def bytearray_example(data: bytearray) -> int:
    values_list = list(data)
    bytes_copy = bytes(data)
    grouped = {"sum": sum(values_list), "length": len(bytes_copy)}
    checkpoints = (grouped["sum"], grouped["length"])
    return checkpoints[0]


def initialized_list_example() -> list[int]:
    numbers = [10, 20, 30, 40]
    return numbers
