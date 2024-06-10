import spacy
from spacy import displacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = """
In the bustling city of New York, John, a seasoned software engineer, woke up to the sound of his alarm clock blaring at 6:00 AM. He groggily reached out to silence it, thinking about the busy day ahead. As he made his way to the kitchen, the aroma of freshly brewed coffee filled the air.
"Another day, another dollar," John muttered to himself, pouring a cup of coffee. He sat down at the table and glanced at the newspaper headline: "Global Markets Hit Record Highs."
His wife, Emily, a renowned chef, was already busy preparing breakfast. "Good morning, honey," she greeted him cheerfully. "I made your favorite pancakes."
"Thanks, Emily," John replied, smiling. "These look delicious."
After breakfast, John hurriedly dressed and grabbed his laptop bag. The subway ride to his office in Midtown Manhattan was uneventful, but the streets were as crowded as ever. People from all walks of life bustled about, each with their own stories and destinations.
At the office, John had back-to-back meetings. First, he discussed a new project with his team, brainstorming ideas for a revolutionary app. "We need to leverage machine learning to personalize user experiences," he suggested.
Later, he presented a progress report to the company's executives, highlighting recent achievements and future goals. "Our user base has grown by 20% this quarter," John reported confidently.
During lunch, John met with a potential client at a chic downtown restaurant. The conversation flowed smoothly as they discussed partnership opportunities. "Your company's innovative solutions are exactly what we need," the client remarked.
The afternoon was spent coding, debugging, and collaborating with colleagues. By 6:00 PM, John was ready to call it a day. He packed up his things and headed home, feeling a sense of accomplishment.
Back at home, Emily had prepared a sumptuous dinner. They enjoyed a quiet meal together, discussing their respective days. "I had a fantastic cooking class today," Emily shared. "The students were so enthusiastic."
After dinner, John relaxed on the couch, reading a novel by his favorite author. The night gradually settled in, and soon it was time for bed.
As John lay in bed, he reflected on the day's events. It had been a busy but fulfilling day, filled with hard work, meaningful interactions, and simple pleasures. He closed his eyes, ready to embrace whatever tomorrow would bring.
"""

# Process the text
doc = nlp(text)

# Define custom CSS
custom_css = """
    .displacy-ent {
        background: black;
        color: white;
    }
    .displacy-token {
        background: black;
        color: white;
    }
    .displacy-arrow {
        color: white;
    }
"""

# Render the output
html = displacy.render(doc, style="dep", page=True)
html = html.replace("<style>", f"<style>{custom_css}")

# Save the HTML to a file and display it in a browser
with open("displacy_output.html", "w") as f:
    f.write(html)

import webbrowser
webbrowser.open("displacy_output.html")
