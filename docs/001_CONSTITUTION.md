# Engineering Constitution: ATHENA
## Adaptive Tournament Hold'em Engine with Neural Architecture

---

## 1. Document Information

* **Document ID:** 001_CONSTITUTION
* **Project Name:** ATHENA
* **Document Type:** Engineering Constitution & Governance Standards
* **Scope:** All software engineers, AI engineers, researchers, and project stakeholders contributing to ATHENA.
* **Core Classification:** Decision Support System and Research Platform (Strictly **NOT** an autonomous poker bot).

---

## 2. Core Principles

รากฐานทางความคิดและปรัชญาหลักในการขับเคลื่อนโครงการ ATHENA ประกอบด้วย:

* **Decision Support & Research Focus:** ระบบถูกสร้างขึ้นเพื่อเป็นเครื่องมือสนับสนุนการตัดสินใจ ฝึกฝน และวิจัยเชิงกลยุทธ์เท่านั้น ห้ามพัฒนาเป็นระบบอัตโนมัติที่เชื่อมต่อหรือควบคุมโต๊ะเกมจริงแบบ Real-time Bot
* **Mathematical & Rule-based Ground Truth:** ตรรกะเชิงกฎเกณฑ์และคณิตศาสตร์ (Rule-based + Mathematical Engine) คือรากฐานหลัก ส่วน Machine Learning เป็นเพียงชั้นเสริม (Enhancement Layer) เท่านั้น
* **Absolute Transparency:** ทุกคำแนะนำและการตัดสินใจของระบบจะต้องมีความโปร่งใส สามารถอธิบายเหตุผล ตรวจสอบ และวัดผลได้

---

## 3. Engineering Rules

กฎเหล็กทางวิศวกรรมซอฟต์แวร์ที่ต้องยึดถือ:

* **No Automated Table Interaction:** ห้ามมีฟังก์ชันการทำงานที่ดึงข้อมูลหน้าจออัตโนมัติ (Screen Scraping) หรือส่งคำสั่งเล่นแทนมนุษย์ไปยังแพลตฟอร์มเกม
* **Modular Decoupling:** แยกส่วนการประมวลผลตรรกะ (Engine Core), ส่วนประสานงานผู้ใช้ (UI Layer), และส่วนวิเคราะห์ข้อมูล (Analytics Layer) ออกจากกันอย่างเด็ดขาด
* **Deterministic Core:** ส่วนคำนวณพื้นฐาน (เช่น Push/Fold และ ICM) ต้องให้ผลลัพธ์ที่ตายตัวและสามารถทำซ้ำได้ (Reproducible) ภายใต้ข้อมูลนำเข้าชุดเดียวกัน

---

## 4. Architecture Rules

กฎระเบียบในการออกแบบสถาปัตยกรรมระบบ:

* **Layered Architecture:** แบ่งโครงสร้างระบบออกเป็นชั้นอย่างชัดเจน ได้แก่ Foundation Layer (Rule-based/Math), Simulation Layer, และ Enhancement Layer (ML)
* **Low Latency Readiness:** ออกแบบโครงสร้างให้รองรับการประมวลผลที่มีประสิทธิภาพ แม้ระบบจะเน้นการใช้งานแบบ Offline/Post-game Analysis เป็นหลัก
* **Stateless Engine Design:** ส่วนประมวลผลตรรกะควรทำงานแบบ Stateless เพื่อให้ง่ายต่อการทดสอบ Unit Testing และการจำลองสถานการณ์ (Simulation)

---

## 5. Coding Standards

มาตรฐานการเขียนโค้ดเพื่อความสะอาดและmaintainable:

* **Clean Code & Readability:** ใช้ชื่อตัวแปร ฟังก์ชัน และคลาสที่สื่อความหมายชัดเจนตามหลักสากล โค้ดต้องอ่านง่ายสำหรับทีมงานทุกคน
* **Type Hinting & Documentation:** สำหรับ Python ต้องระบุ Type Hints ให้ครบถ้วน และมี Docstrings อธิบายการทำงานของฟังก์ชันสำคัญ
* **Error Handling:** จัดการข้อผิดพลาด (Exception Handling) อย่างรัดกุม ห้ามปล่อยให้ระบบล่มจากข้อมูลนำเข้าที่ไม่ถูกต้อง

---

## 6. Testing Standards

มาตรฐานการทดสอบระบบซอฟต์แวร์:

* **Unit Testing:** ฟังก์ชันการคำนวณและตรรกะหลักทั้งหมดต้องมี Unit Tests รองรับ
* **Integration Testing:** ทดสอบการทำงานร่วมกันระหว่างโมดูล เช่น การรับข้อมูลผ่าน UI การประมวลผลผ่าน Engine และการบันทึกลง Hand History Logger
* **Walk-Forward Validation:** สำหรับส่วนวิเคราะห์หรือโมเดล ต้องผ่านการทดสอบย้อนหลังเพื่อป้องกัน Data Leakage

---

## 7. Data Policy

นโยบายการจัดการข้อมูลภายในโครงการ:

* **Data Hygiene:** ข้อมูลประวัติการเล่น (Hand History) และ Dataset ที่ใช้ในการวิเคราะห์ต้องผ่านกระบวนการคัดกรอง Noise และตรวจสอบความถูกต้อง
* **Local Storage Security:** ข้อมูลการบันทึกส่วนบุคคลและ Log การเล่นต้องถูกจัดเก็บอย่างปลอดภัยในรูปแบบที่กำหนด (เช่น CSV หรือ Database ท้องถิ่น)
* **No Sensitive Exfiltration:** ห้ามส่งออกข้อมูลส่วนบุคคลหรือข้อมูลการเล่นออกสู่ภายนอกโดยไม่ได้รับความยินยอม

