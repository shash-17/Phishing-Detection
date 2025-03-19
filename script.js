async function checkURL() {
    let url = document.getElementById("url").value;
    let resultDiv = document.getElementById("result");
    let loadingDiv = document.getElementById("loading");

    if (!url) {
        resultDiv.innerHTML = "<p class='phishing'>❌ Please enter a valid URL!</p>";
        return;
    }

    // Show loading indicator
    loadingDiv.classList.remove("hidden");
    resultDiv.innerHTML = "";

    let response = await fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    });

    let data = await response.json();
    
    // Hide loading indicator
    loadingDiv.classList.add("hidden");

    let statusClass = data.status.includes("Phishing") ? "phishing" : "safe";

    let details = `
        <p class="${statusClass}"><strong>Status:</strong> ${data.status}</p>
        <p><strong>🔢 Confidence Score:</strong> ${data.confidence}%</p>

        <h3>🛡️ Google Safe Browsing</h3>
        <p><strong>Result:</strong> ${data.google_safe_browsing.status ? "Threat Detected" : "No Threats"}</p>
        <pre>${JSON.stringify(data.google_safe_browsing.details, null, 2)}</pre>

        <h3>📊 IPQualityScore</h3>
        <p><strong>Result:</strong> ${data.ipqualityscore.status ? "Threat Detected" : "No Threats"}</p>
        <pre>${JSON.stringify(data.ipqualityscore.details, null, 2)}</pre>
    `;

    resultDiv.innerHTML = details;
}
