from svgpathtools import svg2paths
def bucket():
    paths, attributes = svg2paths('sample.svg')
    total_area = 0
    for i in range(len(attributes)):
        temp_list = attributes[i]["points"].split()
        att_list = []
        for n in range(len(temp_list)):
            att_list.append(temp_list[n].split(","))
        if len(att_list) == 4:
            total_area += (abs(int(att_list[0][0]) - int(att_list[2][0])) - 1) * abs(int(att_list[0][1]) - int(att_list[2][1]))   
    return(total_area)

print(bucket())