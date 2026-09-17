<center>
<b>MAT 336 - Information Systems – Fall 2026  

HW 4:  Introduction to Databases (25 points)  
Due:  Th Sep 24, 2026 at the beginning of class</b>
</center>

**Objectives:**
- reinforce relational database design concepts
- designing a database given a set of business practices using E-R modeling and normalization methods
- practice using `markdown` and optionally `Mermaid` 

**Submission:**
- one `markdown (.md)` file 
    - upload the raw `.md` file to the **Canvas** assignment page
    - print a hard-copy to submit in class that shows the formatted text, not the markdown code (note you can export `.md` to .`pdf`)
    - include the answers to **Part I** (you may copy the questions and other content from this `markdown` file for your homework)
    - for **Part II**, include the E-R diagram in the Markdown file **either** as an included graphic (e.g., draw the diagram by hand and scan) **or** using **`Mermaid`** 

**Using Markdown and Mermaid:**
- **Markdown editors**: You may use any Markdown editor you prefer. Some options include [StackEdit](https://stackedit.io/), [Dillinger](https://dillinger.io/), [Notepad++](https://notepad-plus-plus.org/), and [Visual Studio Code](https://code.visualstudio.com/). StackEdit and Dillinger are web-based and require no installation. If you already use Notepad++ or VS Code, you may want to use one of those. Be sure your editor allows you to save the source file and print the rendered version. Refer to the earlier class material for Markdown information and references. 
- The Markdown syntax to include a graphic is:  
    > ```![E-R diagram](er_diagram.png)```  

    where "E-R diagram" is the text to show and `er_diagram.png` is the image file in this folder to use.
- **Mermaid**: Mermaid is optional on this assignment. It allows you to describe an E-R diagram using text that is converted into a graphical representation of the diagram. 
    - To do so, use Mermaid's Entity Relationship Diagram (erDiagram) syntax. See the [Mermaid E-R Diagram documentation](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) for examples and syntax.
    - The [Mermaid Live Editor](https://mermaid.live/) provides an easy way to create and preview your E-R diagram.
    - You can include your Mermaid code within your Markdown file by putting it between the tags \```mermaid and \```, for example this Mermaid code:
        `````
        ```mermaid
        erDiagram
            STUDENT ||--|{ ENROLLMENT : in
            COURSE ||--|{ ENROLLMENT : has
        ```
        `````
        creates this diagram:
        ```mermaid
        erDiagram
            STUDENT ||--|{ ENROLLMENT : in
            COURSE ||--|{ ENROLLMENT : has
        ```

    - If you use Mermaid and your Markdown editor does not display the Mermaid diagram (some do not without an extension), you may submit a separate screen shot of the Mermaid diagram taken from the Mermaid Live Editor (see link above).



## Part I – Database Design Concepts
Read Tutorial A (pages 3- 11) in the Monk text _Problem-Solving Cases in Microsoft Access & Excel_ 16th edition.  Use the description of the talent agency business operations on page 6 to answer the following questions. 
1)	What is the cardinality of the relationship between each pair of entities below?  (Note: you may switch the ordering of a pair as written to help you answer the question)

    a.	Band Member – Band: 
    <br><br>

    b.	Bookings – Band:
    <br><br>

    c.	Bookings – Club:
    <br><br><br>

2)	What assumption is being made by stating the Band and Band Member relationship is one-to-many?

<br><br>

3)	Why isn’t each band member listed in the Band table?  That is, why is it better to make a separate Band Member table?

<br><br>

4)	Could band phone number be used as the primary key in the Band table?  Why or why not.
Note:  There is not necessarily one correct answer.  However, your explanation and assumptions should justify your response.

<br><br>

5)	Why is member name not a good choice for a primary key in the Band Member table?

<br><br>

6)	Could we create a compound key from Band Name and Booking Date in the Bookings table?  Why or why not?  Note:  There is not necessarily one correct answer.  However, your explanation and assumptions should justify your response.

<br><br>

7)	Why shouldn’t we include Club Phone Number in the Bookings table? 

<br><br>

8)	Why isn’t the agent’s fee included in the Bookings table?

<br><br>

9)	Describe what would change in the database design if it was possible for a band member to play more than one instrument, i.e. if any table(s) would need to be added and if so, what the relationship(s) is/are.

<br><br>

10)	What is a foreign key and what is its purpose?  State the foreign key(s) that show up in the talent agency business.
<br><br><br><br>
## Part II – Database Design, E-R Modeling, and Normalization
Read the IBM reference _Entity Relationship Modeling with UML_, posted in the course repo under the hw04 Assignment. **Initial here to indicate you completed the reading**:  __________

Read the practice database design problem from **Tutorial A** (pages 11-12) in the **Monk text**.  Create the **E-R diagram** for the library database using `Mermaid`, another tool, or sketching by hand.  Denote primary keys for each table and ensure your tables are in 3rd normal form.  Follow all the rules for submission stated at the beginning of this homework assignment.
