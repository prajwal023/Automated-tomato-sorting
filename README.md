# 🍅 Automated-tomato-sorting
The Automated Tomato Sorting System is an innovative project developed using Python and advanced image processing techniques. This system is designed to streamline the sorting of tomatoes based on their ripeness, size, and quality, improving efficiency in agricultural and food processing industries.

# Key Features:
### Image Capture and Analysis:
The system uses a camera to capture images of tomatoes on a conveyor belt or sorting platform. These images are analyzed in real-time using Python libraries like OpenCV and NumPy.

 * Red: Fully ripe tomatoes
 
 * Yellow: Ripe, but not fully matured
 
 * Green: Unripe, raw tomatoes

Automated Pricing: Each tomato's price is determined by its color:

* Red (Good): ₹1000
* Yellow (Edible): ₹800
* Green (InEdible): ₹300


### Size Measurement:
Image processing techniques such as contour detection and pixel-to-dimension mapping are employed to determine the size of each tomato, ensuring consistent grading.

### Defect Identification:
The system detects surface defects, such as spots, cracks, or discolorations, by analyzing texture and irregularities in the tomato's surface.

### Automated Sorting:
Based on the analyzed parameters, tomatoes are categorized and directed to appropriate bins or sections using robotic arms or pneumatic mechanisms.

## Technologies Used  
- **Programming Language**: Python  
- **Libraries**:  
  - OpenCV: For image processing.  
  - NumPy: For numerical operations.
 
  ## Setup and Installation  
### 1. Clone the repository:
   
   git clone https://github.com/prajwal023/Automated-tomato-sorting.git  

### 2. Navigate to the project directory:
   
     cd automated-tomato-sorting
### 3. Install dependencies using pip:

      pip install opencv-python numpy

### 4. Run the main script:

      python main.py  

## 📸 How It Works
### Load images: 
Place your tomato images in the /images folder.

### Processing: 
The script will classify the tomatoes based on their color and calculate their prices.

### Display Results: 
The system will show the classified images and print the total cost for each category.

## 💡 Future Enhancements
* Integrate additional quality parameters (size, defects, etc.).

* Real-time classification using a webcam or camera feed.

* Deploy the application as a web service.

### Feel free to explore, contribute, or suggest improvements! 🌟

github: https://github.com/prajwal023

linkedin: www.linkedin.com/in/prajwal-‎-759274325
   
  
