# day21b_nested_practice.py — Nested JSON/Dictionary Practice

# 3-Level Deep Nested Data (Company -> Departments -> Employees)
company_data = {
    "company_name": "AI Tech Solutions",
    "departments": {
        "development": {
            "team_lead": "Asif",
            "employees": {
                "emp_01": {
                    "name": "Ayesha",
                    "role": "AI Automation Engineer",
                    "skills": ["Python", "OpenAI API", "Requests"]
                }
            }
        },
        "marketing": {
            "team_lead": "Zain",
            "employees": {
                "emp_02": {
                    "name": "Ali",
                    "role": "SEO Specialist",
                    "skills": ["Keyword Research", "GA4"]
                }
            }
        }
    }
}

def practice_nested_parsing():
    print("=== Safely Parsing Nested Data Using .get() ===\n")
    
    # Path 1: Extracting Ayesha's skills (Safe Navigation)
    # .get() use karne se agar koi key missing bhi ho to KeyError nahi aata, balki {} (empty dict) return hoti hai
    dev_dept = company_data.get("departments", {})
    dev_team = dev_dept.get("development", {})
    employees = dev_team.get("employees", {})
    ayesha_data = employees.get("emp_01", {})
    ayesha_skills = ayesha_data.get("skills", [])
    
    print(f"Path 1 (Success) -> Ayesha's Skills: {ayesha_skills}")
    
    # Path 2: Trying to access a non-existent employee or skill safely
    # Agar data mein 'data_science' department nahi hai, tab bhi program crash nahi karega
    ds_dept = company_data.get("departments", {}).get("data_science", {})
    ds_employees = ds_dept.get("employees", {})
    missing_emp_skills = ds_employees.get("emp_99", {}).get("skills", "No Skills Found")
    
    print(f"Path 2 (Safe Fallback) -> Missing Dept Skills: {missing_emp_skills}")

if __name__ == "__main__":
    practice_nested_parsing()