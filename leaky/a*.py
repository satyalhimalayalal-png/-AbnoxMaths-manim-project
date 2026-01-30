from graphviz import Graph
from fpdf import FPDF

# Step 1: Create the graph
dot = Graph(engine='neato')
dot.attr(rankdir='LR')
dot.attr('node', shape='ellipse', fontname='Arial', penwidth='2', fontsize='19')
dot.attr('edge', fontname='Arial', fontsize='18', labelfontsize='17')

nodes = ['Sender', 'Router 1', 'Router 2', 'Router 3', 'Router 4', 'Router 5', 'Receiver']
edges = [
    ('Sender', 'Router 1', '6', {'xlp': '1,3.5!'}),
    ('Sender', 'Router 2', '2', {'xlp': '1,1!'}),
    ('Sender', 'Router 3', '4', {'xlp': '2.2,2!'}),
    ('Router 1', 'Router 3', '2', {'xlp': '3,3.7!'}),
    ('Router 1', 'Router 4', '5', {'xlp': '4.2,4.8!'}),
    ('Router 2', 'Router 5', '4', {'xlp': '4.2,0.3!'}),
    ('Router 2', 'Receiver', '7', {'xlp': '5.2,-0.2!'}),
    ('Router 3', 'Router 5', '3', {'xlp': '5.2,1.5!'}),
    ('Router 4', 'Router 5', '4', {'xlp': '6.5,3!'}),
    ('Router 5', 'Receiver', '2', {'xlp': '7.2,0.3!'}),
]

positions = {
    'Sender': '0,2!',
    'Router 1': '2,4!',
    'Router 2': '2,0.5!',
    'Router 3': '4,2.5!',
    'Router 4': '7.2,4.5!',
    'Router 5': '6.2,1.5!',
    'Receiver': '8.5,0.3!'
}

heuristics = {
    'Sender': 10,
    'Router 1': 8,
    'Router 2': 7,
    'Router 3': 6,
    'Router 4': 4,
    'Router 5': 3,
    'Receiver': 0
}

# Add nodes with heuristic labels
for node in nodes:
    label = f"{node}\nh={heuristics[node]}"
    dot.node(node, label=label, width='1.6', height='1.2', pos=positions[node], shape='ellipse')

# Add edges with weights and positions
for u, v, w, edge_attrs in edges:
    dot.edge(u, v, xlabel=w, **edge_attrs)

# Render graph
graph_path = 'dijkstra_graph.png'
dot.render('dijkstra_graph', format='png', cleanup=True)

# Step 2: Create the PDF
class DijkstraPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, '8', ln=True, align='C')
        self.ln(2)
# Initialize PDF
df = DijkstraPDF(unit='mm', format='A4')
df.set_left_margin(34)
df.set_right_margin(25)
df.set_auto_page_break(auto=True, margin=15)
df.add_page()

# Margins
leftmost_margin = 15
text_margin = 33

# Question Label
df.set_font('Arial', 'B', 11)
df.set_x(leftmost_margin)
df.cell(0, 6, "          (b)")
df.set_font('Arial', '', 11)
df.set_x(text_margin)
df.multi_cell(0, 6, "Now, find the shortest path between the sender and the receiver in the diagram using A* algorithm.")

df.ln(4)
df.set_x(text_margin)
df.set_font('Arial', '', 11)
df.write(6, "Show your working in the table provided.")
df.ln()

# Diagram
diag_width = df.w - df.l_margin - df.r_margin
diag_width *= 0.9
x_pos = (df.w - diag_width) / 2
df.ln(4)
df.image(graph_path, x=x_pos, w=diag_width)

# --- Working Table Section ---
df.ln(6)
df.set_font('Arial', 'B', 11)
df.set_x(text_margin)
df.cell(0, 6, 'Working', ln=True)

df.ln(4)
headers = ['Node', 'Cost from Home Node (g)', 'Heuristic (h)', 'Total (f = g + h)']
col_widths = [20, 55, 40, 40]  # Total = 180, aligns well with A4 text area

# Draw table header
df.set_font('Arial', 'B', 11)
df.set_fill_color(240, 240, 240)
df.set_x(text_margin)
for header, width in zip(headers, col_widths):
    df.cell(width, 10, header, border=1, align='C', fill=True)
df.ln()

# Draw empty rows
df.set_font('Arial', '', 11)
df.set_fill_color(255, 255, 255)
for _ in range(8):
    df.set_x(text_margin)
    for width in col_widths:
        df.cell(width, 10, '', border=1)
    df.ln()

# Answer section
df.ln(10)
df.set_x(text_margin)
df.set_font('Arial', 'B', 11)
df.cell(0, 6, 'Answer', ln=True)
df.ln(2)
# Set font for the first cell (bold for 'Final Path')
df.set_font('Arial', 'B', 11)  

# Set the fill color before creating the cells (light gray or white for the background)
df.set_fill_color(240, 240, 240)  # You can change this color as desired

# Table header (Final Path in bold, empty cell)
df.set_x(text_margin)  # Set position for the left column
df.cell(30, 10, 'Final Path', fill=True, border=1, align='C')  # First cell with "Final Path"
df.set_font('Arial', '', 11)  # Change to normal font for the second cell
df.cell(125, 10, '', fill=False, border=1, align='C')  # Empty second cell, now filled with background color

df.ln(6)  # Space after the table for a line break or additional content
# Final table row line break
df.ln(23)
# Marks
df.set_font('Arial', '', 11)
df.set_x(df.w - df.r_margin - 10)
df.cell(20, -30, '[5]', align='R')
df.set_x(df.w - df.r_margin - 10)
df.cell(20, -10, '[Total: 10]', align='R')

# Footer
df.set_y(df.h - 20)
df.set_font('Arial', '', 8)
df.set_x(text_margin)
avail_w = df.w - text_margin - df.r_margin
df.cell(avail_w / 3, 5, '© ÜCL3S 2025', border=0)
df.cell(avail_w / 3, 5, '9618/32/M/J/25', border=0, align='C')

# Save
pdf_file = 'a*.pdf'
df.output(pdf_file)
print(f"PDF generated successfully: {pdf_file}")