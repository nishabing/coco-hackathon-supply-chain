# 📦 Supply Chain Anomaly Copilot (Snowflake CoCo CLI Hackathon)

**Track:** Domain-Specific AI Copilot
**Participant:** Nisha Singh (Solo)
**Deployed App:** [INSERT YOUR STREAMLIT APP LINK HERE]

## 1. Problem Brief
Supply chain managers lose hours manually writing SQL across fragmented inventory and supplier tables to identify critical stockouts. This copilot provides real-time, natural-language access to inventory deficits and delayed shipments.

## 2. Architecture 
- **Data Layer:** Snowflake AI Data Cloud (`SUPPLY_CHAIN_DB`)
- **Execution & Reasoning:** Snowflake Cortex CLI (`cortex`) with dynamic context injection (`#`) and domain rules (`@rules.md`).
- **UI Layer:** Streamlit in Snowflake (SiS)

## 3. Impact Statement
Reduces time-to-insight from hours to seconds, preventing stockouts through automated risk flagging. Scalable across thousands of SKUs using Snowflake elastic compute.

## 🚀 Quickstart
1. Run `setup.sql` in Snowflake.
2. Launch `cortex` locally.
3. Inject context: `> #INVENTORY_LOGS` and `> #SUPPLIER_ORDERS`.
4. Apply rules: `> @rules.md Act as the supply chain copilot.`
5. Ask: *"Which electronics are below their reorder threshold? Calculate the exact deficit."*
