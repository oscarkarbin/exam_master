import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:8000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setText(response.data.extracted_text);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  return (
    <div>
      <h1>AI Exam Practice App</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <p>Extracted Text: {text}</p>
    </div>
  );
}

export default App;
