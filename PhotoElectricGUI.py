import tkinter as tk

def CreateSlider(app):
    # Create a new Tkinter window for the slider
    SliderWindow = tk.Toplevel(app)
    # Create a Scale widget for the slider
    slider = tk.Scale(SliderWindow, from_=250, to=750,
                       orient=tk.HORIZONTAL,
                       length=400,
                       label="Wavelength (nm)",
                       tickinterval=100,
                       command=lambda value: OnSliderChanged(app, value))
    # Pack the Scale widget
    slider.pack()
    # Define the callback function for the slider
    def OnSliderChanged(app, slider_value):
        # Calculate the frequency of the radiation source using c = λν
        c = 3.00 * 10**8  # speed of light in m/s
        wavelength = slider_value / 10**9  # wavelength in meters
        frequency = c / wavelength  # frequency in Hz
        # Update the value of the radiation source in the main window
        app.radiation_source.wavelength = wavelength
        app.radiation_source.frequency = frequency
        # Update the label displaying the frequency of the radiation source
        app.frequency_label.config(text=f"Frequency: {frequency:.3f} THz")  