---

## 8. AI Development Rules

กฎระเบียบในการพัฒนาและใช้งานปัญญาประดิษฐ์:

* **Enhancement Only:** ห้ามใช้ Machine Learning เป็นรากฐานในการตัดสินใจหลักของระบบ โมเดล AI ทำหน้าที่เป็นเพียงตัวเสริมประสิทธิภาพ (Enhancement Layer)
* **Explainability Requirement:** ทุกโมเดล AI หรือระบบพยากรณ์ต้องสามารถอธิบายที่มาของผลลัพธ์หรือคำแนะนำได้ (Explainable AI)
* **Controlled Complexity:** หลีกเลี่ยงการใช้โมเดลที่ซับซ้อนเกินความจำเป็นในช่วงเริ่มต้น เพื่อป้องกันปัญหา Overfitting และความยากในการตรวจสอบ

---

## 9. Model Validation Rules

กฎการตรวจสอบความถูกต้องของโมเดล:

* **Ground Truth Comparison:** ผลลัพธ์จากโมเดล AI หรือชั้นเสริมต้องถูกตรวจสอบเทียบเคียงกับค่ามาตรฐานทางคณิตศาสตร์ (Mathematical Ground Truth) เสมอ
* **Performance Metrics:** การประเมินโมเดลต้องใช้ตัวชี้วัดที่ชัดเจน (เช่น Precision, Recall, Expected Value Error) ก่อนนำมารวมเข้าสู่ระบบหลัก
* **Version Tagging:** ทุกโมเดลที่ผ่านการ Train หรือปรับแต่งจะต้องถูกกำหนดหมายเลขเวอร์ชันอย่างเป็นทางการ

---

## 10. Security Rules

กฎด้านความปลอดภัยของระบบ:

* **Environment Isolation:** แยกสภาพแวดล้อมการพัฒนาและการทดสอบออกจากกันอย่างชัดเจน
* **Dependency Auditing:** ตรวจสอบความปลอดภัยของไลบรารีและแพ็กเกจภายนอก (Third-party packages) เป็นประจำเพื่อป้องกันช่องโหว่
* **Secure File Operations:** การอ่านและเขียนไฟล์ Log ต้องมีการจัดการสิทธิ์และป้องกัน Path Traversal

---

## 11. Documentation Rules

กฎระเบียบเกี่ยวกับการจัดทำเอกสาร:

* **Markdown Format:** เอกสารทั้งหมดต้องจัดทำในรูปแบบ Markdown และเก็บไว้ภายใน Repository ของโครงการ
* **Bilingual Standard:** ใช้ภาษาอังกฤษสำหรับคำศัพท์ทางเทคนิคและชื่อตัวแปร และใช้ภาษาไทยสำหรับคำอธิบายเพื่อให้ทีมงานเข้าใจตรงกัน
* **Living Documentation:** ทุกครั้งที่มีการเปลี่ยนแปลงสถาปัตยกรรมหรือข้อกำหนดสำคัญ จะต้องอัปเดตเอกสาร (เช่น Project Charter และ Constitution) ไปพร้อมกัน

---

## 12. Version Control Rules

กฎระเบียบการควบคุมเวอร์ชันโค้ด (Git & Versioning):

* **Semantic Versioning:** โครงการใช้รูปแบบ `MAJOR.MINOR.PATCH` สำหรับการกำหนดเวอร์ชันซอฟต์แวร์และโมเดล
* **Descriptive Commits:** ข้อความในการ Commit ต้องสื่อความหมายชัดเจนว่าทำอะไรและเพราะเหตุใด
* **Pull Request Review:** การเปลี่ยนแปลงโค้ดหลักต้องผ่านการตรวจสอบ (Code Review) ตามมาตรฐานก่อนรวมเข้าสู่ Main Branch

---

## 13. Definition of Done (DoD)

เกณฑ์การพิจารณาว่างานชิ้นหนึ่งเสร็จสมบูรณ์อย่างแท้จริง:

* **Code Complete:** โค้ดถูกเขียนขึ้นตามมาตรฐาน Clean Code และผ่านการทดสอบ Unit Test พื้นฐาน
* **Documentation Updated:** มีการอัปเดตเอกสารที่เกี่ยวข้องหากมีการเปลี่ยนแปลงฟีเจอร์หรือโครงสร้าง
* **Verified against Charter:** ฟีเจอร์หรือโค้ดนั้นสอดคล้องกับเป้าหมายของโครงการ และไม่อยู่ข่ายละเมิดกฎ Non-Goals (เช่น ไม่ใช่ Real-time Bot)
* **Review Approved:** ได้รับการอนุมัติจากผู้รับผิดชอบโครงการหรือสถาปนิกซอฟต์แวร์

---

## 14. Golden Rules

กฎทองคำ 4 ข้อที่ทุกการตัดสินใจทางวิศวกรรมต้องยึดถือ:

> 1. **Explainable:** ทุกคำแนะนำและการตัดสินใจของระบบต้องอธิบายที่มาได้เสมอ
> 2. **Measurable:** ประสิทธิภาพและความถูกต้องต้องสามารถวัดผลเป็นตัวเลขได้
> 3. **Reproducible:** ผลลัพธ์จากการประมวลผลต้องทำซ้ำได้ภายใต้เงื่อนไขเดิม
> 4. **Testable:** ทุกฟังก์ชันและโมดูลต้องถูกออกแบบมาให้สามารถเขียน Test ตรวจสอบได้


