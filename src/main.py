from tkinter import Tk, Frame, Button, filedialog, Label
import csv

survey_to_be_processed: str = ""

def prepare_gui_geometry(screen_width: int, screen_height: int) -> str:
    window_width = 400
    window_height = 300

    # Calculate the position to center the window on the screen
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # Set the window size and position
    root_widget.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

def destroy_warning_label(label_to_destroy):
    label_to_destroy.destroy()

def create_warning_label(warning: str):
    label = Label(footer_frame,
                        text=warning,
                        fg="red")
    label.pack()
    root_widget.after(1500, destroy_warning_label, label)

def process_start():
    global survey_to_be_processed
    if survey_to_be_processed:
        # TODO: Should be replaced with the invoke of the algorithms
        with open(survey_to_be_processed, mode='r', newline='') as file:
            data = csv.reader(file)
            for row in data:
                print(row)
    else:
        create_warning_label("Error, no .csv has been loaded")

def close_window():
    root_widget.destroy()

def load_survey():
    global survey_to_be_processed

    survey_to_be_processed = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        title="Select a File"
    )

## GUI CONFIG ##
root_widget = Tk()

root_widget.title("TFM")

prepare_gui_geometry(root_widget.winfo_screenwidth(), root_widget.winfo_screenheight())

# Create a centered Frame to display a start button
middle_frame = Frame(root_widget)
middle_frame.pack(expand=True)

start_button = Button(middle_frame, text="Start!", command=process_start)
start_button.pack(expand=True)

# Create a footer frame and place it at the bottom
footer_frame = Frame(root_widget, height=30)
footer_frame.pack(fill='x', side='bottom')

# Create a close button in the footer frame
close_button = Button(footer_frame, text="Close", command=close_window)
close_button.pack(side='right', padx=10, pady=5)        

load_button = Button(footer_frame, text="Load Data", command=load_survey)
load_button.pack(side="left", padx=10, pady=5)

## GUI CONFIG ##

root_widget.mainloop()


