from lxml import etree


class Handlevalidation:
    def __init__(self) -> None:
        pass

    def validate(self, xml_path, xsd_path) -> bool:
        xmlschema_doc = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        xml_doc = etree.parse(xml_path)
        result = xmlschema.validate(xml_doc)

        return result
