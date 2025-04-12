# Sales Prediction System

A web-based application that uses machine learning to predict sales based on product pricing, advertising budget, and promotional spending. The system allows users to interactively adjust parameters and visualize predicted sales outcomes to optimize business strategies.

## Features

- Interactive sales prediction based on multiple variables
- User authentication and role-based access control
- Responsive web interface built with Streamlit
- Admin and regular user roles with different access permissions

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sales-prediction-system.git
   cd sales-prediction-system
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Ensure you have the machine learning model file:
   ```
   lm_model_prediction.sav
   ```

5. Create a `config.yaml` file in the root directory with the following structure:
   ```yaml
   credentials:
     usernames:
       admin:
         email: admin@example.com
         name: Admin User
         password: $2b$12$abcdefghijklmnopqrstuvwxyz  # hashed password
         role: admin
       user:
         email: user@example.com
         name: Regular User
         password: $2b$12$abcdefghijklmnopqrstuvwxyz  # hashed password
         role: user
   cookie:
     expiry_days: 30
     key: random_signature_key
     name: sales_prediction_cookie
   preauthorized:
     emails:
       - newuser@example.com
   ```

## Running the Application

1. From the project root directory, run:
   ```
   streamlit run streamlit_app.py
   ```

2. The application will start and be accessible at http://localhost:8501

3. Login using one of the predefined accounts:
   - Admin: username `admin`, password `admin_password`
   - User: username `user`, password `user_password`
   
   Or register a new account through the interface.

## Usage

1. After logging in, you'll be directed to the Sales Predictor page.
2. Use the sliders to adjust:
   - Product price
   - Advertising budget
   - Promotional spending
3. Click the "Click to predict unit sales" button to see the predicted sales result.
4. Experiment with different combinations to find optimal strategies.

## Project Structure

```
sales_prediction/
├── modules/
│   |── nav.py               # Navigation components
│   ├── email_alerts.py      # Email alerts configuration
├── pages/
│   └── sales_predictor.py   # Sales Predictor page
├── lm_model_prediction.sav  # Pre-trained ML model
├── config.yaml              # Authentication configuration
└── requirements.txt         # Dependencies
```

## Technologies Used

- Streamlit - Web application framework
- Pandas - Data manipulation
- Scikit-learn - Machine learning (Linear Regression)
- Streamlit-Authenticator - User authentication
- PyYAML - Configuration management
