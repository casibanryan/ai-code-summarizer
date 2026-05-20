from pathlib import Path

class MarkdownExporter:
  def __init__(self, output_filename: str = "README-AI.md"):
    self.output_path = Path(output_filename)

  def generate_report(self, files_collection) -> bool:
    if not files_collection:
      print("⚠️ No data available to export.")
      return False

    # Build the document header
    markdown_content = [
        "# 🤖 Automated Codebase Analysis\n",
        "> This documentation was automatically generated using the Gemini AI Code Summarizer pipeline.\n",
        "---\n",
        "## 🗂️ Project Architecture & Metrics\n",
        "| File Name | Size (Bytes) | Status |",
        "| :--- | :--- | :--- |\n"
    ]

    # 1. Dynamically support both lists and dictionaries for safety
    files_list = files_collection.values() if isinstance(files_collection, dict) else files_collection

    # 2. Append rows to our summary directory table
    for file_model in files_list:
      status = "✅ Analyzed" if file_model.summary and "failed" not in file_model.summary.lower() else "❌ Failed"
      markdown_content.append(f"| `{file_model.filename}` | {file_model.file_size} | {status} |")

    markdown_content.append("\n---\n\n## 📄 Detailed File Breakdowns\n")

    # 3. Append the full rich Gemini summaries for every file
    for file_model in files_list:
      markdown_content.append(f"## 🛠️ File: `{file_model.filename}`\n")
      markdown_content.append(f"**Path:** `{file_model.file_path}`  \n")
      markdown_content.append(f"**File Size:** {file_model.file_size} bytes  \n")
      markdown_content.append("\n### 🧠 AI Analysis Report\n")
      
      # Inject the exact markdown structure returned by analyzer.py
      markdown_content.append(f"{file_model.summary}\n")
      markdown_content.append("\n" + "="*40 + "\n")

    # 4. Write everything cleanly to the file wrapped in a safe try-except block
    try:
      full_text = "\n".join(markdown_content)
      self.output_path.write_text(full_text, encoding="utf-8")
      print(f"💾 Documentation successfully compiled and saved to: **{self.output_path.name}**")
      return True
    except Exception as e:
      print(f"⚠️ Failed to write documentation file to disk: {e}")
      return False