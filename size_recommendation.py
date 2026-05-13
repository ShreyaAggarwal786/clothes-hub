
def recommend_size(gender, height, chest, waist, hips):
    if gender == \"Men\":
        if chest < 91: return \"XS\"
        elif chest < 97: return \"S\"
        elif chest < 103: return \"M\"
        elif chest < 109: return \"L\"
        elif chest < 115: return \"XL\"
        else: return \"XXL\"
    else:
        if chest < 82: return \"XS\"
        elif chest < 88: return \"S\"
        elif chest < 94: return \"M\"
        elif chest < 101: return \"L\"
        elif chest < 108: return \"XL\"
        else: return \"XXL\"

def get_recommendation_html(gender, height, chest, waist, hips):
    size = recommend_size(gender, height, chest, waist, hips)
    html = f\"\"\"
    <div style=\"background-color: #f0f8ff; padding: 15px; border-radius: 10px; border: 1px solid #add8e6; text-align: center; margin-top: 20px;\">
        <h3 style=\"margin-top: 0; color: #0056b3;\">?? Size Recommendation</h3>
        <p style=\"font-size: 28px; font-weight: bold; color: #007bff; margin: 10px 0;\">{size}</p>
        <p style=\"font-size: 14px; color: #555;\">Recommended based on your measurements.</p>
    </div>
    \"\"\"
    return html

