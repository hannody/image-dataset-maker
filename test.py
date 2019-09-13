import image_processing
import data_splitter

from_path = "/home/axis/repos/tennis_vs_baseball/bulk_b/"
to_path = "/home/axis/repos/tennis_vs_baseball/data_set/"

image_processing.process_images(from_path)

data_splitter.distribute_data(from_path, to_path, 0.2, 0.2, "baseball")


from_path = "/home/axis/repos/tennis_vs_baseball/bulk_t/"

to_path = "/home/axis/repos/tennis_vs_baseball/data_set/"

image_processing.process_images(from_path)

data_splitter.distribute_data(from_path, to_path, 0.2, 0.2, "tennisball")
