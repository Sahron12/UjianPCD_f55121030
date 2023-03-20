import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2


class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Image Processing App')
        self.original_image = None
        self.processed_image = None

        # Create a menu bar
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open', command=self.open_image)
        file_menu.add_command(label='Exit', command=self.root.quit)
        menu_bar.add_cascade(label='File', menu=file_menu)

        process_menu = tk.Menu(menu_bar, tearoff=0)
        process_menu.add_command(label='Grayscale', command=self.grayscale_image)
        process_menu.add_command(label='Minimum', command=self.minimum_filter)
        menu_bar.add_cascade(label='Process', menu=process_menu)

        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label='About', command=self.about)
        menu_bar.add_cascade(label='About', menu=about_menu)

        self.root.config(menu=menu_bar)

        # Create a frame for the original image
        original_frame = tk.Frame(self.root)
        original_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # Create a canvas to display the original image
        self.original_canvas = tk.Canvas(original_frame, width=400, height=400)
        self.original_canvas.pack()

        # Create a label for the original image
        original_label = tk.Label(original_frame, text='Original Image')
        original_label.pack()

        # Create a frame for the processed image
        processed_frame = tk.Frame(self.root)
        processed_frame.pack(side=tk.RIGHT, padx=5, pady=5)

        # Create a canvas to display the processed image
        self.processed_canvas = tk.Canvas(processed_frame, width=400, height=400)
        self.processed_canvas.pack()

        # Create a label for the processed image
        processed_label = tk.Label(processed_frame, text='Processed Image')
        processed_label.pack()

        # Create a frame for the status bar
        status_frame = tk.Frame(self.root)
        status_frame.pack(side=tk.BOTTOM, padx=5, pady=5)

        # Create a status bar
        self.status_bar = tk.Label(status_frame, text='Ready', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(fill=tk.X)

        # Create a dialog for about information
        self.about_dialog = tk.Toplevel(self.root)
        self.about_dialog.title('About')
        about_label = tk.Label(self.about_dialog, text='Image Processing App\n\nCreated by SAHRON ANGELINA IHALAUW NIM F55121030')
        about_label.pack(padx=10, pady=10)
        ok_button = tk.Button(self.about_dialog, text='OK', command=self.about_dialog.withdraw)
        ok_button.pack(padx=10, pady=10)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path)
            self.display_image(self.original_image, self.original_canvas)
            self.status_bar.config(text='Image opened: {}'.format(file_path))
        else:
            self.status_bar.config(text='No image opened')

    def minimum_filter(self):
        if self.original_image:
            gray_image = cv2.cvtColor(cv2.imread(self.original_image.filename), cv2.COLOR_BGR2GRAY)
            filtered_image = cv2.erode(gray_image, None, iterations=3)
            self.processed_image = Image.fromarray(filtered_image)
            self.display_image(self.processed_image, self.processed_canvas)
            self.status_bar.config(text='Minimum filter applied')
        else:
            self.status_bar.config(text='No image opened')

    def grayscale_image(self):
        if self.original_image:
            grayscale_image = self.original_image.convert('L')
            self.processed_image = grayscale_image
            self.display_image(self.processed_image, self.processed_canvas)
            self.status_bar.config(text='Grayscale filter applied')
        else:
            self.status_bar.config(text='No image opened')

    def about(self):
        self.about_dialog.deiconify()

    def display_image(self, image, canvas):
        resized_image = image.resize((400, 400))
        image_tk = ImageTk.PhotoImage(resized_image)
        canvas.image_tk = image_tk
        canvas.delete('all')
        canvas.create_image(0, 0, anchor='nw', image=image_tk)


root = tk.Tk()
app = ImageProcessingApp(root)
root.mainloop()