# AI-Powered E-commerce Website on Azure (Ubuntu)

## Made By
- **Name:** Pratham Mehta
- **PRN no:** 24030142014
- **Subject:** Cloud Computing Distributed Systems

## 1. Introduction
Shopy Cloud is an AI-powered e-commerce platform hosted on the Azure cloud using an Ubuntu virtual machine. By leveraging AI technologies, it enhances customer experience, streamlines operations, and ensures efficient management of products and transactions.

## 2. Problem Statement
Traditional e-commerce platforms often struggle with:
- **Personalization:** Difficulty in providing tailored product recommendations.
- **Customer Support:** Delayed and inaccurate responses to user queries.
- **Fraud Detection:** Challenges in identifying and preventing fraudulent transactions.
- **Inventory Management:** Inefficient stock management and demand forecasting.

## 3. Proposed Solution
Shopy Cloud addresses these challenges through:
- **AI Chatbot for Customer Support:** Providing 24/7 automated assistance.
- **Personalized Product Recommendations:** AI-driven insights to enhance shopping experience.
- **Fraud Detection System:** Anomaly detection to identify suspicious activities.
- **Smart Inventory Management:** AI-driven demand forecasting to optimize stock levels.

## 4. Technology Stack
| Component   | Technology Used |
|------------|----------------|
| Frontend   | HTML, CSS, JavaScript |
| Backend    | PHP |
| Database   | MySQL |
| AI Models  | Azure Cognitive Services (Recommendations, Language Understanding, Anomaly Detector) *(Planned for future integration)* |
| Deployment | Azure Virtual Machine (Ubuntu) |
| Web Server | Apache/Nginx |

## 5. Model Selection & Justification
Shopy Cloud plans to integrate Azure Cognitive Services for:
- **Recommendations:** Providing personalized product suggestions.
- **Language Understanding:** Enabling the chatbot to process and understand queries.
- **Anomaly Detection:** Identifying unusual patterns in transactions for fraud prevention.

### Justification:
- **Seamless Integration:** Works effortlessly within the Azure ecosystem.
- **Scalability:** Handles increasing data and traffic efficiently.
- **Cost-Effectiveness:** Pay-as-you-go pricing optimizes cost management.
- **High Accuracy:** Pre-trained AI models ensure robust and reliable performance.

## 6. Technical Architecture
### High-Level Overview:
- Users interact with the platform via a web browser.
- The backend processes user requests, interacts with the database, and integrates AI models.
- AI models provide insights and recommendations to enhance the shopping experience.

## 7. System Workflow
1. **User Browsing:** AI analyzes user behavior to recommend relevant products.
2. **Customer Support:** AI chatbot processes queries and provides automated responses.
3. **Order Processing:** Fraud detection system scans transactions for anomalies.
4. **Inventory Management:** AI forecasts demand and optimizes stock levels.

## 8. Challenges and Considerations
- **Data Security:** Ensuring user data protection and compliance with regulations.
- **AI Model Training & Updates:** Keeping models updated for optimal performance.
- **Cost Optimization:** Managing cloud and AI service expenses efficiently.

## 9. Cloud Deployment Justification
- **Scalability:** Azure provides on-demand resources to handle traffic spikes.
- **Reliability:** High availability and disaster recovery mechanisms ensure stability.
- **Security:** Robust security features protect data and transactions.
- **Cost-Effectiveness:** Pay-as-you-go model ensures budget-friendly scaling.

## 10. Cloud Deployment Details
- **Azure Virtual Machine:** Hosting the platform on an Ubuntu 24.04 VM.
- **GitHub Webhook for Auto-Deployment:**
  - The source code is hosted on GitHub: [ShopyCloud Repository](https://github.com/pratham7723/websitecloud)
  - A GitHub Webhook triggers automatic deployment upon code updates.
  - A listener script on the VM pulls the latest changes and deploys them instantly.
  - Ensures continuous integration without manual intervention.
- **MySQL Database:** Cloud-hosted on the Azure VM to store product, customer, and transaction data.
- **Web Server Configuration:** Apache/Nginx configured with SSL for secure transactions.

## 11. Future Enhancements
- **Voice-Based Shopping:** Implementing voice assistants for hands-free shopping.
- **Augmented Reality (AR):** Enabling virtual try-on for an immersive shopping experience.
- **AI-Driven Fraud Prevention:** Advanced fraud detection mechanisms.
- **AI-Powered Inventory Optimization:** Enhanced stock forecasting for reduced costs.

## 12. Live Demo
Check out the live demo: [Shopy Cloud](https://shopycloud.mooo.com)

## 13. Conclusion
Shopy Cloud harnesses the power of AI and cloud computing to deliver a seamless and intelligent e-commerce experience. Through continuous improvements in AI capabilities and automated cloud deployments, it aspires to become a leading force in the evolving digital commerce landscape.



