### Setup to run project:

1. Start Virtual Environment with the following commands (for Windows):
  - ```python -m venv venv```
  - ```.\venv\Scripts\Activate.ps1```

2. Install Django:
  - ```pip install django```

3. Run application:
  - ```python manage.py runserver```
  - Project should be running and accessible at http://127.0.0.1:8000/

4. To run unit tests:
  - ```python manage.py test```

**Django Admin Panel details:**
- http://127.0.0.1:8000/admin/
- Username: admin
- Password: admin

AI Attribution: AI was used to generate the .gitignore file and for formatting parts of this README file.

### Sample Data (for reference)
The db.sqlite3 database should already be pre-populated with the sample data.
* **Categories:** `Conduit & Raceways`, `Fittings & Bodies`, `Wire & Cable`, `Boxes & Enclosures`, `Fasteners & Hardware`, `Circuit Breakers & Control`, `Tools & Accessories`
* **Tags:** `18AWG`, `4"`, `1"`, `3/4"`, `1/2"`, `Bolt-on`, `Threaded`, `Compression`, `Copper (CU)`, `PVC`, `Plastic`, `Aluminum`, `Steel`
* **Products**:
  
| # | Product Description | Category | Tags |
|---|---------------------|----------|------|
| 1 | 1/2" EMT Conduit - 10FT - Steel | Conduit & Raceways | 1/2", Steel |
| 2 | 3/4" EMT Conduit - 10FT - Steel | Conduit & Raceways | 3/4", Steel |
| 3 | 4" PVC Coated Conduit | Conduit & Raceways | 4", PVC |
| 4 | 1/2" EMT Connector, Compression, Steel | Fittings & Bodies | 1/2", Compression, Steel |
| 5 | 1/2" EMT Coupling, Compression, Steel | Fittings & Bodies | 1/2", Compression, Steel |
| 6 | 1" EMT Coupling, Set Screw, Steel | Fittings & Bodies | 1", Steel |
| 7 | 1/2" Rigid Type LB Aluminum Conduit Body - Series 5 | Fittings & Bodies | 1/2", Aluminum |
| 8 | 1/2" Rigid Type LB Threaded Aluminum Conduit Body with Screw Holes | Fittings & Bodies | 1/2", Threaded, Aluminum |
| 9 | 1/2" Sheet Aluminum Conduit Body Cover - Series 5 | Fittings & Bodies | 1/2", Aluminum |
| 10 | 1-1/4" Deep 4" Square Drawn Outlet Box, 1/2", Steel | Boxes & Enclosures | 4", 1/2", Steel |
| 11 | Southwire C17 (Small) - 27.75"W x 34"T, Steel | Boxes & Enclosures | Steel |
| 12 | 1/2" Clampback / Spacer, Steel | Fasteners & Hardware | 1/2", Steel |
| 13 | 1/2" Rigid Conduit Locknut, Steel | Fasteners & Hardware | 1/2", Steel |
| 14 | 1/2" Chase Nipple, Steel | Fasteners & Hardware | 1/2", Steel |
| 15 | 1/4" X 1-1/4" Slotted Hex Head Anchoring Concrete Screw, Steel | Fasteners & Hardware | Steel |
| 16 | 1/2" Conduit and Pipe Hanger with Bolt, EMT / RMC, Steel | Fasteners & Hardware | 1/2", Steel |
| 17 | Square-D Mini Circuit Breaker, QO, 20A, 1 pole, 120/240BAC, 10kA, bolt on mount | Circuit Breakers & Control | Bolt-on |
| 18 | 1/4" Dia. X 3-1/2" L Pilot Drill Bit, High Speed Steel | Tools & Accessories | Steel |
| 19 | 18AWG Stranded 1/C CU TFFN, PVC-Nylon, Black, 600V | Wire & Cable | 18AWG, Copper (CU), PVC |
| 20 | 18AWG Stranded 1/C CU TFFN, PVC-Nylon, White, 600V | Wire & Cable | 18AWG, Copper (CU), PVC |
| 21 | 18AWG Stranded 1/C CU TFFN, PVC-Nylon, Red, 600V | Wire & Cable | 18AWG, Copper (CU), PVC |
