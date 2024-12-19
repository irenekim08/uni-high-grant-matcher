import streamlit as st

# Code and comments arranged in order of appearance on app/being defined

# Introduction
st.title("Uni High Grant Matcher")
st.write(
    "In need of funding but don't know what grant to apply for? Use the Uni Grant Matcher to find your best fit!"
)

# Association (selectbox)
association = st.selectbox(
    "What is the applicant's association with Uni?",
    ("Faculty", "Student"),
    index = None,
    placeholder = "Select association...")

st.write("Displaying grant uses for:", association)




# Empty to 1. be defined based on selected association's offered purposes and 2. make sure generate_results only runs when pill(s) selected
purposes = []


# Uses available for faculty (pill-buttons)
if association == "Faculty":
    
    # Purposes (keys), Grants that cover them (values)
    grants = {"Classroom Supplies": "Uni High Faculty Classroom Needs & Projects Request",
              "Special Opportunity (Non-Uni)": ["Ang Current Use Fund (Professional Development Funding)", "Uni Endowment Fund (Professional Development Funding)"],
              "Conference": "Ang Current Use Fund (Professional Development Funding)",
              "Research/Publication": ["Frankel Fund For Learning Innovation", "Innovations in Learning (Professional Development Funding)", "Teaching Excellence (Makino Awards)"],
              "Activity": ["Innovations in Learning (Professional Development Funding)", "Teaching Excellence (Makino Awards)"],
              "Project Supplies": ["Innovations in Learning (Professional Development Funding)", "Uni Endowment Fund (Professional Development Funding)", "Teaching Excellence (Makino Awards)"],
              "Startup (New program)": ["Uni Endowment Fund (Professional Development Funding)", "Teaching Excellence (Makino Awards)"],
              "Professional Membership": "Uni Endowment Fund (Professional Development Funding)",
              "Travel/Housing/Food": "Teaching Excellence (Makino Awards)"}
    
    purposes = st.pills("Select all purposes for grant", grants.keys(), selection_mode = "multi")

                                                        
# Uses available for student (pill-buttons) 
if association == "Student":  

    # Purposes (keys), Grants that cover them (values)
    grants = {"Conference": "Barbara Lazarus Memorial Fund",
              "Research": ["Barbara Lazarus Memorial Fund", "Frankel Fund For Learning Innovation"],
              "Activity": ["Barbara Lazarus Memorial Fund", "Makino Awards"],
              "Travel/Housing/Food": ["Barbara Lazarus Memorial Fund", "Boren Scholarship", "Makino Awards"],
              "Supplies": ["Barbara Lazarus Memorial Fund", "Boren Scholarship", "Makino Awards"],
              "Scholarship/Special Opportunity": ["Boren Scholarship", "Eastern Illini Electric Cooperative", "The Illinois Odd Fellow-Rebekah Scholarship Program", "Martin Luther King Scholarship"],
              "Study Abroad": ["Boren Scholarship", "McNevin Scholarship"],
              "AP/ACT Prep": ["Boren Scholarship", "McNevin Scholarship"],
              "Camps (academic, arts, athletics)": ["Boren Scholarship", "McNevin Scholarship"]}
    purposes = st.pills("Select all purposes for grant", grants.keys(), selection_mode = "multi") 




# Takes in selected purposes (pill-buttons) and gives list of grants that cover them
def generate_results(purposes: list) -> list:
    """
    Generates a list of grants that cover all of the chosen purposes.

    Args:
            purposes(list):        List containing strings of chosen purpose options.
    
    Returns:
            matches(list):         List containing string titles of matched grants.
    Example:
                (in the case of student)
            >>> generate_results(["Conference"])
                ["Barbara Lazarus Memorial Fund"]
                (in the case of faculty)
            >>> generate_results(["Startup (New Program)", "Travel/Housing/Food])
                ["Teaching Excellence (Makino Awards)"]
    """
    matches = []

    # All grants in first purpose added
    if type(grants[purposes[0]]) != str:
        matches += grants[purposes[0]]
    else:
        matches += [grants[purposes[0]]]
    del purposes[0]
    
    # If more than one purpose is selected, matches is redefined as the grant(s) that cover all purposes
    while len(purposes) > 0:
        matches = [grant for grant in grants[purposes[0]] if grant in matches]
        del purposes[0]
        
    st.write(f"{matches}")
    return [matches]



# All grants (keys), links to the application(values)
grant_links = {"Barbara Lazarus Memorial Fund": "https://www.uni.illinois.edu/sites/default/files/2024-09/Barbara%20Lazarus%20Memorial%20Fund.pdf",
                "Boren Scholarship": "https://www.uni.illinois.edu/sites/default/files/2022-11/Boren_Scholarship.docx",
                "Eastern Illini Electric Cooperative": "https://eiec.org/youth-washington-program",
                "Makino Awards": "https://www.uni.illinois.edu/sites/default/files/2022-11/MAKINO%20AWARD_Enhancing%20Student%20Life.doc",
                "The Illinois Odd Fellow-Rebekah Scholarship Program": "https://ioof-il.org/programs/scholarship-program.html",
                "Frankel Fund For Learning Innovation": "https://www.uni.illinois.edu/sites/default/files/2023-04/Frankel_Fund_for_Learning_Innovation_Application_Revised_4-4-23.docx",
                "McNevin Scholarship": "https://www.uni.illinois.edu/sites/default/files/2024-08/McNevin_Scholarship_Description_and_application_2024.pdf",
                "Martin Luther King Scholarship": "https://www.collegesuccessfoundation.org/scholarship/martin-luther-king-jr-scholarship/#about",
                "Uni High Faculty Classroom Needs & Projects Request": "https://surveys.illinois.edu/sec/1092747534?referrer=",
                "Ang Current Use Fund (Professional Development Funding)": "https://forms.illinois.edu/sec/4072389?referrer=https://shibboleth.illinois.edu/",
                "Innovations in Learning (Professional Development Funding)": "https://forms.illinois.edu/sec/4072389?referrer=https://shibboleth.illinois.edu/",
                "Uni Endowment Fund (Professional Development Funding)": "https://forms.illinois.edu/sec/4072389",
                "Teaching Excellence (Makino Awards)": "https://www.uni.illinois.edu/sites/default/files/2022-11/Makino_Award_Teaching_Excellence.doc"}


# Run generate_results only when purpose(s) selected
if purposes != []:
    st.write(f"Check out:")
    
    for grant in generate_results(purposes):
        st.write(f"{generate_results(purposes)}")
        st.link_button(f"Apply for {grant}", grant_links[grant])

    st.write("For more information on grants and funds at Uni, visit the Uni High website.")
