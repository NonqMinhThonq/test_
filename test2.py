import os
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

# Định nghĩa thư mục lưu trữ file
def get_file_path(file_name, app_env, contract_server):
    base_path = "C:/imprints_html_file"
    env_map = {0: "AWS", 1: "KS", 2: "T2"}
    server_map = {0: "app0", 1: "app1"}
    
    env_folder = env_map.get(app_env, "Unknown")
    server_folder = server_map.get(contract_server, "Unknown")
    
    file_path = os.path.join(base_path, env_folder, server_folder, f"{file_name}.html")
    return file_path

@app.route("/api/showSerialpaso/", methods=["POST"])
def show_serial_paso():
    try:
        data = request.json
        file_name = data.get("file")
        app_env = data.get("app_env")
        contract_server = data.get("contract_server")
        
        if not all([file_name, isinstance(app_env, int), isinstance(contract_server, int)]):
            return jsonify({"success": False, "message": "Invalid input parameters"})
        
        file_path = get_file_path(file_name, app_env, contract_server)
        
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                encoded_content = base64.b64encode(file.read()).decode("utf-8")
            
            return jsonify({
                "success": True,
                "filename": file_name,
                "content": encoded_content,
                "message": "Seal Info response successfully"
            })
        else:
            return jsonify({"success": False, "filename": "", "message": "File not found"})
    
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)