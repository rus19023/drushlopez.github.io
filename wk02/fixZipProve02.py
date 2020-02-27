def prompt_filename():
    '''return input("Please enter the data file: ")'''
    filename_to_read = "home/cs241/assign02/rates.csv"
    return filename_to_read


def open_reader(filename):
    with open(filename, "r", encoding="utf-8", newline='') as readfile:
        reader = readfile.readlines()
        return reader


def parse_file(reader):
    comm_rate_count = 0
    comm_rate_total = 0.0
    comm_rate = 0.0
    low_rate = 50000.0
    max_company_info = ''
    min_company_info = ''
    high_rate = 0.0
    for line in reader:
        data1 = line.split(",")
        if comm_rate_count > 0:
            comm_rate = float(data1[6])
            '''if len(data1[0]) == 4:
                data1[0] = "0" + data1[0]'''
            if low_rate > comm_rate:
                min_company_info = "{} ({}, {}) - ${}".format(data1[2], data1[0], data1[3], data1[6])
                low_rate = comm_rate
            if high_rate < comm_rate:
                max_company_info = "{} ({}, {}) - ${}".format(data1[2], data1[0], data1[3], data1[6])
                high_rate = comm_rate
        comm_rate_total += comm_rate
        comm_rate_count += 1
    comm_average = comm_rate_total / comm_rate_count
    print(comm_rate_total, comm_rate_count, comm_average)
    return min_company_info, max_company_info, comm_average


def main():
    filename1 = prompt_filename()
    read_file1 = open_reader(filename1)
    min_company_info, max_company_info, comm_average = parse_file(read_file1)
    print()
    print("The average commercial rate is: {}".format(comm_average))
    print()
    print("The highest rate is:")
    print(max_company_info)
    print()
    print("The lowest rate is:")
    print(min_company_info)


if __name__ == "__main__":
    main()
