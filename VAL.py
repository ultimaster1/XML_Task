import lxml.etree as etree
import logging
import os

logging.basicConfig(filename='logs.log', format = '%(asctime)s %(message)s',level=logging.DEBUG)

def valid(xsd_path, xml_path):
    if not xsd_path or not xml_path:
        logging.error('empty file')
        return
    try:
        schema = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(schema)
        document = etree.parse(xml_path)
    except:
        logging.error('error with validation xml by xsd, problem in parsing files')
        return
    try:
        isvalid = xmlschema.validate(document)
        if isvalid:
            logging.info('file ' + os.path.basename(xml_path) + ' successfully validated with ' + os.path.basename(xsd_path))
            return xml_path
        else:
            logging.info('file ' + os.path.basename(xml_path) + ' is invalid based on ' + os.path.basename(xsd_path))
    except:
        err = isvalid.error_log
        for i in err:
            logging.error('error with validation: ' + str(i))


def transform(xslt_path,xml_path):
    if not xslt_path or not xml_path:
        logging.error('empty file')
        return
    try:
        dom = etree.parse(xml_path)
        xslt = etree.parse(xslt_path)
        transform = etree.XSLT(xslt)
    except:
        logging.error('error with transformation xml by xslt, problem with parsing files')
        return

    try:
        newdom = transform(dom)
        newdom.write('result.xml')
        logging.info('file ' + os.path.basename(xml_path) + ' successfully transformed to result.xml using '
                     + os.path.basename(xslt_path))
        return os.path.abspath('result.xml')
    except:
        err = transform.error_log
        for i in err:
            logging.error('error with transformation: ' + str(i))


