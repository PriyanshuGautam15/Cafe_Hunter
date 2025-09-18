# **Cafe Hunter**

## **Project Overview**

Welcome to Cafe Hunter, a web application designed to help coffee lovers in India find the perfect cafe based on their mood and location. This project is a testament to the challenges and triumphs of modern full-stack development, from architecting a robust backend to crafting a beautiful and responsive frontend.

## **The Development Journey: A Battle for Data**

This project was a significant technical challenge, primarily due to the complexities of fetching reliable, real-world data from multiple external APIs. Initial attempts with different mapping services proved difficult, resulting in persistent errors and incomplete data. It required extensive debugging, meticulous refactoring, and a complete overhaul of the backend strategy.

The core of the challenge was finding a single, reliable source for the diverse data points the application needed: real cafe names, accurate ratings, customer reviews, a menu, and high-quality images. The solution was to pivot to a powerful API that could handle all these requirements seamlessly, transforming a frustrating development cycle into a functional and elegant application. I am proud to have successfully implemented this complex data-fetching logic to bring the app to life.

## **Features**

* **Vibe-Based Search:** Find cafes based on your preferred atmosphere, such as "Calm & Relaxed," "Energetic & Social," "Romantic & Cozy," and more.  
* **Two-Step Location Input:** A precise search flow that first asks for your city and then an optional locality for more relevant results.  
* **Comprehensive Cafe Details:** Each cafe listing provides detailed information, including a star rating, review count, customer reviews, contact information, and a beautiful image gallery.  
* **Integrated Menu Highlights:** Get a glimpse of the cafe's menu directly on the details page.  
* **Full-Screen Image Viewer:** Click on any image to view it in a full-screen, swipeable carousel.  
* **Responsive & Attractive UI:** A clean, cozy, and modern user interface that looks great on both desktop and mobile devices.

### **Screenshots**

## **Technical Stack**

* **Backend:** Python with Flask  
* **Frontend:** HTML5, CSS3 (with Tailwind CSS)  
* **APIs:** SerpApi (Google Maps and Google Images)

## **Installation and Setup**

### **Prerequisites**

* Python 3.x  
* A SerpApi API key (sign up for a free account at [SerpApi](https://serpapi.com/))

### **Steps**

1. **Clone the repository:**  
   git clone \[https://github.com/PriyanshuGautam15/Cafe\_Hunter.git\](https://github.com/PriyanshuGautam15/Cafe\_Hunter.git)  
   cd Cafe\_Hunter

2. **Set up a Python virtual environment:**  
   python \-m venv .venv  
   \# On Windows  
   .venv\\Scripts\\activate  
   \# On macOS/Linux  
   source .venv/bin/activate

3. **Install dependencies:**  
   pip install Flask python-dotenv requests

4. Configure your API key:  
   Create a new file named .env in the root of your project and add your SerpApi key:  
   SERPAPI\_API\_KEY=YOUR\_SERPAPI\_API\_KEY

5. **Run the backend server:**  
   python ap.py

   The server will start at http://127.0.0.1:5000.  
6. Open the frontend:  
   Open the ind.html file in your web browser.

## **Usage**

1. On the homepage, select a "vibe" that matches your mood.  
2. Enter a city and, optionally, a specific locality to refine your search.  
3. Click "Find Cafes," and a list of matching cafes will appear.  
4. Click "Click to explore more" on any cafe to view its details, including a photo gallery, ratings, reviews, and menu highlights.  
5. Click on any image to open the full-screen image viewer.

## **Acknowledgments**

A huge thank you to [SerpApi](https://serpapi.com/) for providing the robust APIs that made this project possible, enabling the retrieval of rich, live data for a seamless user experience.