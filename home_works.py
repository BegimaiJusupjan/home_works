with open("data_txt","r") as file:
    lines=file.readlines()


with open("filtered_data_txt","w") as filtered_data:
    for line in lines:
        if line.strip():
            filtered_data.write(line)
















