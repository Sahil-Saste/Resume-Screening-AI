import React, { useState } from 'react';
import { Pie } from 'react-chartjs-2';
import 'chart.js/auto';

const cardStyle = {
  maxWidth: 700,
  margin: '40px auto',
  padding: 32,
  background: '#fff',
  borderRadius: 16,
  boxShadow: '0 4px 24px rgba(0,0,0,0.10)',
  fontFamily: 'Segoe UI, Arial, sans-serif',
};

const headerStyle = {
  color: '#2563eb',
  fontWeight: 700,
  fontSize: 32,
  marginBottom: 8,
  letterSpacing: 1,
};

const subHeaderStyle = {
  color: '#555',
  fontWeight: 500,
  fontSize: 18,
  marginBottom: 24,
};

const labelStyle = {
  fontWeight: 500,
  color: '#333',
  marginBottom: 6,
  display: 'block',
};

const inputStyle = {
  width: '100%',
  padding: '10px 12px',
  borderRadius: 8,
  border: '1px solid #d1d5db',
  marginBottom: 18,
  fontSize: 16,
  fontFamily: 'inherit',
};

const buttonStyle = {
  background: 'linear-gradient(90deg, #2563eb 0%, #1e40af 100%)',
  color: '#fff',
  border: 'none',
  borderRadius: 8,
  padding: '12px 32px',
  fontSize: 18,
  fontWeight: 600,
  cursor: 'pointer',
  boxShadow: '0 2px 8px rgba(37,99,235,0.10)',
  transition: 'background 0.2s',
};

const errorStyle = {
  color: '#dc2626',
  background: '#fee2e2',
  borderRadius: 8,
  padding: '10px 16px',
  marginBottom: 18,
  fontWeight: 500,
};

const resultCard = {
  background: '#f8fafc',
  borderRadius: 12,
  padding: 24,
  marginTop: 24,
  boxShadow: '0 2px 8px rgba(0,0,0,0.04)',
};

const pieContainer = {
  maxWidth: 400,
  margin: '32px auto 0',
  background: '#fff',
  borderRadius: 12,
  boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
  padding: 16,
};

const footerStyle = {
  textAlign: 'center',
  color: '#888',
  marginTop: 40,
  fontSize: 15,
};

function App() {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleJobDescChange = (e) => {
    setJobDesc(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setResult(null);
    if (!file || !jobDesc.trim()) {
      setError('Please upload a PDF and enter a job description.');
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    formData.append('job_description', jobDesc);
    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) throw new Error('API error');
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError('Failed to analyze resume.');
    } finally {
      setLoading(false);
    }
  };

  const pieData = result ? {
    labels: ['Matched Skills', 'Missing Skills'],
    datasets: [
      {
        data: [result.matched_skills.length, result.missing_skills.length],
        backgroundColor: ['#36A2EB', '#FF6384'],
      },
    ],
  } : null;

  return (
    <>
      <div style={cardStyle}>
        <div style={headerStyle}>📄 AI Resume Screening</div>
        <div style={subHeaderStyle}>Upload your resume and paste a job description to see your match!</div>
        <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
          <label style={labelStyle}>Upload Resume (PDF):</label>
          <input type="file" accept="application/pdf" onChange={handleFileChange} style={inputStyle} />
          <label style={labelStyle}>Job Description:</label>
          <textarea
            rows={5}
            style={{ ...inputStyle, resize: 'vertical', minHeight: 80 }}
            value={jobDesc}
            onChange={handleJobDescChange}
            placeholder="Paste job description here"
          />
          <button type="submit" disabled={loading} style={buttonStyle}>
            {loading ? 'Analyzing...' : 'Submit'}
          </button>
        </form>
        {error && <div style={errorStyle}>{error}</div>}
        {result && (
          <div style={resultCard}>
            <h2 style={{ color: '#2563eb', marginBottom: 12 }}>Results</h2>
            <p><strong>Skill Match Score:</strong> {result.skill_match_score}%</p>
            <p><strong>Semantic Similarity Score:</strong> {result.semantic_similarity_score}%</p>
            <p><strong>Combined Relevance Score:</strong> {result.combined_score}%</p>
            <p><strong>Matched Skills:</strong> {result.matched_skills.length > 0 ? result.matched_skills.join(', ') : 'None'}</p>
            <p><strong>Missing Skills:</strong> {result.missing_skills.length > 0 ? result.missing_skills.join(', ') : 'None'}</p>
            <div style={pieContainer}>
              <Pie data={pieData} />
            </div>
          </div>
        )}
      </div>
      <div style={footerStyle}>
        &copy; {new Date().getFullYear()} AI Resume Screening &mdash; Made with FastAPI & React
      </div>
    </>
  );
}

export default App;
