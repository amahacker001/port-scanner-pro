import os
from datetime import datetime

def generate_html_report(target, ports, subdomains, output_path="output/report.html"):
    os.makedirs("output", exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Scan Report</title>
        <style>
            body {{
                font-family: Arial;
                background: #0f172a;
                color: #e2e8f0;
                padding: 20px;
            }}
            h1 {{
                color: #38bdf8;
            }}
            .section {{
                margin-top: 20px;
                padding: 15px;
                background: #1e293b;
                border-radius: 10px;
            }}
            ul {{
                padding-left: 20px;
            }}
        </style>
    </head>
    <body>

        <h1>🔍 Scan Report</h1>
        <p><strong>Target:</strong> {target}</p>
        <p><strong>Date:</strong> {now}</p>

        <div class="section">
            <h2>🚪 Open Ports</h2>
            <ul>
                {''.join(f'<li>{p}</li>' for p in ports)}
            </ul>
        </div>

        <div class="section">
            <h2>🌐 Subdomains</h2>
            <ul>
                {''.join(f'<li>{s}</li>' for s in subdomains)}
            </ul>
        </div>

    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[+] HTML report saved to {output_path}")