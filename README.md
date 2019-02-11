# BioInf_Prj1
http://www.cs.uakron.edu/~duan/class/445/Projects/Project1.htm

Project 1 for Bioinformatics
CS445/545 Introduction to Bioinformatics

 

Project 1

Computer Simulation of PCR

This project involves computer simulation of PCR (Polymerase Chain Reaction). It is to be done in your project group. The effort and responsibilities of the students in a group must be clearly enough delimited and stated in a statement (attached to your project report) so that each of you can be graded fairly and separately.

Introduction

As you’ve figured out, the purpose of PCR (http://en.wikipedia.org/wiki/Polymerase_chain_reaction) is to make huge number of copies of a DNA segment. There are three major steps in PCR: denaturizing, annealing and elongation. Here is a figure that illustrates the process (http://users.ugent.be/~avierstr/principles/pcr.html). Hope it will be helpful for some of our computer science students. On this web site you can also find a computer animation of PCR process (http://users.ugent.be/~avierstr/principles/pcrani.html).

PCR steps

In this project you will write a computer program to simulate the PCR process.

Program Specifications:

 

Your computer program should be written in Python. If any one of you would like to use any other language, he/she needs to get the approval of the entire group.

 

Inputs:

 

1.     You may assume you have favorable experimental conditions throughout your simulation.

2.     Your original DNA template is of n base-pairs (assume n = 2000 for your test case if you generate your template randomly).

3.     The size of the DNA segment to be amplified is m (assume m = 200 if the template is generated randomly).

4.     You may also assume that the length of the original forward and backward primers are fixed at p bases (assume p = 20).

5.     The processivity of the taq polymerase (“fall-off rate”) is d+r, where d is a fixed constant, and r is a random number between [-e, e], (assume d = 200, e=50).

Note: The numbers stated above are rough estimates, not corresponding to the true numbers in any living organism. Use your choices if they make more sense to you. You will get bonus points if it you can add more parameters and some limitations (such as amount of primers, dNTPs, age of taqs, temperature, mutations, …) to your experiment at a later stage after you get the basic things done correctly. I think it’ll be a lot of fun when you see how your results changes with the parameters. Also bonus points will be awarded if your group could present an animation of the simulation process.

 

Simulation:

 

You may simulate only 10 PCR cycles if your computation power is limited, o.w. go for 50 cycles. The initial template can be generated randomly. Primers are designed based on this template. In real life, you might need to use BLAST (http://www.ncbi.nlm.nih.gov/BLAST/) to help you select the primers.

 

You can also run your simulation with a real gene under consideration. For example, you could use the ebola gene as your template. Your simulation could make copies of one coding region of the gene (for example: the region from 10237..10992). Find Ebola sequences here.

 

PCR gel	
 

 

Your output: (What you might see on the gel)

 

1.     Statistics of the PCR products:

(a)   Number of DNA fragments;

(b)  Average length of DNA fragments;

(c)   Distribution of the lengths of the DNA fragments (you may use column chart to show your result).

2.     Other things you find interesting.

 

 

Note: The ladder is a mixture of fragments with known size to compare with the PCR fragments. Notice that the distance between the different fragments of the ladder is logarithmic. Lane 1: PCR fragment is approximately 1850 bases long. Lane 2 and 4: the fragments are approximately 800 bases long. Lane 3: no product is formed, so the PCR failed. Lane 5: multiple bands are formed because one of the primers fits on different places.

 

Submission instructions
Project report. A hard copy of the project report is due at the beginning of the class on the due day. Your report should include the following sections:
1.     Description of PCR, you might want to include some nice pictures;

2.     The data structures and/or algorithms you used in your computer program, with justifications for your choices, you may want to include some diagrams;

3.     Discuss any implementation difficulties you’ve encountered, and how you’ve overcome them.

4.     Results.

5.     Discuss your results. How do the numbers you obtain from the simulation related to what you see on the gel which shows the PCR products.

 

Source code. When you are ready to submit, obtain a printed copy of your program. Remember to sign and attach the required Academic Integrity Pledge cover sheet. The printed program and cover sheet must be turned in to your instructor by the start of class on the date the program is due. You must submit an electronic copy of the program using your Brightplace dropbox. Follow these steps:
1.      Create a folder named jsmith_1 (but use your first initial and last name). 

2.      Place the two zipped folders (Project1Part1.zip, Project2Part2.zip) inside this folder.

3.      Right-click on the folder and choose Send To... Compressed Folder (or use some other Zip utility to archive the entire folder). The goal is to create a zip archive named jsmith_1.zip (your initial and name) that contains the folder which contains two parts of your project. 

4.      Drop this single zipped file to the drop box.

 

Please pay attention to the naming conventions for the submission files. These must be followed exactly in order to receive credit. Invalid submissions will need to be resubmitted with a penalty assessed.

Be sure to electronically submit your working solution before the due date! Do not submit non-working programs. The electronic submission time will be used to assess late penalties (if applicable). 

Grading. Your code will be graded on correctness, efficiency, clarity and elegance.

 
