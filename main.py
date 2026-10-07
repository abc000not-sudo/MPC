'''from fastapi import FastAPI
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
    )'''

'''
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from reportlab.pdfgen import canvas

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP PDF Server Running"}

@app.post("/mcp")
async def mcp(request: Request):

    body = await request.json()
    method = body.get("method")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "tools": [
                    {
                        "name": "generate_pdf",
                        "description": "Generate PDF report"
                    }
                ]
            }
        }

    elif method == "tools/call":

        args = body["params"]["arguments"]

        title = args.get("title", "Report")
        content = args.get("content", "")

        pdf_file = "report.pdf"

        c = canvas.Canvas(pdf_file)

        c.drawString(100, 750, title)
        c.drawString(100, 720, content)

        c.save()

        return {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "message": "PDF generated successfully"
            }
        }

    return JSONResponse(
        status_code=400,
        content={"error": "Unknown method"}
    )
'''

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP PDF Server Running"}

@app.get("/download/{filename}")
def download_pdf(filename: str):
    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=filename
    )

@app.post("/mcp")
async def mcp(request: Request):

    body = await request.json()
    method = body.get("method")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "tools": [
                    {
                        "name": "generate_pdf",
                        "description": "Generate PDF report"
                    }
                ]
            }
        }

    elif method == "tools/call":

        args = body["params"]["arguments"]

        title = args.get("title", "Report")
        content = args.get("content", "")

        pdf_file = "report.pdf"

        c = canvas.Canvas(pdf_file)

        c.drawString(100, 750, title)
        c.drawString(100, 720, content)

        c.save()

        return {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "message": "PDF generated successfully",
                "pdf_url": "https://mpc-uwjm.onrender.com/download/report.pdf"
            }
        }