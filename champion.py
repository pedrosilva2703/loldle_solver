import xml.etree.ElementTree as ET
#Adapted from ChatGPT 3.5

class Champion:
    def __init__(self, xml_element):
        self.name = xml_element.find("name").text
        self.gender = xml_element.find("gender").text
        self.positions = [pos.text for pos in xml_element.find("positions")]
        self.species = [specie.text for specie in xml_element.find("species")]
        self.resource = xml_element.find("resource").text
        self.range = [range_type.text for range_type in xml_element.find("range")]
        self.regions = [region.text for region in xml_element.find("regions")]
        self.release_year = int(xml_element.find("release_year").text)

    def display_info(self):
        print(f"Champion: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Positions: {self.positions}")
        print(f"Species: {self.species}")
        print(f"Resource: {self.resource}")
        print(f"Range: {self.range}")
        print(f"Regions: {self.regions}")
        print(f"Release Year: {self.release_year}")


def load_champions_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return [Champion(champion_xml_element) for champion_xml_element in root.findall("champion")]
