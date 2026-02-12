# This is a simple program to count the quantity of words in a text and to write a resume of the passage.
# count the quantity of word from the next text.
text = """
The implementation of the computarized voting system is considered to be used in US elections,
changing the old manual system. But all this has a big problem of confidence in the system.
The people do not trust because the lack of experience using this kind of technology. However, 
the advantages of using this system helps a lot to people who has some disability, making the voting
more inclusive and accessible. Also, the counting process is way faster than the manual one, reducing the time
to have the final results. Another advantage is the reduction of human error, which can happen in the manual counting.
In conclusion, the computarized voting system has both advantages and disadvantages. 
One thing very crucial in the implementation of this is that a single error in the system can cause a
big problem because this could change the results of an election when this ones are too close.
But considering that the banks use and trust in this kind of technology, the computarized voting system
could be a good option to improve the elections in the US.
"""
word_count = len(text.split())
#print("The total number of words in the text is:", word_count)

text2 = """
To choose sides about this statement I would take in count which are my personal goal to be in
the class with that professor. Besides the other important thing we have to consider is the topic 
that is being discussed. So, if my goal is to learn and understand the topic I would prefer a professor
who have real experience in the field is teaching and good skills to transmit the knowledge, considering
that the subject is something complex and crucial to my career development. On the other hand, if the subject
is about soft skills or management I would prefer a professor who have a great connection with the students,
making the class more dynamic and participative. In conclusion, I think that both types of professors 
have their advantages and disadvantages, and the choice depends on the subject being taught.
"""
word_count2 = len(text2.split())
#print("The total number of words in the second text is:", word_count2)

#1- points to favor : faster system, dont miss votes, help people with disabilities, reducing human error.
#now days we trust in the technology to do banking transactions and to save sensitive information.

Resume= """
The passage has many points to favor the implementation of a computerized voting system. This 
technology tries to improve the confidence in the elections and make more efficient the process. So, 
having computers counting the votes, helps to reduce the mistakes made by humans when they have to 
do something repetitive and monotonous. Also, this system assists people with disabilities, like poor 
eyesight. Even the government trusts in this kind of technology to make banking transactions and save
sensitive information.
However, the professor's opinion opposes this idea, arguing that the lack of experience of the people
using this technology could discourage the voter to vote and trust in the system. Besides, the 
professor claims that a single error in the system could change the result of an election, because at the
end any system is flawless given that humans are the ones who create those sysstems. At the same time, 
even with an error created by the system, this have not any phisical support to try to fix the error. in
addition to the fact of the small frequency of the elections, its going to take time to improve their 
reliability.
"""

word_count3 = len(Resume.split())
#print("The total number of words in the third text is:", word_count3)

#------------------------------------------------------------------------------------------------------------

#The next part is to let notes of the result of a english exam 
1.a
2.a b
3.b c
4.c 
5.d a
6.b 
7.a d
8.c
9. a 
10.b
11.b
           SENT                                          
1. d a She HAS SENT me the money three weeks ago, but I HAVEN'T received it yet.
2. b c I HAVE VISITED my grandmother this morning. She LOOKS much better than last week.
3. c b 
4. b c
5. b 
6. a b
7. c 
8. c