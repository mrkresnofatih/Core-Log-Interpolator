import csv
import datareader
import interpolation as itp


def interpolate_core_with_log(
        core_data_filename,
        core_column_names,
        core_depth_column_index,
        log_data_filename,
        log_column_names,
        log_depth_column_index,
        output_filename
):
    # Load Core Data
    actual_core_data_path = "input_core/" + core_data_filename
    core_data = datareader.read_data(actual_core_data_path, core_column_names)

    # Load Log Data
    actual_log_data_path = "input_log/" + log_data_filename
    log_data = datareader.read_data(actual_log_data_path, log_column_names)

    # For each core data, get log data
    core_data_num_of_rows = core_data.shape[0]
    core_data_num_of_cols = core_data.shape[1]
    log_data_num_of_cols = log_data.shape[1]

    # FieldNames
    log_column_names_copy = log_column_names[:]
    log_column_names_copy.pop(log_depth_column_index)
    field_names = core_column_names + log_column_names_copy

    # Open CSV Writer & Interpolate Each Core Data Row from Log Table
    with open("output/" + output_filename, "w", newline="") as wf:
        writer = csv.DictWriter(wf, fieldnames=field_names)
        writer.writeheader()

        for row_index in range(0, core_data_num_of_rows):
            container_dict = {}
            for col_index in range(0, log_data_num_of_cols):
                if col_index != log_depth_column_index:
                    container_dict[log_column_names[col_index]] = itp.interpolate(
                        log_data[:, log_depth_column_index],
                        log_data[:, col_index],
                        core_data[row_index][core_depth_column_index]
                    )
                else:
                    container_dict[log_column_names[col_index]] = core_data[row_index, log_depth_column_index]

            for col_index in range(0, core_data_num_of_cols):
                if col_index != core_depth_column_index:
                    container_dict[core_column_names[col_index]] = core_data[row_index][col_index]
            writer.writerow(container_dict)
    return
