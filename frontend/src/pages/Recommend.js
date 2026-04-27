import React, { useState } from "react";
import { Sparkles, Sprout, Loader2, CheckCircle2 } from "lucide-react";
import { useLanguage } from "../LanguageContext";

function Recommend() {
  const { t } = useLanguage();
  const [soil, setSoil] = useState("Loamy Soil");
  const [season, setSeason] = useState("Kharif (Monsoon)");
  const [water, setWater] = useState("Medium (Some irrigation)");
  
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);

  const generateRecommendations = () => {
    // Simulate AI network delay
    setLoading(true);
    setResults(null);
    
    setTimeout(() => {
      let recs = [];
      
      // Simple rule-based "AI" engine
      if (soil === "Black Soil") {
        recs.push({ name: "Cotton", confidence: "94%", reason: "Black soil retains moisture excellently, which is perfect for cotton's deep root system." });
        if (season === "Kharif (Monsoon)") recs.push({ name: "Soybean", confidence: "88%", reason: "Thrives in black soil during monsoons with moderate water." });
      } else if (soil === "Clay Soil" || water === "High (Canal/River)") {
        recs.push({ name: "Paddy (Rice)", confidence: "96%", reason: "Clay soil holds standing water perfectly, making it ideal for Paddy cultivation." });
        recs.push({ name: "Sugarcane", confidence: "89%", reason: "Requires high water retention and nutrient-rich soil to maximize yield." });
      } else if (soil === "Sandy Soil" || water === "Low (Rainfed only)") {
        recs.push({ name: "Ragi (Finger Millet)", confidence: "92%", reason: "Highly drought-resistant and grows well in sandy, well-drained soils." });
        recs.push({ name: "Groundnut", confidence: "85%", reason: "Sandy soil allows the pegs to penetrate the ground easily for pod development." });
      } else {
        // Defaults for Loamy/Red
        recs.push({ name: "Maize", confidence: "91%", reason: "Loamy soil provides the perfect balance of drainage and nutrients for Maize." });
        recs.push({ name: "Tur Dal (Arhar)", confidence: "86%", reason: "A hardy crop that performs exceptionally well in moderate conditions." });
      }

      setResults(recs);
      setLoading(false);
    }, 1500); // 1.5 seconds loading simulation
  };

  return (
    <div style={styles.container}>
      <div style={styles.headerArea}>
        <div style={styles.sparkleIcon}>
          <Sparkles size={32} color="#fbbf24" />
        </div>
        <h1 style={styles.header}>{t("AI Crop Guide")}</h1>
        <p style={styles.subtitle}>
          {t("ai_subtitle")}
        </p>
      </div>

      <div style={styles.layout}>
        {/* Left Column - Input Form */}
        <div className="glass-panel" style={styles.formCard}>
          <div style={styles.cardHeader}>
            <Sprout size={20} color="var(--accent-primary)" />
            <h3 style={styles.cardTitle}>{t("Land Profile")}</h3>
          </div>

          <div style={styles.inputGroup}>
            <label style={styles.label}>{t("Soil Type")}</label>
            <select style={styles.input} value={soil} onChange={(e) => setSoil(e.target.value)}>
              <option value="Loamy Soil">Loamy Soil</option>
              <option value="Clay Soil">Clay Soil</option>
              <option value="Sandy Soil">Sandy Soil</option>
              <option value="Black Soil">Black Soil</option>
              <option value="Red Soil">Red Soil</option>
            </select>
          </div>

          <div style={styles.inputGroup}>
            <label style={styles.label}>{t("Current Season")}</label>
            <select style={styles.input} value={season} onChange={(e) => setSeason(e.target.value)}>
              <option value="Kharif (Monsoon)">Kharif (Monsoon)</option>
              <option value="Rabi (Winter)">Rabi (Winter)</option>
              <option value="Zaid (Summer)">Zaid (Summer)</option>
            </select>
          </div>

          <div style={styles.inputGroup}>
            <label style={styles.label}>{t("Water Availability")}</label>
            <select style={styles.input} value={water} onChange={(e) => setWater(e.target.value)}>
              <option value="High (Canal/River)">High (Canal/River)</option>
              <option value="Medium (Some irrigation)">Medium (Some irrigation)</option>
              <option value="Low (Rainfed only)">Low (Rainfed only)</option>
            </select>
          </div>

          <button 
            style={styles.calculateBtn}
            onClick={generateRecommendations}
            disabled={loading}
          >
            {loading ? t("Analyzing...") : t("Get Recommendations")}
          </button>
        </div>

        {/* Right Column - Results / Empty State */}
        <div className="glass-panel" style={styles.resultCard}>
          
          {loading && (
            <div style={styles.emptyState}>
              <Loader2 size={48} color="var(--accent-primary)" className="spin-animation" style={{marginBottom: "24px"}} />
              <h2 style={styles.emptyStateTitle}>{t("Generating AI Insights...")}</h2>
              <p style={styles.emptyStateText}>{t("generating_sub")}</p>
            </div>
          )}

          {!loading && !results && (
            <div style={styles.emptyState}>
              <Sprout size={64} color="var(--text-muted)" style={{marginBottom: "24px", opacity: 0.5}} />
              <h2 style={styles.emptyStateTitle}>{t("Awaiting Input")}</h2>
              <p style={styles.emptyStateText}>
                {t("awaiting_sub")}
              </p>
            </div>
          )}

          {!loading && results && (
            <div style={styles.resultsContainer}>
              <h3 style={styles.resultsHeader}>
                <CheckCircle2 size={24} color="var(--accent-primary)" /> 
                {t("AI Recommendations")}
              </h3>
              
              <div style={styles.recsList}>
                {results.map((rec, index) => (
                  <div key={index} className="hover-3d-lift" style={styles.recCard}>
                    <div style={styles.recHeader}>
                      <h4 style={styles.recName}>{rec.name}</h4>
                      <div style={styles.confidenceBadge}>
                        {rec.confidence} {t("Match")}
                      </div>
                    </div>
                    <div style={styles.reasoningBox}>
                      <span style={styles.aiLabel}><Sparkles size={12}/> {t("AI REASONING")}</span>
                      <p style={styles.reasoningText}>{rec.reason}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

      </div>

      <style>{`
        .spin-animation {
          animation: spin 1.5s linear infinite;
        }
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}

const styles = {
  container: {
    fontFamily: "var(--font-main)",
  },
  headerArea: {
    textAlign: "center",
    marginBottom: "48px",
    maxWidth: "600px",
    margin: "0 auto 48px auto",
  },
  sparkleIcon: {
    display: "flex",
    justifyContent: "center",
    marginBottom: "16px",
  },
  header: {
    color: "var(--text-primary)",
    margin: "0 0 12px 0",
    fontSize: "36px",
    fontWeight: "700",
  },
  subtitle: {
    color: "var(--text-muted)",
    margin: 0,
    fontSize: "16px",
    lineHeight: "1.5",
  },
  layout: {
    display: "flex",
    gap: "32px",
    alignItems: "stretch",
  },
  formCard: {
    width: "360px",
    padding: "32px",
    borderRadius: "16px",
    display: "flex",
    flexDirection: "column",
    flexShrink: 0,
  },
  resultCard: {
    flex: 1,
    borderRadius: "16px",
    display: "flex",
    flexDirection: "column",
  },
  cardHeader: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
    marginBottom: "32px",
  },
  cardTitle: {
    margin: 0,
    fontSize: "20px",
    color: "var(--text-primary)",
    fontWeight: "600",
  },
  inputGroup: {
    marginBottom: "24px",
  },
  label: {
    display: "block",
    color: "var(--text-secondary)",
    fontSize: "14px",
    marginBottom: "8px",
    fontWeight: "500",
  },
  input: {
    width: "100%",
    backgroundColor: "var(--bg-main)",
    border: "1px solid var(--border-color)",
    padding: "14px 16px",
    borderRadius: "12px",
    color: "var(--text-primary)",
    fontSize: "15px",
    outline: "none",
    transition: "border-color 0.2s",
    cursor: "pointer",
  },
  calculateBtn: {
    marginTop: "auto",
    width: "100%",
    backgroundColor: "var(--accent-primary)",
    color: "var(--text-on-primary)",
    border: "none",
    padding: "16px",
    borderRadius: "12px",
    fontSize: "16px",
    fontWeight: "600",
    cursor: "pointer",
    transition: "all 0.2s",
  },
  emptyState: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    height: "100%",
    padding: "60px",
    textAlign: "center",
  },
  emptyStateTitle: {
    color: "var(--text-primary)",
    fontSize: "24px",
    margin: "0 0 12px 0",
    fontWeight: "600",
  },
  emptyStateText: {
    color: "var(--text-muted)",
    fontSize: "16px",
    maxWidth: "400px",
    lineHeight: "1.5",
  },
  resultsContainer: {
    padding: "32px",
    display: "flex",
    flexDirection: "column",
    height: "100%",
  },
  resultsHeader: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
    color: "var(--text-primary)",
    fontSize: "24px",
    margin: "0 0 32px 0",
  },
  recsList: {
    display: "flex",
    flexDirection: "column",
    gap: "20px",
  },
  recCard: {
    backgroundColor: "var(--bg-main)",
    border: "1px solid var(--border-color)",
    borderRadius: "12px",
    padding: "24px",
  },
  recHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "16px",
  },
  recName: {
    margin: 0,
    fontSize: "22px",
    color: "var(--text-primary)",
    fontWeight: "600",
  },
  confidenceBadge: {
    backgroundColor: "rgba(52, 211, 153, 0.15)",
    color: "var(--accent-primary)",
    padding: "6px 12px",
    borderRadius: "20px",
    fontSize: "14px",
    fontWeight: "700",
  },
  reasoningBox: {
    backgroundColor: "rgba(251, 191, 36, 0.05)",
    borderLeft: "3px solid #fbbf24",
    padding: "16px",
    borderRadius: "0 8px 8px 0",
  },
  aiLabel: {
    display: "flex",
    alignItems: "center",
    gap: "6px",
    color: "#fbbf24",
    fontSize: "11px",
    fontWeight: "700",
    letterSpacing: "1px",
    marginBottom: "8px",
  },
  reasoningText: {
    margin: 0,
    color: "var(--text-secondary)",
    fontSize: "14px",
    lineHeight: "1.6",
  }
};

export default Recommend;
