from graphviz import Graph
from fpdf import FPDF

# Step 1: Create the graph
dot = Graph(engine='neato')
dot.attr(rankdir='LR')
dot.attr('node', shape='ellipse', fontname='Arial', penwidth='2', fontsize='19')
dot.attr('edge', fontname='Arial', fontsize='18', labelfontsize='17')

nodes = ['Sender', 'Router 1', 'Router 2', 'Router 3', 'Router 4', 'Router 5', 'Destination']
edges = [
    ('Sender', 'Router 1', '6', {'xlp': '1,3.5!'}),
    ('Sender', 'Router 2', '2', {'xlp': '1,1!'}),
    ('Sender', 'Router 3', '4', {'xlp': '2.2,2!'}),
    ('Router 1', 'Router 3', '2', {'xlp': '3,3.7!'}),
    ('Router 1', 'Router 4', '5', {'xlp': '4.2,4.8!'}),
    ('Router 2', 'Router 5', '4', {'xlp': '4.2,0.3!'}),
    ('Router 2', 'Destination', '7', {'xlp': '5.2,-0.2!'}),
    ('Router 3', 'Router 5', '3', {'xlp': '5.2,1.5!'}),
    ('Router 4', 'Router 5', '4', {'xlp': '6.5,3!'}),
    ('Router 5', 'Destination', '2', {'xlp': '7.2,0.3!'}),
]

# Define node positions and sizes
positions = {
    'Sender': '0,2!',
    'Router 1': '2,4!',
    'Router 2': '2,0.5!',
    'Router 3': '4,2.5!',
    'Router 4': '7.2,4.5!',
    'Router 5': '6.2,1.5!',
    'Destination': '8.5,0.3!'
}

for node in nodes:
    dot.node(node, width='1.6', height='1.2', pos=positions[node], shape='ellipse')

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
        self.cell(0, 10, '7', ln=True, align='C')
        self.ln(2)

def draw_dotted_line(pdf, x1, y1, x2, y2, dot_size=0.35, gap=0.75):
    current_x = x1
    while current_x <= x2:
        pdf.rect(current_x, y1 - dot_size / 2, dot_size, dot_size, 'F')
        current_x += dot_size + gap

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
df.cell(0, 6, "5        (a)")

# Question Text
df.set_font('Arial', '', 11)
df.set_x(text_margin)
df.set_font('Arial', '', 11)
df.write(6, "Routers can use Dijkstra's or A* algorithm to find the most optimal paths for packets in ")
df.ln()
df.set_font('Arial', 'B', 11)
df.set_x(text_margin)
df.write(6, "Packet Switched Networks")
df.set_font('Arial', '', 11)
df.write(6, ".")
df.ln()

df.ln(4)
df.set_font('Arial', '', 11)
df.set_x(text_margin)
df.multi_cell(0, 6, "Calculate the shortest distance between the sender and each of the routers/destination in the diagram using Dijkstra's algorithm.")

df.ln(4)
df.set_x(text_margin)
df.set_font('Arial', '', 11)
df.write(6, "Show your working ")
df.set_font('Arial', 'B', 11)
df.write(6, "and")
df.set_font('Arial', '', 11)
df.write(6, " write your answers in the table provided.")
df.ln()

# Diagram
diag_width = df.w - df.l_margin - df.r_margin
diag_width *= 0.9
x_pos = (df.w - diag_width) / 2
df.ln(4)
df.image(graph_path, x=x_pos, w=diag_width)

# Working section
df.ln(6)
df.set_font('Arial', '', 11)
df.set_x(text_margin)
df.cell(0, 6, 'Working', ln=True)

df.ln(8)
line_count = 8
line_gap = 8.5
start_y = df.get_y()
for i in range(line_count):
    y = start_y + i * line_gap
    draw_dotted_line(df, text_margin, y, df.w - df.r_margin, y)

# Answers section
df.set_y(start_y + line_count * line_gap - 2)
df.set_x(text_margin)
df.cell(0, 6, 'Answers', ln=True)

df.ln(6)
routers = ['Router 1', 'Router 2', 'Router 3', 'Router 4', 'Router 5', 'Destination']
avail_w = df.w - text_margin - df.r_margin
tw = avail_w / len(routers)
th = 10

# Table header
df.set_fill_color(240, 240, 240)
df.set_font('Arial', 'B', 11)
df.set_x(text_margin)
for r in routers:
    df.cell(tw, th, r, border=1, align='C', fill=True)
df.ln()

# Table row
df.set_fill_color(255, 255, 255)
df.set_font('Arial', '', 11)
df.set_x(text_margin)
for _ in routers:
    df.cell(tw, th * 1.5, '', border=1)
df.ln()

# Spacer below table
df.ln(th * 1.5 + 8)

# [5] bottom-right
df.set_font('Arial', '', 11)
df.set_x(df.w - df.r_margin - 10)
df.cell(20, -30, '[5]', align='R')

# Footer
df.set_y(df.h - 20)
df.set_font('Arial', '', 8)
df.set_x(text_margin)
avail_w = df.w - text_margin - df.r_margin
df.cell(avail_w / 3, 5, '© ÜCL3S 2025', border=0)
df.cell(avail_w / 3, 5, '9618/32/M/J/25', border=0, align='C')
df.set_font('Arial', '', 10)
df.cell(avail_w / 3, 5, '[Turn over]', border=0, align='R')

# Save
pdf_file = 'dijkstra_question_final.pdf'
df.output(pdf_file)
print(f"PDF generated successfully: {pdf_file}")