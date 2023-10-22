import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Load your dataset (CSV file)
data = pd.read_csv(r"C:\Users\Anvisha\Desktop\Reports of sem 7\rospl\crop_data.csv")

# Define the features and target variable
X = data[['Temperature', 'Rainfall', 'Humidity', 'Fertilizer', 'Sunlight']]
y = data['Yield']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Create a function to predict crop yield
def predict_yield():
    try:
        temperature = float(temperature_entry.get())
        rainfall = float(rainfall_entry.get())
        humidity = float(humidity_entry.get())
        fertilizer = float(fertilizer_entry.get())
        sunlight = float(sunlight_entry.get())

        # Make a prediction
        prediction = model.predict([[temperature, rainfall, humidity, fertilizer, sunlight]])

        # Display the prediction
        result_label.config(text=f"Predicted Yield: {prediction[0]:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create the main application window
app = tk.Tk()
app.title("Crop Yield Prediction")

# Set the window size
app.geometry("490x390")

# Add background image with transparency
bg_image = tk.PhotoImage(file=r"C:\Users\Anvisha\Desktop\Reports of sem 7\rospl\crop.png")
bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Make the background slightly transparent
bg_label.image = bg_image
bg_label.configure(bg="#f0f0f0", bd=0, highlightthickness=0) 

label = ttk.Label(app, text="Enter Crop Information:", font=("Arial", 18))
label.grid(column=0, row=0, padx=100, pady=20, columnspan=2, sticky='n')

# Create labels and input fields for user input with some styling
style = ttk.Style()
style.configure("TEntry", padding=5, width=20)

temperature_label = ttk.Label(app, text="Temperature (°C):", font=("Arial", 12))
temperature_label.grid(column=0, row=1, padx=50, pady=5, sticky='w')
temperature_entry = ttk.Entry(app, font=("Arial", 10))
temperature_entry.grid(column=1, row=1, padx=0, pady=5, sticky='w')

rainfall_label = ttk.Label(app, text="Rainfall (mm):", font=("Arial", 12))
rainfall_label.grid(column=0, row=2, padx=50, pady=5, sticky='w')
rainfall_entry = ttk.Entry(app, font=("Arial", 10))
rainfall_entry.grid(column=1, row=2, padx=0, pady=5, sticky='w')

humidity_label = ttk.Label(app, text="Humidity (%):", font=("Arial", 12))
humidity_label.grid(column=0, row=3, padx=50, pady=5, sticky='w')
humidity_entry = ttk.Entry(app, font=("Arial", 10))
humidity_entry.grid(column=1, row=3, padx=0, pady=5, sticky='w')

fertilizer_label = ttk.Label(app, text="Fertilizer (kg/ha):", font=("Arial", 12))
fertilizer_label.grid(column=0, row=4, padx=50, pady=5, sticky='w')
fertilizer_entry = ttk.Entry(app, font=("Arial", 10))
fertilizer_entry.grid(column=1, row=4, padx=0, pady=5, sticky='w')

sunlight_label = ttk.Label(app, text="Sunlight (hours/day):", font=("Arial", 12))
sunlight_label.grid(column=0, row=5, padx=50, pady=5, sticky='w')
sunlight_entry = ttk.Entry(app, font=("Arial", 10))
sunlight_entry.grid(column=1, row=5, padx=0, pady=5, sticky='w')

# Create a custom style for the button with the desired font and size
custom_style = ttk.Style()
custom_style.configure("Custom.TButton", font=("Arial", 14))

# Create a button to make predictions with the custom style
predict_button = ttk.Button(app, text="Predict Yield", command=predict_yield, style="Custom.TButton")
predict_button.grid(column=0, row=6, columnspan=2, padx=10, pady=20, sticky='n')

# Create a label to display the prediction with some styling
result_label = ttk.Label(app, text="", font=("Arial", 12))
result_label.grid(column=0, row=7, padx=10, pady=10, columnspan=2)

# Start the GUI application
app.mainloop()
