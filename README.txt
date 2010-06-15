This collection of scripts is designed to facilitate the creation of a usable copy of the Affective norms for English words (ANEW) dataset.

ANEW is offered for free by its creators, but only to other researchers. They won't even give it to students.  I think this is pretty lame.

Fortunately, their 1999 paper on ANEW contains all the information necessary to generate the dataset, and it is widely and freely available as a PDF. These scripts automate the process of converting that PDF into a CSV file, which can be easily used by various automated tools.

It's likely that ANEW has been modified, expanded and improved since 1999.  It would be nice if its authors were more forthcoming with it.

=====

USAGE:

To generate CSV copies of the Affective Norms for English Words (ANEW) system, perform the following steps:

1. Obtain a copy of the following PDF:

  Bradley, M.M., & Lang, P.J. (1999). Affective norms for English words (ANEW): Instruction manual and affective ratings. Technical Report C-1, The Center for Research in Psychophysiology, University of Florida.

(the MD5 of my copy is 36d181722f555ad4ea033a1db069611a)

2. Place the PDF in the directory with README.txt.  Make sure it's named ANEW.pdf (capitalization matters).

3. From the same directory, run the file make_all.sh.  For example:

    prompt> sh make_all.sh
    
4. That's it!  New CSV files named female.csv, male.csv and all.csv should now be present in the working directory.

=====

NOTES ON USING ANEW:

What do I look like, a social scientist?  Well, I'm not.  But there are many papers that show how to use ANEW.  Here's one now!

http://www.springerlink.com/content/757723154j4w726k/fulltext.html

Good luck!