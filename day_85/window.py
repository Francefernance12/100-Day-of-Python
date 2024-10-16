from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WaterMarker:

    def __init__(self):
        self.window = Tk()
        self.window.title("Image Watermarker")
        self.window.minsize(width=400, height=300)
        self.window.geometry("450x500")

        # Image
        self.image_path = None
        self.image = None

        # Upload Image
        label = Label(self.window, text="Image Watermarker", font=("Arial", 16))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        upload_button = Button(self.window, text="Upload Image", command=self.imageUploader)
        upload_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Image
        self.image_label = Label(self.window)
        self.image_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Apply Watermark
        watermark_label = Label(self.window, text="Watermark Text:", font=("Arial", 12))
        watermark_label.grid(row=3, column=0, pady=10)

        self.watermark_entry = Entry(self.window, width=30)
        self.watermark_entry.grid(row=3, column=1, pady=10)

        watermark_button = Button(self.window, text="Apply Watermark", command=self.apply_watermark)
        watermark_button.grid(row=4, column=0, columnspan=2, pady=10)

        # save watermarked image
        save_button = Button(self.window, text="Save Watermarked", command=self.save_watermark)
        save_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Exit
        self.window.mainloop()

    def imageUploader(self):
        fileTypes = [("Image files", "*.png *.jpg *.jpeg *.gif")]
        path = filedialog.askopenfilename(filetypes=fileTypes)
        if path:
            self.image_path = path
            self.image = Image.open(path)

            # Display the resized image (keep original size for watermarking)
            self.display_image(self.image)

    # Helper function to resize image for display purposes
    def display_image(self, image):
        resized_image = image.resize((400, 300))  # Resize only for display
        pic = ImageTk.PhotoImage(resized_image)

        self.window.geometry("560x500")
        self.image_label.config(image=pic)
        self.image_label.image = pic  # Keep reference to the image

    def apply_watermark(self):
        # prep
        watermark_text = self.watermark_entry.get()
        watermarked_image = self.image.copy()  # Keep original size for watermarking
        draw = ImageDraw.Draw(watermarked_image)
        font = ImageFont.truetype("arial.ttf", 40)

        # position the text
        text_position = (watermarked_image.width - 200, watermarked_image.height - 50)

        # draw watermark
        draw.text(xy=text_position, text=watermark_text, font=font)

        # Display the resized watermarked image for preview
        self.display_image(watermarked_image)

        # Store the watermarked image at its original size for saving later
        self.watermarked_image = watermarked_image

    def save_watermark(self):
        if hasattr(self, 'watermarked_image'):
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                self.watermarked_image.save(save_path)  # Save the full-size watermarked image
                print("Watermarked image saved to", save_path)


WaterMarker()
