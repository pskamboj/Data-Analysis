import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('your_dataset.csv')
summary = data.describe()

plt.figure(figsize=(10, 6))
data['column_name'].hist(bins=30)
plt.title('Distribution of Column Name')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.close()

# Create HTML report
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Analysis Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}
        .container {{
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 20px;
            background: #fff;
            margin-top: 30px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1, h2 {{
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }}
        table, th, td {{
            border: 1px solid #ddd;
        }}
        th, td {{
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        img {{
            display: block;
            margin: auto;
            max-width: 100%;
            height: auto;
        }}
    </style>
</head>
<body>

<div class="container">
    <h1>Data Analysis Report</h1>
    <h2>Summary Statistics</h2>
    <table>
        <thead>
            <tr>
                <th></th>
                {''.join(f'<th>{col}</th>' for col in summary.columns)}
            </tr>
        </thead>
        <tbody>
            {''.join(
                f'<tr><td>{idx}</td>{"".join(f"<td>{val}</td>" for val in summary.loc[idx])}</tr>'
                for idx in summary.index
            )}
        </tbody>
    </table>

    <h2>Histogram</h2>
    <img src="histogram.png" alt="Histogram of Column Name">
</div>

</body>
</html>
"""

# Save HTML report
with open('report.html', 'w') as file:
    file.write(html_content)

print("HTML report generated successfully!")
