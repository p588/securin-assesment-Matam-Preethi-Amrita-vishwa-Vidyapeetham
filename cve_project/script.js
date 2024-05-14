fetch('/cves')
    .then(response => response.json())
    .then(cveDetails => {
        const cveList = document.getElementById('cve-list');
        cveDetails.forEach(cve => {
            const cveItem = document.createElement('div');
            cveItem.innerHTML = `<p><strong>CVE ID:</strong> ${cve.cve_id}</p>
                                <p><strong>Description:</strong> ${cve.description}</p>
                                <p><strong>Published Date:</strong> ${cve.published_date}</p>
                                <p><strong>Last Modified Date:</strong> ${cve.last_modified_date}</p>
                                <p><strong>Score:</strong> ${cve.score}</p>`;
            cveList.appendChild(cveItem);
        });
    });