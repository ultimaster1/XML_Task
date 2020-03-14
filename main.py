from VAl import transform, valid

xml_path = 'some path'
first_xsd_path = 'some path'
xslt_path = 'some path'
second_xsd_path = 'some path'

def main():
    valid(second_xsd_path,transform(xslt_path,valid(first_xsd_path,xml_path)))

if __name__ == '__main__':
    main()
