# Software Architecture Specification: ATHENA
## Adaptive Tournament Hold'em Engine with Neural Architecture

---

# 1. System Overview

ระบบ **ATHENA** (Adaptive Tournament Hold'em Engine with Neural Architecture) ถูกออกแบบและพัฒนาขึ้นภายใต้แนวคิดสถาปัตยกรรมแบบแยกส่วน (Modular Architecture) เพื่อทำหน้าที่เป็น **Decision Support System (DSS) และ Research Platform** สำหรับโป๊กเกอร์ทัวร์นาเมนต์ 

ระบบเน้นความมั่นคงทางคณิตศาสตร์และตรรกะเชิงกฎเกณฑ์เป็นรากฐานหลัก (Rule-based & Mathematical Foundation) โดยมีปัญญาประดิษฐ์และ Machine Learning เป็นชั้นเสริมประสิทธิภาพ (Enhancement Layer) ที่แยกส่วนออกจาก Core Engine อย่างเด็ดขาด เพื่อให้มั่นใจว่าระบบมีความโปร่งใส สามารถตรวจสอบได้ (Explainable) และปลอดภัยจากการละเมิดกฎข้อกำหนดการให้บริการ (ToS) ของแพลตฟอร์มเกม

---

# 2. Architecture Principles

หลักการออกแบบสถาปัตยกรรมซอฟต์แวร์ของโครงการประกอบด้วย:

* **Strict Modular Decoupling:** แยกส่วนประกอบของระบบออกจากกันอย่างเด็ดขาด โดยเฉพาะการแยก Core Logic ออกจาก AI และ User Interface
* **Core Independent of AI:** ส่วนประมวลผลหลัก (Core/Engine) ต้องทำงานได้สมบูรณ์แบบด้วยตัวเองโดยไม่ต้องพึ่งพาหรือผูกติดกับโมเดล Machine Learning
* **Plug-and-Play AI Enhancement:** ปัญญาประดิษฐ์ถูกออกแบบเป็นโมดูลเสริม (Enhancement Layer) ที่สามารถเปิด-ปิด หรืออัปเกรดได้โดยไม่กระทบต่อความเสถียรของระบบหลัก
* **Multi-Game Extensibility:** สถาปัตยกรรมรองรับการขยายตัวเพื่อรองรับเกมไพ่รูปแบบอื่นๆ ในอนาคต เช่น Omaha และ Short Deck
* **Full Traceability:** ทุกการคำนวณและการตัดสินใจต้องมีข้อมูลนำเข้า ผลลัพธ์ และเส้นทางการประมวลผลที่สามารถตรวจสอบย้อนกลับได้ (Reproducible & Explainable)

---

# 3. High Level Architecture Diagram (Mermaid)

```mermaid
graph TD
    UI[API Layer / Streamlit UI] --> API[Application Gateway]
    
    API --> Core[Core Layer / Game State & Rules]
    Core --> Engine[Engine Layer / Math & GTO Logic]
    
    Engine --> Sim[Simulation Layer / Monte Carlo / ICM]
    Engine --> Mem[Memory Layer / Hand History & State]
    
    Core --> Decision[Decision Layer / Recommendation Builder]
    Sim --> Decision
    Mem --> Decision
    
    Decision --> Intel[Intelligence Layer / ML Enhancement]
    
    subgraph Data & Storage
        Data[Data Layer / CSV & Database]
    end
    
    Mem --> Data
    Intel --> Data
    
    subgraph Plugin & Extensibility
        Plugin[Plugin Architecture / Game Variants: Hold'em, Omaha, Short Deck]
    end
    
    Core -.-> Plugin
