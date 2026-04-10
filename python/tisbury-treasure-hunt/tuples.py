"""Functions to help Azara and Rui locate pirate treasure."""

# Treasure, Coordinates
AZARA_LIST = [
    ("Amethyst  Octopus", "1F"),
    ("Angry Monkey Figurine", "5B"),
    ("Antique Glass Fishnet Float", "3D"),
    ("Brass Spyglass", "4B"),
    ("Carved Wooden Elephant", "8C"),
    ("Crystal Crab", "6A"),
    ("Glass Starfish", "6D"),
    ("Model Ship in Large Bottle", "8A"),
    ("Pirate Flag", "7F"),
    ("Robot Parrot", "1C"),
    ("Scrimshawed Whale Tooth", "2A"),
    ("Silver Seahorse", "4E"),
    ("Vintage Pirate Hat", "7E"),
]

# Location Name, Coordinates, Quadrant
RUI_LIST = [
    ("Seaside Cottages", ("1", "C"), "Blue"),
    ("Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow"),
    ("vDeserted Docks", ("2", "A"), "Blue"),
    ("Spiky Rocks", ("3", "D"), "Yellow"),
    ("Abandoned Lighthouse", ("4", "B"), "Blue"),
    ("Hidden Spring (Island of Mystery)", ("4", "E"), "Yellow"),
    ("Stormy Breakwater", ("5", "B"), "Purple"),
    ("Old Schooner", ("6", "A"), "Purple"),
    ("Tangled Seaweed Patch", ("6", "D"), "Orange"),
    ("Quiet Inlet (Island of Mystery)", ("7", "E"), "Orange"),
    ("Windswept Hilltop (Island of Mystery)", ("7", "F"), "Orange"),
    ("Harbor Managers Office", ("8", "A"), "Purple"),
    ("Foggy Seacave", ("8", "C"), "Purple"),
]


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    (treasure, _) = record
    for t, c in AZARA_LIST:
        if treasure == t:
            return c


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(c for c in coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    (treasure, coordinate) = azara_record
    (azara_coord_1, azara_coord_2) = convert_coordinate(coordinate)
    (location, (rui_coord_1, rui_coord_2), quadrant) = rui_record

    return azara_coord_1 == rui_coord_1 and azara_coord_2 == rui_coord_2


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    (treasure, coordinate) = azara_record
    (location, (rui_coord_1, rui_coord_2), quadrant) = rui_record
    if compare_records(azara_record, rui_record):
        return (treasure, coordinate, location, (rui_coord_1, rui_coord_2), quadrant)

    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    report = ""
    for treasure, _, location, (coord_1, coord_2), quadrant in combined_record_group:
        t = (treasure, location, (coord_1, coord_2), quadrant)
        report += f"{t}\n"
    return report
