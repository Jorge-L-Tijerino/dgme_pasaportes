```mermaid
flowchart TD
    H["Home (/)"]
    P1["Paso 1: Datos Personales (/paso1/)"]
    P2["Paso 2: Agendamiento (/paso2/)"]
    P3["Paso 3: Pago (/paso3/)"]
    C["Confirmación: Ticket (/confirmacion/)"]
    A["Panel Admin (/admin/)"]

    H -->|"CTA Agendar Cita"| P1
    P1 -->|"Guarda paso 1"| P2
    P2 -->|"Guarda paso 2"| P3
    P3 -->|"Genera Cita y Flush"| C
    C -->|"Volver al inicio"| H

    P2 -. "Sin sesión paso 1" .-> P1
    P3 -. "Sin sesión paso 2" .-> P1