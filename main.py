from fastapi import FastAPI
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP PDF Server Running"}

@app.post("/mcp")
def generate_pdf():

    pdf_file = "report.pdf"

    c = canvas.Canvas(pdf_file)

    c.drawString(100, 750, "Sigma Dashboard Report")
    c.drawString(100, 730, "Generated from MCP Server")

    c.save()

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename="report.pdf"
    )