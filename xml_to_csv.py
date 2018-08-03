import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    #xml_list = []
    value = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        for member in root.findall('object'):
            try:
            
                value.append((root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[1][0].text),
                         int(member[1][1].text),
                         int(member[1][2].text),
                         int(member[1][3].text)
                         ))
                #xml_list.append(value)
            except IndexError:
                print("Differently annotated file : {}".format(xml_file))
            
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(value, columns=column_name)
    return xml_df


def main():
    for folder in ['train','val']:
        image_path = os.path.join(os.getcwd(), ('images/' + folder))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()
