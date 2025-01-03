# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

question_data = [
    {"type": "multiple",
     "difficulty": "medium",
     "category": "Science: Computers",
     "question": "How many bytes are in a single Kibibyte?",
     "correct_answer": "1024",
     "incorrect_answers": ["2400", "1000", "1240"]},
    {"type": "multiple", "difficulty": "medium", "category": "Science: Computers",
     "question": "What did the name of the Tor Anonymity Network orignially stand for?",
     "correct_answer": "The Onion Router",
     "incorrect_answers": ["The Only Router", "The Orange Router",
                           "The Ominous Router"]},
    {"type": "multiple", "difficulty": "medium", "category": "Science: Computers",
     "question": "What does &quot;LCD&quot; stand for?",
     "correct_answer": "Liquid Crystal Display",
     "incorrect_answers": ["Language Control Design", "Last Common Difference",
                           "Long Continuous Design"]},
    {"type": "multiple", "difficulty": "medium", "category": "Science: Computers",
     "question": "What does RAID stand for?",
     "correct_answer": "Redundant Array of Independent Disks",
     "incorrect_answers": ["Rapid Access for Indexed Devices",
                           "Range of Applications with Identical Designs",
                           "Randomized Abstract Identification Description"]},
    {"type": "multiple", "difficulty": "medium", "category": "Science: Computers",
     "question": "In CSS, which of these values CANNOT be used with the &quot;position&quot; property?",
     "correct_answer": "center",
     "incorrect_answers": ["static", "absolute", "relative"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The open source program Redis is a relational database server.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "multiple", "difficulty": "medium", "category": "Science: Computers",
     "question": "Which programming language was developed by Sun Microsystems in 1995?",
     "correct_answer": "Java", "incorrect_answers": ["Python", "Solaris OS", "C++"]},
    {"type": "multiple", "difficulty": "medium", "category": "Science: Computers",
     "question": "What does the term GPU stand for?",
     "correct_answer": "Graphics Processing Unit",
     "incorrect_answers": ["Gaming Processor Unit", "Graphite Producing Unit",
                           "Graphical Proprietary Unit"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
     "correct_answer": "False", "incorrect_answers": ["True"]}
]
